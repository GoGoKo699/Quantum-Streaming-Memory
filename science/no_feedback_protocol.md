# No-feedback pipeline and finite entanglement return

This pipeline achieves exact deadline $`T=B`$, forward packet width $`3k`$, and retained receiver storage at most $`2Bk`$ without feedback. It also supplies the upper construction when feedback delay exceeds $`B`$.

The building block is the inherited [two-out-of-three secret-sharing primitive](primitive.md), with the provenance discussed in [quantum threshold sharing](../references/RELATED_WORK.md#qss1999) and [Leung's communication cipher](../references/RELATED_WORK.md#leung2002). This page proves the causal schedule, finite-session resource return, and storage accounting; it does not claim a new secret-sharing code.

## Assumptions

Use the [streaming model](model.md), with positive integer $`B`$ and positive even $`k`$. A new $`k`$-qubit source $`S_j`$ arrives before slot $`j`$ and is due by the end of slot $`j+B`$. Sources can be jointly entangled with an arbitrary external reference.

A packet is either wholly delivered or erased. In every $`2B+1`$ consecutive slots, all erased positions fit inside an interval of at most $`B`$ slots. The receiver has the erasure flags, but no feedback is used. No external forward classical channel is used. Clock, parameters, and the arbitrary finite source horizon $`N`$ are common protocol parameters.

At startup Alice and Bob share $`Bk`$ Bell pairs, divided into groups $`L_j,Q_j`$ for $`0\le j<B`$. The resource is counted at both endpoints and independent of the input stream. There are no uncharged negative-time transmissions.

## Advance sharing and the three transmission times

For each source $`S_j`$, Alice prepares a local pair $`L_j,Q_j`$ in advance and sends $`Q_j`$ in slot $`j-B`$. For the first $`B`$ indices the initial bank supplies these registers instead. Alice retains $`L_j`$.

When $`S_j`$ arrives, Alice applies the [primitive's local encoding](primitive.md), producing $`A_j,C_j`$. She sends $`A_j`$ in slot $`j`$ and retains $`C_j`$ until slot $`j+B`$. The share times are

```math
j-B,\qquad j,\qquad j+B.
```

They fit within one window of $`2B+1`$ slots, and any two are separated by at least $`B`$. The channel promise therefore permits at most one of them to be erased. For the first $`B`$ sources the advance share is initially present, and the same promise prevents both later transmissions from being erased. Bob decodes as soon as two shares are available, necessarily by slot $`j+B`$.

Sending $`Q_j`$ before the source arrives is causal because it is initially only a Bell half. If it is erased before encoding, the environment holds that share of the eventual codeword. The available $`A_j,C_j`$ pair still recovers the source exactly. Alice does not need to learn whether the advance share survived.

At slot $`t`$, the physical packet is

```math
\bigl(Q_{t+B},\ A_t,\ C_{t-B}\bigr),
```

with fixed padding for an absent register. Each share contains exactly $`k`$ physical qubits, so the packet has exactly $`3k`$ physical positions. The fixed four-element field uses two qubits per symbol; no alphabet that grows with $`B`$ is hidden in this rate.

## Exact return for every finite source horizon

Let $`N\ge1`$ be arbitrary. Introduce $`B`$ additional source groups at indices

```math
N,N+1,\ldots,N+B-1.
```

Each additional source is one half of a fresh pair prepared locally by Alice. Alice keeps the other half, denoted $`R_j`$. These dummy-source pairs are distinct from the advance-sharing pairs $`L_j,Q_j`$. Apply the same pipeline to all $`N+B`$ groups and launch no further codewords.

The complete transmitted-share count is:

| Share type | Indices | Number of groups | Sending slots |
|---|---|---:|---|
| Advance $`Q_j`$ | $`B\le j<N+B`$ | $`N`$ | $`0,\ldots,N-1`$ |
| Middle $`A_j`$ | $`0\le j<N+B`$ | $`N+B`$ | $`0,\ldots,N+B-1`$ |
| Final $`C_j`$ | $`0\le j<N+B`$ | $`N+B`$ | $`B,\ldots,N+2B-1`$ |

The initial bank supplies $`Q_0,\ldots,Q_{B-1}`$. The last nonempty code share is $`C_{N+B-1}`$, sent in slot $`N+2B-1`$. Thus there are exactly $`N+2B`$ forward slots, including the entire $`2B`$-slot tail. Every unused packet position in those slots is filled with a fixed state and charged.

Each dummy source obeys the same recovery theorem as an actual source. Its recovered output is exactly maximally entangled with Alice's retained $`R_j`$, by the primitive's reference-preserving decoding identity. The recovered dummy groups therefore supply exactly $`Bk`$ Bell pairs, independent of every actual payload and its external reference. Decoder junk is discarded, and the returned pairs can be swapped to designated initial bank registers.

This proves exact finite resource return rather than an average entanglement yield. It includes $`N<B`$: some initially shared pairs are then used to encode dummy sources, but the same index ranges, final time, and returned resource apply. No complete block or steady-state warmup is required.

## Receiver storage, including the tail

Measure storage after each slot's decoding and output release. A source with arrival time in the future can contribute only its received advance share. An arrived source that is not yet decoded contributes at most one received share; a second share triggers immediate decoding.

At the end of slot $`t`$, any pending arrived source must have index

```math
t-B<j\le t.
```

Otherwise its established deadline would already have passed. There are at most $`B`$ such indices, giving at most $`Bk`$ pending-source qubits.

Future advance shares and completed dummy outputs together occupy at most another $`Bk`$ qubits. Before the dummy interval, there are at most $`B`$ future shares and no completed dummy outputs. For $`N\le t<N+B`$, the number of future indices is at most $`N+B-1-t`$, while at most $`t-N+1`$ dummy sources have arrived and could have been completed. Their sum is $`B`$. After that interval, there are no future shares and at most $`B`$ returned groups.

Consequently, throughout ordinary operation and the final tail,

```math
M_{\mathrm{receiver}}\le 2Bk.
```

The final shares of codewords decoded earlier are still transmitted and charged. Bob discards them when they arrive. They do not create an additional retained register.

## Sender storage and transient workspace

Alice retains at most $`B`$ delayed $`C_j`$ shares. Her future, unencoded advance-pair halves $`L_j`$ plus her already-created dummy references $`R_j`$ total at most $`B`$ groups, by the same index count used above. Therefore

```math
M_{\mathrm{sender}}\le 2Bk
```

at every cut, including the tail. The returned pairs are included in this count.

At Bob, one incoming packet adds at most $`3k`$ physical qubits. The two-share decoders are in-place permutations; source outputs can be released and junk discarded before the next slot. The hardware peak is therefore bounded by retained storage plus $`3k`$ incoming qubits.

Alice can implement each slot with at most $`4k`$ additional transient qubits for a fresh source or dummy-source pair, a local advance-sharing pair, and fixed padding. Local pair preparation is therefore counted; it is not a supply of free shared entanglement. Both processing overheads are $`O(k)`$, independent of the burst length.

## Rate and role in the memory theorem

The protocol communicates $`Nk`$ actual logical qubits using exactly $`3k(N+2B)`$ reserved forward physical-qubit positions. Hence

```math
R_N=\frac{N}{3(N+2B)}\longrightarrow\frac13.
```

The [no-feedback rate converse](rate.md) is established separately. This pipeline attains its $`1/3`$ asymptotic rate benchmark with finite returned assistance and deadline $`B`$. It also applies unchanged when a feedback link exists but has delay $`D>B`$; the protocol simply ignores it. Together with the [delayed-ACK construction](feedback_protocol.md), it supplies retained receiver memory $`O(k\min(D,B))`$.

## Optional variant: strictly ordered output release

The main storage count releases actual sources as soon as they decode. If release must follow source order, at most $`B-1`$ decoded actual sources need to wait behind an earlier unresolved source. At a cut after slot $`t`$, every unresolved arrived source has index greater than $`t-B`$, and no source with index greater than $`t`$ has arrived. If a gap blocks release, at most $`B-1`$ later indices can therefore be waiting.

All earlier sources have earlier deadlines. Delaying release until every preceding source is available consequently preserves each source's deadline. The optional output buffer adds at most $`(B-1)k`$ retained qubits, for total receiver storage at most $`(3B-1)k`$ before incoming-packet workspace. Dummy outputs are bank resources and are counted in the original $`2Bk`$ bound; they are not actual payloads awaiting ordered release.

## Independent finite pipeline audit

The share-recovery identity and index counts above are the proof. The accompanying `verify_no_feedback_pipeline.py` checker independently tracks every received share, decoder invocation, retained register at both endpoints, and returned dummy output.

It passed 38,217 cases for $`B=1,\ldots,8`$, including every $`N=1,\ldots,4B+3`$ with a single burst at every phase through the final tail, earliest admissible repeated bursts, burst holes, and short horizons $`N<B`$. All sources and dummies met their deadlines, both retained-space bounds were satisfied, and every finite run returned exactly $`B`$ Bell groups after exactly $`N+2B`$ slots. The audit exercised 127,715 erased advance shares subsequently recovered from $`A,C`$.

These finite tests supplement the analytic argument and do not exhaust all admissible infinite patterns. The optional ordered-output buffer is proved above rather than simulated by this checker.
