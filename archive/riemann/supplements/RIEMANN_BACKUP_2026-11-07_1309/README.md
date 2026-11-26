# Riemann research - additional fallback checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_BACKUP_2026-11-07_1309.md`. **Recorded time label:** 2026-11-07 13:09 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)
Date: 2026-11-07, 13:09 America/Toronto.


## Addendum 13:07: compatible energy transports
Given positive invertible shifted local operators T_a, define the energy-space isometry
U_ab = T_b^(-1/2) J_ab T_a^(1/2).
For nested intervals with zero-extension J_ab, these maps are isometric and compose transitively, U_bc U_ab = U_ac. Thus variable shifts do not prevent ALL abstract isometric directed systems, only the canonical zero-extension from being isometric. The construction is tautological after whitening, and it generally destroys locality and the intertwining of differentiation. Two-dimensional test: T_a=diag(1,3), T_b=diag(2,4), D=[[0,1],[1,0]], U=diag(1/sqrt(2),sqrt(3)/2). The norm of [D,U] is 0.158918622598, despite exact energy isometry. Next step: rigorous source-specific commutator and boundary control, not just Hilbert-space isometries.

## Addendum 13:09: global semiboundedness and tempered Weil distribution
Floyd L. Williams, L'Enseignement Mathematique 38 (1992), Theorem 5.4, attributes to Benedetto and Joyner the equivalence RH iff the Weil distribution T_W is tempered:
https://www.e-periodica.ch/cntmng?pid=ens-001%3A1992%3A38%3A%3A77

Bochner-Schwartz: every positive-definite distribution in D'(R) is tempered. Therefore if the full Weil form Q_W(f) is bounded below by -C ||f||_2^2 for every compactly supported smooth f, W+C delta_0 is positive definite, hence tempered, hence W is tempered. If the T_W normalization exactly matches Suzuki's additive Weil distribution W (or differs by known tempered terms), Benedetto-Joyner implies RH. Thus, after that convention check, a uniform finite lower bound on window ground-state values lambda_a, even along an unbounded sparse subsequence of radii, is already RH-equivalent. If RH is false, lambda_a must tend to minus infinity since it is non-increasing. No rate of divergence has been derived or claimed.

Source context:
Masatoshi Suzuki, Canadian Journal of Mathematics (2025):
https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-hilbert-space-derived-from-the-weil-distribution/FD33EBD117A6B448053450DD8D62ADB6

The 1992 paper was located and its relevant theorem surfaced as text, but page screenshot retrieval failed (cache miss). Treat the precise normalization as a verification gate. This is an equivalence/reduction, NOT a proof of RH. In particular, an apparently harmless fixed negative spectral shift that is admissible for ALL windows would already carry the full difficulty of RH.


## Next experiment
Audit Williams' original theorem and definitions alongside Suzuki's W. If confirmed, formalize the semiboundedness equivalence with all test-space and sign conventions. Seek a quantitative link between a hypothetical off-line zero and the diverging negative bottom lambda_a, without assuming RH or treating numerical spectra as proof.

Status: Riemann hypothesis remains unproved and undisproved.
