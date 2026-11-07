#!/usr/bin/env python3
"""Finite symbolic audit of the delayed-ACK quantum streaming schedule.

The QSS quantum identity is checked separately.  This program tracks actual
source identities, bank generations, channel flags, and feedback availability.
An independent pairwise oracle validates the sliding-window erasure promise.
"""

from collections import deque
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
import time


@dataclass
class Bank:
    generation: int = 0
    valid_pair: bool = True
    pending_source: int | None = None
    last_source: int | None = None
    usable_at: int = 0
    confirmed: bool = True
    last_kind: str = "initial"


def validate_erasure_promise(B, erasures):
    """Every 2B+1 window has erasure span <=B, including windows at any phase."""
    losses = sorted(erasures)
    for i, left in enumerate(losses):
        for right in losses[i + 1 :]:
            distance = right - left
            if distance > 2 * B:
                break
            assert distance < B, ("invalid erasure pattern", B, left, right)


def simulate(B, D, N, erasures, collect_trace=False):
    assert 1 <= D <= B and N >= 1
    erasures = set(erasures)
    validate_erasure_promise(B, erasures)
    banks = [Bank() for _ in range(D)]
    queue = deque()
    packets = {}
    delivered = {}
    cursor = 0
    episode = None
    trace = []
    stats = {
        "max_packet_groups": 0,
        "max_receiver_bank_groups": D,
        "max_sender_groups_before_send": D,
        "max_source_delay": 0,
        "recovery_episodes": 0,
        "normal_bank_reuses": 0,
        "refresh_bank_reuses": 0,
    }

    def output(source, t):
        assert source not in delivered, ("duplicate output", source, t)
        assert 0 <= source < N
        assert source <= t <= source + B, ("deadline", B, D, N, source, t)
        delivered[source] = t
        stats["max_source_delay"] = max(stats["max_source_delay"], t - source)

    for t in range(N + 2 * B + 1):
        # Exactly D slots of feedback latency.  The feedback record carries
        # both the transmission time and generation; an old ACK must never
        # certify a newer bank generation.
        ack = packets.get(t - D)
        if ack is not None:
            if ack["kind"] == "normal":
                bank = banks[ack["bank"]]
                if bank.generation == ack["generation"] and ack["received"]:
                    bank.confirmed = True
                if not ack["received"] and episode is None:
                    first_loss = t - D
                    episode = (first_loss, ack["bank"])
                    stats["recovery_episodes"] += 1
                    # Every bank was used at most once after this first loss;
                    # the cyclic rotation is anchored to the failed bank.
                    assert first_loss in erasures
            elif ack["kind"] == "repair":
                bank = banks[ack["bank"]]
                if bank.generation == ack["generation"] and ack["received"]:
                    bank.confirmed = True

        if episode is not None and t == episode[0] + 2 * B:
            cursor = episode[1]
            episode = None
            assert not queue, ("uncleared backlog on resume", B, D, t, list(queue))

        if t < N:
            queue.append(t)
        stats["max_sender_groups_before_send"] = max(
            stats["max_sender_groups_before_send"], D + len(queue)
        )

        packet = {"kind": "padding", "received": t not in erasures, "groups": 0}
        if episode is None:
            if queue:
                source = queue.popleft()
                assert source == t, ("normal mode inherited backlog", source, t)
                bank_index = cursor
                bank = banks[bank_index]
                assert bank.valid_pair, ("used damaged bank", B, D, t, bank_index)
                assert bank.confirmed, ("used unconfirmed bank", B, D, t, bank_index)
                assert t >= bank.usable_at, (
                    "reused before ACK latency", B, D, t, bank_index, bank.usable_at
                )
                if bank.last_kind == "normal":
                    stats["normal_bank_reuses"] += 1
                elif bank.last_kind == "refresh":
                    stats["refresh_bank_reuses"] += 1
                bank.generation += 1
                bank.last_source = source
                bank.usable_at = t + D
                bank.confirmed = False
                bank.last_kind = "normal"
                packet.update(
                    kind="normal", source=source, bank=bank_index,
                    generation=bank.generation, groups=1
                )
                if packet["received"]:
                    output(source, t)
                    bank.valid_pair = True
                    bank.pending_source = None
                else:
                    bank.valid_pair = False
                    bank.pending_source = source
                cursor = (cursor + 1) % D
        else:
            first_loss, first_bank = episode
            offset = t - first_loss
            assert offset >= D
            if offset < B:
                pass  # Vulnerable interval: preserve all unknown data locally.
            elif offset < B + D:
                assert packet["received"], ("repair guard failed", B, D, t, episode)
                j = offset - B
                bank_index = (first_bank + j) % D
                bank = banks[bank_index]
                repaired_source = bank.pending_source
                if repaired_source is not None:
                    output(repaired_source, t)
                else:
                    assert bank.valid_pair
                    assert bank.last_source is None or bank.last_source in delivered
                bank.generation += 1
                bank.valid_pair = True
                bank.pending_source = None
                bank.last_source = None
                bank.usable_at = t + D
                # The first-loss observation certifies these repair slots.
                # Normal-mode reuse below still checks the D-slot ACK time.
                bank.confirmed = True
                bank.last_kind = "refresh"
                packet.update(
                    kind="repair", bank=bank_index, generation=bank.generation,
                    repaired_source=repaired_source, groups=2
                )
                if queue:
                    source = queue.popleft()
                    output(source, t)
                    packet["direct"] = [source]
                    packet["groups"] += 1
            else:
                assert offset < 2 * B
                assert packet["received"], ("catchup guard failed", B, D, t, episode)
                packet["kind"] = "catchup"
                packet["direct"] = []
                for _ in range(2):
                    if queue:
                        source = queue.popleft()
                        output(source, t)
                        packet["direct"].append(source)
                        packet["groups"] += 1

        assert packet["groups"] <= 3
        stats["max_packet_groups"] = max(stats["max_packet_groups"], packet["groups"])
        # Each bank has exactly one retained Bob share, whether a valid ebit or
        # the QSS share protecting a pending source.  All outputs are released.
        assert len(banks) == D
        for bank in banks:
            assert bank.valid_pair == (bank.pending_source is None)
        packets[t] = packet
        if collect_trace:
            trace.append({"slot": t, "erased": t in erasures, "episode": episode,
                          "queue": list(queue), "packet": dict(packet)})

        if t >= N - 1 and len(delivered) == N and not queue and all(
            bank.valid_pair and bank.confirmed for bank in banks
        ):
            assert t <= N + 2 * B - 1, ("flush bound", B, D, N, t)
            stats["completion_slot"] = t
            stats["forward_slots"] = t + 1
            stats["input_slots"] = N
            stats["flush_slots"] = t + 1 - N
            stats["seed_pairs_returned_in_source_groups"] = D
            if collect_trace:
                stats["trace"] = trace
                stats["delivered"] = delivered
            return stats
    raise AssertionError(("did not terminate", B, D, N, sorted(erasures), delivered))


