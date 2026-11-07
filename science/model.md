# Model and main results

An unknown quantum state cannot be copied into a retransmission buffer. If a packet is lost, a sender must recover the state from a distributed encoding or have arranged redundancy before the loss. This project asks how much coherent storage the receiver must retain when every newly arriving state has a strict delivery deadline, and how that storage changes when erasure acknowledgments reach the sender sooner.

The comparison fixes the forward packet budget and the deadline. It counts the entangled bank that makes retransmission possible, permits unlimited classical records, and includes a finite procedure for returning the bank. The main result is an optimal-order dependence on acknowledgment latency, with constants independent of the burst length.

## Slots, sources and communication

Time is divided into slots $`t=0,1,2,\ldots`$. At the start of slot $`t`$, a fresh register $`S_t`$ of $`k`$ logical qubits becomes available to the sender. Its state is unknown and may be entangled with inaccessible references and other source registers. The sender has no access to a source before its arrival. A finite session has a publicly specified horizon $`N`$; this parameter is part of the protocol, not an uncharged end-of-stream message.

In each slot, the sender transmits a system of dimension at most $`2^n`$. Equivalently, use fixed $`n`$-qubit packets and pad unused positions with a fixed state. Each packet is either delivered intact or erased, with an orthogonal flag available to the receiver by the end of that same slot. No packet remains in flight across a slot boundary. A quantum erasure can transfer the lost system to an inaccessible environment; it need not destroy the state.

**Every forward communication resource is charged.** Headers, any classical forward messages, and any distinctions encoded by packet size, timing or occupancy must fit in the same bounded-dimension slot system. The stated packet layouts are determined by public parameters and, in the feedback protocol, the ACK history available to the sender. The receiver can reconstruct that history from its flags and the known delay, so no variable headers or free side channel are required. The sender may have arbitrary local quantum memory in the lower bound.

The reverse link carries only the reliable erasure flag for each slot. A flag generated in slot $`t`$ reaches the sender before encoding slot $`t+D`$, and not earlier, where $`D\ge1`$ is an integer. The sender can condition on all flags already received. Set $`D=\infty`$ for no feedback. No reverse quantum communication or message-dependent feedback is supplied. The receiver may use the erasure flag immediately.

## The deterministic erasure promise

Fix an integer $`B\ge1`$. In every $`W=2B+1`$ consecutive slots, all erased positions must lie inside an interval of at most $`B`$ consecutive slots. This is a bound on the span of losses within a window; the loss positions inside that span may have holes.

An equivalent definition is useful in proofs: **two erased slots may not be separated by a distance from $`B`$ through $`2B`$, inclusive**. Indeed, such a pair violates a window of length $`2B+1`$; conversely, any violating window contains such a pair. In particular, an erasure at $`e`$ guarantees successful delivery in slots

```math
e+B,e+B+1,\ldots,e+2B.
```

The model permits repeated bursts. It includes an isolated run of $`B`$ losses and a periodic pattern of $`B`$ consecutive losses every $`3B`$ slots. It excludes unrestricted adversarial erasures and iid erasures with an unlimited number of consecutive losses. A deterministic hard deadline could not be guaranteed for every history of the latter channel without an additional restriction.

Both constructions and both lower bounds use this same $`2B+1`$ promise. Enlarging the window changes the admissible channel family and is not covered by the capacity statement below.

## Deadline and receiver memory

The receiver must output $`\widehat S_t`$ by the end of slot $`t+T`$. The main result sets $`T=B`$. This is the smallest feasible worst-case delay: an admissible history can erase slots $`0,\ldots,B-1`$, so no receiver can learn the fresh source $`S_0`$ earlier by local processing of source-independent initial assistance.

Outputs may be released as soon as they are recovered, including out of order. A released output is delivered to an external user and becomes **inaccessible to all later protocol operations**. It cannot be borrowed as a hidden memory. An unreleased output counts as receiver memory. The constructions also give optional ordered-release bounds in their own accounts.

Let $`Q`$ denote all receiver quantum systems retained at a slot boundary after that slot's processing and releases. These include Bell halves, unresolved shares, ancillary registers and any unreleased data. Let $`Y`$ be the receiver's classical record, which is free. A bound $`M`$ means

```math
\log_2\dim Q_y\le M
```

in every branch $`y`$ and at every such cut, including the initial cut. It is a worst-case dimension bound, not a mean occupation or entropy budget. Any quantum workspace used during a slot is also a physical resource. We report retained memory and the extra incoming-packet workspace separately. The lower bound on retained memory is automatically a lower bound on total hardware; the upper bounds below include at most another $`3k`$ qubits for the incoming padded packet, using in-place decoders.

All local gates and quantum memories are ideal. Feedback is reliable with the stated delay. The result concerns the amount of coherent storage, not its lifetime under noise or an implementation threshold.

## Initial assistance and exact recovery

The parties may initially share a finite state on sender register $`E_0`$ and receiver register $`Q_0`$, independent of every future source. Shared classical information can be included in $`Y`$. Receiver halves count in $`M`$; sender halves count in the construction's sender storage. The initial assistance may depend on $`B,D,k`$ but is finite and independent of the session length $`N`$.

The exact constructions use a finite Bell bank and return the same number of maximally entangled pairs after a charged, source-free flush. The returned bank factors from every delivered source and the environment; register swaps can place it in the designated bank registers. The flush cost is included in finite-session rate accounting. An endless stream is understood through the sustained protocol or arbitrarily long finite sessions, not by consuming an uncounted supply of preshared entanglement.

Exact recovery means the joint channel from all source registers to the labeled outputs is the identity for every admissible erasure history. It therefore preserves entanglement with arbitrary inaccessible references. The lower bounds allow arbitrary causal quantum operations, measurements and classical records; they do not assume a stabilizer or linear encoder.

