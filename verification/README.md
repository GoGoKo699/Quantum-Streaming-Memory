# Reproduce the finite checks

The scientific account proves the universal claims. These programs check the actual finite-field decoder and exercise the two distinct scheduling mechanisms, including source deadlines, counted memory and finite Bell-bank return.

## Environment and command

Use Python 3.11 or newer. The recorded integrated run used Python 3.12.14 and NumPy 2.3.5. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite uses assertions; do not run Python with optimization flags that disable them. The runner checks this condition and launches its children with Python environment overrides ignored. No network access is used by the checks themselves. Installing the pinned dependency is a separate environment step.

Expected final summary:

```text
PASS: 3 exact decoder identities; 33,707 feedback schedules; 38,217 no-feedback pipelines.
Wrote verification/verification_report.json with exact program hashes.
```

The scripts regenerate their JSON outputs next to the programs. Runtime and execution timestamps can differ on a repeat run; case counts and mathematical invariants should agree. [verification_report.json](verification_report.json) records the actual environment, results and SHA256 digests of the three programs, runner and dependency file.

## What each program checks

| Program | Checked object | Recorded outcome |
|---|---|---|
| [verify_qss_primitive.py](verify_qss_primitive.py) | The normalized reference-entangled $`\mathbb F_4`$ encoding and all three in-place decoders | Three unit-fidelity output/syndrome identities, zero amplitude error; every single share is independent of the reference; successful middle-share delivery returns an exact EPR pair |
| [verify_streaming_schedule.py](verify_streaming_schedule.py) | Actual source labels, bank generations, ACK availability, bank rotation, FIFO service and finite stops | 33,707 cases, no late output, at most three transmitted groups, no premature bank reuse, exact final bank return |
| [verify_no_feedback_pipeline.py](verify_no_feedback_pipeline.py) | Received advance/middle/final shares, local decoding, both endpoint memories, dummy EPR outputs and the whole tail | 38,217 cases, every actual/dummy deadline met, at most $`2B`$ retained groups at both endpoints, exactly $`B`$ Bell groups returned after $`N+2B`$ slots |

The first program evaluates a Choi purification with exactly representable amplitudes for this field representation. It tests the full recovered source/reference state and the other output, rather than only a classical truth table. The algebraic identity in [primitive.md](../science/primitive.md) supplies the general proof for arbitrary input superpositions and references.

The feedback checker covers $`B=1,\ldots,8`$ and every $`D=1,\ldots,B`$. Its families comprise 36 clean cases, 3,750 single contiguous bursts, 9,751 earliest repeated-burst patterns, 14,199 hole-mask cases and 5,971 finite-horizon cases. It exercises 91,118 recovery episodes. The saved [phase-rotation trace](streaming_schedule_verification.json) uses $`B=5,D=3`$ and a shifted first loss to test the nondivisible bank cycle. Sender storage is checked immediately before sending, including the new arrival, against $`B+1`$ groups; the written retained-space proof removes that transient arrival.

The independent no-feedback checker covers $`B=1,\ldots,8`$, including every $`N=1,\ldots,4B+3`$ for its clean and single-burst families. Its 168 clean, 25,032 single-burst, 3,000 repeated-burst and 10,017 hole-mask/short-horizon cases include losses throughout the final tail. It exercises 127,715 advance-share erasures later recovered from the other two shares. The [short-horizon trace](no_feedback_pipeline_verification.json) has $`B=4,N=3`$ and explicitly accounts for initial bank entries used by dummy sources.

Both symbolic checkers validate the loss family using the forbidden pairwise erasure distances $`B,\ldots,2B`$. They track source and register identities, so a stale ACK cannot authorize a new bank generation and an already released source cannot be silently reused.

## Boundaries of verification

Finite cases do not enumerate every admissible infinite history or prove the arbitrary-code converses. The [causal proof](../science/converse.md), [feedback invariant and queue argument](../science/feedback_protocol.md), [pipeline index counts](../science/no_feedback_protocol.md), and [rate converse](../science/rate.md) are the analytical sources for those claims.

The schedule programs treat the separately checked quantum primitive as a correct subroutine. Their memory counts concern retained registers at cuts. Incoming-packet and local preparation workspace are charged analytically in the construction pages. Optional ordered release is also proved analytically; it is not reported as a simulated check.

The suite does not test faulty hardware, unreliable ACKs, unrestricted loss histories, literature priority, or actual GitHub mathematical rendering. Source/code verification and a hosted visual review are different checks.
