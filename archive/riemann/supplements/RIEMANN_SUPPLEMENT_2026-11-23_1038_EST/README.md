# Riemann Proof Watch — append-only secondary mathematical checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1038_EST.md`. **Recorded time label:** 2026-11-23 10:38 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Additional distinct micro-pass G — integer-only exact mesh certificate

The core math from earlier in this run remains: for positive von Mangoldt hinge sum S and G(x)=S(x)-xlogx+(1+γ)x, convexity of S implies one-sided interpolation error D<=h²/(8a). Adaptive node gaps h<=sqrt(8*a^(1+θ)) suffice to transfer node-wise G<=C x^θ to *every* point of [Y,Y^1.5] with coefficient C+1.

For **rational** θ=p/q (1/2<θ<1), choose Y=m², upper endpoint m³, so BOTH window endpoints and ALL interior nodes can be INTEGERS. At each integer a choose the largest integer h satisfying the **EXACT BIG-INTEGER inequality** `h^(2q) <= 8^q * a^(p+q)`; advance to min(m³,a+h). This proves every segment's curvature budget using integer arithmetic alone, no floating rounding and no assumption RH. Independent script test:
- m10, θ3/5: 4 integer intervals, 2,000 sampled real evaluations of G all pass one-sided envelope.
- m30, θ11/20: 10 intervals, 5,000 float sample checks pass.
- m60, θ13/25: 20 intervals, 10,000 checks pass.
- m1000, θ3/5: 87 exact-big-integer intervals to 1e9, prime-sum evaluation intentionally NOT attempted.
All mesh inequalities and maximal h checks exactly confirmed; floating evaluations are mere diagnostics.

## Additional distinct micro-pass H — genuinely independent source G cross-check

Recomputed source's four smoothed prime-power numerical values in Rubinstein Part I.1 using **sympy.primerange** and independently generated all prime powers p^j<=2,000,000, plus mpmath 65-digit accumulation of sum Λ(n)/n and sum Λ(n), not earlier float sieve. Source's printed numbers and independently calculated values:
- G(10000) = **1.749315244618375832977384957858...** vs printed 1.749.
- G(100000) = **3.671461861506784807545832799302...** vs printed 3.671.
- G(1000000) = **11.04043612700127862801409622949...** vs printed 11.040.
- G(2000000) = **-12.267800731448220058323191380718...** vs printed -12.268.
All exactly round to printed 3 decimals. Counts of powers included: 1280, 9700, 78734, 149235, respectively. This independently validates the arithmetic normalization/constant/smoothing in current scripts, NOT the needed x-uniform bounds.

## Additional distinct micro-pass I — countable RH-equivalent integer mesh

Define θ_j=1/2+1/j=(j+2)/(2j), j=3,4,... . For each integer m>=2, build the above grid on [m²,m³], using the purely integer test `h^(4j) <= 8^(2j)*a^(3j+2)`. Exact independent geometry test passed:
- j3,m30: 4 steps;
- j4,m100: 9 steps;
- j10,m1000: 87 steps;
- j100,m1000: 192 steps;
- j100,m10000: 1,129 steps to 10^12, with no large prime computation.
For each fixed j, the number of nodes is O(m^(3(1−θ_j)/2)). **Mathematically proved conditional equivalence** (assuming the published Landau interval criterion): RH is equivalent to the assertion that FOR EVERY j>=3 there exist a constant C_j independent of m and arbitrarily large integers m with `G(n)<=C_j*n^θ_j` at every integer node of this deterministic grid. RH => node bound from source explicit formula G=O(sqrt x). Conversely the semiconvex lemma gives G(x)<=(C_j+1)x^θ_j across [m²,m³]; for an arbitrary τ>1/2 choose j with θ_j<τ, and m so large `(C_j+1)*(m²)^(θ_j−τ)<=1`. Therefore on those whole windows G(x)<=x^τ and the SOURCE's original coefficient-one Landau interval theorem applies with NO extension to arbitrary coefficients. Taking all τ↓1/2 and zeta symmetry yields RH. This is only a restatement of the STILL UNSOLVED arithmetic inequalities, not a proof. It significantly reduces a continuum of x and a continuum of θ to integer nodes and countably many rational θ, without generating bounds.

## Additional primary-source adversarial audit — one-sided interval lemma