## Main memory theorem

Write $`b=\min\{D,B\}`$, with $`b=B`$ when $`D=\infty`$.

**Theorem 1 — acknowledgment latency and coherent storage.** For sustained streaming at $`T=B`$ (equivalently, protocols for arbitrarily long finite source horizons), every exact protocol obeys

```math
M\ge kb.
```

The bound holds at the initial cut of a session with $`N\ge b`$, and at any clean cut with at least $`b`$ real source arrivals remaining at which the two isolated test continuations in the [converse](converse.md) are admissible. For a shorter finite tail with $`r`$ arrivals remaining, the same proof gives $`M\ge k\min\{D,B,r\}`$. Consequently the displayed sustained bound constrains the peak receiver memory of a protocol required to work on the entire erasure family and arbitrarily long sessions. It is independent of forward bandwidth and sender memory. It is not a lower bound at every post-loss history, where the promise may force future delivery and rule out a test continuation.

For every positive even $`k`$, fixed-dimension share encoders attain the following bounds with $`n=3k`$ physical qubits per slot:

| Feedback regime | Initial Bell bank | Retained receiver memory | Total receiver space sufficient | Construction |
|---|---:|---:|---:|---|
| $`1\le D\le B`$ | $`Dk`$ ebits | $`Dk`$ qubits | $`(D+3)k`$ qubits | [Rotating banks and repair](feedback_protocol.md) |
| $`D>B`$ or no feedback | $`Bk`$ ebits | At most $`2Bk`$ qubits | At most $`(2B+3)k`$ qubits | [Three-share pipeline](no_feedback_protocol.md) |

Both use sender storage $`O(kB)`$, recover every source by its deadline, and return their finite bank. For $`D>B`$, the upper bound simply ignores feedback. Combining the bounds gives

```math
M_{\min}=\Theta\!\left(k\min\{D,B\}\right)
```

for the required receiver hardware of sustained streams, at fixed forward rate $`k/n=1/3`$ and $`T=B`$. The constants in this order statement are uniform in $`k,B,D`$. Both constructions also work for short finite horizons, but need not minimize their seed or memory when $`N\lt b`$. For retained memory alone in the sustained problem, the $`D\le B`$ construction reaches the lower coefficient exactly; no optimal coefficient is claimed for complete transient hardware or the no-feedback protocol.

The even-$`k`$ condition is only the physical realization of shares over $`\mathbb F_4`$: one ququart is two qubits. For an arbitrary positive integer $`k`$, pad to $`\kappa=2\lceil k/2\rceil`$ and use $`n=3\kappa`$. All bounds replace $`k`$ by $`\kappa\le2k`$ on the construction side, preserving the order law. Exact rate $`1/3`$ is claimed for the even widths, not for each unpadded odd width.

## Approximate lower bound

At a cut with the required $`b`$ future inputs, use for each tested source a maximally entangled state of dimension $`d=2^k`$ with an inaccessible reference. Let its unconditional entanglement fidelity be

```math
F_e=\langle\Phi_d|\rho_{R_t\widehat S_t}|\Phi_d\rangle.
```

The designated output is a $`d`$-dimensional logical register; any internal failure outcome must still supply such a register by the deadline, with its classical flag allowed separately. The fidelity is squared overlap, not root fidelity and not success-conditioned fidelity. If every labeled output on the independent-EPR input stream satisfies $`F_e\ge1-\epsilon`$ by its deadline for every admissible pattern, then

```math
M\ge b\left[k-h_2(\epsilon)
-\epsilon\log_2(2^{2k}-1)\right]
\ge b\left[(1-2\epsilon)k-h_2(\epsilon)\right].
```

Here $`0\le\epsilon\le1-2^{-2k}`$; a negative right-hand side is replaced by zero. For a shorter finite tail, replace the prefactor $`b`$ by $`\min\{D,B,r\}`$ with $`r`$ remaining arrivals. The proof uses the individual fidelity promises directly, without requiring a high joint-window fidelity or replacing $`\epsilon`$ by $`b\epsilon`$. The [converse](converse.md) gives the derivation and the supporting conditional entanglement-of-formation bound on initial assistance.

## Forward-rate benchmark

**Theorem 2 — no-feedback rate.** In this erasure family, with $`T=B`$ and initial assistance finite independently of session length, every exact no-feedback protocol has asymptotic rate

```math
\frac{k}{n}\le\frac13.
```

The three-share pipeline attains the bound at even logical widths, returning its seed after a charged $`2B`$-slot flush. For $`N`$ real source slots its reserved-bandwidth rate is

```math
\frac{kN}{3k(N+2B)}=\frac{N}{3(N+2B)}.
```

The [rate proof](rate.md) also treats vanishing per-message error and makes the finite initial resource term explicit. The theorem is a no-feedback benchmark. The feedback construction uses that same forward rate to isolate the memory advantage; it does not establish feedback capacity.

## Proof route and meaning

The lower bound freezes the encoder before the first new acknowledgment can arrive and compares two admissible futures with different losses. Their decoders share only the receiver's preexisting coherent system, which must carry enough quantum information to support both recoveries. The entropy inequality is inherited; the causal reduction identifies which resource it bounds here.

The upper bound recycles a known secret-sharing encoding across independent entangled banks. Prompt acknowledgments permit a short bank rotation, while the erasure promise supplies a clean interval in which losses and source backlog can be repaired before the deadlines. The [worked example and interpretation](interpretation.md) show this mechanism at fixed bandwidth. [Related work](../references/RELATED_WORK.md) separates these temporal statements from their established ingredients and neighboring communication models.
