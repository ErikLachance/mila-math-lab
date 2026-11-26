# Riemann Proof Watch — append-only continuation, 2026-11-23 09:29:46 EST, America/New_York

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0930_EST.md`. **Recorded time label:** 2026-11-23 09:30 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity

This checkpoint supplements `RIEMANN_CHECKPOINT_2026-11-23_0919_EST.md` and its companion code archive.

Earlier Riemann checkpoint: November 8, 2026, 15:30:58 EST, Weil collar partial positivity L=.81. No proof of RH was produced here.

### Sources actually inspected this continuation

Rubinstein et al, *The Alpöge-Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, v2, 22 Nov 2026, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf. Examined rendered PDF pages 61, 136, and extracted sections II.4.1–4.3, III.1 pp.63–65, III.8 pp.139–144, III.11 pp.197–200 (Google/web PDF screenshot used for visual scrutiny). The human guide still explicitly treats the main inequality (M) and hypotheses H0–H12 as unproved IN THE GUIDE, but external Lean/Mathlib/MIT formal verifiers independently certified the core theorem. This run did not compile 175,187 Lean modules itself. Supplementary mathematical background sought on finite frame erasures and Welch bounds; no novelty priority claimed for the frame lemma.

## Pass E — sharpened TRACE-AND-KERNEL inequality; mathematically proven from spectral moments

The prior 09:19 checkpoint gave an uncentered inequality t-sqrt(eta*t)≤delta and a rank ratio bound. A **strictly sharper** result follows by centering the kernel projection. For any positive-semidefinite Hermitian D×D matrices 0≤Q'≤Q with trQ>0, define μ=trQ/D, η=tr(Q²)/(Dμ²)−1≥0, γ=tr(Q−Q')/trQ∈[0,1], and t=dim ker(Q')/D. Let P denote the orthogonal projector onto ker(Q'). Then tr(P Q')=0, so tr(PQ)=tr(P(Q−Q'))≤γ μD. Since tr(Q−μI)=0, use the **centered** Hilbert–Schmidt Cauchy bound

tr(PQ)=μ k+tr((P−tI)(Q−μI))≥μD[t−sqrt(η*t*(1−t))],

because ||P−tI||_HS²=D t(1−t), ||Q−μI||_HS²=Dμ²η. Thus

` t − sqrt(eta*t*(1−t)) ≤ gamma `.

For any known γ≤δ<1, solving the quadratic (the t≤δ case is automatically covered), one has the exact universal bound

` t ≤ [2 δ + η + sqrt(η² + 4 η δ (1−δ))] / [2 (1+η)] `.

This is at least as strong as the earlier second-moment rank bound `t≤1−(1−δ)²/(1+η)` for all η≥0, δ∈[0,1]; subtract numerators and use `sqrt(η²+4ηδ(1−δ)) ≤ η+2δ(1−δ)`. It also sharpens the uncentered Cauchy bound. In terms of source frame operators B_i and deleted domain projectors, `δ=(α+sqrt(αe))/(1−sqrt(e))` if e<1 and δ<1, as proved in the preceding checkpoint. In particular **if no directions are discarded (α=0), e disappears from the rank estimate** and `t≤η/(1+η)`. This removes an unnecessary 4√e term in the source's coarse dimension-loss inequality in that regime; it does NOT prove the arithmetic trace estimate that yields η.

SHARPNESS *for the abstract trace constraints*: exact rational D=4 toy Q=diag(1/2,1/2,3/2,3/2), Q'=diag(0,0,3/2,3/2), µ=1, η=1/4, γ=1/4, t=1/2; right side equals 1/2 exactly. This is optimal for those abstract two moments, not necessarily jointly optimal for fixed B_i and e,α.

Executed `frame_sharp_kernel_bound.py` SHA256 to be recorded in script ZIP: 3,500 seeded random complex frames, 3,019 δ<1 cases; all t≤bound, and stronger than previous ratio bound in 2,934 informative cases. Exact rational tight example checked with Sympy. Additional arithmetic comparison using Rubinstein III.8 Corollary T2: η=5κ, e0≤κ²/4, α=αram+α'; let δ as above; projected target E has dimension (1−δp)D, so the codimension bound becomes at most `D * sharp(δ,η)` rather than paper's `D*(5κ+4α+4sqrt(e0))`, and in E the relative error divided by (1−δp). Numerical 20-case mpmath 75-digit sweep found formal reductions, but the bound is only an alternative finite-dimensional deduction, still fully conditional on sources' S,I,P, H8 and all arithmetic constructions; no RH progress claimed. `frame_sharp_T2_comparison.py` PASS.

## Pass F — reciprocity reduction, with exact countermodels for missing conditions

Rubinstein III.1 Step 2 uses q>nn' and m0 divisible by 8 to turn `(nn'/q)` into a fixed sign times the Jacobi `(q/s)`, where s is the product of prime factors outside m0 with odd exponent. Independent finite check `quadratic_reciprocity_progression.py` enumerated 132 reduced residue progressions modulo m0=8,24,40,56,120,168, and **42,768** prime-power pairs, **171,072** exact Legendre/Jacobi checks at primes q∈[2000,20000], all PASS. This is a test of quadratic reciprocity, not prime equidistribution/cancellation.

Exact countermodels show hypotheses are substantive: take m0=3, residue a0=1, n=3,n'=4, q=13 and19. Both q≡1 mod3 and exceed nn'=12, but `(12/13)=+1`, `(12/19)=−1`, while s=1, so no single sign works when `8|m0` is dropped. If q divides nn' (e.g. q=7,n=7,n'=2), Legendre is zero, so the fixed sign ±1 simplification is invalid; source q>nn' prevents it. Script `reciprocity_assumption_countermodels.py` exact PASS. Does not falsify theorem with correct assumptions.

