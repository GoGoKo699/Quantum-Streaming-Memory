# From Preskill's quantum information notes to streaming memory

## Begin with the communication task

A sender receives an unknown quantum state in every time slot. Each state may be entangled with a reference that neither party can access. The receiver must deliver it within a fixed number of slots, even when a packet is lost. The sender cannot keep a second copy for retransmission. A useful recovery option instead comes from sharing an encoding across the sender, the transmitted packet and quantum memory already at the receiver.

The project's question is how much of that coherent memory must remain **at the receiver** when the sender learns packet outcomes only after a delay. In the [complete worked example](../science/interpretation.md#a-complete-burst-repair-example), a burst can span $`B=4`$ slots and acknowledgments take $`D=2`$ slots. Two entangled banks let the sender issue two packets before learning of a loss. The recovery schedule then delivers the first two sources at their deadlines while repairing the banks and clearing the queued sources. The example tracks every forward group and the receiver's retained memory; it is the canonical table for this bridge.

The general result, under the [precise packet and erasure model](../science/model.md), is

```math
M_{\min}=\Theta\!\left(k\min\{D,B\}\right)
```

for sustained streams of $`k`$ logical qubits per slot, deadline $`T=B`$ and forward rate $`1/3`$. Here $`M`$ counts retained coherent receiver storage, and the same order applies when incoming-packet workspace is included. The source of this dependence is a combination of an established recovery-overlap bound and a causal argument about what the sender can know before an ACK arrives.

## The selected anchor and the passages used

The single educational anchor is John Preskill's **Quantum Information** lecture notes, available from the [official Caltech index](https://www.preskill.caltech.edu/ph219/). This bridge uses two chapters of that one work:

| Chapter | Pinned author-hosted draft | Relevant passages |
|---|---|---|
| [7 — Quantum Error Correction](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf) | Title page: **Updated March 2026** | §§7.3.3–7.3.4, printed pp. 9–12: reference-preserving recovery and flagged erasure; §§7.9.2–7.9.3, pp. 25–27: no-cloning and overlapping recovery in the Singleton bound; §7.12, pp. 38–40: quantum secret sharing. |
| [10 — Quantum Shannon Theory](https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf) | Title page: **Updated June 2025** | §§10.2.3–10.2.4, printed pp. 17–19: strong subadditivity and mutual-information data processing. Optional resource context: §10.8.1, pp. 60–62, on entanglement-assisted communication. |

The title pages and these substantive passages were checked on **7 November 2026**. The Chapter 10 filename contains “2022”; the dated draft actually used here says June 2025. Page numbers above are the chapters' printed page numbers. The selected passages supply the foundations needed at each step below; the remainder of either chapter is not a prerequisite.

## Translate the notation and assumptions

| Object | Meaning in this project |
|---|---|
| Reference $`R`$ | An inaccessible system used to test whether communication preserves coherence and entanglement. No physical or virtual decoder receives it. |
| Fresh source $`S_t`$ | The $`k`$-qubit input arriving at the start of slot $`t`$. It is unavailable before that slot. |
| Entropy and information | Preskill's $`H`$ is written $`S`$ in the proofs; $`I(A;B)`$ and $`I(A:B)`$ denote the same mutual information. All logarithms are base two. |
| Dimension versus distance | Here $`d=2^k`$ is a logical dimension. It is not the distance in block-code notation $`[[n,k,d]]`$. The project uses $`n`$ for qubits per forward slot, not a whole codeword's length. |
| Receiver resources $`Q,Y`$ | $`Q`$ includes every quantum system retained across a cut. $`Y`$ is an unlimited classical record. The hardware bound is $`\log_2\dim Q_y\le M`$ in each classical branch, so $`S(Q\mid Y)\le M`$. |
| Sender remainder $`E`$ | In the converse, $`E`$ is Alice's **accessible** retained system after a common encoding prefix. Preskill often uses $`E`$ for an inaccessible environment. These roles must not be exchanged. |
| Locally reused share labels | In the primitive, $`Q,A,C`$ are three shares. In the memory proof, $`A`$ is a whole prefix of packets. In the rate proof, $`C`$ means common surviving packets, not the primitive's backup share. |

Packets are delivered or erased within their slot. Released logical outputs become inaccessible to later protocol operations. All forward signaling fits inside the charged packet dimension; only delayed erasure flags travel backward. These conventions prevent a propagation buffer, a delivered output or a free side channel from supplying uncounted memory.

