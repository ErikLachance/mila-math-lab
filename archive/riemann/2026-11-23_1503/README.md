# Riemann Proof Watch — append-only preliminary checkpoint, 2026-11-23 15:03 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1503_EST.md`. **Recorded time label:** 2026-11-23 15:03 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity
Earlier Riemann checkpoint: Nov 8 at 15:30:58 EST (W12 rational certificate: positive signed Weil form for functions restricted to two endpoint collars on L=.81, not entire support; no RH proof). The preceding research checkpoint `RIEMANN_SUPPLEMENT_2026-11-23_1452_EST.md` was read; previous work there includes conductor-size asymptotics, character nonresidue witness for cutoffs >=2d, exact orbit-gain algebra checks and source-level Lean theorem bridges. Those are not repeated or claimed new.


## Latest authoritative event, verified this run
Sutherland's primary MIT verification log https://math.mit.edu/~drew/grh/ now shows update **2026-11-23 14:35 UTC** (more current than prior fallbacks): all 175,187 Lean modules accept, the stock Lean 4.36 full export kernel **accepted at 2026-11-22 18:44:18 UTC**, stock Lean with changed allocator **accepted 2026-11-23 03:37:42 UTC**, paranoid Lean with allocator **accepted 2026-11-23 04:29:58 UTC**, and standalone Comparator v4.33.0 full check reported “Your solution is okay!” **2026-11-23 09:10:39 UTC**. Default-allocator paranoid export and v4.36 `lake comparator` are STILL running per the log. Lean FRO/Mathlib's November 21 joint statement certifies formal RH statement/proof https://leanprover-community.github.io/blog/posts/riemann-hypothesis/. Clay still shows the problem as `Active` https://www.claymath.org/millennium/riemann-hypothesis/ ; formal proof verification and formal prize acceptance are distinct. No local 17-million-line recompilation performed.

The November 20 author original four-page PDF https://alpo.ge/remark.pdf was read and page screenshots inspected: he describes theta lifts mimicking multiplicity and a ~sqrt(X) chain. Michael Rubinstein's **November 22 v2**, now **265 pages**, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf was read and pages 1/5/22/224 visually inspected. The guide explicitly does **NOT** prove its main inequality (M) and cites 13 unfinished human-reconstruction hypotheses. This is **not** a missing Lean axiom: independent kernel verification is stronger and separate.

## Distinct new test pass A: exact lemniscate sine arithmetic (regression of known source theorem)
Source §III.12 page 224 claims the lemniscate sine `y''=-2y^3`, `y(0)=0`, `y'(0)=1` has integer derivatives `A_n=y^(n)(0)` and inert-prime valuation `v_p(A_n) >= floor(n*p/(p^2-1))` for `p=3 mod 4`. Independent exact Fraction recurrence for `y(z)=z*sum_{k>=0} c_k z^{4k}`:
`c_0=1`, `c_k=-2/[(4k)(4k+1)] * sum_{i+j+l=k-1} c_i c_j c_l`.
For every k=0..50, all `(4k+1)! c_k` were integral. Initial coefficients match published `1,-12,3024,-4390848,21224560896`. Among inert primes `p <= n = 4k+1` and all 1<=k<=50, **668 exact valuation tests passed**, zero violations, 647 equalities. A deliberate overgeneralization to split primes p=1 mod4 was **falsified**: 570 of 570 split p<=n cases violate the same naive inert bound, e.g. n=5,p=5, A5=-12 and v5=0 < floor(25/24)=1. These are exact finite regression tests of an **already proved theorem in the source**, not a new RH proof, not a new theorem, and the split-prime failures are expected.
Code/data `/mnt/data/riemann_run_20261123_1457/lemniscate_exact.py`, `.json`, `lemniscate_split.py`, `.json`; local runtime of 50-term arithmetic pass ~0.15s. The first code write had a Python syntax error in JSON serialization and was repaired before results; do not count that as valid test data.

## Immediate next distinct research angles
1. Independently reproduce the large-n source example n=1945,p=3 valuation excess (reported 4.625) using an O(k^2) series recurrence, and test whether the prior finite bound remains rigorous at n>201. Do not extrapolate from n<=201 into a proof.
2. Audit Rubinstein's I.3 Mellin-transform cancellation at s=1 and the sparse-interval one-sided Landau criterion, with an exact or high-precision regression on prime powers; keep the unproved (M) separate.
3. Examine quantifier constraints of H12 at cell level, only if new source detail is actually inspected; do not promote the toy CRT character family to an alleged gap in the Lean proof.
4. Recheck independent MIT and Clay statuses on future runs.
