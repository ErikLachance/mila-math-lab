# Riemann research checkpoint -- 2026-11-24 00:41 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-24_0041_EST.md`. **Recorded time label:** 2026-11-24 00:41 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## Sources actually consulted
- MIT independent verification https://math.mit.edu/~drew/grh/ last updated 2026-11-24 03:30 UTC (unchanged): 175187 modules compiled and replayed, independent kernels accept, comparator 4.33 passes; 4.36 final Lean kernel stage ongoing. This is externally verified work, not our own replay.
- Waterloo https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ version 2 (22 November): 13 classical hypotheses not fully written out in that exposition. LaTeX direct fetch failed HTTP400 unsupported text/x-tex, so no new detailed comparison of H12 prose asserted.
- Actual Lean sources retrieved at pinned original revision 40e56bab026552e089d7afcfeff08d2defb9c005 of https://github.com/leanprover-community/riemann-hypothesis . Paths under src/Development/AutomorphicArithmetic: CoprimeRanks/{AdmChi,SecondSetNoRelation}; CharacterBoxes/{Imports,FieldChi,TwistForm,HostOfField,Supply,PairGood,IsChiField,BoundedTw,OrdAny}; FrobeniusLocalisation/SizeDefs; ShortNorms/supplyOfAdmOf. Also src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsRanksRankValFrame; src/Formalism/{LocalRingCardinality/DataHost,FrobeniusOrbits/HostDiffSupport}; src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/{HostFacts,ConjEMemHostFIff,InertiaGaloisSymmetry/{OfRawToHostRaw,ExistsHostAxEven,Imports,KcDiff,KcEqOfPowEqOne}} (all .lean). No local Lean compilation.
- Stacks Project tag 0BW0 https://stacks.math.columbia.edu/tag/0BW0 for trace complementary module and inverse different; Mureau 2026 https://arxiv.org/abs/2608.03564 abstract for related CM ideal-lattice research (not theorem dependency). Classical Dedekind-Kummer and coprime-discriminant compositum integral-basis facts used below.

## A. Actual exists_host audit: closes source-level ambiguity, not full geometric proof
`admitted` quantifies EVERY b and Choices c satisfying FieldRows and q,d>4tr+1. `exists_host` in SecondSetNoRelation is a packaging theorem, not itself a fresh CM existence theorem: it chooses square root from FieldRows.sqq, a CM type member from HostAx.der.cmType (nonzero cardinality), and an ideal b from HostAx.der.principal. It returns a Host with the original HostAx, same splitBound and heterogeneous equality of Choices. `nonempty_choices` alone is much weaker: permits TT=T2=empty, CT2=0 and ccK=unit ideal; cannot use it to obtain Shares/large sets. `admissibleClassesTwistedChar` obtains Ranks with exactly the given frame and RankVal (explicit rank existence source uses threshold x0=16), then universally applies admitted. The geometric/number-theoretic input is upstream in `HostRaw.der`, constructed by `HostAx.ofRaw`, NOT assumed separately in FieldChi. `HostRaw.der` in OfRawToHostRaw obtains HostCore and invokes Der.principal, Der.diffSupport, Der.unimodular, etc.
`KcDiff.lean` establishes relative different support over primes dividing QS*q (not d); uses inertia characterization and excludes nontrivial inertia fixing K at d. `kc_below_ne` uses decomp_typeI and Galois transitivity to show the contractions of P and conjugate(P) to K are distinct for every prime in support. `kc_below_smul` shows Psi fixes contractions; `principal` orients each conjugate pair by well-ordering of contracted primes. It gives D=b*c(b), b+c(b)=O_E, b stable under Psi. This is not a statement that b is principal as a generated ideal despite theorem name. `discr_sq` separately uses unramifiedness of E/F to show absolute discriminant square; do not confuse E/F with E/K. No independent verification of HostCore's inertia/decomposition theorems in this pass.
`IsChiField.lean` takes KerChi and constructs witness modulus QS*q*d and cyclotomic embedding; art_spec and primitive root show fixing image equivalent to Artin kernel, then KerChi supplies congruence/character tests. In supplyOfAdmOf, `subst hH` after host construction literally transports all raw-field hypotheses; `isChiField` then rewritten by equalities for e,q,d and consumed by uniform hW.bound. `boundedTw_key` also requires prime support of QS contained in 2*psi.N and excludes i=j=0 by either not-kept or negative sign on iod. This is why nontrivial-twist analytic estimates suffice; cannot use them for the kept character. This is source audit, not an independent cohomology bound.

