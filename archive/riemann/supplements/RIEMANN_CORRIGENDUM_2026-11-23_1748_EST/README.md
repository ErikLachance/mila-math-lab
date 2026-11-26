# Riemann — essential source-code correction and new verification, 2026-11-23 17:48 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CORRIGENDUM_2026-11-23_1748_EST.md`. **Recorded time label:** 2026-11-23 17:48 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)

## IMPORTANT: Explicit correction to previous append-only checkpoints

**The proposed rank-R theta-minor example in `RIEMANN_SUPPLEMENT_2026-11-23_1744_EST.md` (and the earlier 17:37 checkpoint) did NOT establish the essential hypothesis `InClass(p,hhS,F)` as written.** Those records defined `F=p^(-i)*h_(1,1)^i*U_i`, where h_(1,1) was a **single** coordinate pair. Reading the ORIGINAL Lean source now shows that `hhS` sums over **ALL r0*r1 matrix coordinate pairs**. Consequently the claim that our restricted F belonged to the source class was unsupported for R>=2, and the earlier numerical valuations were only formal coefficients, NOT certified applications of the Lean bound. This is a substantive research correction, not a defect in the published Lean proof.

### Original Lean definitions inspected directly using GitHub connector

Repository `CocoSgt/riemann-hypothesis-lean`, source state default branch as retrieved 2026-11-23; exact paths:

1. `src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/CyclicPowerClassOfExpEquiv.lean` defines `sPos` and `hhS`, with `hhS p u = Σ_s u_s Σ_ab (sPos p s ab)^p (sPos p (s+1) ab)`. For ν=1,u0=u1=1 this is H=Σ_{a,b}[(q_{0ab})^p q_{1ab}+(q_{1ab})^p q_{0ab}] with q_{s,ab}=Z_{s,ab}-Z_{s,ab}^{p²}+Z_{s,ab}^{p⁴}-... .
2. `src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/OddLogRelation.lean` defines `InClass pp hh F` as the existence of uniformly integral coefficient-series U_j such that `F= Σ_j pp^(-j) hh^j U_j` coefficientwise. Therefore p^-i h_(11)^i U_i is NOT automatically a witness if h_(11) != hhS.
3. `src/Formalism/GaussJetBounds/StatementP.lean` defines the actual `frameJet` via the product of minors with generic `X_{s,row,a} Z_{s,a,col}` and `jetPairPoly` coefficient multiplied by multi-factorial.
4. `src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementG.lean` defines the exact `FrameJetExcessBound`, `alG,capG,lsG`, with `dSet(TT)`; the CAPPED variant is different and must not be confused with the EXCESS one.
5. `src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementAB.lean` defines `lgN` (base-p digit length) and `deLoss` exactly; `src/Formalism/GrowthSums/StatementA.lean` defines `rhoP=1/(p²-1)`, `gamP=p/(p²-1)` and `excessGain= Σ_{s in TT,e} 1_{odd(2e+1) not in D_s} max(al_s/p^(2e+1)-cap_{s+odd},0)-deLoss`.
6. `src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FrobeniusLiftNorms/EGauss.lean` actually proves `gauss_a_one_bound : FrameJetExcessBound` by transfer from the `EntryExcessBound` theorem, not just a bare definition. This is source structure, not kernel replay by us.

### Corrected construction, with genuine `InClass` witness

Retain p odd, ν=1, any N=p^k, 1<=i<=N/p and any integer R>=2; r0=r1=R; TT={even site0}; N height-one columns at site0, i height-one columns at site1, and ONE height-R column/minor at site0. The full H=hhS defined above has r0*r1=R² summands in each parity. Let `U_i=Z_(0,1,1)^(N+1-pi) * product_{j=2..R} Z_(0,j,j)`, and U_j=0 for all j≠i. Define **F=p^(-i)*H^i*U_i**, not the previously restricted version. `InClass` now holds constructively: the U_j are integral monomials or zero, and all coefficientwise terms agree.

