# Riemann research - append-only checkpoint, 2026-11-23 17:37 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1737_EST.md`. **Recorded time label:** 2026-11-23 17:37 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity


Earlier Riemann checkpoint: 2026-11-08 15:30:58 EST (L=.81 endpoint collars w=1/12 with a conditional restricted Weil positivity certificate, NOT all-test-function RH). The previous checked but inadequate approaches include 16D Galerkin positivity without infinite-dimensional control, mismatched core/collar coercivity and errors of order 0.1 versus margins 0.001 and smaller, naive IMS localization O(10), and a prime-5 shift. Preserve these as negative/partial results; do not claim an implication to global RH.

Preceding research checkpoints were `RIEMANN_CHECKPOINT_2026-11-23_1706_EST.md` and `RIEMANN_SUPPLEMENT_2026-11-23_1719_EST.md`, which were read. The first investigated CM elliptic derivations, weighted-prime analytic center, and Landau kernel; the second height-two Honda formal group integrality, explicit [p]-series, CM residue-field hypothesis, and a positive 1x1 theta-minor certificate. This checkpoint deliberately attacks different questions; it does not repeat earlier results as novel.

The scripts and JSON regression results are bundled separately.

## Primary material actually consulted this run

1. Levent Alpoge original announcement (already read in prior work), https://alpo.ge/remark.pdf ; NOT claimed to have reread the whole PDF in this run.
2. Andrew Sutherland (MIT), original independent verification log, https://math.mit.edu/~drew/grh/ ; directly opened/read the live 2026-11-23 14:35 UTC report. The five canonical theorem statements match and independent kernels con-leche, con-ron, nanoda, lean4lean, Lean default and paranoid with allocator setting accept. Some default long-running comparison variants remained unfinished AT THE REPORT TIME; none is a reported rejection. Our run DID NOT build or kernel-check the 61.57 GB export.
3. Lean mirror archival description, https://github.com/CocoSgt/riemann-hypothesis-lean , as a mirror, not the primary provenance or a new independent verification.
4. Andrew O'Desky statement and proof interpretation: https://andrewodesky.com/rh/s/landau.html , https://andrewodesky.com/rh/lean/Deduction.landau_window_key/ , https://andrewodesky.com/rh/lean/Deduction.landau_coeff/ , https://andrewodesky.com/rh/lean/Deduction.landau_pole_asym/ , https://andrewodesky.com/rh/s/q1-pole-dichotomy.html , https://andrewodesky.com/rh/s/divisibility.html (the detailed theorem PHT.1753), https://andrewodesky.com/rh/s/assembly-existence.html , https://andrewodesky.com/rh/s/family-arithmetic-data.html , https://andrewodesky.com/rh/s/bound-count.html and https://andrewodesky.com/rh/s/family-fixed-constants.html . These are a readable interpretive map of the formally checked code, and some entries explicitly say not yet independently double-checked against the original Lean. Web search snippets and source-page text were actually read; some direct opens to this site returned cache misses. Do not claim all original Lean proofs were read.
5. Secondary reconstruction guide https://github.com/nasqret/riemann-rev , a map, not an independent proof. Its explanation of the crucial one-sided, stretched-window Landau criterion was reviewed.

## Micro-pass 1: extending the inert-CM derivative valuation beyond coordinate generators

The previous 17:06 checkpoint tested x and y for invariant derivation D on two CM elliptic curves and conjectured v_p(D^a f) >= floor(a/p)+floor(a/p^3) for specific inert primes. Here the target was strengthened to arbitrary simple POLYNOMIAL COORDINATE FUNCTIONS. On R=Z_p[x,y]/(y^2-f(x)), D(A(x)+B(x)y)=(2f B'+f' B)+2A' y; the formula follows algebraically from D(x)=2y, D(y)=f'(x).

