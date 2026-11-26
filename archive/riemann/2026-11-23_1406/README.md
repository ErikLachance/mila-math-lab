# Riemann Proof Watch — append-only fallback research checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1406_EST.md`. **Recorded time label:** 2026-11-23 14:06 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Checkpoint date:** 2026-11-23, America/New_York.

## Scientific continuity

Earlier Riemann checkpoint, dated **2026-11-08 15:30:58 EST**: a conditional-on-the-signed-formula exact-rational positivity certificate for support only in two width-1/12 endpoint collars at L=0.81. Its codimension<=14 auxiliary comparison and finite 16D Fourier block do not control mixed interior/collar terms and do not prove RH. Do not repeat the unsupported jump from positive finite block or local supports to global RH.

The preceding Riemann checkpoint `RIEMANN_CHECKPOINT_2026-11-23_1355_EST.md` was read in full. Its genuinely new prior result is the elementary conductor-*uniform* imprimitive single-Euler-factor bound `|G_{chi induced}(x)-G_{chi primitive}(x)|<=2 log x` for x>=2, plus a conductor-growth counterfamily to fixed `O(log p)` constants. The preceding `1313_EST` snapshot had already reconstructed the regularized Riesz/Mellin transforms, RH-conditional zero sums, even/odd/complex Dirichlet residues and exact finite missing-Euler-factor formulas. All remain **previous results**, not new this run.


## Actually read primary mathematical and verification sources

- Levent Alpöge, four-page original November 20 2026 announcement and timeline, https://alpo.ge/remark.pdf ; PDF pages 3 and 4 (zero-index 2,3) visually inspected. It describes Stepanov-inspired automorphic theta-lift chains with m about sqrt(X), not a global consequence of the older local Weil calculations.
- Michael O. Rubinstein and collaborators, *The Alpöge–Claude proof of RH explained for the Riemann zeta function*, **working draft v2, 22 November 2026**, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf ; read Part II §1 printed pp. 30–31, Part III §III.11 printed pp. 213–216, and visual PDF screenshots at zero-index pages 29,30,212,214. It establishes the one-sided sparse-window criterion and assumes thirteen H0–H12 conditions for the human-readable reduction. The central (M) remains **unproved in this human exposition**; this is not a problem detected in the separately formalized Lean proof.
- Lean FRO and Mathlib Initiative joint verification 21 November 2026, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ . Certified formal theorem and proof, independent checkers, no unrestricted all-L-function assertion.
- Andrew Sutherland MIT verification dashboard, updated 23 November 2026 at 14:35 UTC: https://math.mit.edu/~drew/grh/ . Independently reports 175187 modules, full default Lean kernel pass, modified-allocator paranoid pass, Comparator v4.33 pass, independent checkers pass; two other kernel/comparator long runs were still ongoing. This run did NOT rebuild 17M Lean source lines.
- Michael Rubinstein overview https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ states explicitly none of H0–H12 is proved outright in v2 guide.
- Attempt to screenshot working-draft zero-index PDF pages 62 and 63, needed to settle an older suspected local partial-summation denominator typo, failed **`Cache miss`** twice; no visual verification or novel erratum is asserted.

## NEW MICRO-PASS 1 — uniform gamma-Chernoff version of the sparse-interval criterion

The source's Part II §1 proves: if `G(x)<=x^theta` on arbitrarily large entire windows `[Y,Y^(3/2)]`, theta in (0,1), zeta has no zeros with Re(s)>theta. Its `G` has `|G(x)|<<x log x`, and its Mellin transform F(s) is meromorphic. Generalize the **local analytic concentration estimate** to ANY fixed real `alpha>1`, replacing 3/2 by alpha; this does not itself prove that the needed windows exist.

