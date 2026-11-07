# The no-feedback rate benchmark

Under the [sliding-span packet model](model.md) with window length $`W=2B+1`$, deadline $`T=B`$, and finite initial assistance, the exact asymptotic no-feedback rate is

```math
\frac{k}{n}=\frac13.
```

This benchmark calibrates the memory comparison: the delayed-ACK construction operates at the optimal no-feedback rate while reducing receiver storage when $`D<B`$. No feedback-assisted capacity claim is made.

The converse uses the same established overlapping-recovery mechanism as the [memory theorem](converse.md). It is an application of the [Singleton and storage-intersection antecedents](../references/RELATED_WORK.md#ghw2022), not a new entropy inequality.

## Assumptions and finite-horizon statement

Each complete slot system has dimension at most $`2^n`$, including any metadata. It is delivered or erased by the end of its slot, and all forward communication is charged. There is no backward communication. In every $`2B+1`$-slot window, erased positions must fit inside an interval of at most $`B`$ consecutive slots; holes inside that interval are allowed.

Take $`L`$ source groups at slots $`0,\ldots,L-1`$. Each has dimension $`d=2^k`$ and must be released by its arrival slot plus $`B`$. Let $`Q_0`$ be the receiver's initial quantum resource and $`Y`$ its unrestricted classical record. All initial entanglement halves are included in $`Q_0`$, and released logical outputs cannot be used again. The sender's complete initial memory is $`E_0`$.

For exact transmission,

```math
kL\le S(Q_0\mid Y)+\frac{n(L+B)}3
\le M_0+\frac{n(L+B)}3,
```

where $`M_0`$ bounds $`\log_2\dim Q_0`$. More generally, define

```math
f_d(\varepsilon)=h_2(\varepsilon)+\varepsilon\log_2(d^2-1),
\qquad 0\le\varepsilon\le1-d^{-2}.
```

If every source, tested on independent EPR pairs, has unconditional entanglement fidelity at least $`1-\varepsilon`$ under every admissible erasure sequence, then

```math
L\bigl[k-f_d(\varepsilon)\bigr]
\le S(Q_0\mid Y)+\frac{n(L+B)}3.
```

The fidelity convention and its individual-message information bound are proved in [the converse](converse.md#3-individual-message-fidelity-and-the-entropy-conclusion). No joint fidelity guarantee for all $`L`$ outputs is needed.

## 1. Two admissible periodic erasure patterns

For every integer $`j\ge0`$, let

```math
\begin{aligned}
\mathsf P_0 &: [3jB,3jB+B-1]\text{ erased},\\
\mathsf P_1 &: [3jB+B,3jB+2B-1]\text{ erased}.
\end{aligned}
```

Each pattern satisfies the sliding-span promise. The distance from the last erased slot of one burst to the first erased slot of the next is exactly $`2B+1`$. Two positions within one $`2B+1`$-slot window differ by at most $`2B`$, so no such window sees parts of two distinct bursts. Its erasures therefore lie within one $`B`$-slot interval.

Within each $`3B`$-slot period the delivery sets are:

| Relative slots | Under $`\mathsf P_0`$ | Under $`\mathsf P_1`$ |
|---|---|---|
| $`0,\ldots,B-1`$ | erased | delivered |
| $`B,\ldots,2B-1`$ | delivered | erased |
| $`2B,\ldots,3B-1`$ | delivered | delivered |

Their common delivered systems occupy the final third of each period.

## 2. A common no-feedback state

The final source deadline is $`L+B-1`$, so set $`H=L+B`$. Feed the $`L`$ tested sources as independent halves of maximally entangled pairs, with inaccessible references $`R=R_0\cdots R_{L-1}`$. Fix all other inputs independently.

With no feedback, both histories use one encoder through the first $`H`$ slots. Defer receiver operations and erasures to obtain a common pre-erasure state. Restricting packet positions to $`0,\ldots,H-1`$, write:

- $`C`$ for systems delivered in both histories;
- $`A`$ for systems delivered only under $`\mathsf P_0`$;
- $`F`$ for systems delivered only under $`\mathsf P_1`$.

Each history's actual decoder induces a channel recovering the required output marginals from $`Q_0CAY`$ or $`Q_0CFY`$, respectively. Collecting the already released outputs is only a mathematical composition of these maps, as explained in the [memory proof](converse.md#released-outputs-are-not-a-hidden-memory-resource). No released output becomes available to later physical decoding.

Packets sent after the final deadline, including a catalyst-restoration flush, cannot assist these source outputs and are not used in the argument.

## 3. Entropy and the exact overlap count

Apply the classical-record overlap inequality with common quantum register $`Q_0C`$:

```math
I(R:Q_0CAY)+I(R:Q_0CFY)
\le2S(R)+2S(Q_0C\mid Y).
```

The independent-reference, individual-fidelity argument gives a lower bound $`L[2k-f_d(\varepsilon)]`$ for each mutual information on the left. Since $`S(R)=kL`$,

```math
L\bigl[k-f_d(\varepsilon)\bigr]\le S(Q_0C\mid Y).
```

Conditioning on the classical record and using the charged slot dimensions gives

```math
S(Q_0C\mid Y)
\le S(Q_0\mid Y)+S(C\mid Y)
\le S(Q_0\mid Y)+n|C|.
```

There is no term involving the size of the free classical record. Write $`H=3Ba+r`$, where $`0\le r<3B`$. The common positions occur in complete final blocks and any surviving final-block suffix:

```math
|C|=Ba+\max\{0,r-2B\}\le\frac H3=\frac{L+B}3.
```

Combining these inequalities proves the finite-horizon statement, including the endpoint term $`nB/3`$.

## 4. Finite assistance and initially local workspace

The bound can be stated directly in terms of initial shared entanglement rather than the size or entropy of local ancillary memory. Use the [supporting convex-roof argument](converse.md#4-supporting-resource-interpretation-initial-entanglement) to define

```math
\mathcal E_0
=\overline E_F(E_0:Q_0\mid Y)
=\sum_y p_y E_F(\rho_{E_0Q_0}^{y}).
```

Then the same proof gives

```math
L\bigl[k-f_d(\varepsilon)\bigr]
\le\mathcal E_0+\frac{n(L+B)}3.
```

For completeness, attach a pure-ensemble label $`Z`$ to each conditional initial state, give it to both virtual decoders, and run the unchanged code ignoring it. All unconditional output fidelities remain unchanged. The preceding argument yields

```math
L\bigl[k-f_d(\varepsilon)\bigr]
\le S(Q_0C\mid YZ)
\le S(Q_0\mid YZ)+n|C|.
```

Because the common no-feedback encoder acts only on sender systems, the conditional marginal of the original $`Q_0`$ is unchanged. Minimizing its average pure-state entropy over the initial ensembles produces $`\mathcal E_0`$.

This refinement is resource bookkeeping: initially pure local workspace is not assistance. It does not claim an optimal consumed-entanglement rate or replace the main receiver-memory theorem.

## 5. Asymptotic benchmark and limits of the claim

For fixed $`B`$, exact transmission, and initial assistance $`\mathcal E_0=o(nL)`$, divide the bound by $`nL`$ and let $`L\to\infty`$. This gives

```math
\frac{k}{n}\le\frac13.
```

A fixed finite Bell seed, independent of the session horizon, meets this condition. The same conclusion holds for vanishing individual-message infidelity. In particular,

```math
\frac{k}{n}(1-2\varepsilon)-\frac{h_2(\varepsilon)}n
\le\frac{\mathcal E_0}{nL}+\frac13+\frac{B}{3L}
```

controls the correction even when source and packet dimensions vary.

The [three-share causal construction](no_feedback_protocol.md) uses even $`k`$, packets of $`n=3k`$ qubits, and a fixed $`Bk`$-ebit seed. Its [charged finite flush](no_feedback_protocol.md#exact-return-for-every-finite-source-horizon) restores the seed exactly after $`2B`$ additional slots, so its finite-session rate is

```math
\frac{kL}{3k(L+2B)}=\frac{L}{3(L+2B)}\longrightarrow\frac13.
```

Together with the converse, this establishes the exact/vanishing-error asymptotic no-feedback benchmark. The construction already works with the fixed physical choice $`k=2,n=6`$; increasing a local alphabet with $`B`$ is unnecessary.

The converse permits consuming sublinear initial assistance, so requiring its return does not weaken the upper bound. By contrast, saying only that each finite session uses some finite catalyst is insufficient if its initial size may grow linearly with the horizon. We do not infer a catalytic converse outside the stated assistance condition.

For fixed nonzero error, the quantitative bound above is the result; a stronger fixed-error capacity statement is not claimed. The benchmark also depends on the precise $`W=2B+1`$ family. It is not asserted for the stronger $`W=4B`$ promise, and it does not determine feedback-assisted capacity.

## Primary attribution

The common-recovery entropy mechanism is inherited from [Grassl–Huber–Winter](../references/RELATED_WORK.md#ghw2022) and the [storage-intersection formulation of Sun–Jafar](../references/RELATED_WORK.md#sunjafar2025). Here it is applied to two explicitly admissible periodic channel histories. The no-feedback benchmark supplies a common rate for the receiver-memory comparison; it is not a separate claim of a new Singleton principle.
