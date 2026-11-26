# Riemann Proof Watch - append-only continuation - 2026-11-23 08:09:19 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0810_EST.md`. **Recorded time label:** 2026-11-23 08:10 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity and sources

Continuation of `RIEMANN_CHECKPOINT_2026-11-23_0757_EST.md`.

Earlier Riemann checkpoint: Nov 8 15:30:58 EST describing restricted support Weil positivity on endpoint collars at L=.81,w=1/12 but unresolved mixed core/collar control, and earlier negative-index upper bound 14. Prior methods to avoid: extrapolate finite Fourier compressions to infinite tail, trust float64 eigenvalue signs near zero, or crude core/collar IMS/Schur inequalities.

Prior research checkpoints consulted before this continuation: `RIEMANN_CHECKPOINT_2026-11-23_0741_EST.md`, `_0729_EST.md`, `_0718_EST.md`. They already addressed formal Lean `VWinAt`, pair and field witness nonvacuity, Galois/prime existence dependency chain, p-adic toy inversion, H12 long windows and various Landau examples. The new passes below are distinct, independent audits.

Primary / source-linked material actually consulted this continuation:
- Rubinstein, *The Alpoge-Claude proof of RH explained for zeta*, version 2, 22 Nov 2026, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf , particularly Part I.8; Parts II.6.8-6.10; Part III.6,III.11. One relevant PDF page was checked in visual screenshot, not only extracted text. This working human-readable guide explicitly does NOT prove its thirteen input hypotheses or main inequality (M) independently.
- Andrew Sutherland MIT independent formal verification, last update 22 Nov 2026 16:20 UTC, https://math.mit.edu/~drew/grh/ ; 175,187 Lean modules accepted, raw proof accepted by multiple kernels, statement matches Mathlib RH and Dirichlet GRH. These were external reports, NOT rerun in this execution.
- Lean FRO / Mathlib 21 Nov 2026 joint statement https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ .
- Source-guided technical account edition 23 Nov https://alexisdpc.github.io/riemann/technical.html, especially 2.6.4-2.6.7 (quantifier order, two auxiliary primes, mean-square-to-whole-interval, Fourier extraction and cohomology inputs), not an independent Lean verification.
- Actual pinned source at `a6ac91a412dcbaab31801355ec5707024a71bf65`, https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/MeanSquareBounds/pairEx.lean and `StagePow.lean` viewed. `stage` takes a separate mean-square theorem, zero-density counting, prime-counting progression and box-estimate as hypotheses. `pairEx` calls `pair_exists`; no direct numerical reproduction of those deep inputs made.

## Pass 1: Gaussian lattice toy mean-slope inequality and missing rank warning

For the ordinary Hermitian lattice Lambda=Z[i]^2, map phi a full-rank complex 2x2 Gaussian-integer matrix. Its covolume is |det phi|^2; with the squared-norm convention in Rubinstein (III.101), mu(phi Lambda)=-log|det phi|, mu(Lambda)=0, map height ht(phi)=log||phi||_op^2. Thus mu(phi Lambda)+ht(phi)-mu(Lambda)=log(lambda_max / sqrt(D))>=0, where T=sum |phi_ij|^2, D=|det phi|^2>0 and lambda_max=(T+sqrt(T^2-4D))/2. The inequality is elementary from singular values (larger squared singular value >= geometric mean). Exact integer discriminant check plus 597 seeded nonzero Gaussian matrices PASS; diagonal t,t equality and anisotropic unequal maps strict. Rank-deficient maps cannot use the full-rank slope formula. Independent toy warning: infinitely many copies of rank-one map Z -> Z e1 + N Z e2, 1->e1, stay bounded but do not control the target mean slope -0.5 log N. A rank-spanning hypothesis is essential for an averaged target slope. This does not prove the actual high-rank geometric/automorphic lattice statement H8.

`gaussian_lattice_slope_audit.py` sha256 af82fecfd0c6de5e234b48d93f1d06fc3b84b5507e13f9c2c5fa573507bd600b ; JSON sha256 0d9589162a4bd991d36cb249665995b3158c68952c3fc3c896a1207a4d58b674.

## Pass 2: exact optimization of four error exponents

Rubinstein I.8 lists four schematic costs x/m, xm/k, m, k/n^2. Set m=x^a,k=x^b,n=x^c with a,b,c>=0; let n<=x^C. The minimax exponent is EXACTLY
    t_min(C) = max(1/2, (2-2C)/3).
Lower bound: t>=max(a,1-a)>=1/2. If all costs <=x^t, then a>=1-t, b>=1+a-t and b<=t+2c<=t+2C, hence 2-2C<=3t. Equality is attained for C<=1/4 by a=(1+2C)/3,b=(2+4C)/3,c=C; for C>=1/4 use a=1/2,c=C,b=(1+a+2C)/2. Exact rational cases C=0,1/16,1/8,1/5,1/4,1/2,1,2, and independent finite grid checks, PASS. If m^2 replaced the linear per-step m term and other costs were negligible, minimizing x/m+m^2 produces exponent 2/3. This is only a CONSTRAINT-FREE TOY minimax on chosen terms, not the actual arithmetic admissibility or a proof of (M); the real construction imposes many additional conditions.

