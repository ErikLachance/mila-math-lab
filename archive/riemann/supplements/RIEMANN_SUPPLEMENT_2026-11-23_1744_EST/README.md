# Riemann proof watch — addendum, 2026-11-23 17:44 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1744_EST.md`. **Recorded time label:** 2026-11-23 17:44 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Source freshness

The MIT independent verifier's public report, https://math.mit.edu/~drew/grh/ , inspected directly and confirmed its recorded update at `2026-11-23 14:35 UTC`: 175,187 Lean modules built, only three standard axioms in the five main theorems, independent con-leche/con-ron/nanoda/Lean kernel and challenge equivalence passes; some slow comparator/paranoid default replays were still marked *in progress*. We did not download or replay the ~61.6 GB export. The author's primary 4-page note https://alpo.ge/remark.pdf directly retrieved in extracted-text form: key timeline Nov15 theta-lift multiplicity m≈sqrt(X), Nov16 GRH announcement; PDF screenshots attempted through web and returned `Cache miss`, so no claim of image-level inspection. The mathematical intermediary map https://andrewodesky.com/rh/s/divisibility.html had previously been read directly in the immediately preceding research run; current attempt to reopen returned `Cache miss`. The specialization audits below are conditional on the accurately recorded source theorem's precise indices/ranks; independent Lean source reconstruction is STILL REQUIRED.

## New micro-pass 1: rank 2-by-2 determinant specialization of coefficient valuation theorem

This genuinely extends the rank-one coefficient example. For an odd p, N=p^k, 1<=i<=N/p, choose S=Z/2, nu=1, T={0}; a 2x2 determinant at site0, N height-one columns at0, i height-one columns at1, r0=r1=2. In the recorded theta polynomial class put q_s=Z_s-Z_s^(p²)+..., h=q0^p q1+q1^p q0; F=p^-i h^i * (Z_(0,1,1))^(N+1-pi) * Z_(0,2,2), zeroing unused coordinates. In the diagonal X-monomial the coefficient of J_F is exactly (N+1)! i! /p^i (off-diagonal permutations do not yield this selected X-monomial). Valuation v=v_p((N+1)!)+v_p(i!)-i. The claimed theorem's penalty Delta2 = ell_p(N)^2+2ell_p(N)+4(ell_p(2)+ell_p(i)); d_Q=N+2+i; positive-sum component is sum_{odd e>=1}(N/p^e-i)_+. The theorem's RHS B2 is strictly smaller than the rank-one analogous bound B1 because the extra Delta exceeds its +2/(p²-1) correction. The previous formal rank-one infinite-family proof supplies v>=B1, hence v>B2 for THIS coefficient, all odd p,k and indicated i. Exactly 659 rational/integer test cases across 7 parameter sets passed and many had positive B2. This does NOT prove the source theorem for arbitrary 2x2 minors or actual automorphic theta data.

## New micro-pass 2: arbitrary R-by-R diagonal determinant specialization

A symbolic non-vacuous family exists for any R>=2, same p,N,i, S=Z/2, r0=r1=R, nu=1, T={0}, one R-by-R determinant at0 plus N height-one columns at0 and i at1. Choose F=p^-i h^i (Z_(0,1,1))^(N+1-pi) prod_{j=2..R} Z_(0,j,j). Selected diagonal X-monomial coefficient of J_F equals (N+1)!i!/p^i, independently of R. The recorded theorem RHS is
 B_R = sum_{odd e>=1} max(N/p^e-i,0) -(ell(N)^2 + R ell(N)+R^2(ell(R)+ell(i))) +(N+R+i)/(p²-1).
 Relative to the prior rank-one bound B1 for N site0 plus i site1, B_R=B1-(Delta_R-Delta1)+R/(p²-1), with Delta_R-Delta1=(R-1)ell(N)+R²ell(R)+(R²-1)ell(i). Since ell(N),ell(i),ell(R)>=1, this gap is strictly positive for R>=2,p odd. Thus v_p(coefficient)>B_R, based on rank-one base proof and direct factorial identity. **This is a single diagonal coefficient only**, not all terms of determinant nor proof of PHT.1753's entire claimed valuation, and not a reconstruction of global theta-family membership.
 Exact Fraction regression `theta_rank_r_minor_family.py/.json`: 9,048 (p,k,i,R) cases for p=3,5,7,11, k=2..5, R=2..14, 4,424 have positive theorem lower bound; all PASS. Any inference beyond that narrow family would be an invalid leap.

## New micro-pass 3: substantially smaller explicit Landau interval-concentration constants

Earlier proof used q=1000,sigma=1002, A=1 for fixed lambda=3/2. Found a new independent constructive improvement **q=120,sigma=122,A=1** for ALL REAL U>=1, with m=floor(150U), k=m-1. For V~Gamma(shape=m, rate=120), thresholds left r_L=120U/m<=120/149<0.81, right r_R=180U/m>=6/5. Chernoff tail h(r)=r-1-logr >=13/750 for both r_L and r_R: for r<1 use (1-r)^2/2 and for r>=6/5 monotonicity plus log(6/5)<=1/5-1/50+1/375. Since m>=149U, P(V outside [U,1.5U]) <=2exp(-149*13U/750). The target ratio is
 [ integral_{outside [U,1.5U]} u^k exp(-120u)/k!du ] *122^k
 = Ptail /120 * (122/120)^k
 <=(1/60)exp(-(149*13/750-5/2)U)=(1/60)exp(-31U/375)<1.
 All inequalities are analytic and rationally checked; high-precision Gamma CDF tests at 11 distinct U from 1 to 100 PASS. This handles ONLY the isolated analytic gamma concentration lemma; it is not sufficient for the arithmetic interval estimate or RH.

## New micro-pass 4: split-CM adversarial control

Exact F_p polynomial differentiation D(x)=2y, D(y)=f'(x), f=x^3-1 or x^3-x, confirms nonzero D^p(x) at SPLIT primes p=7,13 for j0 and p=5,13 for j1728, whereas D^p(x)=0 at INERT primes p=5 for j0 and p=7 for j1728. Independent recurrence through a=p² (not only p) keeps D^(p²)(x) nonzero in each split case and zero at inert, consistent with ordinary versus supersingular p-curvature. Rigorous general implication: in characteristic p, D^p is a derivation; on a smooth elliptic curve its invariant vector field is proportional by scalar H_p to D; if H_p≠0 then (D^p)^p=H_p^p D^p is nonzero, likewise every D^(p^r). Thus the inert-CM condition is substantive rather than an inessential prime restriction. `split_ordinary_pcurvature.py/.json` 6 cases pass. This does not settle the p^3 divisibility on the CM theta period lattice.

## Limitations and next highest-value experiments

All above are **specific conditional helper results**. Our reconstruction has NOT independently proved the gigantic global existence of integral compatible theta/Hecke families, the passage from theta minors to prime-power interval bounds, the correct quantifier uniformity in eps, or RH. The independent Lean verification stands separately and credibly but was not redone here. Further arithmetic work should (1) inspect exact global `F∈` class membership in the original Lean source, especially permutation invariants, divided power normalization, and integral p-adic coordinates; (2) trace theta chain to the weighted prime-sum constants uniformly in x, eps and characters; (3) inspect critical global family existence, compatibility across auxiliary primes and possible circular dependence on Dirichlet-GRH. Avoid repeating finite minors or gamma toy lemmas merely to fill runtime.
