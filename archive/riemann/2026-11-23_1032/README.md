# Riemann Proof Watch — append-only mathematical research checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1032_EST.md`. **Recorded time label:** 2026-11-23 10:32 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Actual date/time:** 2026-11-23 10:32:57 EST (`America/New_York`).
This report is independent work during this run, not a proof of RH.

## Scientific continuity

Earlier Riemann checkpoint: November 8, 2026 15:30:58 EST, conditional Weil-form positivity for functions supported on two collars of width 1/12 at L=.81, plus separately stated codimension <=14 bound. These do not imply global nonnegativity or RH. Also consulted `RIEMANN_CONTINUATION_2026-11-23_0955_EST.md` and 09:30 EST checkpoint; a DIFFERENT research angle was selected to avoid duplicating tests of generalized Bernoulli, lemniscatic sine, theta moments, rational prime-table or frame-operator kernel bounds.


## Current authoritative sources consulted (November 23 2026)

1. Rubinstein et al., *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, working draft v2 dated **November 22, 2026**, PDF https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf ; abstract, Part I.1 eqs (I.3)–(I.4), one-sided Landau interval criterion, §III.11 H12 requirements. Actual PDF pages 1 and 214 rendered/screenshotted in this run. Crucial caution: its human-readable guide takes (M) and 13 numbered assumptions as source inputs, *not proved within the guide*; this does NOT invalidate a separately independently checked formal Lean theorem.
2. Lean FRO and Mathlib Initiative **November 21 2026** joint statement https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ ; official certification that 17M-line formal proof targets Mathlib RiemannHypothesis with standard axioms and multiple kernel checks.
3. MIT Andrew Sutherland independent verification log https://math.mit.edu/~drew/grh/ last updated **2026-11-23 14:35 UTC**; 175,187 modules compiled, official Lean kernels, independent kernels, Comparator v4.33.0 PASS, v4.36.0 pending at that timestamp. These are external checks, not locally reproduced.
4. Classical unconditional von Mangoldt harmonic sum theorem `sum_(n<=x) Lambda(n)/n = log x + O(1)`, with formal Metamath proof https://metamath.tirix.org/mpeuni/vmadivsum . Used only as known analytic input in a supplementary comparison, not needed for the strongest semiconvex criterion.

## Fixed object and non-circular reference

Define for real x>=1:
`S(x)=sum_(n<=x) Lambda(n)*(x/n-1)=sum_n (Lambda(n)/n)*(x-n)_+` and `G(x)=S(x)-x log x+(1+gamma)x`. This is exactly the smoothed prime-power statistic in Rubinstein Part I.1 and Alpöge's announcement. Von Mangoldt Lambda>=0, so S is globally convex (a locally finite sum of nonnegative-weight hinges). The jump at a prime power is UPWARD in G', not a downward discontinuity. G is continuous. This positivity is unconditional elementary arithmetic and must not be confused with the signed full Weil quadratic form.

## Pass A: elementary grid condition (logarithmic derivative bound)

Away from prime powers `G'(x)=A(x)-log x+gamma`, where `A(x)=sum_(n<=x)Lambda(n)/n`. Elementary `Lambda(n)<=log n` and `sum 1/n <=1+log x` give `|G'| <= (log x)^2+2 log x+1` for x>=2; a safe local bound M_Y at upper endpoint Y^(3/2). Continuity at every jump gives Lipschitz globally on the interval. A left-node mesh with h<=Y^theta/M_Y extends `G(node)<=C node^theta` to `G(x)<=(C+1)x^theta`, for 0<theta<1. Costs `O(Y^(3/2-theta) log^2 Y)` sample nodes. Checked an independent prime-power sieve and randomized probes for Y=40,100,200,1000; no numerical counterexample. This is a sufficient conditional reduction, not new cancellation estimates.

## Pass B: quantifier / hidden-uniformity attack

Source H12 needs arbitrarily late **whole intervals** [Y,Y^(3/2)] and x-independent constants; isolated arbitrarily large x do not suffice. Explicit smooth falsification of such a weakening: `F(x)=x^(4/5)*sin^2(log x)`, threshold theta=3/5. Every Y_k=exp(k*pi) has F(Y_k)=0, yet for x_k=exp((k+1/2)*pi) in [Y_k,Y_k^(3/2)], `F(x_k)/x_k^theta=exp((k+1/2)*pi/5)` diverges. Also allowing a bound constant C_x to vary with x is vacuous. Numerically tested k=1,2,5,...; argument is exact. This is NOT a counterexample to original H12.

## Pass C: classical unconditional derivative improvement

Using classical sum Lambda(n)/n=log x+O(1), `G'=O(1)` away from jumps, and continuity upgrades the Lipschitz grid to `O(Y^(3/2-theta))` nodes, with h~Y^theta. The implied O(1) is NOT obtained by finite testing. Exhaustively computed approximate left/right derivatives for all integer prime-power positions through x=250,000; observed max |G'| ~0.230642 at 2+, illustrative finite-only and NOT a universal bound. This criterion is weaker than next pass.

