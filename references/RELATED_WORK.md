# Related work and contribution

This comparison concerns the exact quantum streaming theorem with delayed erasure acknowledgments. The source and theorem locations below were checked against primary material on 7 November 2026. The contribution is a causal communication resource law; its entropy and coding ingredients have established antecedents.

## The operational statement being compared

A source supplies an arbitrary $`k`$-qubit register in each slot, possibly entangled with an external reference. A causal sender transmits packets of at most $`n`$ qubits. A packet either arrives intact or is erased. In every $`2B+1`$ consecutive slots, the erased positions must lie in a span of at most $`B`$ consecutive slots; holes within that span are allowed. The receiver must release the source from slot $`t`$ by the end of slot $`t+B`$.

The only backward messages are erasure acknowledgments. The acknowledgment for slot $`t`$ is available before encoding slot $`t+D`$, and cannot affect the sender earlier; $`D=\infty`$ means no feedback. All forward communication is charged to the packets. The receiver has unlimited classical records, but every retained quantum register counts toward its coherent memory, including entanglement assistance and pending packets. Released source outputs cannot be used again.

Writing $`b=\min\{D,B\}`$, the converse gives $`M\ge kb`$ receiver qubits at every clean-history cut admitting the two test continuations and with at least $`b`$ real source arrivals still to come. If only $`N_{\mathrm{remaining}}`$ real arrivals remain, the cut bound is $`M\ge k\min\{D,B,N_{\mathrm{remaining}}\}`$. In arbitrarily long sessions, qualifying cuts can occur arbitrarily late along an all-success history. For sustained streams, or the family of arbitrarily long sessions, the corresponding worst-case retained-memory requirement is attained to constant factors:

```math
M=\Theta\!\left(k\min\{D,B\}\right),\qquad T=B.
```

The construction uses packets of $`n=3k`$ physical qubits, a fixed alphabet, $`O(kB)`$ sender memory, and a finite initial entanglement bank whose receiver halves are counted and whose state is restored after a charged finite flush. The exact rate $`k/n=1/3`$ is attained for even $`k`$, including the fixed choice $`k=2,n=6`$; padding an odd group size preserves the storage scaling. This rate is optimal for the no-feedback problem with finite initial assistance. The theorem does not determine the feedback-assisted capacity.

## Entropy, overlapping recovery, and quantum storage

