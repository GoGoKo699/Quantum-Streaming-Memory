#!/usr/bin/env python3
"""Audit the no-feedback Q/A/C pipeline, its storage, and its finite tail.

This symbolic check is independent of the delayed-ACK state machine.  It tracks
each received share, every local decoder invocation, both parties' retained
registers, and the Bell halves produced by dummy source words.  The separate
GF(4) calculation establishes the quantum correctness of those decoders.
"""

from itertools import product
import json
from pathlib import Path
import time


def valid_pattern(B, losses):
    ordered = sorted(losses)
    for i, left in enumerate(ordered):
        for right in ordered[i + 1:]:
            gap = right - left
            if gap > 2 * B:
                break
            assert gap < B, ("sliding-window violation", B, left, right)


def repeated_pattern(B, phase, shapes):
    losses = set()
    start = phase
    for shape in shapes:
        assert shape and min(shape) == 0 and max(shape) < B
        losses.update(start + offset for offset in shape)
        start += max(shape) + 2 * B + 1
    return losses


def simulate(B, N, losses, trace=False):
    assert B >= 1 and N >= 1
    losses = set(losses)
    valid_pattern(B, losses)
    total_words = N + B
    bob_shares = [set() for _ in range(total_words)]
    for j in range(B):
        bob_shares[j].add("Q")
    alice_future_halves = set(range(B))
    alice_backup_shares = set()
    alice_dummy_references = set()
    bob_returned_seed = set()
    delivered = {}
    source_types = ["payload" if j < N else "dummy" for j in range(total_words)]
    arrivals = {"Q": 0, "A": 0, "C": 0}
    stats = {
        "max_receiver_retained_groups": B,
        "max_sender_retained_groups": B,
        "max_packet_groups": 0,
        "max_payload_delay": 0,
        "max_dummy_delay": 0,
        "erased_advance_shares_later_recovered": 0,
        "decoder_pairs": {"AQ": 0, "CQ": 0, "AC": 0},
    }
    trace_rows = []

    for t in range(N + 2 * B):
        outgoing = []
        if t + B < total_words:
            future = t + B
            assert future not in alice_future_halves
            alice_future_halves.add(future)
            outgoing.append(("Q", future))
        if t < total_words:
            assert t in alice_future_halves, ("missing Alice EPR half", B, N, t)
            alice_future_halves.remove(t)
            alice_backup_shares.add(t)
            if source_types[t] == "dummy":
                alice_dummy_references.add(t)
            outgoing.append(("A", t))
        past = t - B
        if 0 <= past < total_words:
            assert past in alice_backup_shares
            alice_backup_shares.remove(past)
            outgoing.append(("C", past))
        assert len(outgoing) <= 3
        assert len({word for _, word in outgoing}) == len(outgoing)
        stats["max_packet_groups"] = max(stats["max_packet_groups"], len(outgoing))

        for kind, word in outgoing:
            arrivals[kind] += 1
            if t in losses or word in delivered:
                continue
            assert kind not in bob_shares[word]
            bob_shares[word].add(kind)
            if len(bob_shares[word]) == 2:
                assert word <= t <= word + B, ("deadline", B, N, word, t)
                pair = "".join(sorted(bob_shares[word]))
                stats["decoder_pairs"][pair] += 1
                if pair == "AC":
                    assert word >= B and word - B in losses
                    stats["erased_advance_shares_later_recovered"] += 1
                delivered[word] = t
                bob_shares[word].clear()  # Both decoder inputs are consumed.
                if source_types[word] == "dummy":
                    assert word in alice_dummy_references
                    bob_returned_seed.add(word)
                    stats["max_dummy_delay"] = max(stats["max_dummy_delay"], t - word)
                else:
                    stats["max_payload_delay"] = max(stats["max_payload_delay"], t - word)

        future_count = 0
        pending_count = 0
        for word, held in enumerate(bob_shares):
            if not held:
                continue
            assert word not in delivered
            assert len(held) == 1
            if word > t:
                assert held == {"Q"}
                future_count += 1
            else:
                assert t - B < word <= t, ("overdue pending share", B, N, word, t)
                pending_count += 1
        assert future_count + len(bob_returned_seed) <= B
        assert pending_count <= B
        receiver_groups = future_count + pending_count + len(bob_returned_seed)
        assert receiver_groups <= 2 * B

        assert all(word > t for word in alice_future_halves)
        assert all(t - B < word <= t for word in alice_backup_shares)
        assert len(alice_future_halves) + len(alice_dummy_references) <= B
        assert len(alice_backup_shares) <= B
        sender_groups = (len(alice_future_halves) + len(alice_backup_shares)
                         + len(alice_dummy_references))
        assert sender_groups <= 2 * B
        stats["max_receiver_retained_groups"] = max(
            stats["max_receiver_retained_groups"], receiver_groups
        )
        stats["max_sender_retained_groups"] = max(
            stats["max_sender_retained_groups"], sender_groups
        )
        if trace:
            trace_rows.append({"slot": t, "erased": t in losses,
                               "packet": outgoing, "future_Q": future_count,
                               "pending_shares": pending_count,
                               "returned_seed": len(bob_returned_seed),
                               "receiver_retained": receiver_groups,
                               "sender_retained": sender_groups})

    assert set(delivered) == set(range(total_words))
    assert all(not shares for shares in bob_shares)
    assert bob_returned_seed == set(range(N, N + B))
    assert alice_dummy_references == bob_returned_seed
    assert not alice_future_halves and not alice_backup_shares
    assert arrivals == {"Q": N, "A": N + B, "C": N + B}
    stats.update({"source_slots": N, "forward_slots": N + 2 * B,
                  "flush_slots": 2 * B, "returned_seed_groups": B,
                  "transmitted_share_counts": arrivals})
    if trace:
        stats["trace"] = trace_rows
        stats["delivery_slots"] = delivered
    return stats


