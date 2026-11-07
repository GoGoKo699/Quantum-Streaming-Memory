# Worked example and physical interpretation

The resource is **coherent receiver storage**. A classical receiver can keep arbitrarily many bits in this model. The lower bound persists because an unknown quantum state, including its entanglement with an inaccessible reference, cannot be replaced by a classical description of a failed transmission. A finite entangled bank allows the sender and receiver to preserve recovery options until a loss flag arrives.

## A complete burst-repair example

Take $`B=4`$ and $`D=2`$, with an even logical width $`k`$. Each forward slot has room for three $`k`$-qubit groups. The parties start with two counted entangled banks, numbered 0 and 1. Suppose slots 0 through 3 are erased, with subsequent slots delivered. This is an admissible burst; the losses force slots 4 through 11 to be good under the [window promise](model.md#the-deterministic-erasure-promise).

In a normal slot, the sender uses one bank and sends a share $`A_t`$, retaining its partner share $`C_t`$. A successful arrival would immediately deliver $`S_t`$ and regenerate the bank. The sender learns the first loss only at the start of slot 2.

| Slot | Fresh source | Forward groups, with unused positions padded | Receiver action |
|---:|---|---|---|
| 0 | $`S_0`$ | $`A_0`$ from bank 0 | Packet lost; retain bank half |
| 1 | $`S_1`$ | $`A_1`$ from bank 1 | Packet lost; retain bank half |
| 2 | $`S_2`$ | Padding after failed ACK for slot 0 | No source output |
| 3 | $`S_3`$ | Padding | No source output |
| 4 | $`S_4`$ | $`C_0,S_2,\text{new bank half }0`$ | Recover $`S_0`$; deliver $`S_2`$; replace bank 0 |
| 5 | $`S_5`$ | $`C_1,S_3,\text{new bank half }1`$ | Recover $`S_1`$; deliver $`S_3`$; replace bank 1 |
| 6 | $`S_6`$ | $`S_4,S_5`$ | Deliver both sources |
| 7 | $`S_7`$ | $`S_6,S_7`$ | Deliver both sources; queue empty |
| 8 | $`S_8`$ | $`A_8`$ from refreshed bank 0 | Normal operation resumes |

The first two sources are recovered exactly at their deadlines, slots 4 and 5. Sources 2 and 3 arrive at slots 4 and 5, before their deadlines 6 and 7. Sources 4 through 7 arrive at slots 6,6,7,7, also within their deadlines. Bank-refresh ACKs from slots 4 and 5 arrive before slots 6 and 7, so bank 0 is ready for reuse at slot 8 and bank 1 at slot 9.

At receiver cuts, the only retained quantum systems are the two bank halves: $`2k`$ qubits. Processing a full incoming packet needs at most another $`3k`$ qubits. Direct sources and recovered sources are released and then become inaccessible. At the sender, the two retained recovery shares and the growing source queue account for the buffering cost. The packet budget stays $`3k`$ even in the repair interval; there is no extra repair channel.

This table begins the first loss at bank 0 for clarity. A loss can begin at any phase. The general protocol rotates the repair-bank labels from the bank used at that first lost slot and restarts the normal phase after recovery. A permanently fixed global bank label $`t\bmod D`$ would be incorrect after some repairs. The [protocol proof](feedback_protocol.md) and [symbolic checker](../verification/README.md) include that phase change.

## Why a source-independent early share is causal

Without feedback, source $`S_t`$ is spread over share times $`t-B,t,t+B`$. The first time precedes source arrival. What is transmitted then is one half of a freshly prepared entangled pair, independent of the source. When $`S_t`$ arrives, a local encoding of the source and the retained half completes the three-share state. If the advance half has already been erased, the other two shares still recover the source.

For the same $`B=4`$ burst, $`S_0`$ has its advance half in the initial bank, loses its middle share at slot 0, and is recovered when its final share arrives at slot 4. Source $`S_4`$ instead loses its advance half at slot 0; its middle and final shares arrive at slots 4 and 8, so it is recovered by slot 8. The unknown source is never copied or accessed before it exists.

At most one of the three share positions can be erased: their pairwise separations are $`B`$ and $`2B`$, which the promise forbids for a pair of losses. This is the whole reason the schedule tolerates recurring allowed bursts. The [pipeline account](no_feedback_protocol.md) proves the storage and finite-session return properties.

## What feedback changes

For sustained streams, the two constructions use the same forward rate and deadline. Without feedback, the receiver must keep a number of coherent groups proportional to the burst length. With a next-slot ACK, a single rotating bank suffices for retained memory. For $`1\le D\le B`$, $`D`$ independent banks keep the sender from reusing a bank before its previous transmission has been acknowledged. For longer ACK delays, the construction uses the $`B`$-group no-feedback pipeline.

The converse makes this more than a feature of a particular encoder. At a clean cut with at least $`\min\{D,B\}`$ real source arrivals remaining, that many groups have first transmissions before any new ACK can arrive, and must support two different admissible future loss patterns. For a shorter tail, the number is capped by the remaining source count. The two recovery descriptions overlap in the receiver's quantum register. That overlap must be large enough to preserve all the reference entanglement. Unlimited sender storage, unlimited classical records and a wider forward packet do not eliminate this requirement.

For fixed $`D`$ and increasing $`B`$, the receiver-memory saving relative to no feedback grows proportionally to $`B/D`$ in order. Feedback moves the coherent buffering burden toward the sender: both explicit constructions still use sender space $`O(kB)`$. The result does not claim that total memory across the two sites decreases by the same factor.

The finite Bell bank is part of the explanation. At deadline $`B`$, starting from only shared classical randomness is insufficient even with next-slot ACKs. The [entanglement-of-formation corollary](converse.md) quantifies this initial assistance requirement. The protocols return the bank after the real stream ends, so the advantage is not financed by a supply of fresh preshared ebits that grows with stream length.

## Ordered delivery

The main memory result allows immediate labeled outputs. If an application requires sources in temporal order, retain early recovered outputs until every smaller index is available. These outputs count in coherent memory while retained. The construction accounts bound this additional buffer by $`(D-1)k`$ for the feedback scheme and by $`(B-1)k`$ for the no-feedback pipeline. Thus ordering preserves the main order law, but it changes the constants and should not be silently included in the exact retained-bank count.

## Limits of the comparison

The deterministic guard promise is load-bearing. It provides a known clean repair interval after a loss. The protocols do not guarantee a finite deadline against arbitrary loss patterns or every iid realization. They assume ideal local operations, ideal quantum storage and reliable reverse flags; no memory-noise threshold or repeater hardware architecture is analyzed.

The rate theorem identifies the optimum without feedback. It does not optimize the feedback-assisted rate or the full tradeoff for deadlines longer than $`B`$. The even-width realization attains rate $`1/3`$ using a fixed ququart primitive; padding an odd logical width has an explicit overhead. Receiver-space lower and upper bounds agree in order, while the exact best transient hardware constant remains outside the claim.

The elementary recovery and entropy ingredients have precedents. [Related work](../references/RELATED_WORK.md) explains why static Singleton bounds, catalytic error correction, quantum ARQ and heralding-latency examples do not by themselves provide this arbitrary-code delayed-ACK theorem with a matching sustained hard-deadline schedule. The conclusion is tied to the explicit model and operational comparison.
