# RIEMANN RESEARCH — CHECKPOINT

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_SECOURS_2026-11-07.md`. **Recorded time label:** 2026-11-07 (time not specified in filename) (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)

Snapshot date: 2026-11-07, about 13:00 America/Toronto.


## Earlier scientific checkpoint
Earlier substantive Riemann checkpoint:
2026-08-23 11:08:50--12:01:17 America/New_York, final checkpoint on
metric-defect zero strip, parity multiplicities, and prolate boundary-normalized gate.

No complete proof/disproof of the Riemann Hypothesis is present.


## New primary literature consulted on 2026-11-07
1. Masatoshi Suzuki, Weil's quadratic form via the screw function,
   arXiv:2606.09096v3, revised 2026-09-23.
   https://arxiv.org/html/2606.09096v3
   Finite localized Weil forms, spectral minimum, self-adjoint extensions,
   and characterization of W(a,theta,lambda;z).
2. Masatoshi Suzuki, Spectral convergence associated with Weil's quadratic form,
   arXiv:2610.32704v1, 2026-10-23.
   https://arxiv.org/html/2610.32704
   ASSUMES RH: Theorem 1.1, t_(a,n) >= gamma_n and t_(a,n) decreases
   to the distinct zero ordinates gamma_n; Theorem 1.2, normalized spectral
   entire functions converge locally uniformly to Delta_Gamma (distinct
   zero ordinates counted once). Theorem 3.3: inverse compression of a
   global self-adjoint Hilbert-Schmidt operator, again within RH setup.
3. Masatoshi Suzuki, A spectral theory of zeta functions of function fields,
   arXiv:2610.41115v1, 2026-10-30.
   https://arxiv.org/html/2610.41115
   Unconditional function-field analogue because Weil RH is already known
   there, with a finite endpoint a_* and Frobenius/Rosati positive pairing;
   this does not transfer positivity to the number-field Riemann case.
4. Connes--Consani--Moscovici, Zeta Spectral Triples (EMS, 2026),
   https://alainconnes.org/2026/07/zeta-spectral-triples/

## Distinct technical micro-passes - algebraic checks

A. Correct limiting target / zero multiplicity.
Under Suzuki 2026-10-23 conditional theorem, W(a,pi;z)/W(a,pi;0)
converges to Delta_Gamma(z) = product over DISTINCT positive ordinates
(1-z^2/gamma^2). It is not necessarily xi(1/2-iz)/xi(1/2).
The latter requires all zeta zeros simple, which is unproved.
This corrects any target identification that silently assumes simplicity.
Neither theorem proves RH: the premise is explicitly RH.

B. Strong-to-Hilbert-Schmidt compression.
If C is Hilbert-Schmidt and P_a -> I strongly, then
||P_a C P_a - C||_2 -> 0. The exact identity
(D_(a,pi))^-1 = j_a^* C j_a is Suzuki's conditional mechanism.
To construct the global positive Weil Hilbert space and spectral C
unconditionally, one must avoid assuming global Weil positivity;
that positivity for all test functions is equivalent to RH.
Simply invoking the compression theorem is circular.

C. Exact no-go for self-adjoint finite spectra alone.
On L2(-a,a), D=i*d/dx with antiperiodic boundary condition
f(a)=-f(-a) is self-adjoint. Its spectrum is
{(k+1/2)*pi/a : k in Z}. The normalized even entire characteristic
function is cos(a*z), with all-real zeros, but
W_a(i)=cosh(a) -> infinity as a -> infinity. Its positive
inverse-square spectral trace is a^2/2 -> infinity.
Therefore finite self-adjointness + reality of all zeros does not
imply normality or compact-uniform convergence as interval grows.

D. Stronger no-go: bounded total inverse-square trace is insufficient.
For integer N >= 1 define distinct positive t_(N,k)^2=N+k/N,
k=1,...,N, and normalized even polynomial
W_N(z)=prod_{k=1}^N (1-z^2/t_(N,k)^2).
All zeros are distinct and real. For each N, sum_k t^-2 < 1.
For each fixed k, t_(N,k)->infinity, but W_N(z)->exp(-z^2)
locally uniformly, NOT the empty zero product 1.
Reason: sum_k t^-2 -> 1 and sum_k t^-4 -> 0; take log products.
The missing condition is uniform SPECTRAL TAIL TIGHTNESS:
lim_(M->infinity) sup_a sum_(n>M) t_(a,n)^(-2) = 0.
With fixed-n zero convergence and such tail tightness, a standard
product truncation argument gives locally uniform convergence to
product over the limiting zeros, without an unaccounted Gaussian factor.
Suzuki's conditional domination t_(a,n)>=gamma_n provides this
uniform tail bound; a noncircular arithmetic replacement is needed.
Numerics: N=1000, positive trace=0.99949983, tail after first 5=0.99449985,
W_N(1)=0.36787956, W_N(i)=2.71556671; limits exp(-1), exp(+1).

E. Positive, even, simple ground state is not generically enough.
Let g(x)=(1-|x|/2)_+, and f(x)=g(x)+(g(x-1)+g(x+1))/4.
Then f is even and strictly positive a.e. on (-3,3).
Fourier transform, convention F(z)=int f(x)exp(i*z*x) dx:
F(z)=2*(sin z/z)^2*(1+cos(z)/2).
It has nonreal zeros z=(2k+1)*pi +/- i*acosh(2).
On L2(-3,3), let P_f be the orthogonal projection onto f and
A=I-P_f. The ground state f has eigenvalue 0, simple;
exp(-t A)=exp(-t)I+(1-exp(-t))P_f is positivity improving for t>0.
Yet F has nonreal zeros. This does NOT refute Suzuki's SPECIAL
extension theorem: it shows that positivity improvement, parity,
and ground-state simplicity alone cannot be substituted for the
special de Branges / boundary-form structure.
Numerical quadrature and the analytic FT formula agreed at z=0.5,
1.3,2.1 at 60-digit precision, and |F(pi+i acosh 2)|~5e-62.

F. Compact inverse obstruction in source topology.
A compact injective diagonal operator S on l2 defined by
S e_n=(1/n)e_n has ||r_n||=1 for r_n=e_n, while
||S^-1 r_n||=n -> infinity. Hence uniform control of boundary
forcing in a weak norm cannot by itself bound the inverse response.
Source-specific Picard estimates are necessary.

## Adversarial / invalid inference list
- Do not use Suzuki 2610.32704 Theorems 1.1-1.2 as unconditional:
  the paper explicitly assumes RH.
- Do not identify Delta_Gamma with xi without proving simplicity
  of all nontrivial zeros or handling multiplicities separately.
- Do not assume finite-level real zeros yield local uniform normality.
- Do not infer product convergence from a bounded TOTAL reciprocal-
  square trace; require a UNIFORM TAIL or another anti-escape condition.
- Do not infer Fourier real-rootedness from positivity improvement alone.
- Do not infer stable inverse response from a weak-norm forcing bound.
- Do not transplant the Rosati/Frobenius model to Q without new positivity.
- Do not claim these toy counterexamples disprove RH or Suzuki's theorems.

## Priority for NEXT pass
1. Look for an unconditional arithmetic/finitary bound on the tails
   sup_a sum_(n>M) 1/t_(a,n)^2 for the Suzuki extension with the
   ACTUALLY admissible shift lambda(a)<lambda_a. Test whether even a
   weaker n-uniform growth bound can be established without RH.
2. Keep spectral TAIL TIGHTNESS separate from convergence of each
   fixed-index t_(a,n) and from identification of the target product.
3. Explore whether an arithmetic Toeplitz/Gram/Dirichlet-form trace
   inequality can replace RH-dependent global compression by a
   source-specific estimate; check against the antiperiodic toy model.
4. Audit whether the proposed Hedenmalm/Suzuki ground-state
   Fourier zero lemma uses only the genuinely valid deficiency
   normalization and not an unjustified abstract positivity argument.
5. Keep function-field finite-endpoint analogy as a controlled
   testbed, not as evidence for RH itself.

STATUS: NO PROOF OR DISPROOF OF RH. Research checkpoint only.
