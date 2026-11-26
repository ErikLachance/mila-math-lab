# Riemann research fallback checkpoint - 2026-11-23 04:58:22 EST (America/Toronto)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0458_EST.md`. **Recorded time label:** 2026-11-23 04:58 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


## Prior checkpoint actually read

Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST, `W12 RATIONAL SUPPORT CERTIFICATE` at L=81/100, two terminal collars of width w=1/12. The checkpoint asserts complete signed Weil form Q(f)>0.001||f||^2 for *arbitrary smooth complex f supported only on those collars*, via 256*192 exact rational p/q even bins checked in four segments and 2048 odd bins, with numerical Galerkin cross-check; not global L=0.81 positivity. Previous 2026-11-08 results included conditional index of negative spectrum <=14 at L=0.81 (different assertion), finite 16-mode Fourier matrices, and unconstrained interfacial coupling that blocks the full-window result. Reported scripts were not independently rerun in this new 2026-11-23 session. Prior full-interval independent Zhu-certified result at L=0.8 has margin 8.9e-18. Never equate restricted support, finite codimension or finite Galerkin positivity with the Riemann hypothesis.

## Primary sources directly opened in this run

1. Xuefeng Zhu, `Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau-Widom decay law`, arXiv:2608.24827v2, https://arxiv.org/html/2608.24827v2 : explicit formula (2)-(3), Lemma 3.1 H(t)>=ln(t/(2pi))-1/t for t>=15/4, support 0.8 certified theorem, odd/even pole sign, and retraction of earlier 1.19 positivity claim.
2. Masatoshi Suzuki, `Weil's quadratic form via the screw function`, NEW v4 published 2026-11-15 (previous journal only v3), https://arxiv.org/html/2606.09096v4 : Weil W functional and its signed pole terms, closed form domain H^log, compact embedding, and Theorem 1.3: a -> lowest eigenvalue lambda_a is continuous, unconditionally.
3. External non-peer-reviewed claim of certification L=1.19 at https://zeta.teal-sea.com/read/hunts/oob_envelope/numerics/RESULTS.html , compiled 2026-11-15. It claims two internal referee routes, explicitly pending external verification; this is NOT adopted as a theorem or independent verified outcome, especially given Zhu's retraction of an earlier flawed L=1.19 claim.

## New independent analytic micro-pass - simple narrow-collar positivity

Let L=81/100 and w=1/40, and let E=(-L,-L+w) union (L-w,L)=(-0.81,-0.785) union (0.785,0.81). For EVERY complex C_c^infinity function supported in E, the complete Weil quadratic form satisfies the elementary uniform inequality

   Q(f) > (9/80) ||f||_2^2 > (1/10) ||f||_2^2,

assuming the standard Weil formula from the cited primary sources. This is a *narrower restricted-support result* than the previous w=1/12 certificate, but has a simpler analytic proof without interval LDL. It is NOT positivity on the full interval and not proof of RH, and novelty is not claimed.

Derivation: F(t)=int f(x)e^{itx} dx, rho(t)=|F(t)|^2/(2pi||f||^2). By Plancherel, int rho=1; Cauchy-Schwarz and |E|=2w imply rho(t)<=w/pi. H(t)=Re psi(1/4+it/2)-ln pi is even and non-decreasing in |t| (strict for |t|>0), since the exact digamma series has derivative a sum of nonnegative terms. The bathtub/rearrangement principle gives int H(t)rho(t)dt >= (2w/pi) int_0^(pi/(2w))H(t)dt. For w=1/40 this upper integration limit T=20pi. By H(0)=-gamma-pi/2-3ln2-ln pi > -6 and Zhu Lemma 3.1 H(t)>=ln(t/(2pi))-1/t for t>=A=15/4, integration gives

   integral arch >= ln 10 - 1 - 87/(80 pi) > 71/80,

using ln10>9/4 and pi>3. For all n with Lambda(n)>0 and ln n<2L, only n=2,3,4,5 are possible; geometry of E forbids 2,3,4 shifts, leaving n=5 alone. The n=5 arithmetic cross-correlation is bounded below by -ln5/sqrt5 ||f||^2 > -3/4||f||^2, by Cauchy-Schwarz and AM-GM. The signed pole is +2|int f cosh(x/2)|^2 - 2|int f sinh(x/2)|^2, hence >= -4w sinh^2(L/2)||f||^2 > -(1/40)||f||^2 since sinh(0.405)<1/2. Thus Q/||f||^2 > 71/80 - 3/4 - 1/40 =9/80. The inequalities ln5/sqrt5<3/4, ln10>9/4, H0>-6, sinh(.405)<1/2 admit elementary series proofs. For C_c^infinity functions all Fourier integrals and shift terms converge; extension to the closed H^log form domain is conceivable by the new Suzuki v4 form-core result, but has not been independently written out here.

