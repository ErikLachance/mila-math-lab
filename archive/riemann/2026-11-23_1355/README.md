# Riemann Proof Watch — independent conductor-uniformity checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1355_EST.md`. **Recorded time label:** 2026-11-23 13:55 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Checkpoint date:** 2026-11-23, America/New_York.

## Scientific continuity

Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST, asserting conditional-on-formula exact rational positivity for signed Weil form only on restricted endpoint collars L=.81,w=1/12. Its mixed interior/exterior form, complement, and full RH remain UNSOLVED by that line.

Also consulted the preceding research checkpoint `RIEMANN_CHECKPOINT_2026-11-23_1313_EST.md`. It had already derived an exact formula for a missing Euler factor, conditional explicit-formula bounds under RH, odd/even/complex character residue distinctions, exact multi-prime imprimitive corrections, and warnings that fixed-conductor O(1) constants are nonuniform. Do NOT count those previous results as new. Consulted earlier research archive for novelty; inverse p-adic series and gamma-window Mellin concentration were already studied and deliberately not repeated. Focus here is a new **sharp conductor-uniform** missing-prime inequality, which resolves part of the prior caution.


## Fresh primary and author sources actually consulted

- Michael O. Rubinstein et al., *The Alpöge–Claude proof of RH explained for ζ*, working version 2, November 22 2026, especially Part II definitions (II.7)-(II.10), Part II §1 (Mellin/one-sided criterion), §§III.10-III.11, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf ; overview https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ . The readable 265-page guide STILL assumes 13 H0-H12 hypotheses and does not independently establish its central (M). This is an exposition limitation, **not** a defect in the formal proof.
- Levent Alpöge original announcement, November 20 2026, https://alpo.ge/remark.pdf ; the Stepanov analogue uses chains of theta lifts of suggested length about sqrt(X), rather than the earlier Weil positivity method.
- Andrew Sutherland, MIT verification log, updated November 23 2026 14:35 UTC, https://math.mit.edu/~drew/grh/ . It now explicitly reports the stock Lean default kernel accepted the full export Nov22; the stock Lean paranoid kernel with allocator-setting change accepted Nov23; Comparator v4.33.0 said "Your solution is okay!" Nov23; v4.36.0 lake comparator and default-allocator paranoid replay still running. All 175,187 modules and independent kernels have passed their respective completed checks. These are **externally reported** verification results; this run did not rebuild 17M Lean lines.
- Source PDF web screenshot attempted at printed p63 (web cache miss); screenshot succeeded at printed p193 and Alpöge p1. No new erratum or source typo claim made from unrendered p63.

## NEW mathematical pass A — exact nonuniformity of fixed-character O(1) constants

Fix primitive nonprincipal χ* modulo prime q and a new prime p not dividing q, and induce it to χ modulo qp. Write a=χ*(p) with |a|=1, and define Rubinstein's centered Riesz-smoothed sum Gχ(x)=sum_{n<=x} Λ(n)χ(n)(x/n−1)+(L'/L)(1,χ)x. The Euler factor L(s,χ)=L(s,χ*)(1−a p^(−s)) gives, for m=floor(log_p x):

`Δ(x):=Gχ(x)−Gχ*(x) = log(p) [ sum_{k=1}^m a^k + x*a/(p−a)*(a/p)^m ]`.

