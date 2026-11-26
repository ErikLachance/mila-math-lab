# Riemann Proof Watch - append-only fallback research checkpoint - 2026-11-23 07:57 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0757_EST.md`. **Recorded time label:** 2026-11-23 07:57 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity


Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST partial Weil-form positivity certificate on the support collars L=81/100,w=1/12 and independent negative-index bound <=14 at L=.81; no full-window result. The preceding checkpoints 07:41, 07:29 and 07:18 were consulted to avoid duplicate source tracing and p-adic experiments.


## Primary sources inspected

- Levent Alpoge, original 2026-11-20 announcement and 20-step chronology, https://alpo.ge/remark.pdf , pages 1, 3, 4 inspected as web PDF screenshots. States Stepanov-inspired construction and roughly sqrt(X) chained theta lifts for a von Mangoldt sum of length X; this is narrative, not a standalone readable proof.
- Andrew Sutherland (MIT), independent Lean verification status last updated 2026-11-22 16:20 UTC, https://math.mit.edu/~drew/grh/ : all 175,187 modules compiled, standard axioms only, two additional kernels and statement comparison accepted; some redundant long-running official kernel export checks still marked running on that page. Independent full Lean recompilation NOT executed here.
- Lean/Mathlib joint certification 2026-11-21, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ : full confidence in formal theorem and proof. This concerns RH and Dirichlet-character GRH, not all automorphic L-functions.
- Michael O. Rubinstein, working guide *The Alpoge-Claude proof ... for zeta*, v2, 2026-11-22, 265 pages, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf ; actual PDF text and screenshots pp.7,22,195 inspected; sections I.1, I.8, III.11. The human-readable text proves RH only CONDITIONALLY on its main inequality (M), reduced to 13 currently UNPROVED-IN-THE-GUIDE hypotheses H0-H12. This is an expository gap, NOT a reported logical/Lean-kernel gap.
- Kaczorowski and Pintz, *Oscillatory properties of arithmetical functions I*, Acta Math. Hung. 48 (1986), pp.173-185, https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf ; primary theorem 1 and corollary 1 inspected with PDF screenshot. The sign-change theorem on [T^(1-alpha),T] requires meromorphic Mellin structure, unlike an arbitrary function with sparse good windows.
- NIST DLMF Chapter 25 background https://dlmf.nist.gov/25 ; no novel claim based on it.

## Distinct micro-passes and independently executed code

