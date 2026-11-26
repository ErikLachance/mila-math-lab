# Riemann research checkpoint — 2026-11-23, EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_205924_EST.md`. **Recorded time label:** 2026-11-23 20:59:24 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity
Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST, W12 rational support certificate. The preceding checkpoint `RIEMANN_CHECKPOINT_2026-11-23_2026_EST.md` was read in full, including scripts. It proposed discrete Mellin analysis of integer-square triangular discrepancy; this run develops that specific proposal and goes beyond squares.


Avoid repeating small-window positivity extrapolation, fixed Galerkin claims, norm-smallness of tiny prime-shift overlap, unsupported core/collar gluing, hidden prime-power omission, one-sided spectral positivity shortcuts, unquantified Scales.Mem existence, finite numerical tests as global proof. Earlier fallbacks have already covered universal dyadic bump, its interval arithmetic, triangular integer-square criterion, and formal source interface q0H without quantitative margin.

## Sources actually consulted
- NIST DLMF https://dlmf.nist.gov/27.4 equation 27.4.12, negative zeta logarithmic derivative Dirichlet series; https://dlmf.nist.gov/2.10 equation 2.10.1 Euler–Maclaurin bounded periodic-Bernoulli remainder and 2.10.9 summation by parts; https://dlmf.nist.gov/25.10 critical-strip symmetry, pole-free boundaries, nontrivial zeros. These support standard inputs; particular sample criteria derived below, no priority claim.
- Jeffrey Lay, https://arxiv.org/abs/1505.03589 abstract; UBC Greg Martin 2025 lecture snippet https://personal.math.ubc.ca/~gerg/teaching/539-Winter2025/Apr1.pdf on Landau's theorem for Dirichlet integrals. Only search snippets/abstract consulted, no PDF analysis. A self-contained Landau argument included below.
- Carneiro and Milinovich https://arxiv.org/abs/2403.17803 abstract for Guinand–Weil context. Prior checkpoint's explicit formula and smoothing argument reused for RH-to-bound direction. Attempted https://arxiv.org/abs/2611.10726 returned DisabledError; do not claim newly read.
- Andrew Sutherland MIT https://math.mit.edu/~drew/grh/ last updated 23 Nov 23:45 UTC: all 175,187 modules, multiple kernels and statement comparisons pass; v4.36 comparator last stage still running, no status change from preceding checkpoint. Clay https://www.claymath.org/millennium/riemann-hypothesis/ still marks Active. External verified formal proof evidence is substantial; no independent kernel run performed here. Waterloo https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ now explicitly lists version 2, 265 pages, 22 November 2026, reducing inequality (M) to thirteen numbered hypotheses and adding a lemniscate example. Index says these hypotheses are not yet independently proved in that working exposition. Read index, not PDF; no claim this is a defect of the formal Lean proof or that a theorem was missing there.

## Pass A: exact continuous Mellin transform without a sum over zeros
Take an even continuous compactly supported nonnegative kernel k(v) on [-1,1], mass 1, bilateral transform K(s)=integral k(v)e^(sv) dv, A=K(1/2). Define for real x>0:
 D_k(x)=A*x - sum_{n>=2} Lambda(n)*sqrt(x/n)*k(log(n/x)).
For triangle k(v)=(1-|v|)_+, K(s)=(sinh(s/2)/(s/2))^2, entire, nonzero when Re s!=0. Let X>0 fixed. For Re s>1/2, I_X(s)=integral_X^infinity D_k(x)x^(-s-3/2) dx converges absolutely by Chebyshev psi(u)=O(u). Change x=n e^v for each prime-power term, use even k and absolute summability in Re(s+1/2)>1. The exact identity is
 I_X(s)=A*X^(1/2-s)/(s-1/2)+K(s)*zeta'(s+1/2)/zeta(s+1/2)+E_X(s),
 E_X(s)=sum_{2<=n<=eX} Lambda(n)/sqrt(n) * integral_0^X x^(-s-1)*k(log(n/x)) dx.