## Pass D: analytic one-sided semiconvexity theorem (strongest result)

For arbitrary 1<=a<x<b, `t=(x-a)/(b-a)`, convexity of S implies `S(x)<=(1-t)S(a)+t*S(b)`; affine Euler-constant part cancels. Hence **exact mathematically proved inequality**:
`G(x) <= (1-t)G(a) + t G(b) + D(a,b;x)`, with
`D=(1-t)*a*log(a)+t*b*log(b)-x*log(x)>=0`.
For a>=Y>=1, because `(x log x)''=1/x <=1/a`, bound `D<=((x-a)*(b-x))/(2*a)<= (b-a)^2/(8*a)`.
Since x^theta is concave for 0<theta<1, `(1-t)*a^theta + t*b^theta<=x^theta`. Thus if **both endpoints** obey `G(a)<=C*a^theta`, `G(b)<=C*b^theta` and `b-a<=sqrt(8*a^(1+theta))`, then EVERY x in [a,b] obeys `G(x)<=(C+1)*x^theta`. Neither RH nor the prime number theorem enters this finite-net implication.
Uniform grid with every h<=sqrt(8Y^(1+theta)) needs `O(Y^(1-theta/2))` cells on [Y,Y^1.5]. 29,100 float64 diagnostic points across Y=100,1000,5000 gave zero violations. This is a mathematical *reduction only*; the difficult endpoint bounds remain unproved.

## Pass E: NEW adaptive grid, sharply reduced point count

Set `a_0=Y`, `a_(j+1)=min(Y^(3/2),a_j+sqrt(8)*a_j^((1+theta)/2))`. Every gap satisfies the local semiconvex requirement `h_j^2/(8 a_j)<=a_j^theta`. A dyadic partition of [Y,Y^1.5] (with any fixed theta in (0,1)) gives a **rigorous upper count `O(Y^(3*(1-theta)/4))` grid intervals**: in each dyadic slab x~A, mesh size >=const*A^((1+theta)/2), so O(A^((1-theta)/2)) points, dominated by last slab with A~Y^1.5. This improves the previous uniform count exponent `1-theta/2`. It is entirely unconditional, but again needs the still unknown uniform bound G at nodes for arbitrarily large Y.

Actual diagnostics with fresh sieve and adversarial points at each prime-power hinge, plus 200 randomized points per interval:
[
  {
    "Y": 100,
    "theta": 0.52,
    "upper": 1000.0,
    "uniform_steps": 10,
    "adaptive_steps": 5,
    "samples_including_prime_power_knots": 1479,
    "C_from_adaptive_nodes": 0.1570196886351914,
    "max_G_minus_exact_interpolant": -0.001996855706180467,
    "max_defect_over_local_quadratic_bound": 0.9751678509686942,
    "worst_defect": 21.36799919180885,
    "violations": 0
  },
  {
    "Y": 1000,
    "theta": 0.57,
    "upper": 31622.776601683792,
    "uniform_steps": 48,
    "adaptive_steps": 10,
    "samples_including_prime_power_knots": 11859,
    "C_from_adaptive_nodes": 0.02985043101260989,
    "max_G_minus_exact_interpolant": -0.0037183876865962695,
    "max_defect_over_local_quadratic_bound": 0.9589451101216999,
    "worst_defect": 256.63739713071845,
    "violations": 0
  },
  {
    "Y": 5000,
    "theta": 0.6,
    "upper": 353553.39059327374,
    "uniform_steps": 136,
    "adaptive_steps": 15,
    "samples_including_prime_power_knots": 92133,
    "C_from_adaptive_nodes": 0.013065767873936653,
    "max_G_minus_exact_interpolant": -0.020847716508354264,
    "max_defect_over_local_quadratic_bound": 0.9296366972917801,
    "worst_defect": 1545.9949186989106,
    "violations": 0
  }
]
Each test `G(x)<=chord(G(a),G(b))+D`, `D<=h^2/(8a)` and `G(x)<=(C+1)x^theta` passed with zero float-level violations. Total samples 105,471. This is NOT a numerical proof of any infinite bound.

## Pass F: attack potential weakness of curvature estimate and check sharpness

On any interval between consecutive prime powers, S is AFFINE and the inequality in Pass D is actually an EQUALITY: `G(x)=chord(G(a),G(b))+D(a,b;x)`. This shows the interpolation correction D cannot simply be omitted. Evaluated 8 largest gaps between consecutive prime powers in [10000,20000], using mpmath with 85 decimal digits and an independently summed prime-power S: midpoint interpolation identity residual <1e-80. At gap (19609,19661), h=52, D(mid)=0.01721416342122836655... and crude bound h²/(8a)=0.01723698301800193788..., ratio 0.998676125819..., nearly sharp. Thus a proposed shortcut dropping D is actually FALSE even for genuine von Mangoldt sums; no Lean gap or RH counterexample.

