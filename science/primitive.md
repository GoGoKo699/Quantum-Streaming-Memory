# Fixed-qubit secret sharing and exact entanglement recycling

The streaming constructions use a standard two-out-of-three quantum secret-sharing primitive. Quantum threshold sharing is established by [Cleve, Gottesman and Lo (1999)](../references/RELATED_WORK.md#qss1999). Local communication-cipher encoding with a receiver-held share, including regeneration of shared entanglement after a successful transmission, is explicit in [Leung (2002)](../references/RELATED_WORK.md#leung2002), especially Section 5 and Appendix C. These are inherited ingredients.

This page gives the exact algebra used by the protocols. Its purpose is to make coherence, erasure recovery, recycling, and physical-qubit costs explicit. The contribution concerns the streaming memory law and its causal protocol; the secret-sharing code and communication cipher are inherited.

## Registers and physical alphabet

Let $`\mathbb F_4`$ be the field with four elements, and choose $`a\in\mathbb F_4\setminus\{0,1\}`$. A computational basis label in $`\mathbb F_4`$ is represented by **two physical qubits**, using all four basis states. The alphabet is fixed independently of burst length and feedback delay.

Alice holds a source symbol $`S`$ and a register $`L`$. Bob holds $`Q`$, with

```math
|\Phi_4\rangle_{LQ}
=\frac12\sum_{r\in\mathbb F_4}|r\rangle_L|r\rangle_Q.
```

Under the two-qubit basis labeling, this is exactly two ordinary Bell pairs. The shared pair is independent of the source sequence and every source reference.

Alice applies the field-linear permutation

```math
|s\rangle_S|r\rangle_L
\longmapsto
|r+s\rangle_A|r+as\rangle_C.
```

The determinant of the corresponding map is nonzero because $`a\ne1`$. The induced three-share isometry is

```math
V|s\rangle
=\frac12\sum_{r\in\mathbb F_4}
|r\rangle_Q|r+s\rangle_A|r+as\rangle_C.
```

Only the source and Alice's local pair half are acted on. Bob's share need not interact with the source during encoding.

## Explicit two-share decoders

Each available pair can be transformed in place into the decoded source $`S'`$ and one other register $`J`$:

| Available pair | Decoded source $`S'`$ | Other output $`J`$ |
|---|---|---|
| $`Q,A`$ | $`A-Q`$ | $`aA+(1-a)Q`$ |
| $`Q,C`$ | $`(C-Q)/a`$ | $`Q+(C-Q)/a`$ |
| $`A,C`$ | $`(C-A)/(a-1)`$ | $`A-(C-A)/(a-1)`$ |

All arithmetic is in $`\mathbb F_4`$. In the first row, $`J`$ equals the missing share value $`C`$; in the second, it equals $`A`$; in the third, it equals $`Q`$.

Let $`XY`$ be the available pair and $`Z`$ the third share. For an arbitrary source entangled with a reference $`R`$, changing the summation variable gives

```math
(I_R\otimes U_{XY})(I_R\otimes V)|\psi\rangle_{RS}
=|\psi\rangle_{RS'}\otimes|\Phi_4\rangle_{JZ}.
```

This proves all three exact recovery statements. In particular:

- The source is recovered coherently, including its reference entanglement.
- The other decoder output and the missing share are independent of the recovered source.
- Each single share is maximally mixed and independent of the source reference.
- Discarding the unused decoder output is harmless to the source.

The reference can include every other source register, including sources that have not yet arrived at the encoder. Thus these identities support arbitrary jointly entangled input streams; they are not limited to independent messages.

## Successful-transmission recycling

Suppose Bob already holds $`Q`$, Alice transmits $`A`$, and Alice retains $`C`$. If $`A`$ arrives, Bob uses the first decoder. Its exact output is

```math
|\psi\rangle_{RS'}\otimes|\Phi_4\rangle_{JC}.
```

Bob releases $`S'`$ and retains $`J`$. Alice's retained register $`C`$ is the other half of the regenerated pair. The pair is independent of the delivered message and can be used again after the sender learns that transmission succeeded.

If $`A`$ is erased, Bob still holds $`Q`$ while Alice holds $`C`$. A later successful transmission of $`C`$ lets Bob use the second decoder. It recovers the source but does **not** itself return a shared pair: both available shares are then at Bob, and the decoder junk is paired with the erased share. The [feedback protocol](feedback_protocol.md) therefore sends a fresh locally prepared Bell half during repair and charges that transmission explicitly.

## Sending the advance share before source arrival

The [no-feedback pipeline](no_feedback_protocol.md) sends $`Q_j`$ before source $`S_j`$ arrives. This is causal: the sender first prepares $`L_j,Q_j`$ locally and sends $`Q_j`$, without interacting with or knowing $`S_j`$.

If that advance transmission is erased, the environment holds $`Q_j`$. Alice's later local encoding still creates the state above, with its first share held by the environment. The pair $`A_j,C_j`$ then recovers the source by the third decoder. The sender does not need to learn whether the advance share arrived.

## Grouping and workspace

For a positive even number $`k`$ of source qubits, use $`k/2`$ copies in parallel. Each of $`Q,A,C`$ then occupies exactly $`k`$ physical qubits, and one shared group contains exactly $`k`$ Bell pairs.

For odd $`k`$, pad the source with one fixed qubit and replace $`k`$ by $`k+1`$ in the construction costs. This preserves the stated memory order and a fixed nonzero rate. The exact packet rate $`1/3`$ with width $`3k`$ is stated for even $`k`$.

All displayed maps are invertible linear maps over the binary representation of $`\mathbb F_4`$. They can be implemented in place by reversible linear circuits on the displayed registers. Their algebra does not require an additional quantum register. The protocols separately charge the incoming packet, locally prepared pairs, and fixed padding; no large-alphabet or uncounted quantum workspace is used.

## Verification boundary

The identity above is the analytic proof. The accompanying `verify_qss_primitive.py` check uses a reference-entangled input to verify all three decoders, the independence of each single share, and the exact recycled pair for successful $`Q,A`$ decoding. Its numerical report records unit fidelity and zero amplitude error for this finite field representation. This finite check does not establish literature priority or the streaming schedule; those are addressed separately.
