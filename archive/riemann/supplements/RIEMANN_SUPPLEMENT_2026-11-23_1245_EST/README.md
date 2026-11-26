# Riemann Proof Watch — third append-only supplemental checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1245_EST.md`. **Recorded time label:** 2026-11-23 12:45 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## New distinct pass 1 — complete ramified-prime classification for the q,d selector

Source: Michael O. Rubinstein et al., *The Alpöge–Claude proof of RH explained for the Riemann zeta function*, **working v2 Nov22 2026**, equations (II.7)–(II.10), printed page 33, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf . For distinct odd primes q≡3 (mod 8), d≡7 (mod 16) with q|(d+1), reciprocity gives (d/q)=−1, (q/d)=+1. Thus for **every x**, the exact expansion of

`S_qd(x) = sum_{p^k<=x} log(p) (1+(p^k/q))(1-(p^k/d)) (x/p^k-1)`

is

`4 * sum_{p!=q,d ; (p/q)=1, (p/d)=-1} sum_{k odd >=1} log(p)*(x/p^k-1)_+ + 2*log(d)*sum_{j>=1}(x/d^(2j)-1)_+.`

All q-power terms vanish; d-powers contribute only for **even** exponent k, with multiplier 2. This is the exact boundary correction to the common shorthand "only split/inert odd powers". Verified **ten** x values for (q,d)=(3,23) and (11,1319), evaluating all integer coefficients of `log(p)` as **exact Fractions**, including x530 where d²=529 gives exact d coefficient `2/529`. Initial regression falsely failed comparing dictionaries containing explicit zero keys; corrected comparison to nonzero coefficients, all tests PASS. This is finite elementary arithmetic, not (M) nor RH.

## New distinct pass 2 — exact finite character-tail identity and growth in conductor

From printed page 33 of same v2, for nonprincipal primitive chi, `c_chi = L'(1,chi)/L(1,chi)`, `Psi_chi(t)=sum_{n<=t} Lambda(n)chi(n)`, `G_chi(x)=sum_{n<=x}Lambda(n)chi(n)(x/n-1)+c_chi*x`. For any real `T>x>=1`, **without any infinite-limit assumption**,

`G_chi(x) + x*integral_x^T Psi_chi(t)/t² dt = x*( c_chi + sum_{n<=T}Lambda(n)chi(n)/n - Psi_chi(T)/T ).`

Derived by exact partial summation for the finite step function. Sending T→∞ to obtain source equation (II.10) requires the prime number theorem for fixed nonprincipal chi and, critically, quantitative bounds **uniform in a chi whose conductor grows with x**. Fixed-character PNT does not imply source Estimate B for q,d exploding with x. Numeric check used χ4, `c_chi≈0.24560958476625327`, mpmath 65-digit L-function derivative, T=1000/10000/30000/100000 and x=10/50/200: all **12** finite identities PASS to 55 decimal digits. Residual at x200,T100000≈0.0361563561 is **not** a certified tail bound. Numerical convergence no RH claim.

## New distinct pass 3 — Theorem III.1.1 size quantifiers remove ramified correction in actual application

Actually read working v2 Theorem III.1.1(a)-(d), printed p61, page screenshot visually checked. It states for fixed epsilon∈(0,1/52), fixed A≥1, large Y: `log q > Y^(epsilon/5)/2` and `log d > Y^(epsilon/5)*(log Y)^2/2`, and x∈[Y,Y^A]. Since `Y^(epsilon/5)/log Y →∞`, **eventually q,d > Y^A >= x**, so no ramified prime powers (including p=d²) occur in the actual large-Y argument. The exact correction from pass 1 is real for toy small primes but asymptotically absent, so no mismatch with published proof. **Quantifier essential:** A must be chosen before Y, not allowed to grow arbitrarily with Y. As a finite exact rational illustration with epsilon=1/100,A=10, logY=6000, the Taylor lower sum through degree14 certifies exp(12)>120000, so 0.5*Y^(epsilon/5)>10logY and hence q>Y^10. Script `auxiliary_scale_and_split.py/.json`. This is a source-fidelity clarification, not new bounds for existence of q,d.

## New distinct pass 4 — Thorner/Zaman original Corollary 1.4 verified and a local printed partial-summation typo uncovered

Inspected original authors' arXiv:2108.10878v2 from Sep 21 2021, both HTML and PDF, and screenshot of **PDF p3** (`https://arxiv.org/pdf/2108.10878` and `https://arxiv.org/html/2108.10878`), *Refinements to the prime number theorem for arithmetic progressions*, Thorner & Zaman. **Corollary 1.4** does indeed require `t>=m^12` and gives exactly the two relative error terms displayed as working-guide `(Q2)`, with main `lambda*t/phi(m)`, including a potential exceptional real zero. As `lambda=1-chi_1(b)t^(beta-1)/beta`, this equals guide `Lambda_b(t)=[t-chi_1(b)t^beta/beta]/phi(m)`. Thus core external theorem quote matches **the original source** including important exceptional-zero contribution, and does NOT assume GRH.

However the *human-readable guide's* text extraction of proof for its (III.6), printed page **63**, gives the partial summation identity

`pi*(U)=theta(U)/logU - theta(sqrtU)/logU + integral_sqrtU^U theta(t)/(t log²t) dt`.

**The correct exact identity** has denominator `log(sqrtU)` for the subtracted endpoint; the right side as printed exceeds the correct value by `theta(sqrtU)/logU`. Exact synthetic log-domain weighted jumps at t=e and e³ with multiplicities 5,7, U=e⁴ give TRUE count7, correct RHS7, **printed RHS33/4**, discrepancy5/4. Independent actual primes p≡1(mod5), U=1,000,000, sqrtU1000: true count19577, correct RHS19577, printed RHS19593.729654537985..., discrepancy 16.729654537985... = theta(1000)/log1e6. Script `partial_summation_endpoint_audit.py/.json` computes high-precision actual weighted step integral. **This is likely a local typographical slip in unfinished explanatory guide, NOT an issue with formally checked Lean code and NOT a counterexample to Theorem (III.6)**: next prose uses error budget factors `(1+2+2)`, as if the correct `/log sqrtU` were already used. Needed one-symbol correction is `theta(sqrtU)/log(sqrtU)`. IMPORTANT LIMITATION: web PDF text and math extraction read, but direct PDF page-63 screenshot returned **cache-miss errors twice**, so a final visual/typeset confirmation of exactly what the PDF displays is still pending before notifying any author as an erratum. The true algebra and numeric counterexample are independent of screenshot. We did not run or audit 17M Lean proof lines.

## Files, status, next

New executed scripts and JSONs:
- `ramified_selector_and_twisted_tail.py/.json` — 10 exact selector tests; 12 high-precision twist finite identities
- `auxiliary_scale_and_split.py/.json` — exact rational Taylor bound, source quantifier check
- `partial_summation_endpoint_audit.py/.json` — exact synthetic and independent real-prime partial-summation counterexample

No result here independently proves RH, disproves RH, or challenges full formal Lean proof. Proposed next distinct high-value test: inspect direct rendered printed page 63 once accessible; if typo confirmed, construct a source-grounded short erratum but do not send without user authorization; check whether corrected boundary is already incorporated in subsequent `k` error bound (1+2+2). Then independently audit the character-averaging Step3 mesh (distinct from prior H12 scalar finite mesh), especially continuity in y and dyadic dyad density selection with growing q,d.