Used exact modular polynomial recurrence, reducing mod p^M only with M >= the maximum claimed threshold+6. For f=x^3-1 at inert p=5, tested bases x^d and x^d y for 0<=d<=15 and 1<=a<=260: 8,320 independent (basis,derivative-order) checks. For f=x^3-x at inert p=7, bases x^d and x^d y, 0<=d<=10, 1<=a<=350: 7,700 checks. TOTAL 16,020 checks. No violations of floor(a/p)+floor(a/p^3). At a=p^3, valuations for nonconstant bases were at least p^2+1 (26 at p5, 50 at p7). These are *finite, p-adically truncated regression checks*, NOT a proof for all polynomials or all derivative orders. Source and JSON: `derivation_extension.py`, `derivation_extension.json`.

Negative controls using the same EXACT derivation at split primes: f=x^3-1, p=7 and13 gave nonzero D^p(x) modp, and f=x^3-x, p=5 and13 also nonzero. Inert p5/p7 had D^p(x)=0 modulo p. Checks with exact modular arithmetic: `split_controls.py/.json`. This documents the geometric inert/supersingular dependence; it does not establish a general Honda-theta link.

## Micro-pass 2: stronger NO-GO theorem for inferring height-two gain from p-curvature only

Earlier counterexample treated an arbitrary module operator T with T^p=pI; the current result strengthens this to an actual *Z_p-linear derivation of a commutative polynomial algebra*. Let R=Z_p[x_0,...,x_{p-1}] and define D(x_i)=x_(i+1) for 0<=i<p-1 and D(x_(p-1))=p x_0, extending uniquely by Leibniz. For every generator x_i, D^p(x_i)=p x_i. In characteristic p, the p-th iterate of any derivation is itself a derivation, since intermediate binomial coefficients vanish; therefore D^p modp vanishes on all generators and hence on all R/pR. RIGOROUSLY D^p(R) subset pR, and D^a(R) subset p^floor(a/p) R.

Nevertheless D^(p^3)(x_0)=p^(p^2)x_0: exactly p^2 powers of p, NOT p^2+1. Thus the proposed height-two bound floor(a/p)+floor(a/p^3) FAILS already for a=p^3 even though D is a genuine derivation with p-curvature zero modp. Counterexamples explicitly evaluated for p=3,5,7,11,13; proof is universal for any prime p. Source/JSON: `derivation_counterexample.py/.json`. This is an independent RIGOROUS negative result about a tempting shortcut, NOT a contradiction to the supersingular CM theorem, which uses further geometric restrictions. NEVER infer second-scale valuation from D^p=0 modp alone.

## Micro-pass 3: self-contained Mellin transform and exact centering conditions

For a nonprincipal primitive Dirichlet character chi, define A_chi(y)=sum_{n<=y} Lambda(n)chi(n)(y/n-1), kappa_chi=L'(1,chi)/L(1,chi), and g_chi(y)=A_chi(y)+y*kappa_chi. For Re s>1, an absolutely convergent termwise calculation gives
  integral_1^infty (y/n-1)_+ y^(-s-1) dy = n^(-s)/(s(s-1)),