Actually READ and visually SCREENSHOT the 1986 original J. Kaczorowski and J. Pintz, *Oscillatory properties of arithmetical functions I*, Acta Math. Hungar. 48, pp.173–185, https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf (Theorem 1 p.175). Its assumptions (1) boundary of meromorphic continuation, (2) isolated singularities with strip continuation, (3) logarithmic-plus-meromorphic local form are all compatible with the Mellin transform F(s) from Rubinstein I.3 when use f=G−2x^θ, with P_n=0 in its condition (3), choose strip away from pole at θ, and use zero-free real 0<s<1 (and cancellation at s=1). Its conclusion (2.2) says EVERY [T^(1−α),T] for large T has sign change, with positive oscillation; choosing T=Y^1.5 and α=1/4 gives [Y^(9/8),Y^1.5] subset [Y,Y^1.5], contradiction if f<0 there. Source Rubinstein v2 p.7 explicitly notes requirement that boundary ordinate gamma be POSITIVE or +∞ (not the gamma=0 case). For zeta, no real zero in (0,1), and discrete nontrivial zeros ensure any boundary ordinate is nonzero, so this condition is appropriately satisfied. This verifies a previously uninspected classical external input; it is not a new proof of Kaczorowski-Pintz itself, which remains a published theorem. A different approach would need its full proof.

Other primary sources reread: Rubinstein et al working v2 Nov22 2026 https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf , especially pp. 6–7 and its Section II.4.1 statement that the (M)→Estimate A/B/C→G(x) deduction works **one x at a time**, with pair q,d allowed to vary with x. Lean/Mathlib Nov21 verified certificate https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ ; MIT Andrew Sutherland live verification https://math.mit.edu/~drew/grh/ (last checked 2026-11-23 14:35 UTC). We did NOT personally compile 17M-line Lean proof.

## Proposed H12_grid hypothesis — distinct weakened target (not established)

The human guide's original H12 says admissible auxiliary arithmetic/geometric data with H0–H11 and uniform constants exist at every **real x** throughout arbitrarily late long intervals. Since its Sections II.4–5 derive the final scalar G(x) bound for ONE x at a time and q,d may depend on x, one can IN PRINCIPLE replace the continuum of required x by the above deterministic integer nodes, provided estimates A/B/C and (M) are all established at every node with **the same ε-dependent constants independent of node and m**. Combine their pointwise scalar bound with semiconvexity to recover the source Landau interval criterion. This weaker H12_grid is a mathematically valid SUFFICIENT TARGET, not verified that the actual theta-lift machinery can satisfy it. Do NOT assume finite sample data at some m yields uniform bounds at arbitrarily large m; do not claim a new full proof. High-value next experiment: trace and quantify which deep H0–H11 source inputs would be weakened by node-only data and which already have uniform-in-x conditions from external estimates.

Independent numerical constant cross-check: source under RH obtains coefficient `2+gamma−log(4pi)` = 0.04619141793224206762862049...; verified using mpmath 80 decimal digits. This is not used as an unconditional bound, since it is deduced under RH.

## Companion source and checksums

`RIEMANN_SUPPLEMENT_SCRIPTS_2026-11-23_1038_EST.zip` ZIP SHA256 `620b389002048fd2473ec98e4be88f1abf5bfdb63440c95a65c09ecbe74444f0`. Contains 3 standalone scripts with JSON reports:
- `riemann_h12_integer_grid.py` SHA256 `c6c619a7016e0fd6c2b5f454f115df54b228272a897c3f6181a282e71fc8b797`
- `riemann_h12_integer_grid.json` SHA256 `9dce2e2db726ed2497aca1f55610097bb86d92c5ba1a796c3845205b4f9640cf`
- `riemann_h12_independent_source_regression.py` SHA256 `17383b0ca93297a3536f8b5ea306d9dbf7028565de4b10abc7cbdcbd8da3ce5d`
- `riemann_h12_independent_source_regression.json` SHA256 `70cba23a3a7ed96f7c086776a5ba590f91d4b63ee3fc946b53c1e4467704432a`
- `riemann_h12_countable_criterion.py` SHA256 `bc2dc4897e354c6d75c83bceaca1eb1cd6d08d58d4520b7c35a200370aa55d53`
- `riemann_h12_countable_criterion.json` SHA256 `04ce5268ed34ab3b2e0246c187d43ff1ae7f63b81aa805c20ce4a021e0c39a04`

**Limitations:** Human Rubinstein guide still conditional on H0–H12/(M) (not all proved within that guide), while independently audited formal Lean proof is a separate result. The discrete criterion is a characterization, not a proof of RH. None of these finite tests or arithmetic source checks establishes required uniform bounds, spectral positivity, or directly validates Alpöge's 17M lines.