## 1. Recovery must preserve a reference

Preskill §7.3.3 formulates correction using a reference entangled with the encoded input. Successful recovery restores that entanglement while separating the recovered state from the discarded environment. Section 7.3.4 then makes the erasure location known by an orthogonal flag; the lost quantum system remains inaccessible.

This is exactly the distinction needed for streaming. A decoder that reproduces the statistics of selected input states is insufficient. Each labeled output must preserve the unknown source's correlations. The constructions therefore prove an identity channel on the source, including an arbitrary reference. The lower bound can test a particularly convenient input: independent maximally entangled pairs, with one half of each pair supplied as a source. For $`b`$ such sources, $`S(R)=bk`$.

The [model's exact and approximate conventions](../science/model.md#initial-assistance-and-exact-recovery) specify the operational promise. The approximate version uses unconditional EPR overlap for each individual message, including failure outcomes; the [converse](../science/converse.md#3-individual-message-fidelity-and-the-entropy-conclusion) supplies the additional entropy estimate.

## 2. Two recovery regions constrain their common quantum part

Preskill §7.9.3 already states the key static picture: if erasing either of two disjoint parts of a codeword is correctable, the remaining common part must be large enough to support the logical information. The project does not introduce a new Singleton or entropy inequality. Its general form follows from the entropy tools in Chapter 10 and is developed in the [overlap lemma](../science/converse.md#1-the-overlap-inequality):

```math
I(R:QAY)+I(R:QEY)
\le 2S(R)+2S(Q\mid Y).
```

Here $`QA`$ and $`QE`$ are two possible recovery regions; their common quantum register is $`Q`$. If either region recovers $`b`$ independent $`k`$-qubit sources exactly, data processing gives at least $`2bk`$ mutual information for each region. The inequality consequently requires $`S(Q\mid Y)\ge bk`$, hence $`M\ge bk`$.

Conditioning on the classical record matters. The bound charges quantum storage even when the receiver keeps arbitrarily many classical bits. For research-level attribution and the general assisted-coding antecedent, see [Grassl–Huber–Winter](../references/RELATED_WORK.md#ghw2022) and the [storage-intersection comparison](../references/RELATED_WORK.md#sunjafar2025). The remaining task is to identify the two regions in a causal protocol.

## 3. A known secret-sharing primitive supplies a recovery option

Preskill §7.12 illustrates the relation between erasure correction and authorized sets in quantum secret sharing using a three-of-five example. The project's two-of-three encoding and its coherent recycling behavior require the primary research ingredients: [Cleve–Gottesman–Lo](../references/RELATED_WORK.md#qss1999) and especially [Leung's quantum Vernam cipher](../references/RELATED_WORK.md#leung2002).

The [local primitive](../science/primitive.md) makes those ingredients explicit over $`\mathbb F_4`$. One field symbol is a four-dimensional register, physically two qubits. Alice holds source $`S`$ and her half $`L`$ of a maximally entangled pair; Bob holds the other half $`Q`$. For a field element $`a\notin\{0,1\}`$, Alice applies the reversible map

```math
(s,r)\longmapsto(A=r+s,\ C=r+as).
```

The arithmetic is in the four-element field, not arithmetic modulo four. Any two of $`Q,A,C`$ recover the source. When $`A`$ arrives, Bob decodes with $`Q`$ and obtains both the source and a renewed entangled pair with Alice's retained $`C`$. The renewed pair factors from the source and its reference, so the bank can be used again.

If $`A`$ is lost, later sending $`C`$ still permits recovery with $`Q`$. That recovery alone does **not** restore a shared bank: its leftover entanglement is with the erased share. The repair schedule must send a fresh Bell half, and charges that transmission explicitly. This resource distinction is essential to sustained communication. Chapter 10's optional §10.8.1 gives resource-accounting context, but its asymptotic entanglement-assisted protocol is not a proof of finite-bank recycling or return.

## 4. Delayed ACKs identify the two recovery regions

Set $`b=\min\{D,B\}`$ and choose a cut from which both isolated future bursts below are admissible. There must be at least $`b`$ real source arrivals remaining. Compare loss intervals

```math
[0,B-1]
\qquad\text{and}\qquad
[b,b+B-1].
```

The sender emits the first $`b`$ packets before any newly generated ACK can change its actions. Thus both continuations have one common prefix state. Let $`A`$ contain those packets, $`E`$ the sender's accessible remainder and $`Q,Y`$ the receiver's resources at the chosen cut.

For the later burst, packets after $`A`$ are erased through the tested sources' deadlines. Recovery must therefore be possible from $`QAY`$. For the earlier burst, $`A`$ is lost. A virtual processor given $`QEY`$ can simulate the remainder of that branch, including later adaptation and independently fixed future inputs, and obtain the same outputs. It never receives the erased packet or its environment. Giving this processor joint access to the parties' accessible systems relaxes locality for a lower-bound argument; it does not add a communication resource to the physical protocol.

These two recovery descriptions now fit the overlap lemma, giving $`M\ge kb`$. Only the prefix is common; after feedback begins the two encoders may evolve differently. The [full causal reduction](../science/converse.md#2-one-common-prefix-and-two-recovery-regions) accounts for measurements, free classical records and previously released outputs.

An arbitrarily late all-success prefix of a sustained stream supplies a valid cut. This is not a claim at every recent-loss history, where the erasure promise may force future packets to succeed. If only $`r`$ actual arrivals remain, replace $`b`$ throughout by $`\min\{D,B,r\}`$. The short-session constructions need not minimize memory for that smaller tail.

## 5. Turn the primitive into a sustained schedule

The channel promise forbids two erased slots whose separation is from $`B`$ through $`2B`$. A loss at slot $`e`$ therefore guarantees delivery in slots $`e+B,\ldots,e+2B`$. The schedule uses that known clean interval to meet deadlines while replacing damaged entanglement.

For $`1\le D\le B`$, rotate through $`D`$ independent banks. A normal successful transmission delivers its source and renews its bank; the sender reuses that bank only once its positive ACK can have arrived. On learning the first loss, the sender freezes the outstanding recovery shares and buffers new sources. In the clean interval, each repair packet carries three groups: a held recovery share, a queued source and a fresh bank half. Subsequent packets drain the source queue. The [schedule proof](../science/feedback_protocol.md) establishes every deadline and restarts the bank rotation at the correct phase for another burst.

The [same $`B=4,D=2`$ example](../science/interpretation.md#a-complete-burst-repair-example) now has a direct interpretation: two banks cover the blind prefix, and the three packet positions pay for recovery, backlog service and renewal. Retained receiver memory is exactly $`Dk`$ in this regime. A full incoming packet needs at most another $`3k`$ qubits; sender storage is $`O(kB)`$.

For $`D>B`$, the construction ignores feedback and uses the [three-share pipeline](../science/no_feedback_protocol.md): source $`S_t`$ has share times $`t-B,t,t+B`$. The advance share is a source-independent Bell half, so sending it before the source arrives respects causality. The promise prevents two of those share positions from being erased. This costs $`O(kB)`$ receiver memory.

Both constructions return their finite, counted initial bank after a charged flush. They do not consume preshared entanglement proportional to session length. The exact rate $`1/3`$ uses even $`k`$, because each field symbol is two qubits; the [model](../science/model.md#main-memory-theorem) states the padding overhead for odd widths.

## 6. Interpret the result at the correct rate benchmark

The no-feedback benchmark also comes from overlapping recovery. Two admissible periodic loss histories have common surviving packets in one third of their slots. A no-feedback encoder supplies one common emitted state for both histories, and the overlap argument bounds the information in those shared survivors plus the finite initial bank. The [rate proof](../science/rate.md) gives $`k/n\le1/3`$ asymptotically; the pipeline attains it.

This is a deterministic, deadline-constrained argument. It is not obtained by substituting a loss probability into a memoryless erasure-channel capacity formula. The delayed-ACK protocol uses this same forward rate to expose the memory advantage; the project does not determine feedback-assisted capacity.

The foundations come from Preskill's reference, erasure and entropy framework. The entropy overlap, secret-sharing code and recycling mechanism have established research antecedents. The locally supplied steps are the delayed-ACK common-prefix reduction, its sustained clean-cut interpretation, and the matching bounded-bandwidth schedule with finite-bank return. The [related-work account](../references/RELATED_WORK.md) records those boundaries explicitly.

For fixed $`D`$ and growing $`B`$, the receiver-memory saving is of order $`B/D`$. Coherent buffering remains at the sender, and the statement assumes ideal gates, ideal storage and reliable ACKs under the specified deterministic loss promise. The [30-milestone map](MILESTONES.md) develops these connections from local objects to the complete result; the [science index](../science/README.md) leads directly to each authoritative statement and proof.