so
  integral_1^infty g_chi(y)y^(-s-1)dy = -[L'(s,chi)/L(s,chi)]/[s(s-1)] + kappa_chi/(s-1).
The integral is initially justified only where Re s>1; extending RHS meromorphically near zeros is an ANALYTIC CONTINUATION, not termwise integral convergence there.

Write K(s)=L'/L=K_0+K_1(s-1)+... near s=1. The apparent pole cancels EXACTLY, leaving limit K_0-K_1. If the centering sign were reversed, a spurious residue -2K_0 remains. This was checked symbolically with SymPy.

For zeta, -zeta'/zeta = 1/(s-1)-gamma+(2 gamma_1+gamma^2)(s-1)+..., with gamma_1 the conventional first Stieltjes constant. Subtracting y(log y-1-gamma) gives regular Mellin transform at s=1 with exact finite value 1+gamma+gamma^2+2 gamma_1. OMITTING the '-1' in y(log y-1-gamma) leaves a spurious residue -1 at s=1. Exact symbolic residue checks all PASS, script `analytic_pole_symbolic.py/.json`.

For a zero rho of L(s,chi) with multiplicity m and rho not 0 or1, the centered transform has simple pole residue -m/[rho(rho-1)]. For the positive weighted sum of REAL parts of g_chi, at a shared zero the multiplicities have common factor and positive weights prevent cancellation; at a real zero beta in (1/2,1), residue is strictly positive because beta(beta-1)<0 (for beta=3/4, residue=16m/3). A toy negative g(y)=-y^beta instead has negative residue and satisfies the one-sided upper bound for any theta<beta despite a pole at beta, so real-pole positivity is ESSENTIAL, not dispensable. This checks the source's analytic assumption; NO new RH proof.

## Micro-pass 4: numerical and algebraic adversarial cancellation near s=1

A first numerical implementation using mpmath's unregularized Hurwitz-zeta difference and `diff` at s=1 returned NaNs or spurious blow-up when s approached 1, even at high precision. THIS WAS A NUMERICAL FORMULATION FAILURE, NOT A COUNTEREXAMPLE TO THE MELLLIN IDENTITY. Repaired with the Laurent series of Hurwitz zeta in generalized Stieltjes constants, valid for beta(s)=L(s,chi_4), where chi_4 is real primitive mod4. High precision yields:
  kappa_chi4=0.245609584777314172388816626179...,
  kappa'_chi4=-0.256583407171585202227176727038...,
  limit of regularized Mellin=0.502192991948899374615993353217... .
The zeta regularized limit is 1.764761897741898085203715474687... . Evaluations at s-1=1e-4,1e-8,1e-12 converge to those limits and errors shrink linearly (the last chi4 error about -6.49718e-13). Prime Euler-product partial sums for chi4 at s=3,3+0.3i,2.5+0.7i with all 17,984 primes <=200000 agree with -L'/L(s) to 3.04e-14,3.04e-14,1.5e-11 respectively, well within crude stated absolute tail estimates (<=2e-10 for Re s=3 and 1.2e-7 for Re s=2.5). The numerical calculations are NOT interval arithmetic certificates; exact identities are analytically proved separately. `mellin_stable.py/.json`, `mellin_pole_audit.py/.json` (the latter intentionally preserves the failed near-1 numerical attempt).

## Micro-pass 5: new multiple-theta-factor test of PHT.1753 with an INFINITE symbolic family proof

Using O'Desky's detailed PHT.1753 theorem statement, choose odd prime p, nu=r0=r1=1, S=Z/2Z, u0=u1=1, q_s=sum_{j>=0}(-1)^j Z_s^(p^(2j)), h=q0^p q1+q1^p q0. For any k>=1 let N=p^k, 1<=i<=N/p, and take F=p^(-i) h^i Z0^(N-pi). This is EXACTLY the integral-U coefficient class (U_i=Z0^(N-pi), other U_j=0). Choose T={0}, with N height-one columns at site0 and i height-one columns at site1; then Q=(X0Z0)^N(X1Z1)^i, and its differential coefficient is J_F=X0^N X1^i (N!i!)/p^i. The target coefficient in h^i is EXACTLY 1 because every h factor contributes at least one power of Z1 and attaining total Z1-degree i forces the term (Z0^p Z1)^i; higher q terms cannot contribute.

Thus v_p(J_F)=v_p(N!)+v_p(i!)-i=(N-1)/(p-1)+v_p(i!)-i. For the theorem, alpha0=N,alpha1=0,C1=i,L0=0,L1=i,dQ=N+i,D0=empty, Delta=ell_p(N)+ell_p(i)+ell_p(N)^2; ell_p(N)=k+1. The stated bound is B=sum_{odd e>=1}(N/p^e-i)_+ -Delta +(N+i)/(p^2-1).

Let r be the number of positive odd-e summands, i.e. e=1,3,...,2r-1 with N/p^e>i. A finite geometric-series calculation gives the EXACT SLACK IDENTITY
  v_p(J_F)-B = Delta+(r-1)i+v_p(i!) + (N*p^(1-2r)-i)/(p^2-1) -1/(p-1).
For r>=1, N*p^(1-2r)>i; hence slack > Delta-1/(p-1)>0, since Delta>=3. For r=0, necessarily i=N/p; the formula simplifies to Delta+v_p(i!)-1/(p-1)>0. Therefore this PHT.1753 specialization is PROVED (given the displayed theorem statement) for ALL odd p, all k>=1 and all permitted i, not just sampled numbers. This is a rigorous independent verification of a narrow theorem FAMILY; it is not the global theorem, not the theta-family membership for arbitrary automorphic forms, and not RH. 20,702 exact Fraction regressions across p=3,5,7,11,13, k=2..7 and varying i verified the slack identity with zero counterexamples. Script `theta_family_symbolic_slack.py/.json`; earlier sweep `theta_high_i_family.py/.json` included 2,146 multiple-factor configurations and found positive bounds in most, with no violations.

## Micro-pass 6: explicit limits and falsifiers

A hypothetical absence of the positive-weight condition makes zero-pole residues cancel: for two copies of the same character with coefficients +1 and -1 the weighted transform is identically zero although the individual L-function may have zeros. This invalidates any variant that permits arbitrary signed coefficients. Likewise a function g(y)=-y^beta, beta>theta, satisfies g(y)<=C y^theta for all y>=1 but has Mellin pole with negative residue at beta, showing that sign of REAL-pole residue is essential. The original Landau lemma explicitly requires both, so no defect in the actual statement is claimed.

Quantifier check: the arithmetic bound G_psi(x)<=x^(1/2+9epsilon) must hold for every sufficiently small FIXED epsilon on arbitrarily large stretched intervals [Y,Y^(3/2)], with family constants fixed independently of x. Given hypothetical zero Re rho=beta>1/2, choose epsilon<min(epsilon1,1/52,(beta-1/2)/18); then theta=1/2+9epsilon<beta<1. One epsilon selected after beta suffices. If epsilon were allowed to depend on x or the 9epsilon margin could not be made arbitrarily small, this final logic would be insufficient. This does not resolve the extremely hard uniform arithmetic family existence theorem.

## Known gaps / next experiment

NO new independent global proof/disproof; the independently kernel-certified Lean proof is an external result, not reproduced here. The strong inert CM derivative bound was tested on finitely many polynomial functions and derivative orders, not proven uniformly on arbitrary algebraic forms, and the rigorous cyclic-derivation counterexample proves that first-level p-curvature is not enough. The PHT.1753 multiple-factor identity audits a highly restricted 1x1 family but does not establish the actual theta coefficient-series class membership or high-rank minor inequality. The Mellin centering and residue results check just the analytic half of the bridge; the arithmetic construction yielding stretched-window upper bounds and uniform epsilon remains the central independent-reconstruction bottleneck.

Priority NEXT: investigate the exact passage from geometric/CM elliptic invariant D to global theta sections and the hypothesis F=sum p^-i h^i U_i (all integral U_i), including full period normalization and local conjugacy. Another high-value direction is reproducing one finite but genuinely NONTRIVIAL case of 'Compatible arithmetic data on intervals' with complete character, lattice and prime-count quantifier checks. Do NOT recycle routine 1x1 i=1 tests, dyadic counterexamples, or Galerkin positivity without a distinct hypothesis. Verify future MIT source updates and original Lean changes; keep external formal certification separate from our local checks.

## Reproducibility

Historical code and JSON directory: `/mnt/data/riemann_20261123_1728`.