## Pass G — exact rational audit of the scaling from unnormalized (III.309) to (M)

Source (III.308): B=|T| m b δ/2, δ=|T2|/n, a=xb, unnormalized error bracket E=|T|a(1+m²/k)+m[2nmb x^ε + |T2| k b x^{2ε}/n²]. With δ≥x^{−ε}, |T|/n≥(1/2)x^{−ε/8}, divide by B: first two costs <=2x^ε(x/m+xm/k); third ≤8m x^{17ε/8}; fourth ≤4(k/n²)x^{17ε/8}. Thus total ≤8x^{17ε/8}(x/m+xm/k+m+k/n²). The exponent **17/8** comes specifically from the B0 term and is sharp within those two density hypotheses.

Script `main_M_normalization_audit.py` uses Fraction **exact arithmetic**, 180 tuples with x^ε=t⁸, |T|/n=1/(2t), δ=1/t⁸ at the endpoints, all bounds PASS, maximum ratio ~0.996244. If |T|/n or δ bound is removed, explicit positive-integer counterexamples violate the normalized inequality. This is an **algebraic conditional step only**; does not establish the unnormalized arithmetic (III.309), support existence or RH.

## Pass H — independent reconstruction of the guide's prime-power cell table

Rubinstein II.4.2 uses **pedagogical**, deliberately nonadmissible q=11,d=1319,N=16,H={±1,±3,±5,±7}, a=10000, cutoff 200000, one weight 10 in row v=1 at translate u, and seven weights 0.05. Independently enumerated 18,098 eligible odd prime powers up to 200000 (excluding q=11), 9,007 with nonzero coefficient `(1−χ_1319(p^j)) log p`, and computed all four translated sums with 40-digit mpmath arithmetic:
P_[1]=84701.03168516253329787894...
P_[3]=84163.13718206608612060346...
P_[5]=84286.66282418900570282389...
P_[7]=84692.52717197116849033608...

To avoid **copying the paper's** L'/L value, evaluated `L'/L(1,χ_1319)` independently via the functional equation of the *odd primitive quadratic* Dirichlet character (root number +1), Hurwitz ζ(0,a/d) and ζ'(0,a/d): `L(0,χ)=−(1/d) Σ aχ(a)=45`, and
` L'/L(1,χ) = γ_E + log(2π) − (1/L(0,χ)) Σ_{a=1}^{d−1} χ(a) logΓ(a/d) `.
Computed 60 digits and paired reflection of Γ terms independently; result `−1.52022788751629681496918779895...`, agreeing with the guide's rounded −1.520227887516. With this *independent* value, center M=84463.394222938394692498376269897..., resulting four P_u−M:
[1] 237.63746222413860538...
[3] −300.25704087230857189...
[5] −176.73139874938898967...
[7] 229.13294903277379784...
mean −2.55450709119628958..., **ALL match the four rounded values** in printed II.4.3.

Scripts `prime_cell_table_reconstruction.py`, `dirichlet_logderivative_gamma.py`, `prime_table_full_independent_constant.py`, reports PASS. **Small textual correction only**: guide §II.4.1 prose says `v=(1+χ_q)/2` equals 1 for a **nonsquare**, but by definition the formula gives 1 for a *square* (χ_q=+1), and the article's own p=23 row-1 table uses the formula correctly. This is a prose typo, NOT contradiction of the calculations or a Lean gap. The source explicitly says q=11,d=1319 do not meet asymptotic construction requirements; reproducing this finite toy is not a proof of (M).

## Limitations, approaches not to repeat, next experiment

This run has not supplied the enormous arithmetic/geometric theta-kernel size, Galois-cohomology, or trace-formula estimates, nor the simultaneous (H12) data at arbitrarily late power windows. Source human exposition is still conditional, while the independent Lean/Mathlib/MIT theorem was externally verified. No complete original RH proof or disproof produced here. No novelty priority claimed for elementary finite-rank/prime-sum lemmas. Do not extrapolate mathematical proof from random floats, toy small primes, a formal kernel's verification of someone else's code, or the collar-supported Weil-form positivity.

Next: inspect a **different core input** (III.9 Galois cohomology) for a precise independently provable finite group/cohomology transfer lemma or show with exact finite counterexamples why the O(m) rather than O(m²) denominator control is essential. Alternative distinct angle: inspect the logical uniform-quantifier order in H12 and the full prime/field construction to avoid circular source assumptions.

**Research status: no RH proof by this run.**
