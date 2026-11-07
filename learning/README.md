# Learning the streaming-memory result

The educational anchor is **John Preskill's Quantum Information lecture notes**: Chapter 7, *Quantum Error Correction*, updated March 2026, and Chapter 10, *Quantum Shannon Theory*, updated June 2025. These are two chapters of one selected source. The [official Caltech index](https://www.preskill.caltech.edu/ph219/) hosts the notes; the bridge records the exact chapter URLs, dates and relevant passages.

| Route | Purpose |
|---|---|
| [Preskill bridge](PRESKILL_BRIDGE.md) | Connect a concrete burst-repair task to reference-preserving correction, entropy overlap, the known secret-sharing primitive, delayed-ACK causality and the sustained schedule. It translates notation and assumptions without requiring the whole book. |
| [30-milestone map](MILESTONES.md) | Follow the project's common understanding targets and their dependencies: 12 background milestones establish the framework, then 18 narrative milestones assemble the mechanism, theorem and scope. |
| [Complete worked example](../science/interpretation.md#a-complete-burst-repair-example) | Trace every packet, output, repair and bank update for $`B=4,D=2`$. The bridge and map use this one authoritative example. |
| [Science index](../science/README.md) | Go directly to the model, proofs, construction and verification boundaries. |

The central result is an optimal-order receiver-storage law,

```math
M_{\min}=\Theta\!\left(k\min\{D,B\}\right),
```

for sustained streams at deadline $`T=B`$ and forward rate $`1/3`$, under the precise [packet, acknowledgment and erasure assumptions](../science/model.md). The lower bound concerns clean cuts admitting two test continuations and enough future sources; shorter finite tails have the explicit cap given in the model. Exact rate $`1/3`$ uses even logical width, with stated padding overhead otherwise.

The bridge distinguishes the anchor's foundations, inherited research ingredients and local streaming derivations. Primary papers remain in [Related work](../references/RELATED_WORK.md) for attribution and research-level dependencies; they are not additional educational anchors. The map is common scientific documentation, independent of any reader's progress or assessment history.
