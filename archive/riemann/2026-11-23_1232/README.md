# Riemann Proof Watch — append-only continuation checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1232_EST.md`. **Recorded time label:** 2026-11-23 12:32 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Actual timestamp:** Monday 2026-11-23 **12:32:21 EST** (America/New_York), 17:32:21 UTC.

## Scientific continuity

Earlier Riemann checkpoint: **2026-11-08 15:30:58 EST**, conditional exact-rational Weil-form positive lower bound over *two endpoint collars* of the support window L=.81, w=1/12, NOT positivity on the entire window, and not an RH proof. Earlier reported negative-index bound <=14, not a proof. Analytic-to-code independent audit has not been done.

Preceding Riemann research checkpoints: `RIEMANN_SUPPLEMENT_2026-11-23_1110_EST.md`, `RIEMANN_CHECKPOINT_2026-11-23_1103_EST.md`, and `RIEMANN_SUPPLEMENT_2026-11-23_1038_EST.md`. These contain prior exact tests of an adaptive semiconvex G(x) grid, optional H12_grid weakening, quadratic residue splitting, finite character selectors, character sums, a Hilbert–Schmidt toy frame, prime-power exact checks, and error-power constraints (m~x^.5, n~x^2, k~x^4.5). No part of this earlier work is relabeled as a discovery in the current run.


## Authoritative sources freshly consulted, Nov 23 2026

1. Levent Alpöge's original remark and proof claim, Nov 20 2026: https://alpo.ge/remark.pdf . Claims RH and GRH for Dirichlet L-functions; Lean archive in 14 parts; Stepanov and ~sqrt(X) chain of theta lifts; distinguish from the August partial zeta-zero result.
2. Lean/Mathlib joint verification, Nov 21 2026: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ . Formal theorem/statement verified by independent checking (no personal independent replay of ~17 million Lean lines).
3. Andrew Sutherland's MIT kernel and statement comparison logs, last updated Nov 23 14:35 UTC at the point checked: https://math.mit.edu/~drew/grh/ . Reports all 175,187 modules compiled, independent kernel tests passing, standard axioms, canonical Mathlib RH statement and Dirichlet-GRH comparison; no assertion of every other automorphic GRH version.
4. Rubinstein et al human-readable **working draft v2 Nov 22**: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf . Its (M), H0-H12 are not all proved there. Do not confuse manuscript gaps with gaps in the fully formalized Lean artifact.
5. NEWLY discovered distinct audit: Jimmie Adriazola, Arizona State University, human reconstruction https://github.com/jimjamzola/RH-Alpoge-Reconstruction ; current statement https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/STATUS.md (dated Nov 22), external-boundary inventory https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/EXTERNAL_THEOREMS.md (older Nov 21 snapshot). The author's dependency ledger covers ~766,788 live declarations (622,409 theorems) and internally classifies 0 unresolved residuals; 4,506 explicitly closed, 631,740 via prior packages, 130,542 as external. Crucial qualification: ~379k region-classified and ~102k dot-dependency extra edges are not individually human audited, and author did NOT rerun Lean kernel. External source fidelity is not complete and independent human line-by-line checking not done. As of Nov22 its initial targeted source-fidelity pass covered 26 high-risk published inputs: two exact, five notation translations, nine via short bridges, nine with unchecked conditions, one with no matching source yet. The large external region Galois representations (`Row0b`→`galoisLocalGlobalStrong_recParameter`), plus published sources for Gallagher PNT progressions, Jutila zero-density, Kato, p-adic Hodge integrality, remain high-value verification priorities. These are limitations of a human reconstruction, not mathematical counterexamples or formal proof defects.
6. Relevant previously inspected Weil positivity source https://arxiv.org/html/2608.24827v2. Independent proof not claimed.

## Fresh micro-pass A — precise quantified supply countermodel (exact integers)

Prior conditional `H12_grid` asks for suitable auxiliary data with constants uniform on nodes of [Y,Y^(3/2)] and mesh gap h²<=8a^(1+theta). Construct unbounded scales `a_j=2^(2^j)`, j>=1, with subsequent b=a² and h=a(a−1). For any 0<theta<=1, a>=4, h²>=9 a² >8 a^(1+theta). Thus *unboundedly many admissible scales alone* DO NOT meet the adaptive mesh sufficient condition; one needs quantitative density AND all auxiliary q,d,theta-lift estimates with common constants. Tested j=1..8 with EXACT big integers at rational theta=3/5. All violate. This is a counterexample to an invalid inference, **not** a counterexample to H12 actually proved inside the Lean archive. Script `fresh_micropasses.py`, result JSON.

## Fresh micro-pass B — avoid assuming height separation from one-sided height bounds

If individual heights y1,y2 merely share an upper bound C, choose y1=C and y2=C−R for arbitrary R>0. Then their spread =R. Tested exactly at R=1,5,100,100000 via Fraction. So the H3 height-spread condition in the human source cannot follow from the *upper-bound part alone* of H1; additional geometric and lower-height information would be necessary. This checks a logical dependency, not a flaw in a published full theorem.

## Fresh micro-pass C — exact lattice-covolume/slope sign test

