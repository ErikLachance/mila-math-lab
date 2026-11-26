# Riemann research checkpoint -- 2026-11-23 23:48:36 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_2348_EST.md`. **Recorded time label:** 2026-11-23 23:48 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## Sources consulted
- MIT independent verification: https://math.mit.edu/~drew/grh/ ; updated 2026-11-24 03:30 UTC (Nov 23 22:30 EST), same as last checkpoint. Reports module compilation, standard axioms, statement comparisons, independent kernels, sandbox rebuild, Comparator 4.33 pass, Comparator 4.36 final stage running. No claim of a new independent proof here.
- Waterloo exposition v2: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ ; H0-H12 schematic hypotheses, not a full independent validation of each.
- Source repository https://github.com/leanprover-community/riemann-hypothesis ; pinned revision 40e56bab026552e089d7afcfeff08d2defb9c005. Dependency guide https://github.com/nasqret/riemann-rev is a navigation aid only. Read actual source at pin via GitHub file fetch: src/Development/AutomorphicArithmetic/CharacterBoxes/{Supply,HostOfField,WinPairs,FieldChi,TwistForm}.lean; ShortNorms/{supplyOfAdmOf,hostOfFieldOf,hostExOneOf}.lean; CoprimeRanks/AdmChi.lean; ThickFrames/{ThickFrame2Large,topsChoiceH}.lean. Also inspected SupplyChi.lean and Formalism/FrobeniusOrbits/FrobeniusOrbitsProofs/ThickExists.lean through web. No local Lean replay. Some direct web requests failed; connector retrieval of listed source succeeded.

## A. Actual host construction and quantifier audit
In WinPairs.winPairs, fix psi, epsilon, c, VWinAt and PairEx. Choose J and X sufficiently large; pick q,d from PairEx at Y=X^(1/J), then obtain W with uniform cohomological bound from VWinAt. With k=c^(1/(2+8eps)), all x in [kW,(kW)^(3/2)] use the SAME q,d,Y, varying page e if necessary. TwistForm.WinDatum contains x^(1/J)<=Y<=x, PairGood psi.N eps Y x q d, x^(2+8eps)<=c*2^e<=2*x^(2+8eps), and the bound for ALL number fields E satisfying IsChiField psi e q d E. This is stronger than pointwise pair selection.

FieldChi.fieldChi constructs the frame and H0 with precisely those q,d, from sufficiently large e, HostHyp, q != 3, coprimality and small-prime splitting. Returns FieldRows, conductor divisibility, kernel/twist conditions. AdmChi.admissibleClassesTwistedChar universally lifts EVERY frame in the scale window and its H0 to R with RankVal and admitted; admissible_ranks_of_CMDatum invokes exists_host. HostOfField.hostOfField invokes hostOfFieldOf shortNorm smallOne. In hostOfFieldOf constants CT2,C8,c6,Cb,x0 are fixed BEFORE all s,R,H0,M,Y. Inputs include PairGood for the actual H0.q,H0.d, FieldRows, admitted; output H preserves toHostAx=H0, satisfies HostGood and Shares. In supplyOfAdmOf the order is fieldChi -> winPairs(QH.pairEx) -> uniform thresholds -> WinDatum for the scale -> pairHyp -> hF -> hB -> hA -> boundedTw/isChiField/hW.bound. The trivial-character hostExOneOf also first chooses good pair then constructs host. Consequently no additional probability-overlap or density hypothesis is needed at this interface of the formal source. The earlier abstract host intersection inequality is valid but not the mechanism actually used. This is a source-level resolution of the specific compatibility question, not an independent proof of geometry or a complete audit of H0-H12.

Further decomposition: hof_exists_host consumes admitted with concrete choices. hof_thick invokes thickFrame2, ultimately hostThickExists, a combinatorial Behrend-type construction, not the entire geometric host. topsChoiceH produces TT separately from T2. hof_box handles conductor support for twisted character conditions. The next dependency to examine is exists_host (CM datum to admitted), then exact IsChiField preservation and the imported ShortNorm, SmallOne and VWinAt results; distinguish their hypotheses from conclusions. Do not infer H12 solely from the combinatorial lemma.

## B. Independent finite combinatorial refinement
For a triple a<b<c, write u=b-a, v=c-b, g=gcd(u,v), u'=u/g, v'=v/g. A nontrivial relation j(s2-s1)=i(s3-s1) with distinct integer coefficients i,j nonzero and absolute values <=L exists for some ordering precisely when max(u',v')<=L. Middle anchor realizes this with opposite signs; endpoint anchor instead requires u'+v'<=L, which implies the same max bound. Conversely the reduced pair at a middle anchor divides any integer coefficients by their common factor. Thus for L>=2 the primitive positive pair has u'+v'<=2L-1 (both L impossible by coprimality); L=1 has sum<=2.

