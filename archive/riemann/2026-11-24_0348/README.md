# Riemann research checkpoint -- 2026-11-24 03:48 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-24_0348_EST.md`. **Recorded time label:** 2026-11-24 03:48 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## Sources actually consulted
- Andrew Sutherland MIT verification https://math.mit.edu/~drew/grh/ (updated Nov 24 03:30 UTC). All original compile/kernel checks, independently implemented kernels and statement comparators reported successful; final Comparator 4.36 still running at stated update time. No local rerun of that proof.
- O'Desky agent-assisted catalogue, https://andrewodesky.com/rh/lean/Formalism.HN.frame_linear_algebra_first/ (ALG.0115 statement); https://andrewodesky.com/rh/lean/Formalism.HN.theoremF/ (ARAK.1120 statement and full proof exposition, especially steps 3–8); https://andrewodesky.com/rh/lean/Deduction.ch_top/ (ANT.0103 conditions 9 and 11, size condition 5, proof steps 4–6); https://andrewodesky.com/rh/overview.html (Nov 21 outline, actual x,m,k,n scales); https://andrewodesky.com/rh/lean/Formalism.MainNotions.LinkS_at/ (first direct open failed, link from overview succeeded; full statement and raw-moment proof); https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.HilbertSchmidtNormSquare.compressTraceSquareBound/ (ALG.1746 isometric restriction statement); https://andrewodesky.com/rh/lean/UpperTheory.Top.topDesWin/ (compatible arithmetic family conditions, first part). Catalogue is a secondary reconstruction with incomplete review, not a new kernel proof.
- Primary source mirror README https://github.com/CocoSgt/riemann-hypothesis-lean ; independent source provenance and verification notes https://github.com/Deicyde/riemann-hypothesis/blob/main/verification/NOTES.md ; selected raw source snapshots and limitations https://alexisdpc.github.io/riemann/sources.html (23 Nov edition). Direct GitHub HN folder opens failed DisabledError; no actual HN Lean proof body independently inspected this run. Lean and lake executables not found in container PATH. No claim of Lean formalization or compilation of new lemmas.

## A. Integrate actual source slope counts, not their pointwise upper envelope
Retain exactly the hypotheses and slope-count/rank/image-transfer setting of theoremF in the catalogue. Let x_j denote the nR shifted source slopes, with mean >=s and each x_j<=s+U; y_j denote the nr target slopes, each y_j>=s-S. S,U>=0. Define f(t)=fraction of x_j<s+t, g(t)=fraction of y_j<s+t. By saturated threshold submodules, actual source discarded K-dimension equals R f(t). The rank comparison applies at every real threshold: g(t)<=min(1,z(t)/(1-delta)), where z(t) is relative codimension in the enlarged target after retaining source spaces. This uses the same image minimal slope and first-row projection as theoremF, which have no restriction on sign of t. It does not presume independent random frames.

For t in [-S,0], integral f = mean(min(S,(s-x_j)_+)). Let H=US/(U+S) for U+S>0, otherwise 0. If S>0, negative fraction p is at least integral(f)/S. The mean source assumption bounds total negative deficit by positive surplus, and surplus <=U(1-p). Thus integral(f)<=U(1-integral(f)/S), giving <=H. S=0 trivial. Equality possible using slopes s-S and s+U in appropriate proportions, e.g. {-2,1,1} with U=1,S=2. This improves U log(1+S/U), which resulted from integrating the pointwise Markov envelope rather than the actual finite slope list.

Using previous checkpoint mass bound (1-e)(q-f)^2<=e f(1-f), and rank-trace bound (1-q)^2<=(1-z)(1+eta), get
  (1+eta) z <= eta+2q-q^2 <= eta+2f+2sqrt(e f(1-f)/(1-e)).
Young's inequality gives <= eta+3f+\[e/(1-e)\](1-f) <= eta+3f+e/(1-e).
Integrating negative tail, target mean deficit is bounded by
  s-mu(C) <= [eta*S+3H+e*S/(1-e)] / [(1+eta)(1-delta)]. (A1)
For e<=1/4, e/(1-e)<=4e/3. No log|I| term needed (as already true for source proof). A1 remains valid if S=0, U=0, e=0, eta=0. It is a direct deduction from the existing geometry hypotheses, not a proof of them.

## B. Signed layer-cake bound, retaining positive target slopes
More powerful: integrate on the entire interval [-S,U], not just the negative part. The source integral exactly equals mean(min(S+U,s+U-x_j))<=U by source upper bound and mean assumption. For S+U>0 let F=U/(S+U). From previous checkpoint define the nondecreasing concave functions
  q_*(f)=min(1,f+sqrt(e f(1-f)/(1-e))),
  Z(q)=[2q+eta+sqrt(eta^2+4eta q(1-q))]/[2(1+eta)].
