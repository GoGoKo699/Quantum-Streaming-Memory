# Scientific account

The question is whether delayed knowledge of packet loss forces a quantum receiver to retain a larger coherent register, even when the forward link is already wide enough to meet every delivery deadline. The answer is an optimal-order law: at deadline $`T=B`$, receiver storage scales as $`k\min\{D,B\}`$ for a stream of $`k`$ logical qubits per slot, erasure span $`B`$ and acknowledgment latency $`D`$.

The result uses a precise deterministic erasure family, finite counted assistance and ideal local operations. Start with the model; the timing and resource conventions are part of every theorem.

| Reading goal | Authoritative account |
|---|---|
| Understand the channel, resource charges and exact results | [Model and main theorems](model.md) |
| Inspect the arbitrary-code causal memory lower bound | [Converse and per-message error](converse.md) |
| Understand the inherited quantum encoding | [Recycled secret-sharing primitive](primitive.md) |
| Follow the memory-saving construction | [Delayed-ACK banks and repair](feedback_protocol.md) |
| Inspect the no-feedback upper bound and finite seed return | [Three-share pipeline](no_feedback_protocol.md) |
| Check why the no-feedback rate is exactly one third | [Rate converse](rate.md) |
| See a complete schedule and its physical implications | [Worked example and interpretation](interpretation.md) |
| Separate the contribution from established results | [Related work](../references/RELATED_WORK.md) |
| Reproduce the finite checks and understand their limits | [Verification](../verification/README.md) |

For a conceptual route, read model → interpretation → primitive → feedback protocol. For a proof route, read model → converse → primitive → both protocols → rate. The general statements are analytical; finite exact and symbolic checks test the implementation and representative schedules.
