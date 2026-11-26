# Riemann Proof Watch — second append-only interim checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1110_EST.md`. **Recorded time label:** 2026-11-23 11:10 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Distinct pass 7: exact local quadratic-residue construction, proof and falsification

Read Rubinstein et al, *Alpöge–Claude proof of RH explained*, working draft v2 **Nov22 2026**, Theorem III.1.1 (c) and Remark (3) printed p61, PDF p60–61, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf . Its congruences are q≡3 (mod8), d≡7 (mod16), and q and every small odd prime p divide d+1. Since d≡3(mod4), the reciprocity identity for odd p|d+1 is `(p/d)=(-1)^((p-1)/2) (d/p)=(-1)^((p-1)/2)*(-1)^((p-1)/2)=1`. Also `(2/d)=1` as d≡7(mod8). Thus all such primes split in Q(sqrt(-d)). The argument is unconditional elementary quadratic reciprocity, not GRH.

Independently created exact Chinese-remainder arithmetic and prime examples with q≡3(mod8), d prime≡7(mod16), q|d+1, and p|d+1 for p<=P. Exact modular Legendre-symbol tests all PASS, examples (P,q,d): (5,11,1319); (7,11,9239); (11,19,526679); (13,19,6846839); (17,19,38798759). Every small odd prime through P and 2 split in the corresponding quadratic field. CRT/product primality done with sympy.isprime and exact modular power arithmetic. **Finite toys do not verify Theorem III.1.1's formidable q,d exponential size, character sum estimates, zero-free boxes, or existence uniformly for all large Y.** Script/report `splitting_reciprocity.py/.json`.

## Distinct pass 8: exact character expansion / finite von Mangoldt coefficients

At source printed p33, identity `(1+chi_q(n))(1-chi_d(n))=1+chi_q(n)-chi_d(n)-chi_q(n)chi_d(n)` is exact, including zeros when n divisible by q or d. With (q,d)=(11,1319), tested all integers n=1..10000, obtaining coefficient counts 7287 zero, 430 two, 2283 four. Independently assembled finite prime-power weights `(x/n-1)` for x=20,30,70,100,1319,4000,10000 **as exact Fraction rational coefficients per prime factor of Λ(n)**; raw selector and expanded Dirichlet-character expression yielded identical coefficients, all cases PASS. Since Λ(p^k)=log p, equality coefficient-wise proves equality of the true real sum without floating-point rounding. First prime with weight4 is p23; at x20 all weighted prime-power coefficients vanish, a useful toy demonstrating the selective sieve mechanism. These finite algebraic identities do not establish the mean residue estimate (M), Estimate B or C, and one may not use fixed tiny q,d in place of auxiliary enormous primes. Script/report `twist_identity.py/.json`.

## Distinct pass 9: adaptive finite-net cost lower bound within THIS interpolation rule

Prior 10:32 and 10:38 fallback gave a rigorous semiconvex *upper* grid count O(Y^(3(1-theta)/4)) on [Y,Y^(3/2)] using `h_i^2<=8 a_i^(1+theta)` with 0<theta<1. An elementary MATCHING LOWER EXPONENT follows for ANY partition respecting that same curvature budget: let T=Y^(3/2); each grid gap has h_i<=sqrt8 * T^((1+theta)/2), yet the last half [T/2,T] has length T/2, so at least `T^((1-theta)/2)/(2 sqrt8)` grid steps are necessary (up to endpoints / ceiling). Thus this specific generic curvature-capped grid paradigm has Θ(Y^(3(1-theta)/4)) cost. This is NOT an algorithmic lower bound for verifying RH using any better or arithmetic-specific method.

Independently executed exact BIG-INTEGER mesh generation for theta values 3/5, 11/20, 13/25, 100/199, each at m=30,100,300,1000,3000 with Y=m², T=m³. Each h was maximal integer satisfying `h^(2q) <=8^q*a^(p+q)`, all inequalities checked using integer arithmetic. In each 20-case run, number of steps exceeded the analytical bound (as predicted); rates and raw counts persisted in `mesh_optimality.py/.json`. Floating approximations used only for **display of** real lower-bound comparisons, never to enforce mesh validity. Bound does not prove node-wise G estimates or RH.

## Distinct pass 10: source-dependency and uniformity audit

Read author working guide v2 printed pp193–198 (PDF pp192–197) and §III.11 pp213–216 and verified PDF screenshots. The author openly categorises 16 rows for H0–H12: nine derived from explicitly named source statements, H7 merely quoted, H4 mixed, and **five assumptions H2,H3,H5,H9,H12** imported from Lean (paper does not prove any H0–H12 outright). Especially §III.11 note (2) p214: O23's unbounded admissible scales do NOT imply complete windows [Z,Z^(3/2)]; it also doesn't force primes q,d to satisfy all d/e auxiliary properties or the constants independent of x. This is a real gap in the **human-readable draft**, not evidence that Lean formal proof is faulty: all assumptions are reportedly discharged internally by the formally verified proof.

The guide p33 explicitly states the reduction from (M), Estimates B/C to the scalar G(x) is **one x at a time** and allows the auxiliary primes q,d to depend on x. Therefore prior `H12_grid` reformulation is logically a conditional sufficient target: for each deterministic node, data with *uniform constants* could be chosen separately, but H12_grid cannot be asserted as true merely because the grid is finite or because primes exist at some scales. Counter to an attractive but WRONG shortcut: do not interpolate the q,d-dependent R_{q,d} across nodes that may use different q,d. Only the fixed scalar G(x) enjoys the global convex/semiconvex property. Preserve this caveat.

Updated primary formal source: Lean FRO / Mathlib joint announcement Nov21 2026, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ ; Andrew Sutherland MIT independent full export verification https://math.mit.edu/~drew/grh/ updated Nov23 14:35 UTC. The reported 17M-line Lean proof, RH and Dirichlet GRH statement comparisons, independent kernels all passed; **NOT independently replayed here**. Working guide v2 differs from full Lean proof and remains conditional; don't claim that this proves an omission in Lean.

## NEXT high-value experiments (distinct)

1. Analyze whether a **uniform family of q,d** on only the O(Y^(3(1-theta)/4)) integer nodes in `H12_grid` can be sourced by a quantitative refinement of the genuine theorem III.1.1 and Lean O23, keeping all same per-epsilon constants. Mere finite toy CRT is insufficient.
2. Build a reproducible dependency ledger for the five assumed human-paper statements H2,H3,H5,H9,H12, separating elementary local height comparison from deep global trace/covolume/existence; locate precise Lean theorem names and prioritize independent external explanation of H12.
3. Audit a finite-dimensional arithmetic lattice pair to demonstrate rigorous slope inequalities including sign conventions, identify which abstract toy constraints are actually used to sum over *all* words; do not extrapolate toy frame identities to automorphic groups.
No complete new RH proof or disproof follows from this historical record.