For the selected diagonal X-monomial of the frameJet, only the h_(11) term at every one of i factors contributes the target Z-monomial `Z_(0,1,1)^(N+1) Z_(1,1,1)^i * product_(j>=2)Z_(0,j,j)`. All terms involving other matrix-coordinate pairs introduce forbidden positive degrees in variables absent from target; all reverse parity terms introduce extra site1 degree; corrections in q_s beyond linear increase degree above target. Thus `Coeff[target](H^i U_i)=1` and the frameJet diagonal coefficient is exactly `(N+1)! i!/p^i`. This proves the **coefficient identity within this source-corrected toy family**, but still does not assert any global automorphic theta compatibility.

`theta_hhS_global_membership_corrected.py/.json` performed an independent sparse monomial expansion with exact integer coefficients in **112 cases** for p=3,5,7, k=2,3, i<=5 and R=1..4. All selected coefficients equal 1 and final targeted support was singleton. Initially the more aggressive diagnostic assertion that ALL INTERMEDIATE truncation supports have cardinal 1 FAILED: when i>=p, reverse-parity monomials can survive for a few early stages before eventually dying. This was an overly strong intermediate invariant, not a failed final coefficient claim. We removed only that unjustified intermediate assertion and retained the final exact coefficient and final support-cardinality checks. Recording that failure is important to avoid masking an error.

### Independent source-to-numeric audit of the exact bound

For TT={0}, dSet(TT)(0)=empty; al0=N,al1=0; cap1=i; ls0=R,ls1=i. The exact original Lean `FrameJetExcessBound` exponent reduces to

`B_R= Σ_{e>=0} max(N/p^(2e+1)-i,0) -Δ_R + (N+R+i)/(p²-1)`, where
`Δ_R=ell_p(N)^2 + R*ell_p(N) + R²*(ell_p(R)+ell_p(i))`
and `ell_p(x)=floor(log_p x)+1` for x>0. This is EXACTLY the previously reported B_R formula—but only now have we verified the source normalization and corrected the F-class membership. The rank-one base R=1 requires no extra tall minor; source formula specializes appropriately with ls0=0.

`theta_source_exact_formula_audit.py/.json` reimplements `alG,capG,lsG,lgN,deLoss,rhoP,excessGain,dSet` **directly from original code** for TT singleton. It compared the resulting rational exponent, independently, to the earlier human shorthand over **3,780 cases** p=3,5,7,11,13, k=1..4, i<=30, R=1..12. ALL 3,780 exact Fraction comparisons PASS. The same cases satisfy coefficient valuation v_p((N+1)!i!/p^i) >=B_R for R>=2 and corresponding R1 valuation, with 1,515 cases where B_R>0; smallest slack 13/2. This is not a Lean kernel check of the theorem for general inputs; it confirms exact consistency of this specific computation with the **actual formal statement**.

### Status and remaining limitations

The source correction is the **main genuine research finding** of this addendum: the earlier claimed family membership was unsupported, but a corrected construction with the full H does supply an elementary witness and preserves the selected coefficient, subject to the primary source theorem's literal definitions (now directly audited). This does **not** amount to an independent proof of arbitrary-rank theta determinant valuation, the global arithmetic/automorphic class of theta periods, or RH. MIT's independent full Lean verifications remain external and separately reported. The author's note `https://alpo.ge/remark.pdf` contains the Nov15 theta-chain insight.

### Next priority

Having fixed a genuine local class-membership oversight, **do not continue polishing trivial minor examples**. Instead inspect original Lean chain from `DesignExists` (source `Formalism/SharpRestriction/SmoothDesignExistence/DesignExistsDes.lean`) and `topDesWin` to show a non-vacuous witness of the class of arithmetic families for every small epsilon, including uniform constants and occupied scales. Pay particular attention to whether theorem hypotheses `DesignExists`, `Closed`, and `WithSm/WithTw` are discharged *by upstream lemmas* in the unconditional Dirichlet GRH proof rather than silently assumed in explanatory prose. The kernel's verified theorem statement and axiom audit make unsupported 'a logical hole was found' claims inappropriate. Also inspect how the TRUE source theta lift data are shown to satisfy global `InClass`, rather than assuming the toy F construction covers them.


