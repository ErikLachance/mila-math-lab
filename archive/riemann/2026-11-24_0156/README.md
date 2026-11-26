# Riemann research checkpoint -- 2026-11-24 01:56 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-24_0156_EST.md`. **Recorded time label:** 2026-11-24 01:56 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## Sources actually consulted
- Andrew Sutherland, MIT https://math.mit.edu/~drew/grh/ last update 2026-11-24 03:30 UTC: unchanged. Compilation and independent kernel verification pass, comparator 4.33 passes, final default kernel stage of comparator 4.36 still running as of that published timestamp. External checks, not our own execution.
- Michael Rubinstein, Waterloo https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ version 2, 22 November, 265 pages. Classical exposition reduces main inequality to thirteen hypotheses; does not independently prove them all. Only HTML overview read this run.
- https://github.com/leanprover-community/riemann-hypothesis, pinned revision 40e56bab026552e089d7afcfeff08d2defb9c005. Actual sources retrieved via GitHub connector under src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/: HostFacts.lean, ConjEMemHostFIff.lean (HostRaw/HostDer), InertiaGaloisSymmetry/{KcDiff,OfRawToHostRaw,Imports,CycAll,DvdDiscrOfInertia,DecompTypeI,KcEqOfPowEqOne}.lean. Raw web access failed DisabledError; connector succeeded. No local Lean compilation. DecompTypeI defines HostCore, not a proof of each field; CycAll.hostCore assembles proofs. Read source declarations and relevant proof bodies, not the full dependency graph.
- Cyclotomic decomposition theorem and proof: https://openmaths.org/courses/NT-ANT/cyclotomic-fields.html theorem 12.3; used standard local inertia/decomposition description. Milne, Riemann form and projectivity theorem 6.7: https://jmilne.org/math/xnotes/svi2005.pdf (search excerpt of theorem, not full PDF analysis). Milne's overview https://www.jmilne.org/math/CourseNotes/av.html. Conductor-discriminant formula standard Hasse theorem, statement retrieved https://en.wikipedia.org/wiki/Conductor%E2%80%93discriminant_formula ; also source DvdDiscrOfInertia uses log_rd from Lean development. Not asserting independent proof of that classical theorem.

## A. Independent classical derivation of decomposition facts, using HostRaw inputs
Let M=QS*q*d, q,d distinct primes, q=3 mod8, d=7 mod16, gcd(QS,qd)=1, 2^(e+2)|QS, e>=2. Let E be cyclotomic subfield via the specified Artin quotient A:U(M)->G. Write K=Q(sqrt(-d)), F=E^+ and c complex conjugation. For each rational prime p write M=p^v m with gcd(m,p)=1. In U(M)=U(p^v) x U(m) inertia is U(p^v) x {1}, decomposition is U(p^v) x <p mod m>. This follows from total ramification of the prime-power factor and unramified Frobenius on the other factor. The images under A are exactly I_p,D_p in E. Important: these are images, not intersections with ker(A). Restriction of Galois decomposition and inertia is surjective.

For p|QS*q, d|m and p splits in K: at odd p this is HostRaw.QS_split or HostHyp q condition, equivalently (p/d)=1 by quadratic reciprocity; at p=2, d=7 mod8 gives (2/d)=1. Hence every u with u mod m=p^k has second sign (u/d)=1. D_p is contained in Gal(E/K)=Psi, and c is not in D_p. This independently gives decomp_typeI from the standard cyclotomic description and character projection, and hence explains why conjugate primes contract to distinct K-primes.

At p=d, the Artin d-inertia is contained in {1,iod} by art_d. It is exactly that set because the second character is the nontrivial Legendre character mod d and the d-coordinate can vary freely by CRT. Thus e(E/Q at d)=2, E/K is unramified at d (relative inertia intersection trivial), and d is excluded from the relative different support. Outside M inertia trivial. For all p, c is not in inertia; therefore E/F is unramified at every finite prime. This is distinct from E/F being split at all finite primes, which need not hold.

At d there is a stronger result: c is not even in D_d. Use HostCore.ps_d (first sign -1 on lifts of d mod QS*q), and art_d (first sign +1 on all d-inertia). Choose a lift u_1 of d mod QS*q by CRT. Any u with u≡d^k mod QS*q has u/u_1^k in d-inertia in the cyclotomic group. Its first sign is (-1)^k. On the other hand, the real dyadic projection hcl at modulus 16 of c is trivial, while d=7 mod16 has nontrivial order-two image in U(16)/{±1}. If A(u)=c, the dyadic projection forces k even; first sign forces k odd. Contradiction. This derivation uses ps_d as an input and does not prove its full general source construction. In the explicit PsQ case ps_d follows from (q/d)=1, q,d=3 mod4, so (d/q)=-1. Combined with the earlier cases this proves splitting in E/F at all p|M. No inference about unramified p splitting.