def main():
    start = time.monotonic()
    counts = {"clean_all_horizons": 0, "single_bursts_all_horizons": 0,
              "earliest_repeated": 0, "hole_masks_and_short_horizons": 0}
    aggregate = {"max_receiver_excess_over_2B": -1,
                 "max_sender_excess_over_2B": -1,
                 "max_packet_groups": 0,
                 "erased_advance_shares_later_recovered": 0,
                 "decoder_pairs": {"AQ": 0, "CQ": 0, "AC": 0}}

    def check(family, B, N, losses):
        result = simulate(B, N, losses)
        counts[family] += 1
        aggregate["max_receiver_excess_over_2B"] = max(
            aggregate["max_receiver_excess_over_2B"],
            result["max_receiver_retained_groups"] - 2 * B
        )
        aggregate["max_sender_excess_over_2B"] = max(
            aggregate["max_sender_excess_over_2B"],
            result["max_sender_retained_groups"] - 2 * B
        )
        aggregate["max_packet_groups"] = max(
            aggregate["max_packet_groups"], result["max_packet_groups"]
        )
        aggregate["erased_advance_shares_later_recovered"] += result[
            "erased_advance_shares_later_recovered"
        ]
        for pair in aggregate["decoder_pairs"]:
            aggregate["decoder_pairs"][pair] += result["decoder_pairs"][pair]

    for B in range(1, 9):
        for N in range(1, 4 * B + 4):
            check("clean_all_horizons", B, N, set())
            # Include losses in the final tail, not only during real inputs.
            for phase in range(N + 2 * B):
                for length in range(1, B + 1):
                    check("single_bursts_all_horizons", B, N,
                          set(range(phase, phase + length)))
        for phase, left, right in product(
            range(2 * B + 2), range(1, B + 1), range(1, B + 1)
        ):
            losses = repeated_pattern(B, phase,
                                      [set(range(left)), set(range(right)), {0}, set(range(B))])
            N = max(losses) + 3 * B + 1
            check("earliest_repeated", B, N, losses)
        for mask in range(1, 1 << B):
            raw = {j for j in range(B) if mask & (1 << j)}
            shape = {j - min(raw) for j in raw}
            reverse = {max(shape) - j for j in shape}
            for phase in sorted({0, B - 1, B, 2 * B + 1}):
                losses = repeated_pattern(B, phase, [shape, reverse, set(range(B))])
                # The N<B cases exercise initial banks also used by dummy words.
                for N in sorted({1, max(1, B - 1), B, B + 1, max(losses) + 2}):
                    check("hole_masks_and_short_horizons", B, N, losses)

    sample_losses = repeated_pattern(4, 1, [{0, 2, 3}, {0}, {0, 1, 2, 3}])
    sample = simulate(4, 3, sample_losses, trace=True)
    record = {
        "status": "PASS", "B_range": "1..8", "W": "2B+1",
        "case_counts": counts, "total_cases": sum(counts.values()),
        "aggregate_checks": aggregate,
        "runtime_seconds": round(time.monotonic() - start, 3),
        "verified_invariants": [
            "Every actual and dummy source is recovered by its arrival+B deadline.",
            "Every emitted packet has at most three source-sized shares.",
            "Receiver retained quantum groups never exceed 2B, including returned dummy outputs.",
            "Sender retained quantum groups never exceed 2B, including dummy reference halves.",
            "For every N, the schedule ends after exactly N+2B slots with exactly B shared Bell groups.",
            "Every initial seed and final dummy label is accounted for, including N<B.",
            "Lost Q shares before source arrival are subsequently decoded from A,C."
        ],
        "limitations": [
            "Symbolic share/register bookkeeping, using the separately verified QSS identity.",
            "Finite cases supplement the analytic proof and do not exhaust all admissible infinite streams.",
            "Retained storage is measured after each slot; incoming packet workspace is charged separately."
        ],
        "short_horizon_example": {"B": 4, "N": 3, "losses": sorted(sample_losses),
                                  "result": sample},
    }
    Path(__file__).with_name("no_feedback_pipeline_verification.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    print(json.dumps({key: value for key, value in record.items()
                      if key != "short_horizon_example"}, indent=2))


if __name__ == "__main__":
    main()