## Consequence and failure modes (strict truth conditions)

Using the SOURCE'S one-sided Landau interval lemma, and its unchanged proof with any constant K>0 (replace 2 x^theta by (K+1)x^theta), a DISCRETE conditional equivalence is obtained: **RH iff** for each theta in (1/2,1) there exists C_theta independent of Y and arbitrarily large Y such that all nodes of the above adaptive grid on [Y,Y^1.5] satisfy `G(node)<=C_theta node^theta`. RH => true by the usual smoothed explicit formula G=O(sqrt x). Conversely grid lemma => continuous bound (C_theta+1)x^theta on arbitrarily long whole intervals => zero-free Re(s)>theta => RH as theta↓1/2 and functional equation. This is a technically justified restatement, **NOT a new RH proof**, since it has not established the node-wise estimates at growing Y. The change from coefficient 1 in source to an arbitrary FIXED coefficient is justified by exactly the same Landau argument; must not permit C_theta to depend on Y.

Hidden assumptions attacked: continuous closure at prime-power kinks (true); nonnegative hinge coefficients (true); no unsupported interchange of infinite sums (sum locally finite); correct sign of `-x log x` (checked); no claim from finite float runs to all Y; avoid extrapolating old Weil collar results; don't treat unproved H12 guide assumptions as a Lean proof flaw; do not mistake improved number of sample points for a method of bounding those prime-power sums. The source proof already verified by independent Lean checkers remains external; our own code did not recompile it.

## Scripts, exact hashes and future reproducibility

The separately generated companion zip `RIEMANN_SCRIPTS_2026-11-23_1032_EST.zip` (SHA256 `22ff2c1bb10eb36b79833ab25a6d8c53726f3c73447db9f427729bfa66e679cd`) contains all 6 Python scripts and 6 JSON reports from this run:
- `riemann_h12_adaptive_semiconvex.py` SHA256 `2637b0a8f53e6b61f42f7a0201a1d7413b4647a645f29da1624fa6fbf6b596a8`
- `riemann_h12_grid_audit.py` SHA256 `75d7c6b32523ddc38b56ac3bac59e6023fd47e5e88f86e01e153f7f5400ba69c`
- `riemann_h12_mertens_upgrade.py` SHA256 `75f1f0a6c98cd2b25345267d164bd1ffde5274cd46a8d9f6cdbc6a4a2eb4684c`
- `riemann_h12_quantifier_countermodels.py` SHA256 `4df998621775ae7164389a86d5b73fa19747b4ae65ccf17bc196fdb2af82d91f`
- `riemann_h12_semiconvex_grid.py` SHA256 `60c5653194e4d9cf3c49ed79c038cf983ffa9638019f5ada11ba1ac90b81be92`
- `riemann_h12_tightness_gap.py` SHA256 `0f6f8a1bcd6008ca68220c90fa18334faf8eaf1d550da2757a6e366e35968790`
- `riemann_h12_adaptive_semiconvex.json` SHA256 `d0aea60079c6c046f6d070df2ab57780f2aacbe4c6cb818d8b4b6fe613cc4a12`
- `riemann_h12_grid_audit.json` SHA256 `88ced6e6642e2370a2929f3047ce66f8386055e692fb128e55176d83115b53be`
- `riemann_h12_mertens_upgrade.json` SHA256 `40c8805ac329c8415060595efc5925801600edff7d018bc93fe68e76973acce1`
- `riemann_h12_quantifier_countermodels.json` SHA256 `0ab466d69932a83bbf457791fcf1a2fad5c300ef506ae3cb9cfd6c9774981ead`
- `riemann_h12_semiconvex_grid.json` SHA256 `5c8d39443550fcaad1ed306055582dc7b18c78058cbb1948ab41b538cfbdfbc5`
- `riemann_h12_tightness_gap.json` SHA256 `874907265f108e8b2316877a96a3454b364563ae3f56876c6b170eb9a5d6eacd`

Scripts executed under this run in conversation sandbox only. The two highest-value novel-to-this-project scripts are `riemann_h12_adaptive_semiconvex.py` and `riemann_h12_tightness_gap.py`. No claim of external novelty or peer review.

## Next most valuable DISTINCT experiments, not repetition

1. Independently audit the analytic **interval Landau criterion** and constant K extension with a second proof, especially any hidden zero sup or real-zero exception; this is what upgrades the discrete lemma to an RH-equivalent statement.
2. See whether the arithmetic theta-lift construction in H12 supplies a computable `C_theta` at adaptive sample nodes **without** requiring uniform H0-H11 for the whole interval; examine quantifier switching and the data pair q,d constraints. If no such theorem, the adaptive restatement alone is mathematically insufficient.
3. Return to a source-level dependency audit of the hard deep trace/covolume/theta-kernel statements that provide (M), rather than finite primes or more numerical RH zero scans.


**Scientific status:** no new proof/disproof; elementary rigorous finite-net theorem plus conditional discrete restatement and new adversarial tests.