## B. Independent exact general orbit criterion for ideal factorization
Let D nonzero integral ideal in a Dedekind domain, c an involutive automorphism, H a group of automorphisms normalized by c, and D invariant under H and c. Work with finite positive prime support of D. H-orbits O have a constant positive valuation d_O, and c induces an involution on these orbits. H-invariant integral ideals B with D=B*c(B) correspond exactly to nonnegative integers b_O with b_O+b_c(O)=d_O. For each two-orbit pair choose any b_O from 0..d_O; for fixed orbit the only candidate is d_O/2. Thus number is zero if any fixed orbit has odd d_O, otherwise product over two-orbit pairs (d_O+1). If impose B+c(B)=O_E (coprimality), exactly one of b_O,b_c(O) must vanish for positive d_O. Consequently count is zero if ANY positive fixed orbit exists, otherwise 2^r for r paired H-orbit pairs. Proof is unique ideal factorization coordinate by coordinate; no need for c to commute with H, normalization suffices. In particular c acting freely on individual primes is not sufficient: H=<swap> acting on {P,Q} with c=swap, D=P Q, has one fixed H-orbit and no H-stable factor. Even valuation 2 on that orbit permits B=P Q but not coprime. This isolates the necessity of the contraction argument in KcDiff, which orients at the K-prime level. When H=Gal(E/K), conjugation swaps the underlying distinct K-primes; no fixed orbit. Generalization is elementary, no priority claim.
Exact regression on all permutations g and involutions c normalizing <g> for n=1..5 and invariant exponents 0..2: 14,337 instances; direct enumeration of all exponent solutions matched both counts every time. 4,095 instances admitted only noncoprime solutions, 8,699 admitted no integral factor at all. The rest admit a coprime solution. These are abstract valuation data, not claims all arise in actual number fields.

## C. Trace-dual lemma and independent explicit CM family
For fractional ideal I in E/K and conjugation c restricting to conjugation of K, dual under h(x,y)=Tr_E/K(x*c(y)) equals D^{-1} c(I)^{-1}. Indeed x*c(I) is an O_E-ideal, and trace-integrality for every y is equivalent to membership in the complementary module D^{-1} because multiplying by all O_E elements stays in that ideal. Thus I=B^{-1} self-dual iff D=B*c(B), irrespective of coprimality. Coprimality and H-invariance are extra constraints, not implied by self-duality. If K imaginary quadratic, E CM, then h is positive definite at fixed complex embedding of K: trace is sum of |sigma x|^2 over extending embeddings. This does not by itself give the required abelian varieties, Frobenius control, height bounds, or positivity on arbitrary analytic test functions.
Concrete infinite family: K=Q(i), E=K(sqrt(m)), m>1 squarefree product of primes 1 mod4. Write pi in Z[i] with pi*bar(pi)=m, choosing one conjugate Gaussian prime above each p. By coprime discriminants (-4 and m), O_E=Z[i][phi] for phi=(1+sqrt(m))/2, f=phi^2-phi-(m-1)/4. D=(sqrt(m)) from f'. Set r=(m+1)/2; f(r)=m(m-1)/4, hence r mod pi is a root. B=(pi,phi-r), a Z[i]-module with displayed basis, equals product of unique ramified primes over selected Gaussian primes by reduction of f at each prime, where f has a double root. Complement conjugate B has other primes, D=B*c(B). I=B^{-1}=c(B)/sqrt(m) has basis e1=bar(pi)/sqrt(m), e2=(phi-r)/sqrt(m). Direct trace gives G=[[2,-bar(pi)],[-pi,(m+1)/2]] (linear first convention) and determinant1. For a,b in Z[i], h(ae1+be2,ae1+be2)=2|a-pi*b/2|^2+|b|^2/2. Taking b=1 and a coordinatewise nearest Gaussian integer to pi/2 gives norm1 (exactly one coordinate of pi odd). Let t=ae1+e2 and z=e1-h(e1,t)t. z orthogonal to t, basis determinant -1, hence norm(z)=1. Thus all these explicit Hermitian lattices are actually standard rank-two Z[i] lattices; merely choosing large discriminant does not create nontrivial geometric complexity.
Negative concrete test: E=Q(i,sqrt(3)), K=Q(i). 3 is inert in K and x^2-3 Eisenstein at the unique prime over 3, hence E/K there is tame ramification index2 and relative different exponent1 at unique prime over 3. Conjugation fixes this prime, so D cannot factor as B*c(B) even without coprimality. This disproves any blanket CM-only hypothesis for the ideal factorization; it does NOT challenge the more specific host source.
Exact regression: 9,968 Gaussian-prime orientation choices over all subsets of 1..4 of 12 primes, m up to 63,651,109. Each checked 4 Gram entries via independent integer pair arithmetic, determinant, norm-one vector, orthogonal split and unimodular basis transform. All pass. These verify algebraic expressions rather than prove infinite result by sampling.