For e=0, q_*=identity. Otherwise uncapped q is concave, reaches 1 at f=1-e and remains >=1 thereafter (square the inequality); its minimum with 1 is concave and nondecreasing. For eta=0, Z=identity; eta>0, sqrt of the nonnegative concave radicand is concave, and derivative on (0,1) is nonnegative since sqrt(eta^2+4eta q(1-q))>=eta. Endpoints by continuity. The composite W(f)=min(1,Z(q_*(f))/(1-delta)) is nondecreasing concave (composition and cap). Pointwise g(t)<=W(f(t)). Jensen on interval gives integral g <= (S+U)W(F). For each y_j>=s-S, its clipped deficit integral equals (s+U-y_j)_+, so mean actual signed deficit is <= integral g - U. Therefore
  s-mu(C) <= (S+U) W(U/(S+U)) - U. (B1)
If S+U=0, target min>=s directly. If e=eta=delta=0, B1 gives s<=mu(C) exactly, eliminating the entire U loss; this is stronger than any bound using only negative target slopes. If U=0, q_*=0 and B1 specializes to S*min(1,eta/[(1+eta)(1-delta)]), independent of e. If eta=0 and delta=0, B1 <= sqrt(e U S/(1-e)), with no additive U term. General bound from sqrt(a+b)<=sqrt(a)+sqrt(b) yields eta, delta, and mixed-moment losses. Use min(A1,B1,S) for a uniform practical estimate. This is not an RH proof, only a new conditional refinement of the stated slope inequality.

Adversarial checks: the use of positive thresholds requires actual height-controlled images for all saturated threshold submodules, not just an abstract claim restricted to negative thresholds; the source proof's step 4 argument depends only on image slope, and step 6 only on dimension. Equality of real and K-rank multiplicities used exactly as stated. Target clipping is in the direction of a lower bound for target mean, no assumption on target maximum. Jensen is valid for finite step functions, endpoint jumps measure zero. No assumption that moment matrices commute. e<1 and 1-delta>0 are essential. The bound need not be sharp for the full arithmetic slope theorem. Simultaneous equality in mass and complementary-projection inequalities is realized by 6 one-dimensional source maps into C^3: two discarded maps along distinct first two coordinates of squared norm 4/3 each, four retained maps along third coordinate of squared norm 2/3 each. f=1/3, e=1/9, q=1/2, z=2/3, eta=1/8; Q=diag(4/3,4/3,8/3). Both squared inequalities are equalities. This verifies that the two error terms are not independently removable in general; it is a matrix toy, not an actual theta lattice.