def concatenate_bursts(B, first, shapes):
    """Start each next burst exactly W slots after the last actual erasure."""
    losses = set()
    start = first
    for shape in shapes:
        assert shape and min(shape) == 0 and max(shape) < B
        losses.update(start + offset for offset in shape)
        start += max(shape) + 2 * B + 1
    return losses


def main():
    started = time.monotonic()
    counts = {"clean": 0, "single_contiguous": 0, "earliest_repeated": 0,
              "all_hole_masks": 0, "finite_horizon": 0}
    aggregate = {"max_delay_minus_B": -1, "max_packet_groups": 0,
                 "max_sender_groups_over_B_plus_1": 0,
                 "recovery_episodes": 0, "normal_bank_reuses": 0,
                 "refresh_bank_reuses": 0, "max_flush_slots": 0}

    def check(kind, B, D, N, losses):
        outcome = simulate(B, D, N, losses)
        counts[kind] += 1
        aggregate["max_delay_minus_B"] = max(
            aggregate["max_delay_minus_B"], outcome["max_source_delay"] - B
        )
        aggregate["max_packet_groups"] = max(
            aggregate["max_packet_groups"], outcome["max_packet_groups"]
        )
        aggregate["max_sender_groups_over_B_plus_1"] = max(
            aggregate["max_sender_groups_over_B_plus_1"],
            outcome["max_sender_groups_before_send"] - (B + 1)
        )
        aggregate["max_flush_slots"] = max(
            aggregate["max_flush_slots"], outcome["flush_slots"]
        )
        for key in ("recovery_episodes", "normal_bank_reuses", "refresh_bank_reuses"):
            aggregate[key] += outcome[key]

    for B in range(1, 9):
        for D in range(1, B + 1):
            check("clean", B, D, 10 * B + 2 * D + 3, set())
            for length in range(1, B + 1):
                for phase in range(0, 2 * B + D + 2):
                    losses = set(range(phase, phase + length))
                    check("single_contiguous", B, D, phase + 5 * B + 2 * D + 3, losses)

            phases = sorted({0, 1, D - 1, D, D + 1, 2 * B - 1, 2 * B, 2 * B + 1})
            for phase, left_length, right_length in product(
                phases, range(1, B + 1), range(1, B + 1)
            ):
                shapes = [set(range(left_length)), set(range(right_length)),
                          set(range(B)), {0}]
                losses = concatenate_bursts(B, phase, shapes)
                check("earliest_repeated", B, D, max(losses) + 4 * B + 2 * D + 3, losses)

            # Every nonempty subset of a B-slot interval, translated so its
            # first actual loss is offset zero, followed by its reversed shape.
            for mask in range(1, 1 << B):
                raw = {j for j in range(B) if mask & (1 << j)}
                first = min(raw)
                shape = {j - first for j in raw}
                reverse = {max(shape) - j for j in shape}
                for phase in sorted({0, D, D + 1, 2 * B}):
                    losses = concatenate_bursts(B, phase, [shape, reverse, set(range(B))])
                    check("all_hole_masks", B, D, max(losses) + 4 * B + 2 * D + 3, losses)

            # End source acceptance before, during, and after detection/repair.
            for phase in sorted({0, 1, D, 2 * B}):
                for length in sorted({1, B}):
                    losses = concatenate_bursts(
                        B, phase, [set(range(length)), set(range(B)), {0}]
                    )
                    for N in range(1, phase + 2 * B + D + 4):
                        check("finite_horizon", B, D, N, losses)

    assert aggregate["max_delay_minus_B"] <= 0
    assert aggregate["max_packet_groups"] <= 3
    assert aggregate["max_sender_groups_over_B_plus_1"] <= 0
    # B=5,D=3 stresses the nondivisibility of 2B by D and shifted first loss.
    sample_losses = concatenate_bursts(5, 2, [{0, 2, 4}, {0}, set(range(5))])
    sample = simulate(5, 3, 50, sample_losses, collect_trace=True)
    result = {
        "status": "PASS",
        "model": {"B": "1..8", "D": "1..B", "W": "2B+1",
                  "physical_packet_capacity_in_source_groups": 3,
                  "receiver_retained_quantum_groups": "D",
                  "source_deadline": "arrival+B", "ack_available": "send_time+D"},
        "case_counts": counts,
        "total_cases": sum(counts.values()),
        "aggregate_checks": aggregate,
        "runtime_seconds": round(time.monotonic() - started, 3),
        "limitations": ["Symbolic schedule audit; QSS quantum identity is verified separately.",
                        "Finite tests support, and do not replace, the analytic induction.",
                        "Outputs may be released out of source order; extra in-order buffering is not simulated."],
        "phase_rotation_sample": {"B": 5, "D": 3, "N": 50,
                                  "erasures": sorted(sample_losses), "outcome": sample},
    }
    target = Path(__file__).with_name("streaming_schedule_verification.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key != "phase_rotation_sample"}, indent=2))


if __name__ == "__main__":
    main()
