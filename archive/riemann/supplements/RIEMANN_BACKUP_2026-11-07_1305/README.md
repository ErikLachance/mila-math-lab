# Riemann research checkpoint - 2026-11-07 13:05 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_BACKUP_2026-11-07_1305.md`. **Recorded time label:** 2026-11-07 13:05 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Actually consulted primary sources
- M. Suzuki arXiv:2606.09096v3, https://arxiv.org/html/2606.09096
- M. Suzuki arXiv:2610.32704v1, https://arxiv.org/html/2610.32704
- M. Suzuki arXiv:2610.41115v1, https://arxiv.org/html/2610.41115
- S. Sra arXiv:2611.02944v1, https://arxiv.org/html/2611.02944
- X. Zhu arXiv:2608.24827v2, https://arxiv.org/html/2608.24827

## Exact new deductions and checks
1. RH-equivalent sparse-window near-positivity criterion: if a_k tends to infinity, eps_k tends to zero, and the bottom lambda_(a_k) of the full localized Weil form obeys lambda_(a_k) >= -eps_k, then Q_W[f]>=0 for every compactly supported smooth f (eventually supported in the k-th window), hence RH. This is a reformulation, not a proof of its hypothesis.
2. The natural zero-extension embedding between shifted local Hilbert spaces has squared-norm defect exactly (tau_a-tau_b)*||f||_2^2. Therefore variable shifts tau_a destroy the isometry needed for Suzuki's global inverse-compression proof unless a new metric-compatible transport is constructed. In particular the choice tau_a=lambda_a-1 is not a free substitute for tau=0.
3. Two-phase Vandermonde toy: V=[[1,1],[1,e^(i theta)]], min eigenvalue(V*V)=2-2|cos(theta/2)| ~ theta^2/4. Numerical check: theta=.1 => .002499479210; theta=.01 => .000024999948. Full rank does not imply a uniform quantitative bound when phases collide. This is an obstruction to naive transfer from function fields, not a rebuttal of Suzuki's finite-field theorem.
4. Metric-defect toy: D=diag(i,0), G=diag(eps,1), 0<eps<=1. Then ||GD-D*G||=2eps tends to zero, ||G||=1, min eigenvalue(G)=eps, while D retains its nonreal eigenvalue i. Thus normalized relative defect (2eps)/(2eps)=1. Never infer small imaginary parts from raw defect norm without a metric lower bound.
5. Schur toy: A_k=[[0,k],[k,1]] has min eigenvalue (1-sqrt(1+4k^2))/2 <0 despite both diagonal blocks being nonnegative. Requires coupling estimate B+eps-K*(C+eps)^(-1)K >=0; do not only inspect finite blocks.
6. Spectral completeness toy: A(z)=(1-z^2)*(1+z^4) and Delta_real(z)=1-z^2 share all distinct real zeros but A has nonreal zeros. Knowing a canonical product over observed distinct real ordinates alone does not eliminate an invisible off-real factor.
7. Sra 2026 proves enormous but FINITE PF order based on finite verified zero heights, not PF_infinity or RH. Zhu 2026 certifies finite-window positivity with tiny margin and documents a double-exponential wall for pointwise prime-comb envelopes.

## Current rigor/status
No proof or disproof of RH; all numerical checks above are exact toy diagnostics, not evidence establishing RH. The Oct 23 2026 Suzuki spectral-convergence theorem explicitly ASSUMES RH; the global positive Hilbert-space compression cannot be imported unconditionally. The Oct 30 finite-field theorem uses Weil's established function-field RH and Frobenius/Rosati geometry, not an immediately available number-field analogue.

## Next distinct, falsifiable research pass
- Start with a fixed a>0.8 and construct rigorous interval arithmetic certificates for an arithmetic-side Schur complement. Track even/odd sectors and true complement coercivity; do not mistake Galerkin positivity for operator positivity.
- Seek arithmetic cancellations or a bounded commutator for the off-block coupling rather than an absolute pointwise prime-comb envelope.
- Study metric-compatible transports under variable shifts; derive and test a genuine source-specific bound not requiring a global positivity assumption.
- For any purported spectral convergence, verify completeness of the product and exclude hidden nonreal factors before claiming RH.