## D. Independent cyclotomic kernel stabilization (explicit cyclic-character constant)
The source `OrdAny.lean` proves eventual ord=c*2^e by monotonicity of image of the dyadic kernel and stabilization in finite group. For one Dirichlet character psi modulo N=2^v M, M odd, write psi=psi_2*psi_odd by CRT. For e+2>=v, e>=1, consider G=U(2^(e+2)) x U(M) and map to U(2^(e+2))/{+-1} x C^* by (a,b)->([a],psi_2(a mod2^v)*psi_odd(b)). First projection is surjective and has size 2^e. Image of kernel of first projection consists exactly of products generated by psi_2(-1) and image psi_odd. Both finite cyclic roots of unity, so size c=lcm(ord(psi_odd),ord(psi_2(-1))) and total image order c*2^e. This explicit formula for cyclic-character case removes unknown stabilization threshold (at most max(1,v-2) for this calculation). It does not claim a formula by single lcm for a general multi-generator character subgroup. For q,d distinct odd primes not dividing N (and q,d congruent 3 mod4 as host), adding Legendre symbols independently multiplies image order by4 via CRT. KerChi then identifies image field inside Q(zeta_lcm(2^(e+2),N)*q*d) using Galois correspondence: compositum of real dyadic cyclotomic field, field cut out by psi, and quadratic fields Q(sqrt(-q)), Q(sqrt(-d)). Degree is 4*c*2^e, consistent with HostDer.finrank_E=4*ord. This identifies field up to isomorphism given the exact kernel, not pointwise equality of arbitrary representations. Need q,d coprime to N and distinct; if one already occurs in character conductor then CRT independence fails. Psi_2(-1) cannot be omitted: pure odd dyadic character with no odd part yields c=2, not1. Numerical test all exact character phases for v=0..5, odd prime moduli 3,5,13,17 and two admissible e each: 2176 character cases, 443520 unit-pair evaluations, including 120 pure dyadic-odd cases. Separate full CRT enumeration N=8*5*11*7: 960 units, image32, kernel30, agrees with e=1,c=4. This toy e=1 is group algebra only, not full host conditions e>=2. General finite image argument supplies proof, not the enumeration.

## E. Adversarial status and next research
- Exact classical sublemmas above, no independent proof of RH/GRH, no claim of novelty in literature. External announced proof and external machine checks distinct from our own research. No new MIT status since last run.
- Avoid repeating old endpoint-Galerkin positivity or inferring global positivity from local tests. Avoid treating `exists_host` as entire geometric construction, `nonempty_choices` as quantitative, `principal` as principality, CM alone as sufficient, or collapsing kept and twisted characters. Do not assume existence of suitable analytic windows uniformly over auxiliary fields without proof.
- Next highest-value source audit: trace HostCore.decomp_typeI and exact inertia via cyclotomic CRT and the explicit character kernel. Seek an independent derivation of support over QS*q and K-splitting including dyadic place and q; then study how trace-self-dual lattice passes to genuine period datum and algebraic descent. The explicit cyclic c formula may simplify classical constants but does not replace the hard arithmetic/cohomological estimates. Compare to Waterloo detailed H12 once source text is accessible. Distinguish general subgroup from cyclic case.

## Reproducible tests (actual scripts and output)

### riemann_0041_orbits.py


[Extracted file: riemann_0041_orbits.py](files/riemann_0041_orbits.py) · 2,000 bytes · Source block 1.

### riemann_0041_orbits.json


[Extracted file: riemann_0041_orbits.json](files/riemann_0041_orbits.json) · 436 bytes · Source block 2.

### riemann_0041_cm.py


[Extracted file: riemann_0041_cm.py](files/riemann_0041_cm.py) · 2,023 bytes · Source block 3.

### riemann_0041_cm.json


[Extracted file: riemann_0041_cm.json](files/riemann_0041_cm.json) · 148 bytes · Source block 4.

### riemann_0041_cyclotomic.py


[Extracted file: riemann_0041_cyclotomic.py](files/riemann_0041_cyclotomic.py) · 1,842 bytes · Source block 5.

### riemann_0041_cyclotomic.json


[Extracted file: riemann_0041_cyclotomic.json](files/riemann_0041_cyclotomic.json) · 213 bytes · Source block 6.