E_X is entire because finite and each integrand supported in [n/e, en] away from zero. Signs checked: prime part of D is negative; negative of sum Lambda(n)n^(-s-1/2) gives +zeta'/zeta. Residue at s=1/2 cancels since A=K(1/2) and zeta has simple pole at 1. At centered nontrivial zero z=rho-1/2 the residue is m_rho*K(z), nonzero when Re z!=0; no cancellation by E_X or main term. Hence RH is equivalent to absence of poles in Re s>0 for this meromorphic continuation. This is independent of the prior spectral interchange or non-smooth explicit formula, but not a new proof of RH. No positive real poles: zeta(r) has no zero for r>0 real (r<1 follows positive alternating eta series divided by 1-2^(1-r), r>1 Euler product). The only potential real pole at s=.5 was canceled.

## Pass B: discrete Mellin transform, triangular kernel sampled at fourth powers
For fixed positive integer p, let B_p(y)=D_k(y^p)/y^(p/2)=A*y^(p/2)-sum Lambda(n)/sqrt(n)*k(log n-p log y), y>=2. Write f_s(y)=B_p(y)*y^(-ps-1). Define S_p(s)=p*sum_{m>=2} B_p(m)*m^(-ps-1), initially absolutely convergent in Re s>1/2. Substitution gives I_(2^p)(s)=p*integral_2^infinity f_s(y)dy.

For triangle, B_p=O_p(y^(p/2)); continuous derivative is piecewise, with B_p'=O_p(y^(p/2-1)), B_p''=O_p(y^(p/2-2)) away from finitely many local knots. Proof: active n in [y^p/e,e*y^p], sum Lambda(n)/sqrt(n)=O(y^(p/2)) by elementary Chebyshev; on pieces k is affine in log n-p log y. B_p' jumps at y=(n/e)^(1/p), n^(1/p), (en)^(1/p), absolute magnitudes p,2p,p times Lambda(n)/(y sqrt(n)). In a unit interval [m,m+1], each family contains at most O_p(m^(p-1)) integers n, each jump <=O_p(m^(-p/2-1)log m). Thus total jump variation plus regular variation of B_p' is O_p(m^(p/2-2)log(2m)). This uses only trivial counting of integers in a short interval, not RH or a short-interval prime theorem. In particular the nonsmooth knots cannot be discarded.

By product rule the total variation of the distributional second derivative measure of f_s on (m,m+1) is O_{p,C}(m^(p/2-p Re s-3) log(2m)), uniform for s in a compact set C. For a continuous function with piecewise AC first derivative and BV derivative, integrate the exact ramp representation f(y)=a+b(y-m)+integral(y-t)_+ d f''(t). The integral-minus-trapezoid error R_m(s) is -1/2*integral_(m,m+1)(t-m)(m+1-t) d f_s''(t). Hence |R_m(s)| <= ||f_s''||_TV/8. Endpoint derivative jumps have zero weight and are not counted twice. This formula is valid also for complex f. Each R_m is entire as a finite interval integral of entire f_s; local uniform convergence of sum R_m follows for Re s>1/2-2/p. In initial half-plane where f_s(N) tends to 0, telescope the trapezoids:
 I_(2^p)(s)=S_p(s)-p*f_s(2)/2 + p*sum_{m>=2} R_m(s).
The last two terms are holomorphic in Re s>1/2-2/p. Therefore S_p has the same poles and residues as I in that region. For p=2 the region is Re s> -1/2; for p=3, Re s> -1/6; for p=4, Re s>0. This extends the preceding square criterion to FOURTH POWERS for the SAME triangular kernel, without Lipschitz interpolation between sample points, and without an unjustified sampling interchange. For p>4 this particular second-order estimate gives a positive cutoff; it cannot detect a hypothetical zero with arbitrarily small positive Re z. Do not extrapolate the triangular proof to all p.