`four_cost_parameter_linear_program.py` sha256 38180d5c83abfe8e6d9a900f130e43936c610a61fbcb01dab22e497ad2fbb3e5 ; JSON c01684d123c81bc350dd004ec5e78e5f2132d0a92eb88a3246d89b38cc64e853.

## Pass 3: finite character Fourier extraction with inertia

For finite abelian Gamma and subgroup I, additive Frobenius element F, `v_chi(p^j)=(1/|I|)sum_{h in I} chi(jF+h)`. Exactly
    (1/|Gamma|) sum_chi conjugate(chi(g)) v_chi(p^j) = (1/|I|) 1[g-jF in I].
Proof: sum over characters vanishes unless jF+h-g=0, and at most one h in I can solve it. Tested 240 groups/inertia/points/j cases for (Z/2)^2 x Z/n with n=3,5,7,9 at 65 decimal digits, max error ~6.72e-66. An explicit counterexample shows that omitting the complex conjugation yields 0 instead of 1 for n=5, g=F and trivial I. This is an exact algebraic identity with high-precision regression, not the deep analytic prime sum estimate.

`finite_abelian_inertia_fourier.py` sha256 4bec2efbd2f18e84439db1b9e2db9e60fbbbb6cf7d433138804b9adcb8669e7c ; JSON d875bd41d9da6471f9a67f7466286bc55ab3df8b22b80983d7cd8daa27a643a8.

## Pass 4: correct sign of truncated Dirichlet smoothed sum

For arbitrary coefficients a_n (finite n<=T), ell any constant, 1<=y<=T, define A(y)=sum_{n<=y} a_n(y/n-1), S(y)=sum_{n<=T} a_n min(1,y/n), C=sum_{n<=T}a_n/n, R=-ell-C, G=A+y*ell. EXACT algebra: A=y*C-S, therefore G=-S-yR. This is the sign-sensitive statement in technical §2.6.7.5. Fraction exact random tests 239 cases, including interval breakpoints, ALL PASS; all 5 selected examples refute an erroneous plus-sign variant. No actual L'/L analytic tail estimate was proved.

`prime_twist_truncation_identity.py` sha256 24a5c50c5c3a0ad0cd8141703c18d83d3cf871c7ad1fc20ab43268a6272f2b75 ; JSON 74094bc53287821f6ddf12241a4c320a97bb2f34f31c924e3e1b9111561d59e4.

## Pass 5: deriving the whole-interval bad-prime proportion from mean-square assumptions

Assume at every a and v the source's UNIFORM prime-average input sum_p |S_p(a)|^2<=C*a*log(a)*|P| and sum_p |D_p(v)|^2<=C*log(v)/v*|P|, D_p=S'_p, with a>=2. For any a<=b<=2a, choose a witness w_p for each prime bad somewhere in [a,b]. Cauchy-Schwarz along [a,w_p] gives sum_p |S_p(w_p)|^2<=4C a log(2a)|P|. If bad means |S_p(w_p)|>.5*w_p^(1/2+tau), then bad fraction on block <=16C log(2a)/a^(2tau) <=32C/(tau*a^tau) for 0<tau<=1. A dyadic union bound for all blocks up to Y^K gives at most `[32C/(tau*(1-2^(-tau)))]*Y^(-tau)` of primes bad SOMEWHERE. No probabilistic independence and no finite grid substitution needed: the uniformity step is elementary once both deep mean-square inputs are truly available. At illustrative C=1, eta=.1, tau=.005, sufficient log10(Y)>1453.43; at tau=.0025 >3147.53, at .0005 >18532.92. These thresholds are NOT effective certified constants for the actual proof; uniform C, prime counting and analytic tails remain assumed. Numeric threshold equality validated at 90 digits and on either side.

`uniform_twist_window_bound.py` sha256 d794aacf2ee593f5aaa2a18eaed28b621abce37be3000dfe9194be91da6cbc11 ; JSON 58e88065b7f9ddd4445045a561a4af544696cb11b5f70e2769f6ad87ddc40e94.

## Pass 6: elementary size-feasibility for the two auxiliary primes (not existence)

Let W=log Y, z=Y^(eps/5), z'=z W^2. Source requires q prime log q in (z/2,z], q=3 mod8; d prime log d in (z'/2,z'], d=7 mod16 and divisible `d+1` by q and all odd primes p<=z. Source's second-stage mean-square modulus m0 includes 16 M q prod_{odd p<=z}p. Let P(N)=prod_{p<=N}p. Elementary binomial divisibility yields P(N)<=2^N P(ceil(N/2)) and therefore theta(N)<=log2*(2N+ceil(log2 N)). Checked exactly in integers for N=2..2000, PASS. For real z>=20, ceil(log2 z)<=z/4, so log m0<=log(16M)+(1+(9/4)log2)*z, leaving positive coefficient margin 4−1−9/4 log2 =1.440418843740... for the source's log m0<=4z requirement as z grows and M is fixed. CRT congruences themselves are compatible; *simultaneous primes in those progressions with prescribed sizes* are deep and not proved here.