This formula had already appeared in the 13:13 fallback; the NEW question is its dependence on conductor. Choose q prime, r=q−1; choose a prime p primitive modulo q (possible unconditionally by Dirichlet's theorem on prime progressions, for each fixed q), and a nontrivial primitive Dirichlet χ* with χ*(p)=exp(2πi/r). Put x=p^(r/2). Then

`|Δ(x)|/log(p) >= 1/sin(π/r) − 1/(p−1)`, which grows like r/π.

Therefore a uniform `|Δ(x)| <= C log(p)` with C independent of q/character order is FALSE, even though a≠1. As q grows, the extra factor `1−a p^(−s)` has a zero on Re(s)=0 with smallest positive ordinate `2π/(r log p)`, approaching the origin; it does not create a zero in the open critical strip. This is an elementary exact counterexample to a naive uniform-constant strengthening; not an RH counterexample.

High-precision (mpmath 110 digits) values for (q,p,r)=(11,2,10),(31,3,30),(101,2,100),(211,2,210),(307,5,306),(1009,11,1008): observed |Δ|/log p approximately 2.7636,9.4778,31.7582,66.8102,97.4010,320.8565. All satisfy the exact lower bound. Finite-form original prime-power correction versus the closed geometric formula checked for q=11,31,101 with errors <7e-97. Script `phase_conductor_growth.py`, JSON of same stem. Analytical proof does not depend on floating point.

## NEW mathematical pass B — SHARP conductor-uniform logarithmic bound, resolving the above apparent hazard

The same exact identity can be rewritten as a **single absolutely convergent positive-coefficient envelope**:

`Δ(x)/log p = sum_{k>=1} a^k min(1,x/p^k)` for all x>=1.

This holds since for k<=m the coefficient is 1 and for k>m it is x/p^k. Since |a|=1,

`|Δ(x)| <= log p * [m + (x/p^m)/(p−1)]` if m>=1, and `|Δ(x)|<=x log p/(p−1)` if m=0.

**Rigorous sharp claim: for EVERY x>=2, every prime p, every primitive χ*, and induced χ by adjoining the missing prime p,**

`|Gχ(x)−Gχ*(x)| <= 2 log x`.

Proof for x>=p: put t=x/p^m in [1,p), m>=1. Let h(t)=m+2log_p(t)−t/(p−1). Its second derivative is negative, so minimum on [1,p] occurs at an endpoint. h(1)=m−1/(p−1)>=0 and h(p)=m+2−p/(p−1)>=0. Thus m+t/(p−1)<=2log_p x. For 2<=x<p, decreasing `log p/(p−1)` as a function p>1 gives x log p/(p−1) <= x log x/(x−1) <=2log x. **Sharpness**: q=7, primitive quadratic χ* modulo7, χ*(2)=1, induce to modulus14 and take x=p=2; the discrepancy equals `2 log 2`, exactly the bound.

This resolves the conductor-size worry for **a bounded number** of additional bad primes: for a fixed finite set P, triangle inequality gives `|Gχ−Gχ*| <= 2 |P| log x` for every x>=2, regardless of conductor or proximity of a to1. Thus these corrections are always o(x^ε) for fixed P and any ε>0, and cannot by themselves destroy an x^(1/2+ε) target. For an unbounded number of missing primes, the factor |P| MUST still be tracked. No use of RH was made. This is an elementary lemma, probably not historically novel, but useful to audit quantifier transfer.

Code: `sharp_imprimitive_uniform.py/.json`, independent 5,320 high-precision tests over p,x,roots-of-unity phases with no violations and equality at p=x=2,a=1. These tests support, but do not replace, the analytic proof.

## NEW mathematical pass C — direct full prime-power regression

Construct primitive complex characters modulo prime q via actual primitive roots/discrete logs, with q=11,31,101. Induce to modulus qp for p=2,3,103. Directly enumerate ALL prime powers n<=x for 34 choices of x, evaluate both G-functions independently on prime powers (and the exact Euler centering correction), and compare to the closed geometric formula. Every case passes at mp.dps=100, worst absolute residual <8e-99. Special p=103>x cases tested; closed formula correctly uses m=0. Script `direct_dirichlet_regression.py/.json`. This checks a real Dirichlet-character realization, not only formal roots of unity.

## Adversarial limitations and follow-on

1. None of this proves or refutes Riemann or its generalized versions; the Lean theorem is from external authors and was not independently rebuilt by this agent. The conditional H0-H12/(M) inputs are still missing in the readable guide.
2. Bounds concern induced characters after adding finite missing Euler factors. Uniform in a,q,p holds for each individual factor, but if the number of missing primes is not bounded, the aggregate bound may grow; avoid silently replacing `O_{q}(1)` with `O(1)`.
3. Numeric root-of-unity experiments are high-precision but **not interval-rational**; the sharp inequality and conductor lower bound are self-contained elementary proofs independent of numerics.
4. Previous 13:13 work already established exact factor correction and its order-dependent behavior for fixed characters; this run's genuine addition is the *sharp unconditional uniform 2log(x) envelope*, its exact equality example, and explicit growing-conductor counterfamily with quantitative lower bound.
5. Next high-value: audit the number of missing primes in **the actual H12 auxiliary character conventions**, and test whether the source ever uses absolute `O(1)` uniformly with q,d growing; the new sharp log bound may repair a presentation ambiguity without changing the formal theorem. Separately inspect zero-free strip estimates and precise quantifiers in the formal source.

**Status:** No independently produced RH/GRH proof or disproof.
