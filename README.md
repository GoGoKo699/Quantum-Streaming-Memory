# Quantum Streaming Memory

**How much coherent storage does a quantum receiver need while the sender waits to learn which packets were lost?** For a sustained stream of unknown quantum states with the smallest possible delivery delay, this project gives a matching lower bound and construction:

```math
M_{\min}=\Theta\!\left(k\min\{D,B\}\right),\qquad T=B.
```

Here $`k`$ is the number of logical qubits arriving per slot, $`D`$ is the delay of a reliable erasure acknowledgment, and $`B`$ is the allowed erasure span. Every window of $`2B+1`$ slots must contain losses within a span of at most $`B`$ slots; holes within the span and repeated bursts are allowed. Every source must be delivered by the end of its arrival slot plus $`B`$.

The constructions use a fixed ququart primitive, packets of $`3k`$ physical qubits for even $`k`$, and a finite counted Bell bank that is returned after a charged flush. The forward rate $`1/3`$ is **optimal without feedback** for the same channel family. At that rate and deadline, faster acknowledgments reduce the receiver's required coherent storage. The theorem permits arbitrary causal encoders, free classical records and unrestricted sender memory; the upper constructions use sender space $`O(kB)`$.

| Feedback | Universal retained-memory lower bound | Explicit retained receiver storage | Extra incoming-packet space |
|---|---:|---:|---:|
| Next-slot ACK, $`D=1`$ | $`k`$ | $`k`$ | At most $`3k`$ |
| $`1\le D\le B`$ | $`kD`$ | $`kD`$ | At most $`3k`$ |
| $`D>B`$ or no feedback | $`kB`$ | At most $`2kB`$ | At most $`3k`$ |

The lower bounds apply at clean cuts with enough future source arrivals and hence to the peak memory of sustained protocols. With only $`r`$ source arrivals left, the bound is $`k\min\{D,B,r\}`$. Released payloads become inaccessible; every retained Bell half, unresolved share and unreleased output counts. The full [model and theorem statements](science/model.md) specify these conventions, the per-message approximate bound and odd-width padding.

## Read the science

The [scientific entrypoint](science/README.md) connects the account. For a quick physical explanation, read the [complete burst-repair example](science/interpretation.md). For the proof, start with the model and follow the causal converse and the two constructions.

| To inspect | Read |
|---|---|
| Assumptions, deadlines, resource charges and exact results | [Model](science/model.md) |
| Why acknowledgment delay forces quantum storage for every encoder | [Causal converse](science/converse.md) |
| The exact inherited code, coherent recovery and Bell-pair recycling | [Secret-sharing primitive](science/primitive.md) |
| A rotating-bank protocol with $`Dk`$ retained receiver qubits | [Feedback construction](science/feedback_protocol.md) |
| Causal advance shares and exact finite seed return | [No-feedback pipeline](science/no_feedback_protocol.md) |
| Why the no-feedback rate cannot exceed one third | [Rate benchmark](science/rate.md) |
| A worked schedule, memory placement and ordered delivery | [Interpretation](science/interpretation.md) |
| Established ingredients and the precise additional statement | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Executed finite checks and their limitations | [Verification](verification/README.md) |

The entropy inequality, threshold secret sharing, communication-cipher recycling and catalytic renewal are established ingredients. The contribution is the delayed-ACK causal resource bound and its matching sustained deadline schedule. The [comparison](references/RELATED_WORK.md) identifies the relevant primary sources and avoids attributing those ingredients to this project.

## Reproduce the checks

Use Python 3.11 or newer with the pinned dependency, then run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite checks the reference-entangled four-dimensional encoding, 33,707 delayed-ACK schedule cases, and 38,217 independent no-feedback pipeline cases, including the finite return tail. It reports the exact program hashes used. The general lower bounds and infinite-stream guarantees are established by the written proofs; finite enumeration checks the implementation and illustrated invariants.

## Scope

The erasure promise supplies a guaranteed clean repair interval. The analysis assumes ideal local gates and memories, reliable ACKs and same-slot delivery or erasure. It does not establish a deterministic deadline for unrestricted iid losses, a noisy-memory threshold, feedback capacity, or the full rate–delay–memory tradeoff. Exact rate $`1/3`$ is realized at even logical widths, already at $`k=2,n=6`$; padding an odd width has an explicit constant cost.

Both protocols work for every finite source horizon and return their counted initial bank. Their sustained optimal-order memory statement need not minimize the seed for an exceptionally short session. Optional ordered release is proved separately and adds a counted quantum output buffer.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