A separate q>T condition with T=(Y^K)^400 needs z/2>400K W, which holds only far along the large branch. An illustrative calculation eps=.01,K=3, fixed base level M=1000 gives log10 Y ~3652.51 merely to satisfy q>T, and ~4156.75 to satisfy ALSO first-stage `(logY)^2 log(8M)/4 <= z`. eps=.005: ~7624.65 and8982.82; eps=.001: ~41819.00 and52588.92. These describe elementary necessary asymptotic size inequalities, not actual prime existence, root zero-density applicability or a verified effective Y0. Detected and repaired an initial erroneous line `ceil(log2 z)<=z/4 for z>=16`; correct sufficient range is z>=20. The final executed JSON uses the corrected range; avoid the earlier false boundary.

`auxiliary_prime_scale_feasibility.py` sha256 a1a9b1a7638f124cd735d0d0c0ed8e954c35a393759e95046b8e24727cb9e1fd ; JSON 4b1f731b2da7379a9968cdeac35e4d953894b5dc60c317d98ceed5c49c69758f.

## Pass 7: exact square-class decomposition and an elementary uniform bound

At finite cutoff T define a(n)=Lambda(n)min(1,y/n), supported on prime powers. For a(n)a(m) with nm a perfect square: if n,m are distinct prime bases, both exponents must be even; if same prime base, parity of their exponents agrees. Therefore the coherent square-class double sum is EXACTLY
    D_T(y)=E_T(y)^2 + sum_p O_{p,T}(y)^2,
where E_T sums even prime-power exponents and O_p sums odd exponents for each prime. This identity is independently checked by 25 direct n,m loops at 65-digit precision, zero failures, including samples at T=30,80,200,500. Larger T=100000, y=2,10,100,1000,10000 show D_T/(y log y)=3.4786,2.7535,2.6095,2.4439,2.1561 respectively (not asymptotic evidence of the actual character-average theorem).

A self-contained elementary *uniform* upper bound is D_T(y)<=400*y*log y for all y>=2,T>=2, independently of the cutoff. Proof sketch with explicit constants:
1. Chebyshev theta(x)=sum_{p<=x}log p <=3 log2*x from P(N)<=2^N P(ceil(N/2)). Then psi(x)=sum_{p^k<=x}log p <=3 log2*x+3 sqrt x log x <=(3 log2+6/e)x<5x, using max(log x/sqrt x)=2/e.
2. E_T(y)<=psi(sqrt y)+y sum_{p^k>sqrt y} Lambda(p^k)/p^(2k) <=5sqrt y+10sqrt y=15sqrt y via partial summation. So E_T²<=225y.
3. For p<=y, O_p<=3 log y, and sum_{p<=y}O_p<=psi(y)+(4/3)theta(y)<8y, yielding sum O_p²<=24y log y.
4. For p>y, O_p <=(4/3)y log p/p. Partial summation against theta(t)<=3log2*t yields sum_{p>y}(log p)^2/p² <=3log2*(2log y+1)/y. Thus sum_{p>y}O_p² <=(16/9)*(3log2)*(2log y+1)*y.
5. Since log y>=log2, D_T(y)<[225/log2+24+(16/9)*3log2*(2+1/log2)]y logy =361.3333... y log y<400y logy.
This audits only the square-coherent diagonal terms of the source's averaged mean-square expansion. The difficult **non-square correlations**, progression prime counts, exceptional character zeros and full uniform estimate remain entirely outside this lemma, and it does not prove RH. This is independently reproducible elementary analysis, not a priority/novelty claim.

`square_class_diagonal_audit.py` sha256 bc08c8cb43c4357f2504c91ef1974cf07a800afddbbd6ad91f83232e30757c64 ; JSON 63fd77444093e2797757affbd0560e45fb7076a2764122cfe4fb5a101e334749.

## Next distinct highest-value passes

Audit an explicit source theorem connecting the source's diagonal square-class term to a uniform off-diagonal cancellation in prime progressions; follow exact hypotheses for the meanSqK and CountBad modules, especially arbitrary coefficients kappa and allowable modulus factors. Independently check any estimate with exact exponent constants and search for missing uniformity, dependence on truncation T, and exceptional zeros. Examine whether the source's quoted square-class bound has a stronger requirement than theta/psi Chebyshev; do not claim source theorem from this diagonal lemma. If this avenue exhausts, return to Rubinstein (M) rank/covolume and cohomological denominators, with exact finite countermodels where a rank hypothesis is removed.

Scientific state: Formal proof externally verified by Lean/Mathlib/MIT; no new RH proof independently obtained here, only precise mathematical sublemmas and falsification checks.