## C. Exact substitution into ch_top, linear rather than square-root diagonal tolerance
In Deduction.ch_top the original numerical condition 9 bounds s_u-mu^C_u by log|W_u|+[4U_u log(1+S_u/U_u)+(eta_u+4sqrt(e_u))S_u]/(1-delta_u). The only other appearances of e_u and bar e in the stated counting theorem are range/order conditions and size condition 5. Using A1 and e<=1/4, drop 1+eta from denominator, use H<=U log(1+S/U) (log(1+t)>=t/(1+t), with U=0 interpreted continuously). Then the original inequality holds with numerical surrogate e'_u=(e_u/3)^2, bar e'=(bar e/3)^2, since 4sqrt(e')=4e/3. The ordering and range conditions still hold. Thus one can invoke the UNCHANGED numerical counting theorem under its other hypotheses, if the actual slope data are supplied and size condition 5 is replaced by
  (bar eta + (4/3)bar e) x^{c_*} b <= K x^eps |T| a.
This is a valid substitution into the stated real-parameter theorem, not substitution into the matrix hypothesis (which still uses the actual e). If available residual budget T0=K x^eps |T| a/(x^{c_*}b)-bar eta>0, old e<=T0^2/16, new e<=3T0/4, both capped at 1/4. For small T0 the allowed squared HS error is substantially larger. Original raw LinkS gives much smaller exponential errors anyway, so no claim of new exponent or immediate reduction of k or n. Need verify where that particular e bound is used outside the numerical lemma, and whether independent off-diagonal bounds dominate. This addresses prior checkpoint's precise next question, not merely a new asymptotic rephrasing.

## D. New restriction lemma: error linear in discarded fraction
Compare ALG.1746, isometric restrictions V_u, original dimensions d_u and retained r_u, sum R_d, R_r, target D, comparison dimension D_*, parameters sigma<=1/20, alpha<=1/4, sqrt(e0)<=sigma/2, eta0,eta1<=sigma/2, eta0>=-1, D*/sigma<=R_d. Write weighted maps C_u=sqrt(gamma_u)A_u; Q_d=sum C_u C_u*, Q_r=sum C_u V_u V_u* C_u*. Then 0<=Q_r<=Q_d, hence tr(Q_r^2)<=tr(Q_d^2) by trace product positivity; no commuting requirement. With h_u=C_u*C_u-I, HS contraction under compression implies sum ||V_u*h_u V_u||_HS^2<=e0 R_d<= e0 R_r/(1-alpha). This improves factor 2 to <=4/3.

Trace lower bound: T_r>=R_r-sqrt(e0 R_d R_r)>=R_d(1-alpha-sqrt(e0)). Trace upper second moment for full family:
  tr(Q_d^2)=sum_{u,v}||C_u*C_v||_HS^2
  <= (1+eta0) R_d^2/D_* + R_d (1+sqrt(e0))^2.
Reason: discard the negative diagonal-exclusion correction since 1+eta0>=0; each diagonal squared norm <=d_u(1+sqrt(e0))^2 by triangle inequality. Therefore
  D tr(Q_r^2)/T_r^2 <= (1+eta1)[1+eta0+sigma(1+sqrt(e0))^2]/(1-alpha-sqrt(e0))^2
  <= (1+sigma/2)[1+sigma/2+sigma(1+sigma/2)^2]/(1-alpha-sigma/2)^2.
All denominators positive. D=0 is inconsistent with R_d>0 and e0<1, because every C_u would vanish. Bounds on D and eta1 therefore imply 1+eta1>0. For sigma<=1/20 numerator <=1+(21/10)sigma: expand as (1+sigma/2)^2+sigma(1+sigma/2)^3 and use 1/80+(41/40)^3+1 <21/10. For t=alpha+sigma/2<=11/40, (1-t)^-2 <=1+(10/3)t, since (2-t)/(1-t)^2 increases on [0,11/40] and its endpoint is 2760/841 <10/3. Multiply using 1+(21/10)sigma<=221/200; coefficient of alpha <=221/60<4, coefficient of sigma <=21/10+221/120<4. Consequently
  tr(Q_r^2) <= (1+4sigma+4alpha) T_r^2 / D. (D1)
Compared with catalogue 1+5sigma+3sqrt(alpha), D1 is uniformly no worse in its stated range and improves dependence on alpha from square root to linear. This uses the original uncompressed global moment, so no need to estimate individual off-diagonal compressed entries by a new random model. One cannot simply drop alpha entirely: exact tight Q_d can lose all maps covering a fraction of target coordinates; e.g. balanced coordinate repetitions, removing all columns on alpha D coordinates yields eta_r=alpha/(1-alpha). Thus linear dependence is generally necessary. D1 does not by itself prove a larger allowed arithmetic restriction, since the same alpha can affect other geometric and local constraints.

## E. Next steps / failure boundaries
1. Trace where alpha is chosen in actual source and whether moment restriction loss is a binding parameter; combine D1 with A1 and B1, looking for a concrete simpler choice of theta dimension parameters without weakening off-diagonal estimates. Source LinkS uses exponentially tiny e0, eta0, eta1 with a uniform family threshold and the dimension proviso; cannot replace it by a claim about one scale or only diagonal moments. Need extract actual HN Lean source and formalize the signed integral and restriction lemmas if a suitable Lean toolchain becomes available. Do not claim compilation until kernel check actually happens.
2. Independent direction: use full slope distributions or moments beyond the maximum/minimum bounds, especially if geometry supplies variance. Avoid rerunning pointwise Markov integration or finite prime residue and torsion enumerations. Continue genuine analytic/geometry bridge work; no global RH proof or disproof here, no claim of publication novelty. The MIT report unchanged as of timestamp above.

## F. Reproducible experiments (observed outputs)
Exact finite rational regression on source lists of lengths 1..6 with slopes in [-2,2], nonnegative sum, S=1..4: 43,544 negative-tail harmonic comparisons and 43,544 exact signed-threshold integration comparisons, 92 nonzero equality examples. 3,500 randomized coordinate frames with rational weights and source slopes, 68,115 exact pointwise frame inequalities, 3,500 independent float checks of B1, four exact equality identities for six-map example, and 2,501 exact budget substitutions. Script runtime 1.861105426 sec. Separate exact rational grid for D1: 25,100 (sigma,alpha) pairs, five comparisons per pair, maximal fraction of new error budget 0.9177083333333333, runtime 0.777646327 sec. These are regressions of the algebra, not evidence of arithmetic family existence or a proof via sampling.

### Script 1

[Extracted file: block-001.py](files/block-001.py) · 3,529 bytes · Source block 1.

### Script 2

[Extracted file: block-002.py](files/block-002.py) · 649 bytes · Source block 2.