Counterexample to weakening d=7 mod16 to d=7 mod8 in the explicit PsQ case: QS=16, q=19, d=31, L=Q(zeta_16)^+, E=L(sqrt(-19),sqrt(-31)). Conditions q=3 mod8, d=7 mod8, (q/d)=1, 2 splits in K hold. But d≡-1 mod16, (d/q)=-1; at d, c belongs to D_d, not inertia. Direct exact enumeration confirms D_d size 4 with c=(1,-1,-1). Hence E/F is inert at the relevant prime(s) over d, despite unramifiedness. This is a counterexample only to weakening the host hypothesis, not to the published proof.

## B. A canonical compositum and norm simplification
Under general HostRaw/HostCore, let A0=E^{<iod>}. Since iod has second sign -1, G is a direct product of <iod> and Psi (abelian group, trivial intersection), and E=A0*K. The d-inertia description implies A0 is unramified at d; more strongly art_d gives A0 inside Q(zeta_(QS*q)), by quotienting out U(d). A0 is CM because c acts nontrivially there (first sign -1, while iod has first sign +1). Thus the discriminants of A0 and K are coprime. By the standard coprime-discriminant compositum integral basis theorem O_E=O_A0 O_K and |disc E|=|disc A0|^2*d^[A0:Q]. In particular rd(E)=rd(A0)*sqrt(d). The relative different is the extension of the absolute different of A0 (base change of trace-dual integral basis). Since every ramifying rational prime of A0 splits in K, an explicit factor B can be made by choosing one of its two K-primes for each rational p, taking the full p-part of D_E/K only above that K-prime. This B is Psi-invariant, D=B*c(B), and B+c(B)=O_E. This is a direct arithmetic construction in the model, not a proof of analytic estimates.

Root-of-unity norm: if z in E is a root of unity of order n, then d cannot divide n: otherwise Q(zeta_d) embeds in E and e_d=d-1>2, contrary to e_d(E/Q)=2. Since d is coprime to n, the d-inertia automorphism fixes z (reduction modulo a prime above d is injective on n-th roots; equivalently Q(zeta_n) unramified at d). Thus z belongs to A0. Since E=A0*K with disjoint fields, N_E/K(z)=N_A0/Q(z)=1, the latter by pairing conjugate embeddings of CM field A0. This supplies an alternate short proof of the source's norm_mu via compositum structure, matching KcEqOfPowEqOne. No assumption that all roots are ±1.

In the explicit cyclic-character PsQ construction from preceding checkpoint, E=L(sqrt(-q),sqrt(-d)) with L contained in Q(zeta_QS). Coprime discriminants then give rd(E)=rd(L)*sqrt(qd). Do not claim this last decomposition for arbitrary HostRaw without the independent q-factor/kernel hypothesis. At d the residue degree is order of (Frob_d(L),-1) in Gal(L/Q)x{±1}. Since L contains Q(zeta_16)^+, Frob_d(L) has even order, so residue degree is exactly ord(Frob_d(L)), not necessarily 2. E/F splitting is not a consequence of e=2 alone.

## C. From trace-self-dual Hermitian ideals to a principally polarized complex abelian variety
Let g=[E:K], delta=sqrt(-d) with fixed embedding delta=i sqrt(d), and use CM type consisting of all embeddings extending this K embedding (confirmed actual source CycAll.cmType and HostRaw.cmType). Let I=B^{-1} with B as above. Hermitian h(x,y)=Tr_E/K(x*c(y)), linear first; h positive definite and I is h-self-dual by previous checkpoint. Define the Z-bilinear form R(x,y)=-Tr_K/Q(h(x,y)/delta). Since conjugation(delta)=-delta and h(y,x)=bar(h(x,y)), R is alternating. Since inverse different of K is delta^{-1} O_K, R is integral on I. Conversely, if R(x,y) integral for all y in I, also test all ay for a in O_K. Trace-duality then forces h(x,y) in O_K for every y, so x belongs to I. Hence R is unimodular on the full Z-lattice (not merely nonsingular). Under the fixed embedding R=-(2/sqrt(d)) Im h, so R(Jx,Jy)=R(x,y) and R(x,Jx)=(2/sqrt(d)) h(x,x)>0 for x!=0. Sign checked explicitly; positive convention with J multiplication by i. Milne theorem 6.7 gives projectivity of complex torus E_R/I with this complex structure; unimodularity gives principal polarization. Multiplication by O_E acts on I, and Rosati adjoint of multiplication by a is multiplication by c(a), from the trace identity. This establishes the analytic abelian variety and its polarization, not the field of definition, model, reduction, cohomology, or estimates required by Alpöge.