## Pass C: weaker one-sided cumulative criterion and explicit integrated prime weight
Let A_p(t)=sum_{2<=m<=t}B_p(m) (notation A_p distinct from constant A). For p<=4 and triangle, RH is equivalent to EACH of the following separate assertions: A_p(M)<=C M eventually, or A_p(M)>=-C M eventually, for some finite C (and integer M). It is also equivalent to S_p holomorphic on Re s>0. Proof of sufficient direction: summation by parts for initial Re s>.5 yields S_p(s)=p*(ps+1)*integral_2^infinity A_p(t)t^(-ps-2)dt. If upper bound, increase C to cover finite initial values, set g(t)=Ct-A_p(t)>=0. Its Mellin transform G(s)=integral_2^infinity g(t)t^(-ps-2)dt equals C*2^(-ps)/(ps)-S_p(s)/(p*(ps+1)). This meromorphic expression has no real singularity at s>0, but any off-line zero of positive centered real part gives a nonreal pole there. Landau positivity: a nonnegative locally integrable function's transform has a real singularity at its finite real abscissa of convergence. In this setting substitute u=p log t, absorb t^-2 dt into a positive measure. If analytic at abscissa sigma_c, choose real s0>sigma_c so close that the Taylor disk extends past sigma_c. Taylor derivatives at s0 integrate (-u)^j e^(-s0 u); evaluating Taylor at a real point to the left has all nonnegative summands, so monotone convergence forces finite integral there, contradicting abscissa. Here abscissa <=.5; it cannot be positive because real continuation is regular. If <=0 (or -infinity), G holomorphic in Re s>0 contradicts the alleged off-line pole. Lower bound use g=Ct+A_p. Functional equation symmetry covers negative centered real parts. For converse, use prior smoothed explicit formula for x>e: D_k(x)/sqrt(x)=sum_rho K(rho-.5) x^(rho-.5)+sum_{j>=1} K(2j+.5) x^(-2j-.5). Under RH first sum bounded since K(i gamma)=O((1+|gamma|)^-2) and zero count O(T log T); trivial sum bounded for x>=4. The sign of the trivial correction is positive here. The triangle follows by smooth mollification with uniform spectral domination as in prior checkpoint, not by assuming smoothness. Thus B_p(m)=O(1), A_p(M)=O(M). This reduces the target from a pointwise bound to a one-sided bound on signed cumulative averages. Still an unknown arithmetic bound in this independent approach; it is not a proof of RH. Even weaker A_p(M)<=C_epsilon M^(1+epsilon) for every epsilon>0 suffices by the same argument with shifted real pole epsilon/p, then arbitrary epsilon->0; no uniformity in epsilon needed, provided bound holds for all sufficiently large M for each epsilon.

For p=2, a computationally useful exact primitive: J(t)=integral_0^t (1-|2 log u|)_+ du, with a=e^(-1/2), b=e^(1/2). J=0 below a; on [a,1], J=2t log t-t+2a; on [1,b], J=3t-2t log t-4+2a; above b, J=A/2. Consequently
 C(M)=integral_2^M B_2(y)dy=A*(M^2-4)/2 - sum Lambda(n)*(J(M/sqrt(n))-J(2/sqrt(n))).
All prime terms have n<=e M^2. This gives a monotone prime weight with exact elementary antiderivative; the signed discrepancy is not automatically small. Unweighted trapezoid errors are O(log m/m), total O(log^2 M). Thus C(M)=A_2(M)-(B_2(2)+B_2(M))/2+O(log^2 M). Unconditional B_2(M)=O(M) ensures one-sided O(M) bound transfers between cumulative discrete and continuous quantities. The half-endpoint terms must not be omitted.

Executed check.py: sieve limit 437103, 36,907 prime powers, 798 numeric prefix-sum vs independently evaluated direct triangular sums (max absolute diff 5.33e-14), 101 J evaluations versus direct quadrature (max 2.45e-16), 398 interval trapezoid checks versus actual signed curvature-measure upper bound (max fraction 0.134), 30 independently split quadratures for C(M+1)-C(M) (max diff 4.20e-16). Exact rational test of Peano signed-atom formula and 1/8 bound on 500 generated piecewise affine functions all passed. C(400)=0.0358205940, B_2(400)=0.0405245635; finite numerical checks only, not certified enclosures or asymptotic evidence. Script time 5.585s. The previous exact rational square sample values agree at common points. Code and JSON included below.

## Pass D: arbitrary fixed polynomial sparsity by finite repeated-uniform kernels
This is a distinct higher-order remedy to the p>4 obstruction in Pass B. For integer k>=2, let h be the convolution of k unit-mass uniforms on [-1/(2k),1/(2k)]; let kernel kappa=h*h, supported [-1,1], nonnegative even, mass 1. Its entire transform K(s)=(sinh(s/(2k))/(s/(2k)))^(2k), only zeros on imaginary axis, and on vertical strips decays O((1+|Im s|)^(-2k)). Its exact piecewise polynomial density is
 kappa(v)=k^(2k)/(2k-1)! * sum_{j=0}^{2k}(-1)^j binom(2k,j)*(v+1-j/k)_+^(2k-1).