For real-rational diagonal lattice basis B=diag(1/2,1/3,1/5), det=1/30. The sublattice B diag(1,2,3) has index6, covolume1/5; uniform scaling B/7 has covolume 1/10290. Thus for mu=-log(covol)/3: mu(sub)-mu(B)=−log(6)/3, mu(B/7)-mu(B)=+log7. Verified determinants and indexes symbolically by exact SymPy rationals. Useful sign/normalization regression for the slope arguments, but NOT a genuine Shimura or automorphic lattice or global theta trace estimate.

## Fresh micro-pass D — Robin/Lagarias finite regression plus edge-cases

Built integer exact sum-of-divisors sieve sigma(n) for n<=100000, independently spotchecked 131 values by SymPy factorization; mpmath high precision for functional bounds. No Robin violations at any n in [5041,100000], no Lagarias violations n<=100000. Initial code incorrectly asserted STRICT Lagarias inequality for all n; found exact EQUALITY at n=1, repaired to `>=` and reran. Adversarial cutoff test at n=5040 has sigma=19344, e^gamma*n*loglog n=19237.06153166..., so Robin inequality FAILS with gap (bound−sigma)=−106.938468336..., as expected because its RH equivalence quantifies only n>5040. At n=5041 gap >0; Lagarias equality at n=1. Finite checks are NOT proof of either universal criterion nor of RH.

## Fresh micro-pass E — imprimitive character zero-free bridge / boundary warning

For quadratic primitive chi4 mod4, induce character chi20 mod20 by zeroing multiples of 5. Euler-product identity for Re(s)>1 and analytic continuation: `L(s,chi20)=beta(s)*(1−5^(−s))`. For Re s>0, |5^(−s)|<1, so the Euler factor is nonzero and all zeros of L(s,chi20) in the open critical strip 0<Re s<1 inherit beta(s)'s zeros. At boundary s=(2*pi*i*k)/log5 for every integer k, factor=0, so L(s,chi20)=0 even when beta(s) is nonzero (k=±1, ±2 checked). This proves one must not oversimplify the Dirichlet GRH extension to a zero-free **closed** half-plane, nor confuse imprimitive boundary zeros with nontrivial zeros. Numerically cross-checked using the Hurwitz-zeta formula for beta(s) with 75-digit mpmath at 5 general complex points (error near 1e−75), and boundary factor zero residual <1.1e−75. Exact character table and numeric report in `imprimitive_euler_factor.py/.json` and `boundary_and_cutoff.py/.json`.

## Fresh micro-pass F — independently derive the classical Laurent/psi integral normalization

Let psi(x)=sum_{n<=x}Lambda(n). For Re(s)>1,

`integral_1^infty (psi(x)-x)x^(−s−1)dx = −zeta'(s)/(s*zeta(s)) − 1/(s−1)`.

Using zeta(s)=1/(s−1)+gamma+O(s−1), -zeta'/zeta=1/(s−1)−gamma+O(s−1), the limit as s→1+ is **−1−gamma**. Passing limit under the integral requires an integrable unconditional PNT remainder (classical zero-free region), not just pointwise PNT or bare Abelian manipulation. Independent EXACT finite identity for every X>1:

`integral_1^X (psi(u)-u)/u² du = sum_{n<=X} Lambda(n)/n − psi(X)/X − log X`.

Numerically recomputed by independent prime-power enumeration for X=100,1000,10000,100000,1000000, errors vs −1−gamma respectively .0172168665, .0015309133, .0001749315, .0000367146, .0000110404. Independently evaluated Mellin expression at s=1.1,...,1.00001 approaching −1.5772156649. These numerics support sign/constant only, NOT proof of RH or uniform zeta error bounds. Script `laurent_integral_audit.py/.json`.

## High-value next tasks, approaches to avoid

1. Source-fidelity audit of **one exact published theorem interface** from Adriazola's external ledger: prioritize Gallagher's 1970 two-exceptional-zero windows for `(C7)`, the Galois local–global compatibility for CM polarized cuspidal representations, or the Jutila density bound. Compare full conditions, dependence of constants, and whether the Lean formal statement has a *proved bridge*. Avoid simplistic textual matching; formal proof already independently certified, human reconstruction not.
2. Obtain *exact* Lean declaration paths for H12 and source-to-code map with reproducible archive/version; distinguish the row-level admissible scales from the extra condition that windows and q,d auxiliary data are uniform; unbounded supply alone is useless, as exact countermodel shows.
3. Direct mathematically justified proof of combined main Weil form Schur complement at L=.81 only if full tail/mixed cross term controlled. Do not extrapolate finite Fourier positivity (8D,16D), endpoint collar positivity, or negative-index <=14 into the whole interval.
4. Re-read latest changed Riemann fallback files first; avoid recycling prior 10:38/11:10 grid or quadratic residue tests as new progress. No evidence that a new independent complete RH proof was produced in this run; external formal proof claim is a different project/source, and human-readable mathematical understanding remains an audit target.

## Reproducibility

Local source and JSON reports under `/mnt/data/riemann_20261123_1225/`:
`fresh_micropasses.py`, `fresh_micropasses.json`, `imprimitive_euler_factor.py`, `imprimitive_euler_factor.json`, `boundary_and_cutoff.py`, `boundary_and_cutoff.json`, `laurent_integral_audit.py`, `laurent_integral_audit.json`.

