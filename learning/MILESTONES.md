# Project understanding map: M01–M30

This is the common understanding map for **Quantum Streaming Memory**. Its 30 stable milestones follow the scientific dependencies of the project. They describe conceptual targets and connections, independently of any reader's background or progress. The [learning index](README.md) gives the entry route; the [Preskill bridge](PRESKILL_BRIDGE.md) translates the selected source into this project's setting.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The foundations must connect reference-preserving communication, entangled assistance, entropy and erasure recovery before time enters the proof. The larger narrative phase then joins the causal converse, two sustained constructions, finite-resource accounting and the rate benchmark. Each phase ends by integrating its components.

| Phase | Milestones | Movement from local to global |
|---|---|---|
| I — Background and preliminaries | [M01](#m01)–[M12](#m12) | A single unknown message and its reference → recovery and entanglement → entropy constraints → a complete timed communication problem |
| II — Narrative and innovation | [M13](#m13)–[M30](#m30) | Loss geometry and a small encoding → causal lower bound and sustained schedules → resource-balanced rate comparison → the complete architecture result and its limits |

## One educational anchor

The selected anchor is John Preskill's **Quantum Information**, using two chapters of the same official [Caltech notes](https://www.preskill.caltech.edu/ph219/):

- **Chapter 7, Quantum Error Correction**, March 2026 working draft, [chap7_26_6A.pdf](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf).
- **Chapter 10, Quantum Shannon Theory**, June 2025 working draft, [chap10_6A_2022.pdf](https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf). The filename retains “2022”; the stated edition follows the document's title page.

Below, **P7** and **P10** refer to those chapters. Page numbers are their printed chapter pages; links open at the corresponding PDF pages. The pointers identify useful passages, not an assignment to read either chapter in full.

Preskill supplies the foundations. The project pages supply the timed model, causal reduction, concrete recycling identities and schedules. In particular, P7 §7.12 illustrates secret sharing with a three-of-five scheme; it does not present this project's recycled two-of-three primitive. Primary papers linked through [related work](../references/RELATED_WORK.md) establish research attribution and proof antecedents. They are not additional educational anchors.

The authoritative parameters and qualifications are in the [model](../science/model.md). Here $`k`$ is the source width in qubits, $`n`$ the charged forward packet width, $`B`$ the burst-span limit, $`D`$ the erasure-flag delay, and the deadline is $`T=B`$. Write $`b=\min\{D,B\}`$, with $`b=B`$ without feedback. At a qualifying cut with only $`r`$ real arrivals remaining, the lower-bound prefactor is instead $`\min\{D,B,r\}`$. The principal order law concerns sustained streams or arbitrarily long finite sessions.

## Phase I — Background and preliminaries

<a id="m01"></a>
### M01 — A quantum message includes its correlations

**Central question.** What must communication preserve when the transmitted state is unknown?

**Understanding target.** Describe a source jointly with an inaccessible reference and distinguish preserving that joint state from reproducing measurement statistics for selected input states. Exact transmission means an identity channel on the labeled sources, including their correlations with other sources and references.

**Dependencies and story role.** No earlier milestone is required. This establishes the smallest operational object used by every recovery and converse argument.

**Conceptual connection.** A maximally entangled test input turns an abstract requirement on arbitrary quantum messages into a concrete source–reference state that a decoder must preserve.

**Source pointers.** Preskill: [P7 §7.3.3, pp. 9–10, Eqs. 7.29–7.32][p7-reference]. Project: [initial assistance and exact recovery](../science/model.md#initial-assistance-and-exact-recovery) and [reference-preserving decoder identities](../science/primitive.md#explicit-two-share-decoders).

<a id="m02"></a>
### M02 — What an erasure flag reveals

**Central question.** What does knowing the location of a loss make recoverable?

**Understanding target.** Distinguish a delivered packet, an orthogonal erasure flag and the inaccessible system carrying the lost state. A flag identifies a missing subsystem; it does not supply its quantum content. Located erasures therefore define a different recovery problem from errors at unknown positions.

**Dependencies and story role.** Builds on [M01](#m01), adding the channel's elementary failure event before any burst or scheduling assumptions.

**Conceptual connection.** Correctability depends on which surviving subsystems retain the source's reference correlations. This connects the physical loss model to secret sharing and to the recovery regions used later.

**Source pointers.** Preskill: [P7 §7.3.4, pp. 10–12, especially Eq. 7.33][p7-erasure]. Project: [slot channel and flag convention](../science/model.md#slots-sources-and-communication) and [recovery when the advance share is erased](../science/primitive.md#sending-the-advance-share-before-source-arrival).

<a id="m03"></a>
### M03 — Recovery is a physical channel

**Central question.** Which operations must a universal communication bound allow?

**Understanding target.** Treat encoding and recovery as arbitrary quantum channels, allowing ancillary systems, measurements, classical records and discarded systems. A dilation may help analyze a channel, but inaccessible purifying systems are not thereby available to the physical protocol.

**Dependencies and story role.** Uses [M01](#m01) and [M02](#m02). It expands the description from a particular code to the full class of operations covered by the converse.

**Conceptual connection.** The common-prefix proof must survive nonunitary operations and adaptive classical control. Its virtual decoders are mathematical channels on specified accessible registers, not an assumption that every encoder is a stabilizer circuit.

**Source pointers.** Preskill: [P7 §7.3.3, pp. 9–10][p7-reference] and [P10 §10.2.4, p. 19, Eqs. 10.89–10.91][p10-data-processing]. Project: [one common prefix and two recovery regions](../science/converse.md#2-one-common-prefix-and-two-recovery-regions).

<a id="m04"></a>
### M04 — Entangled assistance has a location and a cost

**Central question.** What resource does a shared Bell pair provide before a source arrives?

**Understanding target.** Distinguish a locally prepared pair from a pair shared between the endpoints, and count each receiver half as coherent storage. Initial assistance is independent of future sources. A finite bank that is returned after communication has a different resource balance from an unlimited supply of consumed entanglement.

**Dependencies and story role.** Uses [M01](#m01) and [M03](#m03). This introduces the physical resource that will support both successful decoding and sustained reuse.

**Conceptual connection.** The receiver can possess useful assistance without possessing information about a future unknown message. Its value arises through later joint decoding with a transmitted share.

**Source pointers.** Preskill: [P10 §10.4, opening pp. 31–33, especially Eq. 10.171][p10-pure-entanglement]. Project: [initial assistance and finite-bank return](../science/model.md#initial-assistance-and-exact-recovery) and [the primitive's registers](../science/primitive.md#registers-and-physical-alphabet).

<a id="m05"></a>
### M05 — No-cloning constrains recovery sets

**Central question.** Why can two disjoint collections of systems not both recover an arbitrary quantum message?

**Understanding target.** Relate recovery of an unknown source to the no-cloning obstruction. When two alternative surviving regions must each support recovery, their shared quantum resource becomes essential; classical redundancy alone does not establish the same possibility.

**Dependencies and story role.** Uses [M01](#m01) and [M02](#m02). It gives the qualitative obstruction before entropy measures its size.

**Conceptual connection.** The streaming converse will produce two hypothetical decoders from different loss histories. Their overlapping access is the physical reason a receiver-memory lower bound can exist even with unlimited sender memory and forward bandwidth.

**Source pointers.** Preskill: [P7 §7.9.2, pp. 25–26][p7-no-cloning]. Project: [the overlap inequality](../science/converse.md#1-the-overlap-inequality) and [its prior-work setting](../references/RELATED_WORK.md#entropy-overlapping-recovery-and-quantum-storage).

<a id="m06"></a>
### M06 — Entropy and memory capacity are different quantities

**Central question.** How does an entropy argument constrain a dimension-limited memory?

**Understanding target.** Distinguish von Neumann entropy, quantum conditional entropy and the hardware bound $`\log_2\dim Q_y\le M`$ in each classical branch. When $`Y`$ is a classical record, $`S(Q\mid Y)`$ is an average of branch entropies and is at most $`M`$. Local mixedness alone is not evidence of useful shared entanglement.

**Dependencies and story role.** Uses [M01](#m01) and [M04](#m04). It translates the physical storage resource into the quantity controlled by the proof.

**Conceptual connection.** Unlimited classical records can be conditioned on without removing the bound on retained coherent space. Retained memory must also be distinguished from transient incoming-packet workspace.

**Source pointers.** Preskill: [P10 §§10.2.1–10.2.2, pp. 15–17][p10-entropy]. Project: [receiver-memory convention](../science/model.md#deadline-and-receiver-memory) and [conditioning the overlap inequality](../science/converse.md#1-the-overlap-inequality).

<a id="m07"></a>
### M07 — Strong subadditivity controls conditioning

**Central question.** Which entropy relation remains valid when conditioning systems are quantum?

**Understanding target.** Interpret strong subadditivity as nonnegative quantum conditional mutual information and as the statement that additional conditioning cannot increase conditional entropy. Understand that the weak-monotonicity form used by the project follows through purification; it is not obtained by treating quantum systems as ordinary random variables.

**Dependencies and story role.** Uses [M03](#m03) and [M06](#m06). It supplies the main entropy relation needed to quantify overlap.

**Conceptual connection.** The project combines weak monotonicity with subadditivity to limit how much reference information two overlapping recovery regions can jointly contain.

**Source pointers.** Preskill: [P10 §10.2.3, pp. 17–19, Eqs. 10.80, 10.84–10.85][p10-ssa]. Project: [derivation of the overlap inequality](../science/converse.md#1-the-overlap-inequality) and [the entropy bridge](PRESKILL_BRIDGE.md).

<a id="m08"></a>
### M08 — Decoding cannot create reference information

**Central question.** What must already be present in a system from which a message can be recovered?

**Understanding target.** Use data processing to relate the mutual information between a reference and a decoder's input to that between the reference and its recovered output. Perfect recovery of a maximally entangled $`d`$-dimensional source requires $`2\log_2 d`$ bits of reference mutual information in the accessible recovery region.

**Dependencies and story role.** Uses [M03](#m03), [M06](#m06) and [M07](#m07). It turns the operational recovery requirement into an entropy lower bound.

**Conceptual connection.** Entropy overlap provides an upper bound; successful decoding provides the matching lower demand. Their combination, rather than either statement alone, charges recovery to memory.

**Source pointers.** Preskill: [P10 §10.2.4, p. 19, Eqs. 10.89–10.91][p10-data-processing]. Project: [individual-message fidelity and the entropy conclusion](../science/converse.md#3-individual-message-fidelity-and-the-entropy-conclusion).

<a id="m09"></a>
### M09 — The overlap obstruction behind Singleton bounds

**Central question.** How much common quantum space is required by two successful recovery regions?

**Understanding target.** Connect the quantum Singleton argument to the inequality $`I(R:QA)+I(R:QE)\le 2S(R)+2S(Q)`$. Identify the common system $`Q`$ and understand why mixed states and free classical conditioning do not invalidate the bound.

**Dependencies and story role.** Combines [M05](#m05), [M07](#m07) and [M08](#m08). This is the first synthesis of the physical obstruction and its quantitative proof.

**Conceptual connection.** The entropy inequality is inherited. The new task in streaming is to justify the relevant recovery regions from causal timing, without assuming that the whole adaptive encoder is common to both histories.

**Source pointers.** Preskill: [P7 §7.9.3, pp. 26–27, especially Eq. 7.114][p7-singleton] and [P10 §10.2.3][p10-ssa]. Project: [the overlap lemma](../science/converse.md#1-the-overlap-inequality), [Grassl–Huber–Winter](../references/RELATED_WORK.md#ghw2022) and [Sun–Jafar](../references/RELATED_WORK.md#sunjafar2025).

<a id="m10"></a>
### M10 — Secret sharing joins recovery and privacy

**Central question.** How can several shares jointly contain a message while one share reveals nothing about it?

**Understanding target.** Relate authorized recovery sets, correctable erased sets and independence of an unauthorized share from the source reference. Distinguish this distributed encoding from storing copies of an unknown state.

**Dependencies and story role.** Uses [M02](#m02), [M05](#m05) and [M09](#m09). It supplies the structural idea behind the constructive side of the project.

**Conceptual connection.** A threshold recovery property can support both advance assistance and later retransmission. The project will use a particular two-of-three encoding and an explicit recovery factorization.

**Source pointers.** Preskill: [P7 §7.12, pp. 38–40][p7-secret-sharing], whose worked example is three-of-five. Project: [the two-of-three primitive](../science/primitive.md), with the inherited secret-sharing foundation credited to [Cleve–Gottesman–Lo](../references/RELATED_WORK.md#qss1999).

<a id="m11"></a>
### M11 — Recovery quality needs precise quantifiers

**Central question.** What does a small communication error promise actually guarantee?

**Understanding target.** Interpret entanglement fidelity as a squared overlap on the source and reference. Distinguish unconditional fidelity from fidelity conditioned on a declared success, and individual-output promises from joint-window fidelity. Recovery must satisfy the stated promise for every admissible erasure pattern and by each output's deadline.

**Dependencies and story role.** Uses [M01](#m01), [M03](#m03) and [M08](#m08). It fixes the quality criterion before the robust converse is introduced.

**Conceptual connection.** A meaningful streaming bound should use the individual-message guarantee directly. It must not silently assume that a whole group of outputs has a stronger joint guarantee.

**Source pointers.** Preskill: [P10 §10.3.2, concluding discussion on pp. 30–31, Eqs. 10.161–10.163][p10-entanglement-fidelity]. Project: [approximate lower-bound convention](../science/model.md#approximate-lower-bound) and [converse assumptions](../science/converse.md#statement-and-assumptions).

<a id="m12"></a>
### M12 — Assemble the timed communication problem

**Central question.** What changes when unknown sources arrive continuously and every source has its own deadline?

**Understanding target.** Assemble source arrival, flagged loss, feedback delay, reference-preserving recovery, counted receiver memory and finite entangled assistance into one operational model. Distinguish a block-code recovery statement from a causal streaming guarantee, and distinguish retained memory from bandwidth and transient workspace.

**Dependencies and story role.** Integrates [M02](#m02), [M04](#m04), [M09](#m09), [M10](#m10) and [M11](#m11). This closes the foundations phase with the complete question that the project answers.

**Conceptual connection.** The central comparison holds deadline and forward bandwidth fixed while varying when the sender learns a loss. Every forward resource is charged, and a released output cannot become hidden future storage.

**Source pointers.** Preskill: [P7 §7.9.3][p7-singleton] and [P10 §10.8.1, pp. 60–62][p10-father], the latter only as asymptotic entanglement-resource context. Project: [model and assumptions](../science/model.md) and [what feedback changes](../science/interpretation.md#what-feedback-changes).

## Phase II — Narrative and innovation

<a id="m13"></a>
### M13 — The loss promise creates a clean repair interval

**Central question.** What deterministic future delivery follows from observing one loss?

**Understanding target.** Relate the $`2B+1`$-slot window definition to the prohibition on two losses separated by $`B,\ldots,2B`$ slots. A loss at $`e`$ certifies delivery at $`e+B,\ldots,e+2B`$. Losses may have holes, and repeated bursts remain possible.

**Dependencies and story role.** Uses [M02](#m02) and [M12](#m12). It extracts the local timing fact that will power every repair schedule.

**Conceptual connection.** A worst-case deadline requires a deterministic channel restriction. The certified clean interval is a scheduling resource supplied by this precise promise, not an inference from an average erasure probability.

**Source pointers.** Preskill: [P7 §7.3.4][p7-erasure] for located-erasure recovery. Project: [the deterministic erasure promise and its equivalence](../science/model.md#the-deterministic-erasure-promise).

<a id="m14"></a>
### M14 — Choose a valid cut and the minimum deadline

**Central question.** Where can a memory lower bound be imposed, and why is $`T=B`$ the minimum feasible deadline?

**Understanding target.** Use an initial burst and no-signalling to rule out earlier delivery of a fresh source. Identify cuts admitting both test continuations and enough future real inputs: $`b=\min\{D,B\}`$, or $`\min\{D,B,r\}`$ for a tail of $`r`$ arrivals. An arbitrarily late clean history can qualify; a recent-loss history need not.

**Dependencies and story role.** Uses [M04](#m04), [M05](#m05), [M12](#m12) and [M13](#m13). It establishes the domain of the causal converse before choosing its registers.

**Conceptual connection.** Pre-cut $`Q`$ is source-independent assistance, not a stored copy of future inputs. Already released outputs and packets remaining in flight cannot supply uncounted memory.

**Source pointers.** Preskill: [P7 §7.3.3][p7-reference] and [§7.9.2][p7-no-cloning]. Project: [deadline and memory](../science/model.md#deadline-and-receiver-memory), [the main theorem's cut and finite-tail qualifications](../science/model.md#main-memory-theorem) and [converse assumptions](../science/converse.md#statement-and-assumptions).

<a id="m15"></a>
### M15 — Build the fixed-qubit shared encoder

**Central question.** Which small encoding makes every pair of three shares sufficient?

**Understanding target.** Interpret the reversible map $`(s,r)\mapsto(r+s,r+as)`$ over $`\mathbb F_4`$, with $`a\notin\{0,1\}`$, and the three explicit inverse decoders. Each decoder recovers the source while factoring the residual entanglement. A field symbol is two physical qubits, so the exact $`n=3k`$ implementation uses even $`k`$; odd widths require the stated padding.

**Dependencies and story role.** Uses [M04](#m04), [M10](#m10) and [M12](#m12). This supplies the local quantum operation used by both schedules.

**Conceptual connection.** Fixed alphabet size prevents a hidden growth of physical resources with burst length. Field arithmetic here is not integer arithmetic modulo four.

**Source pointers.** Preskill: [P7 §7.12][p7-secret-sharing] for the secret-sharing framework. Project: [registers and alphabet](../science/primitive.md#registers-and-physical-alphabet), [decoders](../science/primitive.md#explicit-two-share-decoders), [grouping and workspace](../science/primitive.md#grouping-and-workspace), and [inherited QSS attribution](../references/RELATED_WORK.md#qss1999).

<a id="m16"></a>
### M16 — Recycling and advance sharing use the same primitive

**Central question.** How can the encoding reuse assistance or send a share before the source exists?

**Understanding target.** Explain why successful receipt of $`A`$ lets Bob decode from $`QA`$ and returns a Bell pair with Alice's retained $`C`$. If $`A`$ is lost, recovery from $`QC`$ does not itself restore a shared bank. Sending $`Q`$ before source arrival is causal because it is initially a source-independent Bell half.

**Dependencies and story role.** Uses [M01](#m01), [M02](#m02), [M04](#m04) and [M15](#m15). It connects one exact decoder to two distinct temporal uses.

**Conceptual connection.** Recovering payload and replenishing assistance are separate resource obligations. The later repair schedule must pay for a fresh pair when recycling fails.

**Source pointers.** Preskill: [P7 §7.3.3][p7-reference] for recovery factorization and [§7.12][p7-secret-sharing] for secret sharing. Project: [successful recycling](../science/primitive.md#successful-transmission-recycling), [advance sharing](../science/primitive.md#sending-the-advance-share-before-source-arrival), and explicit primitive attribution to [Leung's communication cipher](../references/RELATED_WORK.md#leung2002).

<a id="m17"></a>
### M17 — Freeze only the prefix before feedback

**Central question.** Which part of an adaptive sender's state is identical in two loss histories?

**Understanding target.** Construct the common state after the first $`b`$ emissions, before any relevant new ACK is available. Identify $`R,Q,A,E,Y`$: reference, pre-cut receiver memory, prefix packets, accessible sender remainder and classical record. Here $`E`$ is the sender's accessible remainder, not the inaccessible environment denoted by that letter in some textbook discussions.

**Dependencies and story role.** Uses [M03](#m03), [M12](#m12) and [M14](#m14). This is the causal step connecting a timed adaptive protocol to the static entropy framework.

**Conceptual connection.** Pre-cut ACKs have the same values and arrival times in both continuations. Later sender operations may differ after new feedback arrives; the proof does not freeze the entire adaptive encoding.

**Source pointers.** Preskill: [P7 §7.3.3][p7-reference] and [P10 §10.2.4][p10-data-processing] for reference systems and channel dilation. Project: [common state before the first relevant ACK](../science/converse.md#common-state-before-the-first-relevant-ack).

<a id="m18"></a>
### M18 — Obtain two recoveries from one common state

**Central question.** How do the two loss continuations identify the recovery regions $`QAY`$ and $`QEY`$?

**Understanding target.** Explain why the later burst forces the tested outputs to be recoverable from the prefix packets and receiver memory. For the earlier burst, describe a virtual processor that jointly accesses the receiver memory and sender remainder, simulates the future adaptive branch and recovers the same sources.

**Dependencies and story role.** Uses [M09](#m09), [M14](#m14) and [M17](#m17). It completes the reduction that makes the overlap lemma applicable.

**Conceptual connection.** The virtual processor receives neither the erased prefix nor inaccessible references or past released outputs. Collecting logical outputs for the proof does not authorize the physical receiver to reuse released data as storage.

**Source pointers.** Preskill: [P7 §7.9.3][p7-singleton] for the two-recovery logic. Project: [the two recovery regions](../science/converse.md#2-one-common-prefix-and-two-recovery-regions) and [released outputs are not hidden memory](../science/converse.md#released-outputs-are-not-a-hidden-memory-resource).

<a id="m19"></a>
### M19 — Charge the overlap to coherent storage

**Central question.** Why must the receiver retain at least $`kb`$ qubits at a qualifying cut?

**Understanding target.** Combine the two decoding demands with the overlap inequality conditioned on $`Y`$, then use $`S(Q\mid Y)\le M`$. The result is independent of forward bandwidth and sender-memory size. Restore the shorter-tail prefactor whenever fewer than $`b`$ actual inputs remain.

**Dependencies and story role.** Synthesizes [M06](#m06), [M08](#m08), [M09](#m09) and [M18](#m18). This is the exact memory converse.

**Conceptual connection.** The bound concerns coherent recovery capacity shared across alternative futures. It does not assert that the pre-cut memory already contains the future message: initially $`I(R:Q)`$ can be zero.

**Source pointers.** Preskill: [P10 §10.2.3][p10-ssa] and [§10.2.4][p10-data-processing]. Project: [conditional overlap inequality](../science/converse.md#1-the-overlap-inequality), [entropy conclusion](../science/converse.md#3-individual-message-fidelity-and-the-entropy-conclusion), and [precise theorem statement](../science/model.md#main-memory-theorem).

<a id="m20"></a>
### M20 — Preserve robustness message by message

**Central question.** How does imperfect recovery weaken the memory bound without accumulating a whole-window error?

**Understanding target.** Interpret the penalty $`f_d(\epsilon)=h_2(\epsilon)+\epsilon\log_2(d^2-1)`$ and the bound $`M\ge b[k-f_d(\epsilon)]`$ for $`d=2^k`$. Independent references allow individual recovery guarantees to be combined. The derivation uses conditional-entropy concavity under bilateral twirling, not a claim that correlated twirling is mutual-information monotone.

**Dependencies and story role.** Uses [M07](#m07), [M08](#m08), [M11](#m11) and [M19](#m19). It extends the exact obstruction to the project's operational error convention.

**Conceptual connection.** The admissible error range, fixed-dimensional unconditional output and zero-clamping of negative bounds matter. The same finite-tail replacement applies; no high joint-window fidelity or $`b\epsilon`$ substitution is assumed.

**Source pointers.** Preskill: [P10 §10.2.3][p10-ssa] and [§10.3.2, concluding pp. 30–31][p10-entanglement-fidelity]. Project: [individual-fidelity derivation](../science/converse.md#3-individual-message-fidelity-and-the-entropy-conclusion) and [error conventions](../science/model.md#approximate-lower-bound).

<a id="m21"></a>
### M21 — Identify the required initial entanglement

**Central question.** Can a sufficiently large but separable initial memory replace the entangled bank?

**Understanding target.** Interpret the supporting conditional entanglement-of-formation bound on initial sender–receiver assistance. An artificial pure-ensemble label can be supplied to the virtual decoders while the physical protocol ignores it. The unconditional fidelity promise survives that refinement; individual ensemble components need not each meet the fidelity bound.

**Dependencies and story role.** Uses [M04](#m04), [M06](#m06), [M19](#m19) and [M20](#m20). It strengthens the resource interpretation of the converse without changing the main storage theorem.

**Conceptual connection.** Local entropy alone cannot supply the necessary shared coherence. This is a bound on an initial entanglement measure, not a claim about entanglement consumption rate, distillable entanglement or globally optimal catalysts.

**Source pointers.** Preskill: [P10 §10.4][p10-pure-entanglement] and [§10.5.1, pp. 36–38][p10-mixed-entanglement] for pure- and mixed-state entanglement context. The project supplies the convex-roof definition and proof in [initial-entanglement resource interpretation](../science/converse.md#4-supporting-resource-interpretation-initial-entanglement).

<a id="m22"></a>
### M22 — Interleave banks without premature reuse

**Central question.** How can normal transmission continue while the sender waits $`D`$ slots for a flag?

**Understanding target.** Follow the invariant for $`D`$ independent banks when $`D\le B`$: successful delivery recycles a bank, and the sender reuses it only when its positive ACK is available. Identify the first unresolved bank uses when a loss occurs and why the sender freezes them when the first negative flag arrives.

**Dependencies and story role.** Uses [M13](#m13), [M14](#m14) and [M16](#m16). This turns the local recycling identity into the normal-operation phase of a stream.

**Conceptual connection.** ACK latency sets how many independent shared resources must be simultaneously outstanding. Both endpoints can infer the layout from the same public parameters and delayed flag history, without an uncharged forward header.

**Source pointers.** Preskill: [P7 §7.3.3][p7-reference] for coherent recovery and [P10 §10.4][p10-pure-entanglement] for shared pairs. Project: [normal bank invariant](../science/feedback_protocol.md#the-bank-invariant-during-normal-operation) and [loss detection and freezing](../science/feedback_protocol.md#detecting-a-loss-and-freezing-the-banks).

<a id="m23"></a>
### M23 — Repair loss and clear the queue before deadlines

**Central question.** How can the same $`3k`$-qubit packet budget repair banks and serve arriving sources?

**Understanding target.** Explain the two stages of the clean-interval schedule: first send a held recovery share, a queued source and a fresh bank half; then send two queued sources per slot. Track the first $`D`$ affected sources to their exact deadlines and the backlog to its disappearance by $`e+2B-1`$.

**Dependencies and story role.** Uses [M13](#m13) and [M22](#m22). It supplies the scheduling mechanism that makes prompt feedback useful at a hard deadline.

**Conceptual connection.** The sender's coherent queue absorbs the period during which transmission cannot safely proceed. The receiver retains the short bank rotation while bandwidth in the certified clean interval pays for both recovery and renewal.

**Source pointers.** Preskill: [P7 §7.3.4][p7-erasure] for erasure recovery. Project: [repair and queue service](../science/feedback_protocol.md#repair-and-queue-service), [deadline calculation](../science/feedback_protocol.md#queue-calculation-and-deadlines), and the complete [B = 4, D = 2 example](../science/interpretation.md#a-complete-burst-repair-example).

<a id="m24"></a>
### M24 — Sustain and terminate the feedback protocol

**Central question.** Why do repeated bursts and a finite stopping time preserve the bank invariant?

**Understanding target.** Resume the bank cycle from the bank used at the first loss, rather than an assumed global phase. Verify that every replacement ACK precedes its bank's reuse. Include arbitrary public source horizons, even $`N\lt D`$, and explain exact return of the $`Dk`$-ebit bank within the charged $`N+2B`$ slots.

**Dependencies and story role.** Combines [M04](#m04), [M22](#m22) and [M23](#m23). This closes the feedback construction as a sustained, finite-resource protocol.

**Conceptual connection.** Retained receiver space is $`Dk`$, sender space is at most $`Bk`$, and incoming receiver workspace adds at most $`3k`$. Optional ordered release has its separately charged output buffer; it is not assumed in the main bound.

**Source pointers.** Preskill: [P7 §7.3.3][p7-reference] and [P10 §10.4][p10-pure-entanglement] for reference-preserving recovery and pairs. Project: [rotation](../science/feedback_protocol.md#correct-bank-rotation-and-repeated-bursts), [resources](../science/feedback_protocol.md#storage-and-physical-resources), [finite return](../science/feedback_protocol.md#arbitrary-finite-horizon-and-exact-bank-return), and [optional ordered release](../science/feedback_protocol.md#optional-variant-strictly-ordered-output-release).

<a id="m25"></a>
### M25 — Run the no-feedback pipeline causally

**Central question.** What replaces bank recycling when the sender cannot react before the deadline?

**Understanding target.** Follow the three shares for source $`S_j`$ at slots $`j-B,j,j+B`$. The loss promise allows at most one of these positions to be erased, so two shares suffice by the deadline. Initial shared pairs supply the advance shares whose transmission times precede the session.

**Dependencies and story role.** Uses [M13](#m13), [M15](#m15) and [M16](#m16). It provides the second construction and the upper bound for $`D>B`$ by ignoring feedback.

**Conceptual connection.** The early share is independent of the not-yet-arrived source. The schedule reserves three groups per slot and retains at most $`2Bk`$ qubits at either endpoint, with a finite initial $`Bk`$-ebit bank.

**Source pointers.** Preskill: [P7 §7.3.4][p7-erasure] and [§7.12][p7-secret-sharing]. Project: [advance sharing and transmission times](../science/no_feedback_protocol.md#advance-sharing-and-the-three-transmission-times), [receiver storage](../science/no_feedback_protocol.md#receiver-storage-including-the-tail), and [sender storage](../science/no_feedback_protocol.md#sender-storage-and-transient-workspace).

<a id="m26"></a>
### M26 — Close the no-feedback resource balance

**Central question.** How can a pipeline stop without consuming its initial assistance?

**Understanding target.** Append $`B`$ dummy source halves entangled with locally retained references. Their decoded outputs restore $`Bk`$ shared ebits independently of real payloads and the environment. Count all advance, middle and final transmissions through the $`N+2B`$-slot session, including $`N\lt B`$.

**Dependencies and story role.** Uses [M04](#m04) and [M25](#m25). It completes the no-feedback protocol's finite-horizon resource accounting.

**Conceptual connection.** Returning a bank is an operational obligation with a paid tail, not a declaration that consumed assistance is free. Counting future shares, unresolved sources and returned seed together proves storage remains bounded throughout that tail.

**Source pointers.** Preskill: [P7 §7.3.3][p7-reference] and [P10 §10.4][p10-pure-entanglement]. Project: [exact return for every finite horizon](../science/no_feedback_protocol.md#exact-return-for-every-finite-source-horizon), [tail storage count](../science/no_feedback_protocol.md#receiver-storage-including-the-tail), and [finite-session rate](../science/no_feedback_protocol.md#rate-and-role-in-the-memory-theorem).

<a id="m27"></a>
### M27 — Compare periodic loss histories

**Central question.** Which admissible histories bound the entire no-feedback stream's forward rate?

**Understanding target.** Compare periodic losses occupying the first or second block of $`B`$ slots in each $`3B`$-slot period. Both obey the same loss promise, while their common surviving positions occupy the final third. Count the intersection through the finite transmission horizon, including the deadline tail.

**Dependencies and story role.** Uses [M09](#m09), [M13](#m13), [M18](#m18) and [M19](#m19). It applies the recovery-overlap idea globally, rather than only to a short common prefix.

**Conceptual connection.** A no-feedback sender supplies a common emitted state for both complete histories. This stronger common-state property is unavailable to a general adaptive feedback encoder.

**Source pointers.** Preskill: [P7 §7.9.3][p7-singleton]. Project: [periodic patterns](../science/rate.md#1-two-admissible-periodic-erasure-patterns), [common no-feedback state](../science/rate.md#2-a-common-no-feedback-state), and [exact overlap count](../science/rate.md#3-entropy-and-the-exact-overlap-count).

<a id="m28"></a>
### M28 — Extract the qualified rate benchmark

**Central question.** Under which resource and error limits is the no-feedback rate exactly $`1/3`$?

**Understanding target.** Interpret the finite-horizon rate inequality, including its initial-assistance term and per-message fidelity penalty. For fixed $`B`$, finite or sublinear initial assistance and exact or vanishing-error transmission give $`k/n\le1/3`$. The pipeline attains the asymptotic bound at even source widths, with its flush charged.

**Dependencies and story role.** Combines [M20](#m20), [M21](#m21), [M26](#m26) and [M27](#m27). It supplies the common bandwidth benchmark for the architecture comparison.

**Conceptual connection.** The delayed-ACK construction operates at this same rate, exposing a memory advantage. The result does not determine feedback capacity or establish a fixed-nonzero-error strong converse.

**Source pointers.** Preskill: [P10 §10.8.1, pp. 60–62][p10-father] for asymptotic resource-bookkeeping context, not this deterministic capacity proof. Project: [finite assistance](../science/rate.md#4-finite-assistance-and-initially-local-workspace), [asymptotic benchmark and limits](../science/rate.md#5-asymptotic-benchmark-and-limits-of-the-claim), and [the stated rate theorem](../science/model.md#forward-rate-benchmark).

<a id="m29"></a>
### M29 — Separate inherited ingredients, proof and finite checks

**Central question.** Which parts are established ingredients, which are the project's temporal argument, and what do the programs verify?

**Understanding target.** Identify the inherited entropy/Singleton reasoning, threshold secret sharing, communication-cipher recycling and finite catalytic assistance. Locate the project's common-prefix reduction and sustained deadline schedule. Distinguish exact finite-field decoder checks and bounded schedule audits from proofs covering arbitrary protocols and all admissible histories.

**Dependencies and story role.** Integrates [M09](#m09), [M10](#m10), [M17](#m17), [M18](#m18), [M24](#m24), [M26](#m26) and [M28](#m28). It establishes how the complete result is supported and attributed.

**Conceptual connection.** A construction check can catch bank-rotation or tail-accounting errors; it cannot prove a universal converse or literature priority. Existing ACK retransmission and convolutional-memory results must be compared under their actual models.

**Source pointers.** Preskill: [P7 §§7.9.3][p7-singleton] and [7.12][p7-secret-sharing] for foundational antecedents. Project: [related work and precise subtraction](../references/RELATED_WORK.md), [what each program checks](../verification/README.md#what-each-program-checks), and [verification boundaries](../verification/README.md#boundaries-of-verification).

<a id="m30"></a>
### M30 — Synthesize the architecture law and its limits

**Central question.** What does faster loss feedback change when deadline and forward bandwidth are held fixed?

**Understanding target.** Combine the converse and constructions into $`M_{\min}=\Theta(k\min\{D,B\})`$ at $`T=B`$ for sustained streams. Explain the receiver-memory saving of order $`B/D`$ when $`D\le B`$, while coherent backlog remains at the sender. Preserve finite-tail qualifications, incoming workspace, finite-bank return and the exact even-width scope of rate $`1/3`$.

**Dependencies and story role.** Integrates [M19](#m19), [M20](#m20), [M21](#m21), [M24](#m24), [M26](#m26), [M28](#m28) and [M29](#m29). This closes the narrative phase with the complete result, its mechanism and evidence boundary.

**Conceptual connection.** The theorem concerns placement of ideal coherent storage under a specific deterministic loss promise and reliable delayed flags. It does not establish a total-memory saving, noisy-memory lifetime law, feedback capacity or a complete rate–delay–memory region.

**Source pointers.** Preskill: [P7 §7.9.3][p7-singleton] and [P10 §10.8.1][p10-father] for the foundational recovery and resource viewpoints. Project: [main theorem and qualifications](../science/model.md#main-memory-theorem), [what feedback changes](../science/interpretation.md#what-feedback-changes), [limits of the comparison](../science/interpretation.md#limits-of-the-comparison), and [consequence and scope](../references/RELATED_WORK.md#consequence-and-scope).

[p7-reference]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=15
[p7-erasure]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=16
[p7-no-cloning]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=31
[p7-singleton]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=32
[p7-secret-sharing]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=44
[p10-entropy]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=21
[p10-ssa]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=23
[p10-data-processing]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=25
[p10-entanglement-fidelity]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=36
[p10-pure-entanglement]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=37
[p10-mixed-entanglement]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=42
[p10-father]: https://www.preskill.caltech.edu/ph219/chap10_6A_2022.pdf#page=66