**Grassl, Huber, and Winter [GHW22](#ghw2022)** establish general entanglement-assisted and catalytic Singleton bounds using entropy, including arbitrary CPTP encoders and an approximate-error discussion. Their Theorem 6, Eq. (26), supplies the relevant high-erasure branch. The no-feedback endpoint of the present memory converse can be obtained by grouping two packet regions into two superletters and applying that bound. The present work therefore does not claim a new Singleton inequality, or novelty from allowing non-stabilizer encoders alone.

**Sun and Jafar [SJ25](#sunjafar2025)**, Theorem 1, Eq. (4), state the intersection bound for exact distributed quantum storage: a message's dimension is limited by the size of the overlap between any two authorized recovery sets. Their Section 5.1 gives the entropy argument. This is a direct antecedent for interpreting a retained receiver register as the common part of two recovery regions.

The additional step here is temporal. At a qualifying cut with at least $`b`$ real arrivals remaining, no post-cut acknowledgment can affect the first $`b`$ emissions, so they define one common state with early packets $`A`$, the sender's retained remainder $`E`$, and the pre-cut receiver register $`Q`$. Compare bursts on slots $`0,\ldots,B-1`$ and $`b,\ldots,b+B-1`$. The later burst forces recovery of the first $`b`$ sources from $`QA`$. The earlier burst erases $`A`$, but the subsequent protocol can be simulated by a virtual decoder granted $`QE`$. The initial common state, together with these two virtual recovery maps, makes the inherited overlap obstruction apply despite the later branch-dependent encoder. This reduction identifies acknowledgment delay as the number of fresh source groups whose coherent protection must already be represented at the receiver.

The no-feedback rate bound $`1/3`$ is another application of the same mechanism. Two admissible periodic burst patterns have common survivor density $`1/3`$. Their recovery regions, with finite initial assistance included, yield the asymptotic rate converse. This capacity calibration is useful for comparing memory costs, but is not a separate new entropy principle.

## Secret sharing, communication ciphers, and finite assistance

**Cleve, Gottesman, and Lo [CGL99](#qss1999)** establish quantum threshold secret sharing and its relation to erasure correction. **Leung [L02](#leung2002)**, Section 5 and Appendix C, gives the particularly close communication primitive: Alice encodes an unknown quantum source using her half of a shared pair, sends one share, and successful decoding both delivers the source and regenerates shared entanglement. The construction here uses this existing primitive over a fixed four-dimensional field alphabet, implemented with two physical qubits per symbol.

**Brun, Devetak, and Hsieh [BDH14](#bdh2014)**, Section 4 and Lemma 4.1, already explain how a finite catalyst can be renewed across arbitrarily many coding blocks. A finite returned entanglement bank is therefore an accounted resource, rather than a novel coding concept.

The present schedules give these ingredients a particular causal use. Without feedback, the three shares for source $`t`$ are transmitted at $`t-B,t,t+B`$; the first share is independent of the unknown future source and is implemented by preparing entanglement in advance. With $`1\le D\le B`$, $`D`$ cyclic banks support normal operation. A reported loss freezes the affected retained shares. The burst promise supplies a guaranteed clean repair interval in which the held shares, replacement entanglement, and buffered payload are sent within the same packet budget and every source deadline. The schedule, memory accounting, and bank return are needed for the matching streaming theorem; none is supplied merely by citing the cipher.

## Feedback protocols and memory placement

**Yu, Lai, and Zhou [YLZ21](#yu2021)**, Section IV.C and Protocol 3, use recursive secret sharing for ACK-controlled quantum retransmission. Their analysis concerns variable completion times and expected transmission cost under an independent-loss model. This directly precedes the retransmission idea, but does not give the present fixed-deadline stream schedule or a converse over all encoders.

**Leung, Lim, and Shor [LLS09](#leunglimshor2009)** study quantum erasure-channel capacity with backward classical communication, using coherent communication and entanglement regeneration. Their asymptotic independent-erasure model has no retained receiver-memory restriction or deadline for each arriving quantum source.

**Jones et al. [J16](#jones2016)**, Section III.B and Fig. 4, explicitly connect local heralding, acknowledgment delay, and asymmetric memory placement in entanglement-generation architectures. Consequently, the general observation that signaling affects memory requirements is established. The result here quantifies an unavoidable coherent-memory cost for all causal quantum data encoders in the stated packet model, and supplies a schedule meeting that cost in order.

## Convolutional codes and implementation memory

**Wilde and Brun [WB09](#wildebrun2009)** demonstrate reduced memory demand for entanglement-assisted quantum convolutional encoders. **Houshmand, Hosseini-Khayat, and Wilde [HHW12](#houshmand2012)** calculate the minimum memory needed to implement a specified pearl-necklace encoder. These results concern code or circuit realization; the latter optimizes a given encoder representation. They do not identify the minimum retained receiver storage over all protocols with the source arrivals, erasure promise, and deadlines used here. Entanglement-assisted convolutional coding nonetheless supplies relevant background for online coding and careful accounting of supplied entanglement.

## Consequence and scope

At the same rate $`1/3`$ and deadline $`B`$, timely erasure acknowledgments change the optimal order of receiver storage from $`kB`$ to $`kD`$ when $`D\le B`$. For fixed $`D`$, the receiver requirement remains bounded as the tolerated burst length grows, while the sender retains an $`O(kB)`$ buffer. The converse is independent of forward packet width: increasing bandwidth alone cannot remove the clean-cut storage obstruction.

This is a resource statement for a specified idealized communication model. It does not cover noisy memories, unreliable acknowledgments, arbitrary independent losses with deterministic deadlines, or a general rate–deadline–memory region. Its burst promise provides the clean interval used by the achieving schedule. The lower bound is a worst-case storage requirement, not a claim about every cut immediately after a recent burst. Near a finite session's end it counts only real source arrivals remaining; the displayed constructions need not minimize assistance or memory for sessions shorter than the acknowledgment delay. These restrictions are part of the theorem's content and the comparison with prior work.

The resulting contribution is the matched acknowledgment-delay/receiver-memory law under a hard source deadline, including its sustained operation and resource accounting. The shared foundations are entropy-based overlapping recovery, quantum secret sharing, communication-cipher recycling, and catalytic coding.

## Primary references and inspected locations

Machine-readable entries are available in [references.bib](references.bib). The named anchors below match the BibTeX keys.

<a name="ghw2022"></a>

### GHW22 — Entropic Singleton bounds

Markus Grassl, Felix Huber, and Andreas Winter, *Entropic proofs of Singleton bounds for quantum error-correcting codes*, IEEE Transactions on Information Theory **68**(6), 3942–3950 (2022). [arXiv:2010.07902v4](https://arxiv.org/abs/2010.07902v4), 31 May 2022; Theorems 5–6 and Section VI. [DOI](https://doi.org/10.1109/TIT.2022.3149291).

<a name="sunjafar2025"></a>

### SJ25 — Distributed quantum storage

Hua Sun and Syed A. Jafar, *On the Capacity of Distributed Quantum Storage*. [arXiv:2510.10568v1](https://arxiv.org/html/2510.10568v1), 12 October 2025; Theorem 1, Eq. (4), and Section 5.1.

<a name="qss1999"></a>

### CGL99 — Quantum secret sharing

Richard Cleve, Daniel Gottesman, and Hoi-Kwong Lo, *How to share a quantum secret*, Physical Review Letters **83**, 648–651 (1999). [arXiv:quant-ph/9901025v1](https://arxiv.org/abs/quant-ph/9901025v1), 12 January 1999. [DOI](https://doi.org/10.1103/PhysRevLett.83.648).

<a name="leung2002"></a>

### L02 — Quantum Vernam cipher

Debbie W. Leung, *Quantum Vernam Cipher*, Quantum Information and Computation **2**(1), 14–34 (2002). [arXiv:quant-ph/0012077v4](https://arxiv.org/abs/quant-ph/0012077v4), 9 October 2001; Section 5 and Appendix C.

<a name="bdh2014"></a>

### BDH14 — Catalytic quantum error correction

Todd Brun, Igor Devetak, and Min-Hsiu Hsieh, *Catalytic quantum error correction*, IEEE Transactions on Information Theory **60**, 3073–3089 (2014). [arXiv:quant-ph/0608027v2](https://arxiv.org/abs/quant-ph/0608027v2), 3 August 2006; Section 4, particularly Eqs. (39)–(43) and Lemma 4.1. [DOI](https://doi.org/10.1109/TIT.2014.2313559).

<a name="yu2021"></a>

### YLZ21 — Quantum packet retransmission

Nengkun Yu, Ching-Yi Lai, and Li Zhou, *Protocols for Packet Quantum Network Intercommunication*, IEEE Transactions on Quantum Engineering **2**, 4103709 (2021). [arXiv:1903.10685v3](https://arxiv.org/abs/1903.10685v3), 12 September 2021; Section IV.C and Protocol 3. [DOI](https://doi.org/10.1109/TQE.2021.3112594).

<a name="leunglimshor2009"></a>

### LLS09 — Feedback-assisted erasure capacity

Debbie Leung, Joungkeun Lim, and Peter Shor, *Capacity of Quantum Erasure Channel Assisted by Backwards Classical Communication*, Physical Review Letters **103**, 240505 (2009). [arXiv:0710.5943v4](https://arxiv.org/abs/0710.5943v4), 2 January 2010. The preprint title is *On quantum capacity of erasure channel assisted by back classical communication*. [DOI](https://doi.org/10.1103/PhysRevLett.103.240505).

<a name="jones2016"></a>

### J16 — Quantum repeater communication protocols

Cody Jones, Danny Kim, Matthew T. Rakher, Paul G. Kwiat, and Thaddeus D. Ladd, *Design and Analysis of Communication Protocols for Quantum Repeater Networks*, New Journal of Physics **18**, 083015 (2016). [arXiv:1505.01536v1](https://arxiv.org/abs/1505.01536v1), 6 May 2015; Section III.B and Fig. 4. [DOI](https://doi.org/10.1088/1367-2630/18/8/083015).

<a name="wildebrun2009"></a>

### WB09 — Entanglement and convolutional encoder memory

Mark M. Wilde and Todd A. Brun, *Extra shared entanglement reduces memory demand in quantum convolutional coding*, Physical Review A **79**, 032313 (2009). [Author-hosted published article](https://markwilde.com/publications/PhysRevA_79_032313.pdf); Theorem 1. [arXiv:0812.4449v2](https://arxiv.org/abs/0812.4449v2), 10 February 2009.

<a name="houshmand2012"></a>

### HHW12 — Memory of a specified convolutional encoder

Monireh Houshmand, Saied Hosseini-Khayat, and Mark M. Wilde, *Minimal memory requirements for pearl-necklace encoders of quantum convolutional codes*, IEEE Transactions on Computers **61**(3), 299–312 (2012). [arXiv:1004.5179v2](https://arxiv.org/abs/1004.5179v2), 1 November 2010; the encoder-dependency graph and longest-path memory construction. [DOI](https://doi.org/10.1109/TC.2010.226).

The locations listed identify the material used in this comparison. They do not assert a complete audit of every cited paper or a global priority certification.
