# Exact streaming with delayed erasure acknowledgments

This protocol achieves deadline $`T=B`$, forward packet width $`3k`$, and retained receiver memory $`Dk`$ when $`1\le D\le B`$. It uses the inherited [secret-sharing and recycling primitive](primitive.md), credited to [quantum threshold sharing](../references/RELATED_WORK.md#qss1999) and [Leung's communication cipher](../references/RELATED_WORK.md#leung2002). The construction supplies the upper bound matching the [receiver-memory converse](converse.md); it does not assert optimal feedback-assisted rate.

## Assumptions and conventions

Use the [streaming model](model.md). A fresh $`k`$-qubit source $`S_t`$ arrives before each slot $`t`$ and is due by the end of slot $`t+B`$. Here $`k`$ is positive and even, so the fixed-qubit primitive applies without padding. Sources may be jointly entangled with an external reference and with one another.

Each forward packet has $`3k`$ physical qubits. It either arrives intact in that slot or is wholly erased, with a receiver flag. Every window of $`2B+1`$ slots has its erased positions contained in an interval of at most $`B`$ slots. Erasures within that interval may have holes. The flag for slot $`t`$ reaches the sender before slot $`t+D`$ and not earlier. Only this one-bit backward flag is used; there is no external forward classical channel.

The burst promise implies the following clean guard:

```math
e\text{ erased}
\quad\Longrightarrow\quad
e+B,e+B+1,\ldots,e+2B\text{ all arrive}.
```

Indeed, an erasure at any of those later times would share a $`2B+1`$ window with $`e`$ while being separated from it by at least $`B`$ slots, contradicting the promised erasure span.

Both parties know the clock, the parameters, and, for a finite session, its arbitrary source horizon $`N`$. This makes packet labels and the end of source acceptance part of the protocol definition rather than an uncharged header or stop message. Retained quantum storage includes every reusable quantum register and every unused pair half. Outputs are released immediately unless the optional ordered variant below is chosen.

## The bank invariant during normal operation

The initial resource consists of $`D`$ banks, each containing $`k`$ Bell pairs. Their $`Dk`$ qubits at each endpoint are counted as retained storage. Label the banks physically by $`\mathbb Z_D`$, and maintain a classical cursor specifying the next bank.

For each normal-mode source:

1. Alice encodes the source with her half of the selected bank using the primitive.
2. She sends the $`A`$ share and retains $`C`$. The other two packet lanes contain fixed padding.
3. If the packet arrives, Bob decodes from $`Q,A`$, releases the source, and retains the new bank half $`J`$. The pair $`J,C`$ is exactly maximally entangled and independent of the source.
4. The cursor advances cyclically. A bank is reused only after its preceding normal transmission has a positive ACK.

A normal reuse occurs exactly $`D`$ slots after the preceding use of that bank, so its ACK is available at the start of the reuse slot. A negative ACK triggers the recovery below before the damaged bank can be reused.

## Detecting a loss and freezing the banks

Let $`e`$ be the first erased normal-mode packet of an episode, and let $`r`$ be its physical bank label. Before this loss can be reported, the sender transmits sources $`S_e,\ldots,S_{e+D-1}`$, using the distinct banks

```math
b_j=(r+j)\bmod D,\qquad 0\le j<D.
```

At the beginning of slot $`e+D`$, the first negative ACK arrives. Alice freezes the current register of every bank. She buffers every subsequent source, without encoding it, and sends only fixed padding until slot $`e+B`$.

The initial $`D`$ middle shares need not all be erased. Bob knows which arrived. Every held bank register is nevertheless in one of two controlled states: a valid pair half following a success, or the retained share of the secret-sharing encoding following an erasure.

Because the receiver knows every erasure flag and the delay $`D`$, it can reconstruct when the sender receives each flag and which control transition occurs. It therefore knows the packet interpretation and bank rotation without a forward control message.

## Repair and queue service

The entire recovery below lies inside the guaranteed clean guard. For a continuing input stream, the schedule is:

| Slot | First $`k`$-qubit lane | Second lane | Third lane |
|---|---|---|---|
| $`e+B+j`$, $`0\le j<D`$ | Alice's held register from bank $`b_j`$ | Direct source $`S_{e+D+j}`$ | Fresh local Bell half for bank $`b_j`$ |
| $`e+B+D+\ell`$, $`0\le\ell<B-D`$ | Direct source $`S_{e+2D+2\ell}`$ | Direct source $`S_{e+2D+2\ell+1}`$ | Fixed padding |

For the first row, if the bank's middle share was erased, Bob combines $`Q`$ with the arriving $`C`$ and recovers $`S_{e+j}`$ at time $`e+B+j`$, exactly its deadline. If the middle share arrived, that source has already been delivered and Bob discards the old pair after Alice's half arrives. In either case, the third lane installs a new independent shared pair for that bank. Its preparation is local and its forward transmission is charged.

### Queue calculation and deadlines

After the initial $`D`$ normal transmissions, the queue is empty. By the end of slot $`e+B-1`$, $`B-D`$ sources have arrived while transmission is frozen. During the $`D`$ repair slots, one source arrives and one queued source is served each slot, leaving the queue size at $`B-D`$.

The direct sources in the first row have delay $`B-D`$. The second row serves two sources per slot while one new source arrives. The queue decreases by one per slot and is empty at the end of slot $`e+2B-1`$. The two displayed source indices have delays

```math
B-D-\ell
\quad\text{and}\quad
B-D-\ell-1,
```

which are nonnegative throughout the indicated range. Thus those sources are available when sent and all meet the deadline. Together, the two rows account for all sources from $`e`$ through $`e+2B-1`$, with a source whose middle transmission succeeded released earlier. No source is dropped, postselected, or delivered twice.

## Correct bank rotation and repeated bursts

At slot $`e+2B`$, resume normal operation with cursor $`r`$, the physical bank used at the first loss. The first reuse of refreshed bank $`b_j`$ is then at $`e+2B+j`$. That bank was refreshed at $`e+B+j`$, and its ACK arrives by

```math
e+B+j+D\le e+2B+j.
```

Every reuse is therefore causal. Thereafter the cyclic normal schedule again separates successive uses of each bank by exactly $`D`$ slots.

The rotation is tied to the bank used at the first loss. It is **not** obtained by blindly using a global time index modulo $`D`$ after repair; that would fail to express the required order when $`D`$ does not divide $`2B`$.

The clean guard includes the resume slot $`e+2B`$, and the source queue is already empty. A later erased normal-mode packet starts a fresh episode with its own bank rotation. The same invariant applies even if a new burst occurs before every refreshed bank has completed its first normal reuse. Induction over episodes proves indefinite operation for every admissible pattern, including repeated bursts at the earliest allowed spacing.

## Storage and physical resources

Bob retains one $`k`$-qubit register per bank. During normal operation it is a shared pair half. Following an erased middle share it is the $`Q`$ register protecting that source. Repair consumes or discards it and replaces it one-for-one. All payloads are released after decoding. Hence retained receiver storage is exactly

```math
M_{\mathrm{receiver}}=Dk.
```

Alice retains one $`k`$-qubit register per bank and at most $`B-D`$ queued sources after any slot. Her retained storage is therefore at most $`Bk`$. These counts include the initial and returned entanglement resources.

The pair decoders act in place. Bob needs at most $`3k`$ additional qubits for one incoming packet, so the hardware peak is bounded by retained storage plus $`3k`$. Alice can use at most $`4k`$ additional transient qubits for an arriving source, a locally prepared repair pair, and padding. These workspace bounds are independent of $`B`$ and $`D`$; no growing decoder buffer is omitted.

Every packet has three physical lanes, including the fixed-state lanes in clean operation. The rate counts all of them. The only classical communication outside those packets is the declared one-bit delayed erasure ACK. Local control records may be arbitrarily large and do not supply quantum storage.

## Arbitrary finite horizon and exact bank return

Let $`N\ge1`$ be the common finite source horizon. No divisibility by $`B`$ or $`D`$ is required. After the last source at slot $`N-1`$, Alice launches no new normal-mode source encodings, continues any necessary repair, and serves only the remaining actual queue. Unused lanes carry fixed padding. Losses of padding-only packets do not initiate recovery because those packets put neither a source nor a bank at risk.

If all outstanding normal transmissions succeeded, the recycling identity has already regenerated every bank. The last normal ACK arrives within $`D`$ further slots.

If a first lost normal packet at $`e<N`$ is reported, repair all $`D`$ banks on the same schedule. A nominal source time $`e+j\ge N`$ means that bank was not used after the first loss. Its previous use preceded $`e`$ and succeeded, or it remains an unused initial pair. Alice can send that valid bank half, let Bob discard the old pair, and install the same fresh replacement. Real queued payloads are sent in FIFO order; missing payloads are replaced by padding.

All $`D`$ pairs are restored by $`e+B+D-1`$, and all real queued sources have been served by $`e+2B-1`$. Both times are less than $`N+2B`$. The channel promise itself certifies the repair slots, so termination need not wait another ACK round for their replacements. Padding may continue through slot $`N+2B-1`$ to give a fixed common ending time.

Every normal success factors the new pair from the source. Every repair installs an independent locally prepared pair through a guaranteed clean transmission. Thus the final shared bank is exactly $`\Phi_2^{\otimes Dk}`$, independent of all delivered sources and their references. It can be swapped to designated initial bank labels. The argument covers $`N<D`$ and a stop in the middle of any normal or repair phase.

With all physical positions charged, the finite-session rate is at least

```math
\frac{Nk}{3k(N+2B)}=\frac{N}{3(N+2B)},
```

which tends to $`1/3`$. For $`D>B`$, the [no-feedback protocol](no_feedback_protocol.md) uses $`Bk`$ initial pairs and $`O(kB)`$ receiver storage while ignoring feedback. These two cases supply the upper order $`O(k\min(D,B))`$.

## Optional variant: strictly ordered output release

The main protocol permits an already-decoded source to be released before an earlier source. If an application requires strictly increasing source indices, at most $`D-1`$ decoded sources need to be buffered at Bob.

Before the first repair, only successful members of the initial $`D`$ transmissions can wait behind the first loss, so at most $`D-1`$ outputs wait. After repair slot $`e+B+j`$, every source through $`e+j`$ is available. If an earlier gap still blocks release, at least one of the remaining $`D-j-1`$ initial sources is unresolved. At most $`D-j-2`$ of those can therefore be waiting as decoded outputs. At most $`j+1`$ direct sources have arrived alongside repairs. The sum is at most $`D-1`$. If there is no gap, those outputs are released instead.

By the final repair slot, all initial sources and their accompanying direct sources can be released. The subsequent FIFO phase is ordered already. An initial source is released by its own deadline because all preceding initial sources have earlier repair deadlines. A direct source waiting for the last initial repair is released by $`e+B+D-1`$, before its deadline. Thus every deadline remains satisfied.

The optional variant adds at most $`(D-1)k`$ retained output qubits, giving total receiver storage $`(2D-1)k`$ before the incoming-packet workspace. This variant preserves the memory scaling and is separate from the main protocol's $`Dk`$ retained-space count.

## Finite schedule audit

The analytic queue calculation and bank invariant are the proof. The accompanying `verify_streaming_schedule.py` independently tracks source identities, physical bank generations, ACK availability, cursor rotation, finite horizon, and packet width. It passed 33,707 cases for every $`B=1,\ldots,8`$ and $`D=1,\ldots,B`$, including burst holes, shifted first losses, earliest admissible repeated bursts, and finite-horizon truncations. The optional ordered-output bound is proved above rather than simulated by that checker.