Set `u=log x`, `g(u)=G(e^u)`, suppose for some `B>theta`, `|g(u)|<=C exp(Bu)` globally (e.g. B=2 by Chebyshev). On *each* window `[U,alpha U]`, assume `g(u)<=K exp(theta u)`, with constants K,C independent of U. Let `sigma>B`, `lambda=sigma-B`, `q=sigma-theta`, `h=(alpha-1)/log(alpha)` (the logarithmic mean of 1 and alpha), and choose integer `n=j+1` nearest `lambda*h*U`. Let `I(v)=v-1-log v`. Then `a=1/h<1`, `b=alpha/h>1`, and exactly `I(a)=I(b)=kappa>0` by the chosen h. For Gamma(shape n,rate lambda), Chernoff gives

`Pr(V<U or V>alpha*U) <= exp[-n I(lambda*U/n)] + exp[-n I(lambda*alpha*U/n)]`.

As U tends to infinity along arbitrarily large windows, `n/(lambda U)->h`, so for every small fixed delta>0 eventually the two exponents are at least n(kappa-delta). Meanwhile the positive part of g on the good window contributes at most `K q^(-j-1)` to the signed Taylor coefficient; off window contributes at most `C lambda^(-j-1) Pr(outside)`. Thus if

`log((sigma-theta)/(sigma-B))<kappa`, choose delta with strict margin and get **uniform** (along the sequence of j)

`|A_j(sigma+it)| + A_j(sigma) = O(q^(-j-1))` for all real t,

where `A_j(s)=(-1)^j F^(j)(s)/j!` and `F(s)=integral_0^inf g(u)e^(-su)du` on Re(s)>B. The source's existing pole-isolation argument excludes nonreal poles in Re(s)>theta when this estimate holds; for a real pole a separate sign condition is mandatory (see pass 3). For alpha fixed >1, one can choose sigma sufficiently large because the log-ratio tends to zero. This reproduces the source's statement that ANY fixed alpha>1 works, with a transparent optimized center, not a new RH proof or priority claim.

`riemann_20261123_interval_gamma_audit.py/.json` executed mpmath 90-digit Gamma integrals and Chernoff bounds at U=1,2,5,10,20,40,80,160 for five parameter sets. All 40 numerical Chernoff checks PASS; no numerical check substitutes for the analytic Chernoff proof. For alpha=1.5, theta=.6, B=2, **kappa≈0.02050349137426344**; sigma=252 gives log-ratio≈.00558437829 PASS, sigma=100 gives ≈.01418463499 PASS. With tighter Chebyshev-derived B=1.1, sigma=40 passes (ratio≈.01277156568). For alpha=1.02, B=2, sigma=60000 passes with narrow margin ≈2.568e−5. The deliberately insufficient sigma=30 at alpha=1.5 fails kappa>log-ratio and its normalized tail grows exponentially in tested U: that **falsifies this insufficient parameter choice only**, NOT the RH criterion. There is no interval-rational rounding certificate for the displayed decimal values; theorem of existence needs none.

**Asymptotic obstruction:** write alpha=1+delta with delta→0. Then `a=log(1+delta)/delta=1-delta/2+O(delta²)` and `kappa=I(a)=delta²/8+O(delta³)`. A fixed permissible sigma therefore generally needs scale of order `(B-theta)/delta²`. If alpha(Y) shrinks toward 1 with Y, there need not exist a fixed sigma proving the criterion. Do NOT promote arbitrary sparse points or bounded-ratio windows to the full H12 requirement.

## NEW MICRO-PASS 2 — exact toy counterexample to weakening fixed-power windows to bounded multiplicative width

Define a **toy Mellin function, not the zeta prime sum**:

`G_toy(x)=x^(3/4) cos(log x)`, `g_toy(u)=exp(3u/4) cos(u)` and `theta=3/5`. For every integer n>=0 choose `Y_n=exp(pi+2*pi*n)` and `c=exp(pi/3)>1`. For all x in `[Y_n,c Y_n]`, write u=pi+2*pi*n+t, 0<=t<=pi/3. Then `cos(u)=-cos(t)<=-1/2`, so `G_toy(x)<=0<=x^(3/5)` on **infinitely many full bounded-ratio windows**. Nonetheless its Mellin transform for Re(s)>3/4 is exactly `F_toy(s)=(s-3/4)/((s-3/4)^2+1)`, with poles at `3/4+i` and `3/4-i`, both to the right of theta. This is a rigorous **countermodel to an invalid over-generalization** `[Y,cY]` for fixed c, even though `[Y,Y^alpha]` for fixed alpha>1 is sufficient under the source's hypotheses.

`riemann_20261123_sparse_countermodel.py/.json`: nine disjoint windows, 101 points each checked cos negative; high precision direct Laplace integral vs exact rational function at s=1.5+0.2i differs by <8e−93. The all-x sign proof is the elementary cosine identity, not the finite sampling. The countermodel is not an RH counterexample because it is NOT the zeta G.

## NEW MICRO-PASS 3 — essential residue-sign condition for real poles

Even an upper bound on **every x** does not exclude arbitrary **real** poles for a generic signed Mellin transform: `G_minus(x)=-x^(3/4) <= x^(3/5)` globally, but `F_minus(s)=-1/(s-3/4)` has a real pole at s=3/4. For all j>=0, its signed Taylor coefficient at real sigma>3/4 is `A_j(sigma)=-(sigma-3/4)^(-j-1)`, so `|A_j|+A_j=0`: the positive-part bound cannot contradict the pole. Conversely `G_plus=x^(3/4)` gives residue +1 and positive A_j. For actual nonprincipal real-character Dirichlet L, a real zero beta in (0,1) would contribute residue `-nu/[beta(beta-1)]=nu/[beta(1-beta)]>0`, so the source's separate favorable-sign argument can apply; the negative toy pole is not a refutation. For ζ itself there are no nontrivial real zeros in (0,1). Complex-character sums have no natural one-sided inequality without taking a suitable real-valued combination.

`riemann_20261123_real_pole_sign_guard.py/.json` exact SymPy rational checks for j=0,1,2,5,10,20 all PASS, including residue and signed-derivative identities; this proves the elementary countermodel independently of numerics.

## Adversarial comparison, missing parts, next experiment

- The main mathematical difficulty in the original user's Weil approach remains its uncontrolled off-block/collar coupling; no new proof via that approach. The 2026 Alpöge–Claude formal proof has strong independent **external** verification. This run does not claim to understand/replay the complete Lean formalization.
- The human-readable guide **assumes H0–H12**, especially H12: compatible inputs M, B and C must hold at each x throughout arbitrarily large windows, with constants independent of x. Existence of compatible data merely along an unbounded sequence does not suffice. New toy experiment provides an explicit reason.
- The generic sign/pole countermodels deliberately do NOT contradict the source's correctly stated zeta/Dirichlet criteria; do not report them as an erratum, a gap in Lean, an RH disproof or mathematical novelty priority.
- No exact interval certification of the floating point gamma values; theorem follows from standard Chernoff/Cauchy analytic facts, but is not an independently peer-reviewed new theorem.
- The old suspected `theta(sqrt U)/log U` typo on explanatory p63 remains screenshot-unverified; do not issue an erratum without visually confirming typeset source.
- Next distinct high-value work: read H12's exact quantifiers at printed pp213–214 and independently test **synchronization** of the pair q,d between (M), Estimate B and Estimate C and fixed-in-x constants; reconstruct a minimal finite countermodel to illegal swaps. Also audit rigorous n=m=√x rounding and the dependence of auxiliary growth parameters on epsilon when obtaining the global-window bound. A more demanding task is tracing H12's exact premises into the formal Lean modules, not just the human draft.


**STATUS:** Riemann/GRH theorem accepted by independent proof checkers **externally**; no proof/disproof independently found this run. Three distinct, adversarial mathematical checks finished and code executed.