Adversarial check: The pole is INDEFINITE on arbitrary complex f; dropping it as positive would be WRONG. We used its negative odd component explicitly. Rho is not assumed even for complex f; a symmetric bathtub comparison applies to any rho bounded by w/pi. The nonzero n=5 shift has a **non-vanishing operator norm** as the geometric overlap shrinks, so O(delta) as an L2-operator bound is INVALID.

## Computational tests actually executed

Script `/mnt/data/riemann_research_20261123/independent_collar_bound.py`, JSON `/mnt/data/riemann_research_20261123/collar_bound_report.json`. mpmath at 65 dps for diagnostics, exact rational constant 9/80 asserted with fractions; numeric H(0)=-5.372183419225665..., actual integral bathtub lower for w=1/40 is ~1.29009564744 vs conservative analytic low ~0.95642309177 (and rigorously >0.8875). n5 coefficient ln5/sqrt5 ~0.71976251555, odd pole worst bound ~0.01731915132, delta=2L-ln5 ~0.01056208757<1/40. For independent exchange-block matrices 2N-by-2N N=1,2,4,8,16,32, the computed eigenvalues all matched +/-ln5/sqrt5 to float tolerance 2e-15, confirming the prime5 **arithmetic term alone** has norm independent of overlap; these numerics are falsification checks, not the proof.

Additional scalar investigation: applying the sharper exact H bathtub integral plus worst prime5 and negative pole norm gives a sufficient (NOT necessary) collar width threshold approximately w=0.0425620263 (inverse 23.4951): w=1/24 gives positive diagnostic ~0.02232768681, w=1/23 negative diagnostic ~-0.02239013068. A negative *sufficient bound* does not exhibit any Q-negative function. This illustrates why the earlier p-geometry information is needed to certify wider w=1/12; numeric threshold not interval-certified.

## Distinct new literature connection and conceptual obstruction

Suzuki v4 (2026-11-15) unconditionally proves continuity of the lowest eigenvalue lambda_a. Combined with Zhu's explicit lambda_0.8 >=8.9e-18, continuity implies *existence* of SOME epsilon>0 with lambda_a>0 for all a in [0.8,0.8+epsilon]. It does NOT establish epsilon>=0.01 and gives no explicit radius to justify L=0.81. Mathematical corollary is nonconstructive and novelty is not asserted.

The 5-shift compression makes an instructive counterexample to naive operator-norm continuity. Let s=ln5 and a0=s/2~0.8047189562. The compression of shift by s to L2(-a,a) vanishes for a<=a0. For a>a0 but a<s, a nonzero active cross-window subspace exists and the self-adjoint arithmetic block has exact spectral values +/-ln5/sqrt5. Its L2-operator norm jumps from 0 to ln5/sqrt5 at a=a0 even as overlap delta=2a-s ->0+. Suzuki's continuity of the **bottom eigenvalue of the complete UNBOUNDED form** is not contradicted: concentrating on a vanishing overlap forces high Fourier frequency and growing archimedean H-log energy. Therefore do not prove continuity or small mixed coupling by claiming that a prime-shift operator is O(delta) in L2 norm.

## Unsolved gaps and next experiment

No proof or disproof of RH; no complete L=0.81 window positivity. Existing index<=14 and w=1/12 collar proofs await independent reproducibility checks. Need independently audit Suzuki v4 Theorem 1.3 at prime-entry thresholds and verify extension of restricted support estimates to the form domain. Try a dual norm / Schur complement comparison with H^log, NOT an L2 norm estimate, and seek an explicit radius epsilon above 0.8 using certified eigenvalue Lipschitz/modulus estimates. Test a putative operator-norm smallness assertion against the exact n5 exchange counterexample before trusting it. The third-party L=1.19 candidate remains unverified externally. Avoid repeating float64 Galerkin eigenvalue sign as proof.