Structural caution: this CM type is induced from K. A K-basis identifies E with K^g, and I is commensurate with O_K^g under that identification. Hence the resulting complex abelian variety is isogenous to the g-fold power of the CM elliptic curve C/O_K. For g>1 it is not simple up to isogeny. The given principal polarization need not be the product polarization, and E can still embed in the endomorphism algebra M_g(K). Do not assume a large CM field automatically gives a simple abelian variety, or that complex isogeny supplies quantitative descent/Frobenius bounds. This is an important distinction for the next source audit.

## D. Exact discriminant constants in the stabilized cyclic-character model
Let L be cut out by the real dyadic characters of U(2^(e+2)) together with one Dirichlet character psi of modulus dividing QS; assume v_2(QS)<=e+2 (or psi's local conductor divides 2^(e+2)). For each prime p the conductor-discriminant formula says v_p(rd(L)) is the uniform average of local conductor exponents across character group X_L; projection to the local character group has constant-size fibers. Thus correlations between different primes do not change this local average. At odd p the local image is cyclic of order m=t p^a, t|p-1. The number of characters with conductor exponent <=j is 1 at j=0, gcd(m,phi(p^j)) for j>=1. Summing tail probabilities gives exact average a+1 - 1/m - (1-p^(-a))/(p-1), valid also m=1 (zero). No dependence on arbitrary ambient modulus once it contains the local conductor.
At 2, the even subgroup has size 2^e; the 2^(j-1) characters of exact order 2^j have conductor exponent j+2 (j>=1), trivial character exponent zero. Hence mean e+1-2^(-e). If psi_2(-1)=-1, the local subgroup is the full product of even subgroup and odd sign; the sole difference in the odd coset is that the trivial even factor becomes conductor exponent 2. Averaging gives e+1 exactly. Thus for the cyclic stabilized model v_2(rd(L)) has a closed exact formula, and rd(E)=rd(L)*sqrt(qd) in the independent PsQ case. More generally the odd-prime formula applies to arbitrary abelian local image since U(p^v) is cyclic; dyadic formula requires precisely the stated full even subgroup and bounded conductor. These identities isolate the arithmetic constants, not the hard analytic inequality. The lower bound rd(E)>=2^(e+1-2^(-e))*sqrt(qd) follows in this model. No estimate on the number of auxiliary primes or zero-free region is smuggled into this calculation.

## E. Adversarial limitations and next experiment
- No independent RH/GRH proof, no novelty priority claim. External Lean verification and our elementary derivations are separate. The prior W12 proof does not glue to full-support positivity; do not repeat finite positivity tests absent a new uniform argument.
- Do not use d=7 mod8 as substitute for d=7 mod16 when proving decompConj. Do not confuse I_p with D_p or absolute unramifiedness with relative splitting. Do not use q-factor independence outside PsQ/kernel model. Do not assume arbitrary CM type is induced; here it is directly confirmed from source.
- Next: locate actual source proving `ps_d` and the use of `ordinary`, `unimodular`, `eta`, and the period datum. Identify precisely how the induced CM elliptic-power structure is used in algebraic descent and reduction, then trace which dimension/height bounds are quantitatively needed for theta lifts. Audit the extent to which exact root-discriminant exponents can replace conservative bounds in RdBound/RdDiff without changing quantifiers. Explore a genuinely new analytic bridge only after specifying the uniform arithmetic inequality (M); no unsupported RH implication.

## F. Actual reproducible tests
The following scripts were executed during this run. Numerical/group checks are falsification tools, not proofs of RH. Exact computations use integer residues, rational arithmetic and exact matrices. They test the explicit models, not all general HostRaw instances.

### test.py


[Extracted file: test.py](files/test.py) · 3,568 bytes · Source block 1.

### results.json


[Extracted file: results.json](files/results.json) · 343 bytes · Source block 2.

### conductor.py


[Extracted file: conductor.py](files/conductor.py) · 1,480 bytes · Source block 3.

### conductor.json


[Extracted file: conductor.json](files/conductor.json) · 121 bytes · Source block 4.