This follows by convolving the 2k interval densities using successive primitive differences. It is C^(2k-2), including support endpoints. In particular no atom at derivative order r=2k-2. Choose even r=2k-2>p/2 (or >=p/2 for open half-plane Re s>0); k depends on fixed p. Every derivative B_p^(j)(y)=O_{p,k,j}(y^(p/2-j)) for j<=r, by chain rule and the same active prime sum estimate; compact support and endpoint smoothness justify locally differentiating the finite prime sum. Thus f_s^(r)(y)=O_{p,k,C}(y^(p/2-p Re s-1-r)) locally uniformly in s. Apply Euler–Maclaurin (DLMF 2.10.1) on [2,N], in Re s>.5 let N->infty: all upper endpoint terms vanish. The difference S_p-I_(2^p) equals an entire finite collection of endpoint derivatives at 2 plus an integral of a bounded periodic Bernoulli remainder times f_s^(r). That integral converges locally uniformly and is holomorphic for Re s>1/2-r/p. Because r>p/2, S_p therefore carries ALL off-line positive-real poles of I in Re s>0. Pass C Landau argument works verbatim for this kernel and any fixed p. Reverse direction under RH follows from the same explicit formula by mollification and faster vertical decay. Hence for every fixed positive integer p there is a finite elementary piecewise polynomial kernel for which one-sided O(M) bound on cumulative normalized discrepancy at integer p-th powers is equivalent to RH. Not a claim for p varying with M, exponential/geometric sampling, uniform constants in p, or proof of the bound. Does not use the published formal proof as an assumption. If an infinite C-infinity bump from prior run is used instead, the same argument works for all fixed p with the same kernel and order r chosen separately, but finite repeated uniforms are easier to evaluate exactly.

Executed spline.py: 912 exact rational checks across k=1..8 of all piece boundaries, derivatives through 2k-2, outside support polynomial, moments 0,1,2,4 (variance 1/(6k), fourth 3 variance^2 -1/(60k^3)); 20 independent 45-digit numerical complex transform integrals for k=1..5, max discrepancy 8.41e-42. Code runtime 1.779s. These test the kernel identity and regularity, not the uniform prime bound or Euler–Maclaurin at infinity.

## Adversarial audit and next highest-value experiment
- Mellin transform absolute convergence initially Re s>.5, not Re s>0 unconditionally. Only analytic continuation proven there; treating continued series as convergent would be circular. Residues cannot cancel against the holomorphic correction in its actual half-plane; no claim beyond that half-plane for triangle. In Euler–Maclaurin upper endpoint terms vanish only in initial domain before continuing; no use of RH in correction estimates. All constants may depend on p and kernel, not sample index. No spectral pollution or claim of eliminating hypothetical zeros by finite sampling.
- Signed cumulative bound permits arbitrarily large individual excursions; the Landau theorem, rather than positivity of individual samples, is essential. The extra smoothing does not make the conjectured bound elementary by itself. Chebyshev only gives O(M^(1+p/2)), not O(M). The primitive J is monotone but subtracting its main term destroys monotonicity, so no free Tauberian result. No use of PNT error under RH to prove RH. No priority claim, external peer audit required.
- Next: derive direct arithmetic cumulative bounds from restricted modulus/window hypotheses of Alpoge (M), precisely trace which uniformity/square-root cancellation is needed. Use Waterloo v2 LaTeX source to map the thirteen hypotheses before selecting one; no need to repeat already verified formal kernel checks or claim a proof from the guide. Separately investigate if average prime discrepancy admits a useful unconditional bound near M^(1+epsilon), rather than new reformulations alone. If no meaningful advance, switch to quantitative auxiliary-prime margin in formal source. Avoid another routine finite triangular sample scan without a falsifiable new hypothesis.
- No independent proof/disproof found; this run achieved a discrete pole-preservation result and sparse/cumulative equivalent criteria, not the missing asymptotic estimate.


### Reproducible check.py


[Extracted file: check.py](files/check.py) · 4,283 bytes · Source block 1.


### Reproducible report.json


[Extracted file: report.json](files/report.json) · 1,331 bytes · Source block 2.


### Reproducible spline.py


[Extracted file: spline.py](files/spline.py) · 2,012 bytes · Source block 3.


### Reproducible spline.json


[Extracted file: spline.json](files/spline.json) · 1,702 bytes · Source block 4.


END CHECKPOINT — discrete Mellin pole preservation and sparse cumulative criteria — 2026-11-23.
