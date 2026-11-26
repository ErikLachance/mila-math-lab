# RIEMANN RECHERCHE — checkpoint intermédiaire append-only — 2026-11-23 15:18 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1518_EST.md`. **Recorded time label:** 2026-11-23 15:18 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Sources directly consulted
- Alpöge original Nov20 note `https://alpo.ge/remark.pdf`, Stepanov method and ~sqrt(X) theta-lift chain, read original PDF and page images.
- Andrew Sutherland MIT independent formal verification status last updated Nov23 14:35 UTC `https://math.mit.edu/~drew/grh/`: all 175187 Lean modules compile; kernels and independent comparator passes succeed; long additional checks remain running. Lean FRO and Mathlib Nov21 community certification `https://leanprover-community.github.io/blog/posts/riemann-hypothesis/`. None of those 17 million source lines was locally recompiled during this run.
- Michael Rubinstein Waterloo human guide v2 Nov22, 265 pages, `https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf`, pages 6 (0-index5) formula (I.3) and (I.4) visually checked; page 224 lemma for lemniscate sine. Human guide does not complete proof of (M), expressly cites 13 hypotheses still needing mathematical reconstruction; this does NOT contradict formal Lean certification.
- Clay status `https://www.claymath.org/millennium/riemann-hypothesis/`: institutional prize listing not yet accepted.
- Re-read independent working manuscript through GitHub connector repo `jimjamzola/RH-Alpoge-Reconstruction`, `manuscript/sec16_local.tex` around Lemma `r5:lem:primesizes` and `manuscript/sec12_loss.tex` around Proposition `r2:star`; this is an independent *incomplete reconstruction*, NOT the formal source proving RH and should not be used to claim a Lean defect.

## New pass E — exact high-n regression of existing lemniscate-sine source theorem
Starting from `y''=-2y^3`, y(0)=0,y'(0)=1, rational coefficient recursion of earlier pass, computed k=486, n=1945 with exact integer arithmetic, after remedying the Python integer-print 4300-digit safety limit. `A_1945` has 5034 decimal digits. Exact v_3(A_1945)=734 and floor(1945*3/8)=729, hence excess =734−1945*3/8=4.625 EXACTLY; v_7=283 and floor(1945*7/48)=283. This duplicates/passes the published numerical example, not a novel claim. `lemniscate_long.py/.json` code measured 21.87s. Initial attempt raised a `ValueError` while converting a >4300-digit integer to decimal; was rerun after `sys.set_int_max_str_digits(100000)`. No numerical result relied on the failing attempt.

## New pass F — independent Mellin-transform regression, including constants and prime powers
For x>=1 put `G(x)=sum_{n<=x} Lambda(n)(x/n−1) − x log x+(1+gamma)x`, zero at n=x terms harmless. For Re s>1, termwise integration yields
`F(s)=int_1^infty G(x)x^{-s-1}dx=−(zeta'/zeta)(s)/[s(s−1)]−1/(s−1)^2+(1+gamma)/(s−1)`.
Using `zeta(1+h)=1/h+gamma−gamma_1 h+O(h²)` (standard signed first Stieltjes convention), Laurent cancellation gives a *finite* `F(1)=1+gamma+gamma²+2 gamma_1`, numerically 1.764761897741898..., confirmed by high-precision direct evaluation for h=10^{-5} through 10^{-30}. `mellin_laurent_primes.py/.json` enumerated 149235 prime powers up to 2e6; two independent finite forms for G gave x=10000 1.749315..., x=100000 3.671461..., x=1e6 11.040436..., x=2e6 −12.267800..., matching visually inspected Waterloo examples to their quoted 3-decimal precision. Prime powers were included; primes-only shortcut is NOT equivalent. This is reproducibility of classic explicit formula, NOT independent RH proof.

## New pass G — Landau sparse interval parameters; only a local sufficient constant audit
Waterloo guide page31 establishes one-sided Mellin criterion from `G(x)<=x^theta` on arbitrarily large whole intervals `[Y,Y^{3/2}]`, not just along sparse sampled x. For the given gamma concentration window, with eta=max(0.8 e^{.2},1.2 e^{−.2})=0.982476903693..., `log((1+eta)/(2eta))=0.008878287...>0.008`. With sigma=252, theta=.8, eta*(sigma−theta)/(sigma−2)=0.98719<1. Gamma-window outside mass bounds decrease in actual numeric examples U=5..80 from ~5.48e−14 to ~1.73e−194. Source formulas were inspected with PDF screenshots. These numerical inequalities test arithmetic constants but do not prove existence of the required long intervals, nor full contour continuation, nor inequality (M). Script `landau_interval_audit.py/.json`.

