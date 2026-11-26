# Riemann research checkpoint — 2026-11-23 evening, EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_2026_EST.md`. **Recorded time label:** 2026-11-23 20:26 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

No newly claimed proof of RH.

## 1. Scientific continuity
Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST, W12 rational support certificate. The preceding checkpoint `RIEMANN_CHECKPOINT_2026-11-23_1929_EST.md` was read in full, including scripts. This continuation develops its proposed exact arithmetic and simpler kernels.

Prior rejected routes: positivity on small collars is not global Weil positivity; core/collar mixing and spectral pollution remain; finite Galerkin cannot control all functions; no vanishing p-curvature shortcuts or quantifier interchange; no omission of matrix blocks. Earlier fallback already audited G.cls, nonzero IsLift, square-root parameter budget, Mellin pole, Landau-window constants, residue typo, universal dyadic bump, its product tail, one-sided Landau criterion, and elementary short-support bathtub bound. Do not repeat these without a specific new target.

## 2. Sources actually consulted, external verification and source audit
- Andrew Sutherland MIT https://math.mit.edu/~drew/grh/ last updated 23 Nov 23:45 UTC: 175,187 compiled modules, multiple independent kernel and statement checks accepted, stock paranoid full export passed 23 Nov 19:01:08 UTC. Comparator v4.36 last default-kernel stage still running at that update. No change from last checkpoint; external verification is not our own kernel run. Clay https://www.claymath.org/millennium/riemann-hypothesis/ still shows Active; do not conflate prize recognition with formal proof verification. Waterloo guide index https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ consulted (working human exposition and (M)).
- Payam Danesh https://arxiv.org/abs/2611.10726 (7 Nov 2026), rendered article §2 equations 1–7, §5 equations 32–36 and pole argument. Equation 34 explicitly includes the prime-power sum; the renderer suppresses a row of eq 36. Retain the sum. This is the mathematical source for the explicit formula below, not an attribution of our particular specializations.
- Bradley and Gupta, distribution of nonidentical uniform sums, https://arxiv.org/abs/math/0411298 (abstract, formula independently derived below). Hasanalizade, Shen, Wong, explicit zero count https://arxiv.org/abs/2107.06506, JNT 235 (2022), abstract. For T>=200 their bound implies N_+(T)<=T^2, counting multiplicities. Platt and Trudgian https://arxiv.org/abs/2004.09765 and DOI 10.1112/blms.12460 rigorously verified RH up to height 3e12 (and simplicity); no extrapolation beyond the verified height.
- Public Lean source https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/main/src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/AuxiliaryPrimeMemAvoidedPrimes.lean lines 65–76, 95–121, 174–235. NEW interface detail: `globalTwisting_le_fact` explicitly gives q0H<=p for *any* prime p congruent 1 modulo rPrH*(QS*q*d) when ccK=top. Norm is then 1. `eq_of_from` transfers the prime from host H to q0Av of the constructed point when both ideals are top, by matching the relevant host data. Hence a quantitative witness can transfer through that interface. Mere existence in `globalTwisting_spec_fact` still gives no upper bound; one must trace an actual quantitative witness and the window parameters. Standard Linnik polynomial bound (context: Sachpazis, https://doi.org/10.1112/mtk.12211) could supply log q0H <= log C + A log(rPrH*QS*q*d) with absolute constants if ccK=top; this does NOT imply log q0H<=L unless an independent margin is proved. A conditional sufficient route, not an independent proof of this formal sublemma or any error in Lean. `ThinScalesIffHostBound.lean` and `Scales.lean` raw web fetches returned DisabledError; no claim to have traced their content. Need actual source on Scales.Mem nonvacuity and quantitative witness next. No re-run of entire 17-million-line development.

## 3. New rigorous interval method for the earlier infinite smooth dyadic bump
Let h be the probability density of sum U_j with independent U_j uniform on [-2^-j,2^-j], j>=1. h is even, smooth, supported [-1,1], H(z)=product sinh(2^-j z)/(2^-j z). H nonzero for Re z!=0, proven in prior checkpoint. The autocorrelation k=h*h is the distribution of two independent copies of each U_j. Define k_N as density of finite sum of these 2N independent uniforms. Exact formula from convolution of uniform intervals: for r=0,2 and N>=3,

k_N^(r)(v) = 2^(N(N-1))/(2N-1-r)! * sum_b c_b (v+2-2^(1-N)-b*2^(1-N))_+^(2N-1-r),
where c_b are the integer coefficients of product_{j=1..N} (1-z^(2^(N-j)))^2. Derivation: for each uniform of width w, its integral effect is a difference of translated primitives divided by w. Starting from delta and applying 2N such convolutions yields the truncated-power formula, with width product 2^(-N(N-1)); differentiate r times. All operations at dyadic points rational. k_N and k_N'' even.

Let Y be the remaining independent tail, centered symmetric, with variance V=2/(9*4^N). For independent centered uniforms their fourth moments are <=3 variance squared; expand the fourth power of finite sums and pass to limit by bounded convergence: E Y^4 <=3 V^2. For N>=3, derivative sup norms follow by differentiating separate uniform factors as finite signed measures and using Young's inequality: ||k_N'||_inf <=2 (differentiate a width-1 factor, use remaining width-1 factor density<=1); ||k_N'''||_inf<=32 (differentiate widths 1,1,1/2, TV norms 2,2,4 and density of remaining width-1/2 factor <=2); ||k_N''''||_inf<=256 (differentiate widths 1,1,1/2,1/2, product TV64 and density of next width-1/4 factor <=4). For our N=8 the density is C^14. Taylor at order three and symmetry give the uniform bound

|k(v) - k_N(v) - V k_N''(v)/2| <= 256 E Y^4/24 <= 32 V^2.

At N=8 this is exactly 1/2717908992, less than 3.68e-10. To evaluate at v=log(n/x), round to a dyadic grid with B=48, using exact rational log series and outward intervals; add (2+16V)*radius by the derivative sup bounds. For log r reduce by powers of 2 to r in [1,2], w=(r-1)/(r+1) in [0,1/3]. Sum 2 sum_{j=0..23} w^(2j+1)/(2j+1), remainder <= 2 w^49/(49(1-w^2)). Handle negative powers of 2 with the interval endpoints reversed. Inverse square roots enclosed by integer sqrt of n*2^(2B). All interval endpoints rational; only decimal displays are float approximations. Independently integrate truncated powers against v^0,v^1,v^2,v^4: exact agreement with mass 1, mean 0, variance sum 2/(3*4^j), fourth moment 3 variance^2 - (4/15)*sum 16^-j. This catches coefficient, support, derivative normalization errors.

For t=log x>2, exact complete arithmetic formula from prior checkpoint and Danesh eq34:
F(t)=sqrt(x)H(1/2)^2 - sum_n Lambda(n)/sqrt(n)*k(log(n/x)) - sum_{m>=1} H(2m+1/2)^2 / x^(2m+1/2).
The prime range is inside [x/8,8x] since e^2<8. Trivial-zero tail after M=12 terms <= r^(2M+2)/(1-r^2), r=8/x<1, from H(s)^2<=e^(2s) (support of k). For s real positive, each factor is between 1 and exp(w^2/6) since (2k+1)! >=6^k k!, so H(s) lies between H_32(s) and H_32(s)/(1-s^2/(18*4^32)), whenever denominator positive. Finite factors enclosed via first 49 Taylor terms (k=0..48), geometric bound on positive tail with decreasing ratios; multiply intervals with outward dyadic rounding. Square x gives exact integer sqrt. No numerical integration assumptions or RH needed in arithmetic evaluation. Underlying analytic derivation still warrants external peer audit; these are exact-rational conditional-on-formula certificates for finite inputs only, not a proof of RH.

Actual certified arithmetic intervals (decimal representations; exact fractions in report):
- x=16: [2.7399179192570738e-6, 2.7730336718276764e-6]; 44 candidate prime powers, 39 used.
- x=64: [-2.596734581760526e-5, -2.5940701007500385e-5]; 112 candidates, 104 used.
- x=256: [-5.514788071018021e-5, -5.509449713139535e-5]; 323 candidates, 302 used.
- x=1024: [-4.024103841917017e-5, -4.0134703122371184e-5]; 1035 candidates, 962 used.
These signs are not evidence of a negative Weil quadratic form; F is an off-diagonal cross term, which can have either sign even if RH holds. Script measured 7.16s. Exact full endpoint fractions in inline JSON.

Independent falsification-only spectral calculation: use 79 mpmath zero ordinates below 200 (next ordinate ~201.26475), 45 decimal precision and 80 product factors. All four spectral sums lie in the above arithmetic intervals even without adding an explicit tail. The rigorous high-zero tail bound uses |sinh(a z)|<=cosh(a Re z), |z|>=|Im z|, all other factors bounded by exp(a |Re z|). Taking first 7 factors gives |H(z)|^2 <= e*2^56/|Im z|^14 <3*2^56/|Im z|^14. From N_+(u)<=u^2 for u>=200, dyadic bands on both signs give tail <=24 sqrt(x)*2^56/[200^12*(1-2^-12)]. Values 1.69e-9 to 1.35e-8 for the four x. Finite mpmath zero list/ordinate evaluations and product are NOT interval certified, so the comparison remains numeric cross-check only. Independent trial division verified all 8191 integer primality decisions up to 8192 against sieve; 482 mpmath log enclosures cross-checked. Code measured 14.06s. No off-line zeta zeros presumed and no global conclusion.

## 4. Distinct simplification: triangular kernel and an integer-square-only RH criterion
The infinite smooth bump is NOT necessary for a fixed detecting probe; the finite uniform density h0(v)=1 on [-1/2,1/2] and 0 elsewhere already suffices. Its transform H0(z)=sinh(z/2)/(z/2), with value 1 at 0, vanishes only on the imaginary axis. Its autocorrelation k0(v)=(1-|v|)_+ is a triangular continuous function with support [-1,1]. For |Re z|<=1/2, H0(z)=O((1+|Im z|)^-1), so sum |H0(z_rho)|^2 is absolutely convergent via N(T)=O(T log T). No smoothness assumption is hidden: for a nonnegative even smooth unit mass mollifier with support [-delta,delta], convolve h0 with it. The transformed factors tend pointwise to H0 and are uniformly bounded by e^(delta/2)|H0| on the zero strip. For fixed t>1 choose delta<(t-1)/2, so cross support stays away from zero; autocorrelations converge uniformly by continuity of k0, prime sum has finitely many terms in a common compact range and arch integral is dominated on a compact away from zero. Dominated convergence in the absolutely summable spectral series and arithmetic terms establishes the full explicit formula for h0. This avoids any illegitimate use of a nonsmooth test function in the usual smooth formula.

Define A0=H0(1/2)^2=16 sinh^2(1/4). D(x)=x A0 - sum_{n>=2} Lambda(n) sqrt(x/n)*(1-|log(n/x)|)_+ for x>e. Then F0(log x)=D(x)/sqrt(x)+E0(log x), with E0=O(x^-5/2) as x->infty. Absolute convergence and the Laplace-meromorphic pole argument from the previous checkpoint work verbatim (the extra denominator in the meromorphic series is not needed for convergence). Every centered off-line zero with positive real part gives a nonzero residue m H0(z)^2. The one-sided Landau argument in previous checkpoint works too: no positive real centered zeta zero; if F0(t)<=C exp(eta t) eventually, g=C' exp(eta t)-F0>=0 eventually and globally after increasing C', then the real abscissa of its Laplace transform would have to be singular; all possible poles there are nonreal except eta. Thus an off-line zero Re z>eta yields contradiction. Apply same to -F0. Conversely if RH, the absolute sum bounds |F0| uniformly. Therefore either ONE-SIDED bound D(x)<=C sqrt(x) or D(x)>=-C sqrt(x) for all sufficiently large real x is equivalent to RH. This is a simple reformulation, not the difficult bound itself or a claim of literature novelty.

NEW reduction to integer squares: D(x) is globally Lipschitz on x>=4 with a universal constant. For completeness elementary Chebyshev upper bound psi(y)=sum_{n<=y} Lambda(n)<=4 y log 2 for y>=1: for positive integer n, each p^k in (n,2n] contributes one to the p-adic valuation count of binomial(2n,n) (the other floor differences are nonnegative). Thus psi(2n)-psi(n)<=log binomial(2n,n)<=2n log2. Sum dyadically up to the next power of 2 >=y. For each n, g_n(x)=sqrt(x/n) k0(log(n/x)) is locally absolutely continuous, derivative almost everywhere zero outside active support, and |g_n'(x)|<=3 sqrt(e)/(2x) on support. For a compact interval only finitely many terms occur, so |D'(x)|<=A0+3 sqrt(e)/(2x) psi(ex)<=A0+6 e^(3/2) log 2<64 (e<3, sqrt e<2, log2<1, A0<=sqrt e). Thus if D(m^2)<=C m for all sufficiently large integers m, take m=floor sqrt x; x-m^2<2m+1, hence D(x)<=C m+64(2m+1)=O(sqrt x). Similarly for the lower bound. Reverse trivial. **RH is equivalent to a one-sided uniform O(m) bound on this explicit finite prime-power sum at ALL sufficiently large integer squares.** No logarithmic penalty, no smoothly shrinking supports, no spectral computation. Generalizes to any cofinal sample sequence with gaps O(sqrt x). Sparse geometric samples do not have this property; prior phase counterexample remains relevant. This does not provide the crucial uniform bound; an arbitrary finite collection of squares is not sufficient.

Exact arithmetic test: 39 squares m=2..40, 7855 active prime-power terms in total, exact rational outward bounds for D using triangular weight and same log/sqrt methods, with A0 enclosed by positive Taylor series. Widths <=2.732e-10; D(m^2)/m ranged about -0.0312025010 to 0.0657474647. 38 exact consecutive Lipschitz comparisons passed against conservative constant 64. These finite tests are arithmetic diagnostics only, not a proof of uniform bound; source script measured 6.42s. The simplest next approach is to exploit that piecewise-linear log weights let W(x) be written in terms of four weighted summatory functions over [x/e,x] and [x,ex]. Avoid using GRH-conditional prime estimates to claim an independent RH proof.

## 5. Attack, limitations and next experiments
- Arithmetic interval accuracy at x up to 1024 or 1600 does not control x->infinity; even exact computation at all finite tested points cannot imply the eventual uniform constant. The smooth kernel N=8 tail is uniform in v but summing over primes grows with x; increase N with x or use triangle to avoid this error. Prime weights retain *all* prime powers, not just primes. Triangular kernel has transform zeros on the critical line, which is harmless for detecting nonreal-axis centered zeros; no claim of detecting every critical zero. The one-sided criterion uses absence of positive real centered zeros and absolute convergence, not simply positivity of coefficients. No spectral pollution or truncation extrapolation.
- Next distinct analytic pass: use the triangular exact identity with partial summation to compare the one-sided fixed-square bound with Alpoge inequality (M), and derive explicit slack propagation if only a restricted range of moduli or windows is available. Try an exact discrete Mellin transform over integer squares; audit convergence and possible sampling aliasing rather than merely repeating prime sum numerics.
- Formal source pass: inspect the real quantitative lemma bounding auxiliary prime q0H and Scales.Mem existence in the archived Lean proof (alternate mirror/connector if needed), then verify the numerical exponent margin, not just existence. Consult MIT external verification for updates. No newly found proof/disproof by this project.


### Reproducible script: certified_bump.py


[Extracted file: certified_bump.py](files/certified_bump.py) · 4,545 bytes · Source block 1.

### Report: certified_bump.json


[Extracted file: certified_bump.json](files/certified_bump.json) · 2,736 bytes · Source block 2.


### Reproducible script: spectral_check.py


[Extracted file: spectral_check.py](files/spectral_check.py) · 2,115 bytes · Source block 3.

### Report: spectral_check.json


[Extracted file: spectral_check.json](files/spectral_check.json) · 1,365 bytes · Source block 4.


### Reproducible script: triangle_square.py


[Extracted file: triangle_square.py](files/triangle_square.py) · 1,988 bytes · Source block 5.

### Report: triangle_square.json


[Extracted file: triangle_square.json](files/triangle_square.json) · 9,636 bytes · Source block 6.


END CHECKPOINT — triangular square criterion and exact smooth-kernel arithmetic — 2026-11-23.
