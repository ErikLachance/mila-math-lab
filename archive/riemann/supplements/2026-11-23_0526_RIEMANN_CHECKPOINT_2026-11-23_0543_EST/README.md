# Riemann Proof Watch — checkpoint 2026-11-23 05:43:09 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `2026-11-23_0526_RIEMANN_CHECKPOINT_2026-11-23_0543_EST.md`. **Recorded time label:** 2026-11-23 05:43 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)

**Status:** Riemann hypothesis is NOT proved by this research. Independently announced Alpöge–Claude full Lean proof is not this project's achievement. All local compact-support positivity statements below are **conditional on the correctness of the standard signed Weil-form formula and its application to smooth functions** and require independent source-to-code audit. Not a proof for all support lengths, nor for the whole interval.


Prior same-day research record `2026-11-23_RIEMANN_DELTA_2026-11-23_0522_EST_W15_EXACT.md` and its code, recording older conditional all-rational `w=1/15` restricted-support bound >1/100 on 256 bins and `w=1/16` >1/20. This run is not the first on November 23. The earlier stored code was inspected; the old scripts were not silently counted as new experiments.

## Independently studied primary sources / status as of 2026-11-23

- Lean FRO + Mathlib Initiative public certification November 21: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ . It reports that Alpöge–Claude's formal proof compiles with no nonstandard axioms and matches the known mathematical statement.
- Andrew Sutherland (MIT), November 22 log: https://math.mit.edu/~drew/grh/ . All 175,187 modules built, independent Lean/nanoda/con-leche kernel checks and declaration matching; several redundant monolithic checks were still progressing when logged. Do not confuse with a new proof from this project.
- Michael Rubinstein at Waterloo, November 22 v2 readable draft, 265 pages: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf ; and overview https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ . Readable presentation still reduces key bound (M) to thirteen auxiliary hypotheses requiring further explanation, despite formal Lean certification.
- Masatoshi Suzuki, Weil form and form domain: https://arxiv.org/html/2606.09096v4 . Xuefeng Zhu, complete Weil archimedean symbol and compact-support positivity: https://arxiv.org/html/2608.24827v2 . NIST digamma asymptotics: https://dlmf.nist.gov/5.11 .
- Anthropic August report (distinct from November claimed complete Lean result): https://www.anthropic.com/research/riemann-zeta . Clay still administratively lists Riemann under 'unsolved': https://www.claymath.org/millennium-problems/ .

## Micro-pass A: Rubinstein readable draft, gamma and power scaling

New reproducible scripts + reports stored locally alongside this checkpoint:
- `prime_ramp_audit.py` and `.json`: independent sieve of 149,235 prime powers n<=2,000,000 checked smoothed explicit-function `S(x)=Σ_{n≤x} Λ(n)(x/n−1)` and `G(x)=S(x)-x log x+(1+γ)x`. Rounded values G(10^4)=1.749315, G(10^5)=3.671462, G(10^6)=11.040436, G(2e6)=−12.267801 agree with Waterloo table to displayed digits; numerical regression only, not a proof of RH. Discrete isolated good sample points cannot replace a point on each multiplicative interval `[Y,Y^(3/2)]`: explicit oscillatory toy f(x)=x^β cos(ω log x) falsifies such a naive inference.
- `gamma_window_check.py/.json`: for positive gamma kernel u^j exp(−a u)/j!, choose j≈5aU/4 to center at 1.25U. For shape k=j+1, rate a, exact Chernoff upper bound to tails outside [U,1.5U] is sum exp[−k(r−1−ln r)] for r=aU/k and 1.5aU/k. At U=160 observed tail 1.03e−4 versus bound 0.001094; at U=640 observed 3.06e−14 versus bound 6.235e−13. Choosing j≈aU instead loses mass (~0.485 left tail). Numerical integration only falsifies bad parameter settings; bounds analytically derived.
- `main_inequality_scaling.py/.json`: for the Waterloo error terms x/m + x m/k + m + k/n², exact fraction substitution m=x^(1/2),k=x^(9/2),n=x² gives exponents (1/2, −3,1/2,1/2). Universal lower max(a,1−a)>=1/2 for m=x^a, preventing improvement past sqrt by tuning m alone. Wrong k=x^.9 produces O(x^.6) first-related term. This is a local parameter analysis, not independently proving bound (M).

## Micro-pass B: exact closed-form, no p bins, w=1/15

Reconstructed earlier adaptive Weil collar cap with delta=2L−ln5. For complex f in E_w two mirrored endpoint collars (normalized ||f||=1), let p∈[0,1] be L² mass in active delta-wide prime5 segments. Upper Fourier density `M(p)=[sqrt(delta*p)+sqrt((w−delta)*(1−p))]^2/pi`, and signed pole ≥−4w sinh(L/2)^2. Using H(t)=Re ψ(1/4+it/2)−lnπ increasing, apply bathtub inequality with cutoff T, and arch bound h+2M(I−Th), h=H(T), I=∫0^T H. All rational coarse constants verified exactly with Machin atan, log atanh, Euler–Maclaurin and sinh Taylor; digamma series truncated at 400 with positive lower, left Riemann integral 768 cells at 10^10 floor. Introduced analytic minimization over p without grid using p=(1+y)/2:
`max_p [D(a p+b(1−p)+2sqrt(ab p(1−p))) + c p] = [D(a+b)+c+sqrt(D²(a+b)²+2D(a−b)c+c²)]/2`, where a=delta_upper,b=w−delta_lower,D=2(Th−I)/pi_lower,c=18/25. Three rational p intervals [0,2/5], [2/5,11/25], [11/25,1] with respective T=4711/200,25,26 each certified exact lower >1/60. Conservative decimal minima respectively .01831890024698, .01676829984613, .01693648050855. `w15_three_intervals_closed_form.py/.json` (0.23s). **Adversarial bug found and fixed in this run:** initial derivation wrongly used p*=(1−X/sqrtR)/2 and inverted minimizer sign. Correct maximizer p*=(1+X/sqrtR)/2; after correcting formula and branch naming, exact all-interval comparisons remained positive with unchanged conservative bounds. Do not rerun the original erroneous version; use corrected uploaded script.