A. **Exact normalization audit of smoothed prime-power Mellin transform.** For n>=2 and Re(s)>1, proved by elementary antiderivatives that integral from n to infinity of `(x/n-1)*x^(-s-1) dx = n^(-s)/[s(s-1)]`. Checked 12 combinations with n in {2,3,5,11} and real or complex s at 85 decimal digits, max numerical error below 1e-55. With F(s) = -(zeta'/zeta)(s)/[s(s-1)] -1/(s-1)^2 +(1+gamma)/(s-1), derived Laurent cancellation at s=1 using zeta(s)=1/(s-1)+gamma-gamma1*(s-1)+...; resulting F(1)=1+gamma+gamma^2+2*gamma1 = 1.7647618977418980852... where gamma1 is the FIRST signed Stieltjes constant. Verified high-precision symmetrically down to h=1e-22 (last error ~1.17e-42). At s=0, residue of F is log(2pi)=1.837877..., confirmed independently to relative error ~1e-13 at s=1e-12. These local analytic identities neither prove the uniform bound (M) nor RH.

B. **Four-cost exponent balance.** Rubinstein (I.35) writes scaled error terms x/m, xm/k, m, k/n^2. For integer square x=q^2 take m=q, k=q^9=x^(9/2), n=q^4=x^2. Exact Fraction arithmetic for q in {10,100,1000,10000} yields costs q, q^-6, q, q, respectively, so O(sqrt(x)). More generally for x=q^(r+1), m=q and cost x/m+m^r =2q^r =2x^(r/(r+1)), exact cases r=1,2,3,4 and q=10,100,1000; r=2 gives exponent 2/3, NOT 1/2. This only validates algebraic scaling IF the complete (M) inequality and all uniform bounds hold. The paper specifically warns that getting the per-step cost down to m rather than m^2 requires deep Galois-cohomology/denominator control; algebra cannot replace that theorem.

C. **Completed xi identity without assuming RH.** From Hadamard product and xi(s)=xi(1-s), derived sum over ALL nontrivial zeros (with multiplicities) `sum 1/[rho(1-rho)] = 2 xi'(1)/xi(1) = 2+gamma-log(4pi) = 0.04619141793224206762862...`. Numerical symmetric log-derivative checks passed at h=1e-4,1e-5,1e-6. Independently computed the FIRST 60 zeta zeros on the critical line, paired with their conjugates; partial sum 0.0379258397278986572631, deficit 0.00826557820434341036549 relative to exact identity. This finite check is NOT evidence that all zeros are on the line and NOT an RH proof. The identity itself is unconditional.

D. **Euler factors for imprimitive Dirichlet characters.** If an imprimitive character is induced from chi*, then L(s,chi)=L(s,chi*) product over deleted primes of `(1-chi*(p)p^(-s))`. For Re(s)>0, each factor is nonzero because |chi*(p)p^(-s)|<=p^(-Re s)<1. This explains why primitive reflection extends to all characters on the critical strip; it is NOT true without the strict Re(s)>0 hypothesis (e.g. 1-2^(-s) has a zero at s=0). Eighteen high-precision finite cases checked, and a general inequality proof recorded.

E. **Independent prime-ramp/Stieltjes identity.** Let psi(t)=sum_(n<=t)Lambda(n). By finite Fubini and integration by parts, `S(x)=sum Lambda(n)(x/n-1) = x*integral_1^x psi(t)/t^2 dt = integral_1^x [sum_(n<=t)Lambda(n)/n]dt`. Two independent algorithms using events/plateau integrals verify 13 real x values (including prime powers, nonintegers, x=10000) at >=52 digits, and 13 left/right derivative jump checks at n=2,...,64 confirm jump Lambda(n)/n. At x=10^4, G(x)=1.74931524461837583..., consistent with Rubinstein's printed 1.749. Initial finite-difference test FAILED due to Python `int/int` division producing float64 for G(n) at integer n, amplified by dividing the difference by 1e-9. Repaired by coercing x to mp.mpf inside the independent sum routines; all assertions now pass. Do NOT represent this numerical bug as a mathematical counterexample.

F. **Independent long-window Landau route.** From Kaczorowski-Pintz 1986 corollary 1 for the Mellin transform of f(x)=G(x)-2x^theta with zero real-axis pole at Theta=sup Re(zeta zeros)>theta: if any zeta zero lies right of theta then the meromorphic F yields a sign change in `[T^(1-alpha),T]` for all sufficiently large T. Setting alpha=1/4 and T=Y^(3/2) yields `[Y^(9/8),Y^(3/2)]` contained in `[Y,Y^(3/2)]`. But under the postulated window upper bound G(x)<=x^theta, f<=-x^theta on that whole subinterval, contradiction. This is a conditional analytic implication, not a proof that the required windows exist; it is NOT valid for arbitrary C1 or Lipschitz functions without the meromorphic Mellin hypothesis (prior fallback 07:41 contains an explicit countermodel).

G. **Formal proof status and gaps.** The Lean theorem is externally verified by several kernel implementations, but the 265-page human-readable guide only derives the key inequality (M) from H0-H12 and does not prove these thirteen in that guide. The most valuable target for independent mathematical understanding is H12: existence at EVERY scale x inside arbitrarily late long intervals, with uniform constants and auxiliary primes simultaneously satisfying B/C. Earlier fallbacks 07:41 traced the actual Lean source construction of q,d and the existence of an arithmetic field, preventing vacuous-quantifier objections at that junction. Do NOT repeat them without a new issue.

## Scripts and exact reports

- `/mnt/data/riemann_20261123_0751/mellin_scaling_audit.py` SHA256 397905e96276a35a70e1e7f20fbf1d9aaac5595ac9d3e339dae158c8342061c7, JSON sha256 6d357b1ce42449820252f2aa118d6afd0ab481a1616041577a6333cade97f14b.
- `/mnt/data/riemann_20261123_0751/xi_zero_sum_audit.py` SHA256 ad5079d6af48636ca6a310a271e8768e1435f9669256c64a41c74385b4f23adc, JSON sha256 55e1547d52cd648b84960b2f06a8ccd501d9b4ba6fa3546ac4f284d199f747df.
- `/mnt/data/riemann_20261123_0751/prime_ramp_stieltjes_audit.py` SHA256 10575f54190f9f7a4a06bd1545d633b9c3dd18b887ec5a992083419d012051c2, JSON sha256 7ff367dae6263a19f88c0dfb0d24c569b0492afce381d751c2d1beae4a1da2c8.
All three final scripts ran to PASS; no code run on user's Linux.

## Next distinct experiments

1. Study the precise simultaneous-uniformity contract H12 in Rubinstein III.11 versus Lean VWinAt/WinPairs/supplyOfAdmOf, focusing on dependence of parameters m,k,n, epsilon, q,d and the field E on x. Audit whether a change of scale and choice of constants are mathematically uniform across a whole power interval, without assuming it from a finite sample. Earlier checkpoints already confirmed existence at selected calls, so do not claim an empty family.
2. Inspect the quote/reference of Galois-cohomology comparison bound in H6/H7 and audit the O(m) versus O(m^2) normalized error, which is the exact source of exponent 1/2 instead of 2/3.
3. Look for an independently checkable, nontrivial small lemma concerning theta lift norm/covolume and character conjugation, together with a falsifying numerical or symbolic test.


**Status:** no new proof or disproof of RH from this run. External verified Lean theorem is reported as a major independent result; this research only independently audited small analytic/algebraic bridges and tracked remaining human exposition gaps.
