# Receiver memory with delayed acknowledgments

For a sustained stream at the minimum decoding deadline $`T=B`$, delayed erasure acknowledgments impose the clean-cut lower bound

```math
M\ge k\min\{D,B\}.
```

The proof holds for arbitrary causal CPTP encoders and decoders, unrestricted sender memory, and unrestricted forward packet width. Its entropy ingredient is the established overlapping-recovery/Singleton argument. The contribution is the causal reduction that makes the acknowledgment delay enter this storage bound; see the [primary-source comparison](../references/RELATED_WORK.md#ghw2022) and the [distributed-storage intersection antecedent](../references/RELATED_WORK.md#sunjafar2025).

## Statement and assumptions

Use the [packet model](model.md). A fresh group of $`k`$ qubits arrives in each slot, and source $`S_t`$ must be released by the end of slot $`t+B`$. Each complete forward slot system, including metadata, has dimension at most $`2^n`$ and is delivered or erased within that slot. All forward communication is charged to these packets. The only backward messages are erasure flags: the flag for slot $`t`$ reaches the sender before encoding slot $`t+D`$, and cannot affect it earlier. We take $`D\ge1`$ and write $`D=\infty`$ for no feedback.

At a chosen initial cut, let $`Q`$ contain every retained receiver quantum system, including all entanglement assistance, and let $`Y`$ be its unrestricted classical record. The memory cap is $`\dim Q\le2^M`$. Released source outputs are inaccessible to subsequent protocol operations. The cut must admit both future bursts used below and have at least $`b=\min\{D,B\}`$ further source arrivals. An arbitrarily late all-success prefix of a sustained stream provides such a cut. We do not claim the bound after every recent-burst history or after the final source arrival.

Let

```math
d=2^k,\qquad b=\min\{D,B\},\qquad \min\{\infty,B\}=B.
```

Feed the next $`b`$ source groups as independent halves of maximally entangled pairs $`\Phi_d^{R_iS_i}`$, where every $`R_i`$ is inaccessible to the protocol. Other actual source inputs are independently maximally mixed, equivalently their EPR references are traced out. Suppose that for each tested message and either of the two erasure patterns, the output satisfies the unconditional entanglement-fidelity promise

```math
F_i=\langle\Phi_d|\rho_{R_iO_i}|\Phi_d\rangle\ge1-\varepsilon.
```

This is EPR overlap, with all internal measurement and abort outcomes included. It is not a postselected promise or a square-root-fidelity convention. No joint output-block fidelity is assumed.

For $`0\le\varepsilon\le1-d^{-2}`$, define

```math
f_d(\varepsilon)
=h_2(\varepsilon)+\varepsilon\log_2(d^2-1).
```

Here $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$ is binary entropy, with $`0\log_2 0=0`$.

**Theorem.** At every cut described above,

```math
S(Q\mid Y)\ge b\bigl[\log_2d-f_d(\varepsilon)\bigr],
\qquad
M\ge b\bigl[\log_2d-f_d(\varepsilon)\bigr].
```

In particular, exact transmission requires $`M\ge kb`$. If only $`N_{\mathrm{rem}}\lt b`$ source arrivals remain, the same theorem and proof use $`b'=\min\{D,B,N_{\mathrm{rem}}\}`$ in place of $`b`$. Shorter finite tails therefore have a correspondingly smaller lower bound. A simpler approximate expression for the full $`b`$-source window is

```math
M\ge\min\{D,B\}\bigl[(1-2\varepsilon)k-h_2(\varepsilon)\bigr].
```

Negative lower bounds may be replaced by zero. Entropies and logarithms are in bits.

## 1. The overlap inequality

For every state on disjoint registers $`R,Q,A,E`$,

```math
I(R:QA)+I(R:QE)\le2S(R)+2S(Q).
```

Weak monotonicity and subadditivity give, respectively,

```math
\begin{aligned}
S(RQA)+S(RQE)&\ge S(A)+S(E),\\
S(QA)+S(QE)&\le S(A)+S(E)+2S(Q).
\end{aligned}
```

Substitution into the two mutual informations proves the inequality. The state need not be pure, and the encoder need not be an isometry.

For a shared classical record $`Y`$, condition on each value and use the chain rule:

```math
\begin{aligned}
I(R:QAY)+I(R:QEY)
&=2I(R:Y)+I(R:QA\mid Y)+I(R:QE\mid Y)\\
&\le2I(R:Y)+2S(R\mid Y)+2S(Q\mid Y)\\
&=2S(R)+2S(Q\mid Y).
\end{aligned}
```

No independence assumption between $`R`$ and $`Y`$ is needed for this step. The classical memory contributes through $`S(Q\mid Y)=\sum_y p_yS(\rho_Q^y)\le M`$, not through its own size or entropy.

## 2. One common prefix and two recovery regions

Translate the initial cut to just before slot zero. Let $`E_0`$ be the sender's complete accessible memory at that cut, including its classical controls. Inaccessible past outputs and environments are traced out. Compare the fixed future patterns

```math
\mathsf E:\ [0,B-1]\text{ erased},\qquad
\mathsf L:\ [b,b+B-1]\text{ erased}.
```

### Common state before the first relevant ACK

The first $`b`$ packets are encoded before any ACK generated in those slots can affect the sender. Pending pre-cut ACKs have identical fixed values and arrival times in both continuations. Thus the sender uses one common prefix.

Defer the receiver's operations in these first $`b`$ slots. They act on systems disjoint from subsequent sender operations and cannot influence the sender through an allowed ACK during this prefix. Denote its emitted packets jointly by $`A`$, and denote the sender's retained remainder after their emission by $`E`$. There is one common pre-erasure state

```math
\sigma_{RQAEY},\qquad R=R_0\cdots R_{b-1}.
```

Here **$`Q`$ is the receiver memory at the initial cut**, not its branch-dependent state after the prefix. Prefix encoder maps may discard systems, so this common state can be mixed. The reference marginal remains the product of maximally mixed states.

### The late burst gives recovery from $`QAY`$

For $`0\le i\lt b`$, source $`i`$ is due at $`B+i`$, and

```math
b\le B+i\le b+B-1.
```

Under $`\mathsf L`$, every packet after $`A`$ through these deadlines is erased. Therefore the actual receiver induces a channel

```math
\mathcal D_{\mathsf L}:QAY\longrightarrow O_0\cdots O_{b-1}.
```

It uses only the initial receiver resources, the first $`b`$ packet systems, and the fixed erasure flags. Subsequent sender operations cannot signal through erased packets. This remains true when ACKs cause the sender to adapt after the common prefix.

### The early burst gives recovery from $`QEY`$

Under $`\mathsf E`$, every packet in $`A`$ is erased. Starting with the marginal on $`RQEY`$, a virtual joint processor can simulate the physical receiver's deferred initial operations and the entire remaining protocol: sender and receiver maps, later ACKs, erasures, and independently fixed future inputs.

The processor possesses all accessible sender systems $`E`$ and receiver systems $`Q,Y`$. It receives neither erased $`A`$ nor inaccessible $`R`$ or past outputs. Granting joint access to these sender and receiver systems relaxes locality, so the actual protocol supplies a CPTP map

```math
\mathcal D_{\mathsf E}:QEY\longrightarrow O_0\cdots O_{b-1}.
```

This map reproduces the physical output marginals in the early-burst branch. Only the initial prefix state is common. We do not assert a common emitted state after feedback starts; all later branch-dependent adaptation belongs to the virtual decoding maps.

### Released outputs are not a hidden memory resource

Each physical decoding step updates retained memory and emits output registers on which later protocol maps do not act. Composing these steps while collecting the emitted registers in an external mathematical output register gives the channels above. The collector does not help decode later messages and is not a physical receiver-memory allocation.

The overlap bound is charged to the actual initial $`Q`$. It therefore does not reuse released source outputs or silently apply $`M`$ to a larger deferred receiver.

## 3. Individual-message fidelity and the entropy conclusion

For a state $`\rho_{RO}`$ on $`d`$-dimensional reference and logical-output registers, with $`\rho_R=I/d`$ and EPR overlap $`F\ge1-\varepsilon`$,

```math
I(R:O)\ge2\log_2d-f_d(\varepsilon).
```

A direct proof uses the bilateral twirl $`U\otimes\overline U`$. Each component preserves conditional entropy, while concavity implies that twirling cannot decrease $`S(R\mid O)`$. The twirled state is

```math
\omega_F
=F\Phi_d+\frac{1-F}{d^2-1}(I-\Phi_d).
```

It has maximally mixed marginals and

```math
S(R\mid O)_{\omega_F}
=h_2(1-F)+(1-F)\log_2(d^2-1)-\log_2d.
```

Since $`f_d`$ is increasing on $`[0,1-d^{-2}]`$, the claimed mutual-information bound follows. The justification is conditional-entropy concavity, not a claim that correlated-randomness twirling is mutual-information-monotone.

For independent reference marginals, conditional-entropy subadditivity gives

```math
I(R_0\cdots R_{b-1}:X)\ge\sum_{i=0}^{b-1}I(R_i:X).
```

Data processing from $`X`$ to each recovered output then implies

```math
I(R:X)\ge b\bigl[2\log_2d-f_d(\varepsilon)\bigr]
```

for either $`X=QAY`$ or $`X=QEY`$. This step needs only the individual output fidelities; it does not accumulate the message errors into a joint-block error promise.

Using $`S(R)=b\log_2d`$ in the overlap inequality yields

```math
2b\bigl[2\log_2d-f_d(\varepsilon)\bigr]
\le2b\log_2d+2S(Q\mid Y).
```

Rearranging proves the theorem. The error penalty depends on the logical group dimension $`d`$, not the packet width or the total number of transmitted systems.

## 4. Supporting resource interpretation: initial entanglement

The same argument identifies why separable memory does not suffice. Define the classical conditional average of entanglement of formation by

```math
\overline E_F(E_0:Q\mid Y)
=\sum_y p_y E_F(\rho_{E_0Q}^{y}).
```

Then

```math
\overline E_F(E_0:Q\mid Y)
\ge b\bigl[\log_2d-f_d(\varepsilon)\bigr].
```

To see this, choose any pure-state ensemble of each conditional initial state:

```math
\rho_{E_0Q}^{y}
=\sum_z p(z\mid y)|\psi_{yz}\rangle\langle\psi_{yz}|.
```

Attach its classical label $`Z`$, run the unchanged protocol ignoring that label, and give $`Z`$ to both virtual decoders. Tracing $`Z`$ reproduces the original protocol, so all unconditional fidelity promises are unchanged. The proof above now bounds $`S(Q\mid YZ)`$ from below.

The common prefix acts only on the sender and fresh inputs. Its trace-preserving map leaves each conditional initial marginal of $`Q`$ unchanged. Thus

```math
S(Q\mid YZ)
=\sum_{y,z}p_y p(z\mid y)
S\!\left(\mathrm{Tr}_{E_0}|\psi_{yz}\rangle\langle\psi_{yz}|\right).
```

Minimizing over these ensembles gives the stated convex-roof bound. The proof never assumes that every artificial ensemble component separately meets the fidelity promise.

For exact transmission, at least $`kb`$ ebits of this initial conditional entanglement measure are required at the cut. This is a supporting interpretation of the storage obstruction. It does not identify a consumed-entanglement rate, a distillable-entanglement rate, or an optimal catalyst size beyond the stated model. Warmup and seed return are accounted for in the [no-feedback](no_feedback_protocol.md) and [delayed-ACK](feedback_protocol.md) constructions.

## Scope and attribution

The bound is a worst-case retained-space requirement because admissible clean cuts with enough future arrivals can occur arbitrarily late in a sustained stream. A recent burst may exclude one test continuation, and a finite tail may contain fewer than $`b`$ messages, so the proof does not give the full bound at every history. If quantum systems sent before the cut could arrive afterward, those systems would be additional common quantum assistance and would have to be charged; the same-slot-delivery model excludes that loophole.

The inherited entropy mechanism is documented in [Grassl–Huber–Winter, Theorems 5–6 and Section VI](../references/RELATED_WORK.md#ghw2022), with the overlap interpretation also explicit in [Sun–Jafar, Theorem 1 and Section 5.1](../references/RELATED_WORK.md#sunjafar2025). The result established here is the delayed-ACK causal reduction and the resulting receiver-storage law. The [rate calibration](rate.md) applies the same overlap mechanism to two periodic no-feedback histories.