## Micro-pass C: parity-separated larger collars, exact Fraction tests

Use support E_w=(-L,-L+w)∪(L−w,L), L=81/100 and Delta=2L−ln5. Prime-power shifts 2,3,4 vanish by geometry; only n5 is nonzero. Signed Weil form decomposes evenly/oddly by reflection (cross term 0) for complex f.

**Odd parity:** fhat(0)=0, giving `rho(t) ≤ M(p)*min(1,(L*t)^2)`. For fixed T≥1/L, define v=1/L, effective density cap mass coefficient a_T=T−(2/3)v. Arch bound `h+2M*(L²∫0^v t²H(t)dt +∫v^T H(t)dt−a_T h)`, provided 2M*a_T<1; add negative prime5 charge ≤c*p and pole ≥−4w sinh(L/2)². All integrals lower via exact rational 400-term positive digamma series with 480 left-cell bounds; p via 256 intervals and outward isqrt; T adaptive half-integer grid 20..36. `w14_odd_weighted_exact.py/.json` certifies exact lower >0.1166052 for w=1/14; `w13_odd_weighted_exact.py/.json` >0.05740165 for w=1/13. Both stronger than 1/10 and 1/20 respectively **in odd sector only**, and conditional on source formula. A floating SciPy exploration `w14_odd_refined_exploratory.py/.json` agrees, but floating output is not proof.

**Even parity:** define q=|∫ f cosh(x/2)dx|², 0≤q≤2w*(11/10)². Positive signed pole +2q, and for |t|≤τ=7/10, `rho(t) ≤ B(q)=[sqrt(q)+sqrt(2w)L²(τ²/2+11/80)]²/(2pi)`. Full density cap M(p) remains. Arch below `h+2M(I_T−Th)+2[max(0,M−B)]*(τh−I_τ)`. For lower bound use conservative M_upper, M_lower, B_upper; lower h,I_T, UPPER I_τ (computed from finite digamma upper with provable tail t²/[8(N−1)²], 512 RIGHT cells); each case asserts 2 M_upper*T<1, q,p rational intervals. Nonnegative pole +2 q_lower and prime -c p_upper. `w14_even_two_parameter_exact.py/.json` exact rational 128×128 p/q rectangle grid produces full lower >0.1096354525; `w13_even_two_parameter_exact.py/.json` >0.05209288805. All 16,384 rectangles covered, zero untested bins, no float decision. Independently verified H0 upper and lower via rational gamma bounds. Therefore **conditional on normalization/source-to-code**, combined parity supports all complex smooth f in E_(1/13) with `Q_W(f)> (1/20) ||f||²` and all f in E_(1/14) with `Q_W(f)> (1/10)||f||²`. These are *quantitative improvements on smaller supports already within the earlier w1/12 positive region*, not global RH or breakthrough novelty. Independent mathematical peer review is still missing.

**Negative/falsification checks:** w1/12 attempted using same simplified schemes `w12_even_two_parameter_exact.py/.json`: worst lower −.0103315 and 5,376 q/p bins without admissible cutoff; this indicates FAILED SUFFICIENT BOUND, NOT a negative Q vector, and does not refute earlier w1/12 certificate. `w12_odd_weighted_exact.py/.json` extending T grid down to 15 yielded −.0067392 lower, another inconclusive insufficient bound. w1/11 and w1/10 odd exploratory negative sufficient lower, not counterexample. Do not waste time rerunning identical crude cuts; use better q and frequency-dependent caps or prior w12 scheme.

## Micro-pass D: independent real time-domain signed Weil sanity check

`w15_two_mode_time_domain.py/.json` builds exact integral kernel and prime5 shift for two normalized indicator functions on ±w1/15 collars. 2×2 numerical full Weil matrix has diagonal ≈1.409668889 and offdiagonal ≈0.029487913, eigenvalues ≈1.380180976,1.43915680. Correct pole plus/minus/cross, prime5 cross≈−0.1140329207. Indicator jumps require closed-form-domain justification; matrix numerics are only checks, not proof of positivity of all infinite-dimensional f.

## Next most valuable independent steps

1. Independently derive/check full signed Weil Q convention from Suzuki v4 & Zhu v2 for **complex** f and parity. Compare normalization of Fourier/archimedean term and pole with source; this is the biggest remaining source-to-code audit for local collar certificates.
2. Seek narrower finite rational simple paper proof of combined w1/13 Q>1/20 (currently grid-heavy), and a genuine mixed core/collar Schur complement estimate. Do not infer whole-window positivity from collar support, and do not extrapolate finite Galerkin positivity or codimension bounds.
3. Continue adversarial verification of readable Alpöge–Claude proof: in the Waterloo v2 derive exactly which quantifiers and uniform constants in (M) and H0..H12 are needed; investigate gamma-window and smoothed prime-sum bridge with no off-line-zero circular assumptions. Distinguish published Lean proof from our own validation; no claim of reproducing 17million lines.