Take vectors v in {0,...,d-1}^S on one fixed squared Euclidean norm shell. Encode by base B=(2L-1)(d-1)+1 for L>=2, or B=2(d-1)+1 for L=1. B>=d so injective. If three distinct encoded points a<b<c violate NoRel, (u'+v')b=v'a+u'c. At each digit, the signed discrepancy in the relation has magnitude <=(u'+v')(d-1)<B. Reduction modulo B forces low digit discrepancy 0, then divide and repeat. The middle vector is a strict convex combination of the two distinct outer vectors of equal squared norm, contradicting strict convexity. Thus shell encodings have NoRel. This refines the sufficient base 4Ld of the source finite construction; no novelty priority claimed. Base d alone fails: d=6,S=2, vectors (4,3),(3,4),(0,5) have norm squared 25 and encodings 22,27,30 (gaps 5,3), violate L=5.

Largest shell >= d^S/[S(d-1)^2+1] by pigeonhole. Independently, let V uniform digits and Q=sum V_i^2, with variance sigma^2=S Var(V^2). Chebyshev gives at least 3/4 mass within 2sigma of mean and at most 4sigma+1 integer shells in that interval. Therefore largest shell >=3d^S/[4(4sigma+1)], and sigma <= (d-1)^2 sqrt(S)/2 by bounded-variable variance. This yields a sqrt(S) rather than S loss in the shell-count denominator. For [0,N), take d=floor(N^(1/S)/(2L))>=2, B<=2Ld, hence B^S<=N. Using d>=N^(1/S)/(4L) and d^2<=N^(2/S), log cardinality >=log N-S log(4L)-(2/S)log N-O(log S), with S near sqrt(2 log N/log(4L)) for log L=o(log N). Hence subpower density loss. In source range 4Lw a<n0 take N=floor((n0-1)/(4Lw))+1, Lw=O(log x), n0 on order x^(2+8eps) for bounded o. Then log loss O(sqrt(log x log log x))=o(log x), so eventually cardinality after removal of zero >=x^(-eps)*ord. Also 4Lw*card<=n0. This recovers cardinality order, not all exact source constants and not arithmetic or geometric positivity.

Regression: all shells for S=2..4,d=2..6,L=1..5; 1680 shell checks and 1,018,545 exact triple checks; 4896 independent anchor/coefficient checks; 15 central-mass checks; explicit small-base counterexample. Scripts/results below. Finite tests are falsification/regression only; deduction above proves the finite construction.

## C. Independent scaling-window generalization
For k>=1,W>=1,1<alpha<2, [kW,(kW)^alpha] lies in [W,W^2] iff W>=k^(alpha/(2-alpha)), by division of the upper endpoint inequality by W^alpha. Source alpha=3/2 yields W>=k^3. If x=k*x' and one has cohomological bound up to (x')^A, to use x^B for A>B>0 requires x'>=k^(B/(A-B)); source A=401,B=400 gives W>=k^400. Combined threshold W>=max(k^(alpha/(2-alpha)),k^(B/(A-B))). Monotonicity of floor and exp(x^eps) preserves the bound. For k>1 alpha=2 cannot fit without a larger original window. For sufficiently large x choose e=ceil(log2(x^(2+8eps)/c)) to guarantee x^a<=c2^e<2*x^a; O(log Z) possible pages on a fixed proportional log window, but source uniformity over fields means no extra finite union is required. This is an algebraic generalization of the bookkeeping and supplies no new cohomology estimate. Exact tests: 840 window equivalences, 210 sharp integer threshold checks, 96 cohomology cutoff checks, 10452 dyadic rank checks.

## Adversarial limits and next experiment
Do not repeat finite Galerkin as proof, extrapolate local positivity to whole support, omit prime powers without proof, conflate analytic continuation with absolute convergence, assume host/prime independence or rerun finite numerical scans without a specific falsifiable target. No new independent RH/GRH proof; imported source theorems not independently reproved, no local Lean verification. MIT verification status externally strong but distinct from this research. Next: trace exists_host and its CM datum construction, locate exact preserved IsChiField conditions, compare to Waterloo H12 prose. Verify full quantifier order and whether any uniformity in choice of auxiliary primes is lost in translation. Then seek an independent classical proof of one precisely isolated geometric or analytic implication, or a concrete counterexample to a weakened premise. Preserve both source-derived and independently proved parts separately.

## Reproducible tests

### riemann_2348_norel.py


[Extracted file: riemann_2348_norel.py](files/riemann_2348_norel.py) · 2,355 bytes · Source block 1.

### riemann_2348_norel_results.json


[Extracted file: riemann_2348_norel_results.json](files/riemann_2348_norel_results.json) · 234 bytes · Source block 2.

### riemann_2348_window.py


[Extracted file: riemann_2348_window.py](files/riemann_2348_window.py) · 1,348 bytes · Source block 3.

### riemann_2348_window_results.json


[Extracted file: riemann_2348_window_results.json](files/riemann_2348_window_results.json) · 180 bytes · Source block 4.