## New pass H — exact trivial-zero correction to the explicit formula
Nontrivial zero rho of zeta contributes residue `−1/[rho(rho−1)]` to F, while trivial zero at s=−2k contributes `−1/[2k(2k+1)]`, so its inverse Mellin contribution for x>1 is `−T(x)`, where
`T(x)=sum_{k>=1}x^{−2k}/[2k(2k+1)] = 1−1/2*log(1−x^{−2})−x*atanh(1/x)`.
Elementary absolutely convergent series proves `x^{−2}/6 <= T(x) <= x^{−2}/[6(1−x^{−2})]` for x>1. The pole at s=0 contributes `log(2pi)` because zeta'(0)/zeta(0)=log(2pi). Thus, given the standard justified contour shift, source `G(x)=log(2pi)−sum_rho x^rho/[rho(rho−1)]+O(x^{−2})` refines to an exact known trivial-zero term `−T(x)` (at x>1). A 350-term high-precision sum matches the closed form for x=1.5,2,3,10,100,10000 to ~1e−90; code `trivial_zero_tail.py/.json`. The contour shift and zero-sum arrangement are standard analytic inputs not independently re-proved here. No new RH theorem.

## New pass I — zero-sum truncation and EXACT conditional tail envelope
Under RH, write rho=1/2±i gamma, so `−sum_rho x^rho/[rho(rho−1)] = 2 sqrt(x)*sum_{gamma>0}cos(gamma log x)/(.25+gamma²)`. Standard Hadamard `xi` factorization yields the exact weight identity
`C := sum_rho 1/[rho(1−rho)]=2+EulerGamma−log(4pi)=0.0461914179322420676...`.
For the FIRST K positive ordinates (provided they are individually correct and no earlier zeros omitted), the absolute tail is bounded by
`|tail_K(x)| <= sqrt(x)*( C−2*sum_{j<=K}1/(.25+gamma_j²) )`.
This bound requires RH for positivity of all weights; other zeros or uncertified zero enumeration require caution. At K=100 `C_K≈0.0399697048078476106`, tail weight `C−C_K≈0.006221713124394457`. Using mpmath's **uncertified** first 100 ordinates, and full exact finite-prime G at x=2,3,10,100,1000,10000, all 6 observed reconstruction errors lie inside this calculated tail bound; e.g. x10000 |error|≈.0326567 vs bound≈.622171. This is falsification only, NOT certified zeros or independent RH verification. Scripts `explicit_formula_zeros.py/.json` (first 200 ordinates, 27.6s, error x10000 ~.00119883); `explicit_formula_tail_envelope.py/.json` (100 ordinates, 12.3s) and the prior 20 and 100 passes. Initial attempt for N=250 at precision55 timed out after requested execution window; a separate N=200 envelope timed out at 75s, so those runs did NOT produce certificates. N=100 rerun passed. Do not mistake small numerical errors for proof.

## New pass J — quantitative conductor scale: asymptotics can start astronomically late
In independent sec16 local manuscript, admissible conductor bound is `log d <= x^(epsilon/5)*(log x)^2`; `log X'=x^(epsilon/3)` for `X'=exp(x^(epsilon/3))`. Put t=log x. Sufficient for the comparison `log X' > log d` is `exp((2epsilon/15)t)>t²`. The large positive boundary t values are approximately 31027.929 for epsilon .005, 14358.105 for .01 and 7427.448 for .018. Corresponding x scales exceed 10^13475, 10^6236 and 10^3226. These are thresholds of this **sufficient bound**, not a falsification of the asymptotic theorem nor proof that no better argument applies earlier. Script `conductor_asymptotic_threshold.py/.json` tracks the two logarithmic scales without constructing physically enormous x.

## Unresolved, rejected shortcuts, next distinct work
- No proof independently created: Lehmann/Weil earlier finite-support mixed blocks unresolved, (M) and H0-H12 not completely established in public *human-readable* drafts; this does not undermine independently kernel-checked Lean.
- Failed/invalid shortcuts: mpmath finite-zero comparisons are not proof; finite check of lemniscate coefficients does not prove all n; naive split-prime valuation bound definitely false; primes-only shortcut ignores powers; uniformity in expanding conductor cannot be inferred from fixed-conductor PNT; a missing local arithmetic cell condition must not be claimed to be a Lean contradiction.
- Next: independently audit the quantitative `N_m² X'' log a <= b` inequality in the sec16 scale, taking logarithms to avoid underflow, including exactly which inputs are presumed by `admissible data`; test whether source claims uniform constants in epsilon incorrectly or merely thresholds dependent epsilon. Then investigate finite exact source-level statement about period gamma or a separate named published automorphic theorem with reference provenance, instead of repeating same examples. Check MIT latest at later runs.

