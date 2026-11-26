# Riemann Proof Watch — intermediate append-only checkpoint — 2026-11-23 09:43 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_INTERIM_2026-11-23_0943_EST.md`. **Recorded time label:** 2026-11-23 09:43 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Fresh primary source verification

1. Michael Rubinstein, *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, v2 22 Nov 2026, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf . Actually inspected extracted text for III.9 pp.151–159 and III.11 p.199, and PDF screenshots of printed pages 152,157,199. The guide reduces RH to main inequality (M) and 13 hypotheses H0–H12 and does **not** independently prove these hypotheses; it is a human-readable working reconstruction of a separately verified Lean proof. In III.9, Theorem G (`VWinAt`) and `LinkN_at` are explicitly quoted, Proposition G2 is proved conditionally on them. The guide itself says the tie between final record `etaJ` and the local lattice quotient length has not yet been traced in its human exposition (printed pp.154–155). That is an expository OPEN AUDIT, **NOT** a known formal Lean defect.
2. Lean FRO/Mathlib joint certification (21 Nov), https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ confirms formal statement matching and independent kernels.
3. Andrew Sutherland (MIT), independent status last updated **2026-11-23 09:35 UTC**, https://math.mit.edu/~drew/grh/ : 175187 modules pass, 3 standard axioms only, independent `nanoda`/`con-leche`/`con-ron` and lean4lean pass, comparator v4.33.0 succeeded 2026-11-23 09:10 UTC; separate `lake comparator` and paranoid-kernel export replay were still running at the recorded update. Derived formal Robin and Lagarias inequalities are reported. I did not rerun the giant Lean verification locally.

## New independently executed and falsifiable micro-passes

**I. Exact scale-transfer check (Theorem G, III.255 to III.256).** Fix eps=1/100, a=2+8 eps=52/25, kappa=2^25, cpsi=kappa^a=2^52. For x'=2^(25r), x=kappa x', choose n'=2^(52r), so cpsi*n'=x^a exactly. Then `floor(x^400)<=floor((x')^401)` is equivalent to r>=400 (since exponents differ by 25(r−400)); tested r=1,25,75,100,399,400,401,700 exactly without floating exponents. At r=399 it FAILS by 25 binary exponent units; at r=400 equality; r>400 PASS. The source **explicitly requires** x'>=kappa^400; this necessity corroborates rather than falsifies it. At Y=2^10000 and Z=kappa Y, `[Z,Z^(3/2)]` is contained in `[kappa Y,kappa Y²]`, and kappa³<=Y holds. This checks scaling only, not the universal field or primes supply H12.

**II. Ramification/residue-degree normalization and index warning.** For 288 exact parameter choices p in {2,3,5,7}, e in 1..4, f in 1..3, s in 1..6, the O-module O/p^s O for a degree ef extension has O-length e s, Z_p-length e f s, cardinal p^(e f s), verifying the factors of Lemma G1. For e=3,f=2,s=2,p=3, lengths 6 and 12, cardinal 3^12. An explicit abstract countermodel: coefficient field K=Q, lattices A=Z and A'=3^N Z, index 3^N, but if the twisted-prime set is empty H_j=0, so **one cannot equate twisted-only H_j with the total lattice index without controlling untwisted primes**. The human guide already cautions about the missing etaJ-to-etaW tie. This is not a contradiction of `LinkN`.

**III. G2 growth condition adversarial test.** The proof requires y=x^eps >=(log x)^2. For log x=log(10^6), eps=.001, C=f=m=1, N_c=10^9 and V=0, saturating the `LinkN` right-hand side gives roughly 1.90868e11 versus purported G2 target 2.02782e9; **the conclusion fails if the growth hypothesis is removed**. At log x=100000, eps=.001, y=e^100>1e10, the conclusion passes. The source states the condition, so it survives this attack.

**IV. Cyclotomic field-group and parity checks.** For n=1,2,4,...,256, exact modular arithmetic verifies `(Z/4n)^× / {±1}` has order n and the class of 5 has order n. For q=3 mod 8 and d=7 mod16 the distinct odd ramification primes give two independent quadratic factors, hence Gal E/Q has order 4n and shape C_n × C_2 × C_2, consistent with the guide. For ℓ=2, a naive plus/minus eigenspace splitting is INVALID: T=Z/2Z with involution identity has both ± eigenspaces equal to T, their lengths sum 2 while length T=1. The guide's odd-ℓ setting avoids this obstruction.

**V. Sharper ABSTRACT cohomology error allowance at Proposition G2.** From `H_j<=D0[C(f m b y²+L² N_c)+V]` for C>=0, L=log x, B0=f m b y, and L²<=y, the desired `H_j<=D0(C+1)y(B0+N_c)` holds **iff** (at saturation) `V <= y(B0+N_c)+C(y−L²)N_c`. Source uses much stronger V<=b. This algebraic allowance equals y B0 when N_c=0, a factor f m y² larger than b. All **2688 exact Fraction parameter tests** pass; threshold equality and failures just above the threshold are tested. This identifies possible room to WEAKEN one cohomology bound if a new theorem could supply it; it does NOT supply such theorem, and does not reprove Theorem G or (M).

**VI. Generalized Bernoulli normalization: independent finite arithmetic cross-check for source PsiBound (III.261).** For 9 primitive real quadratic characters (prime conductors 3,5,7,11,13,17,19,23,29), degrees k=1..10, independently computed 90 values of `B_{k,chi}` using rational Bernoulli-polynomial sums and an independent rational exponential-generating-series division. All 90 pairs EXACT equality. 63 tests against `L(1−k,chi)` via high-precision Hurwitz zeta satisfy error <1e−65. All opposite-parity Bernoulli values vanish exactly, and multiplication by N times product of primes <=k+1 clears the denominator in these 90 cases. This checks normalization/denominators of the quoted RHS, **NOT** the deep cohomology length inequality or uniform character estimates.

## Executed reproducible artifacts

All under `/mnt/data/riemann_20261123_0936/`: `independent_galois_scale_audit.py`, `.json`; `denominator_budget_exact.py`, `.json`; `generalized_bernoulli_audit.py`, `.json`. Final scripts were actually executed to PASS. Hashes can be independently recomputed from ZIP.

## Failures, limitations and future test

- No new RH proof or disproof; do not conflate the Lean community's verification of Alpöge's proof with an independently constructed proof in this chat.
- Need to audit `linkN_of_twGood_galoisPreconditions` and `NumTie` for precise etaJ/etaW relation in the Lean dependency path; human guide explicitly marks it missing.
- Need a genuine arithmetic replacement for Theorem G under the potentially weaker V-budget. Merely observing slack in G2 is not sufficient.
- Need to audit H12's simultaneous choice of q,d,field E,n(x), all constants and all scales, not merely finite power-of-2 examples.
- Avoid repeating the 09:30 frame lemma, prime toy table and reciprocity checks without a new specific hypothesis.


