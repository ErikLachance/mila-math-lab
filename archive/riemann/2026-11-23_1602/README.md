# Riemann research — append-only continuation checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1602_EST.md`. **Recorded time label:** 2026-11-23 16:02 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Checkpoint time:** 2026-11-23 16:02:21 EST (America/New_York).

## Scientific continuity

Earlier Riemann checkpoint, dated 2026-11-08 15:30:58 EST. The asserted L=.81, two endpoint collars width 1/12, exact-rational Q(f)>.001||f||² is restricted to support in those collars, not full support or global RH. Prior bad attempts: 16D Galerkin positive block cannot control infinite complement; core/collar off-diagonal Schur estimate too large; IMS crude commutator losses too large; numerical sign alone proves nothing; earlier scripts not rerun here.

Consulted the preceding Riemann checkpoint `RIEMANN_CHECKPOINT_2026-11-23_1537_EST.md` (fully) and its immediate predecessor `RIEMANN_SUPPLEMENT_2026-11-23_1518_EST.md` (fully); no semantic duplicate of their conductor threshold calculations, sparse Mellin window counterexample, exact prime logsum, conditional spectral gap, prime-power formula, or lemniscate sine valuations claimed here.


## Primary published sources actually consulted

1. **Allen–Newton–Thorne**, “Automorphy lifting for residually reducible l-adic Galois representations, II,” *Compositio Mathematica* **156** (2020), 2399–2422, DOI 10.1112/S0010437X20007484. Source full primary theorem 1.1 (iv),(v),(vi)(c): https://www.cambridge.org/core/journals/compositio-mathematica/article/automorphy-lifting-for-residually-reducible-ladic-galois-representations-ii/91B814A109E34CC8DA2A5689BFA5CFA4 . (iv) demands *each* absolutely irreducible residual constituent individually conjugate self-dual with multiplier cyclotomic^(1-n); (v) a special Steinberg-type prime, (vi)(c) a Steinberg local automorphic seed.
2. **Independent incomplete HUMAN reconstruction** `jimjamzola/RH-Alpoge-Reconstruction`, `STATUS.md` (updated 2026-11-23), `manuscript/sec17_twisted.tex`, `sec18_assembly.tex` and `sec19_frontier.tex`: https://github.com/jimjamzola/RH-Alpoge-Reconstruction . Read via connected GitHub connector, especially §17 around “Selmer bound on windows,” “a consequence in the direction of Vandiver’s conjecture,” “(OneChar)” and (G3). Its own status explicitly states no independent conventional proof yet: hypotheses not yet established; independent Lean formal verification is a separate issue.
3. **MIT Andrew Sutherland** independent RH formal verification update 2026-11-23 14:35 UTC: https://math.mit.edu/~drew/grh/ . Compilation of 175,187 modules; standard axioms; five statements exact; independent comparator/kernel passes. Robin and Lagarias combined exported theorems also verified. Did not personally execute giant 17-million-line or 61 GB proof.
4. **Lean FRO and Mathlib Initiative**, joint certification 2026-11-21: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ . Distinguished formally checked result from incomplete human exposition. Formalized GRH scope explicitly all Dirichlet L-functions, *not* all Hecke, Dedekind or automorphic L-functions.
5. **Original Alpöge author announcement** dated November 20: https://alpo.ge/remark.pdf , and Clay institutional status https://www.claymath.org/millennium/riemann-hypothesis/ previously consulted in this workflow. Prize administration is not a theorem verifier.

## Micro-pass 1 — rigorous source-to-source audit of the automorphy-lifting bridge

The independent human manuscript tries to derive the strong window estimate for Selmer/Tate–Shafarevich groups via `(V) <- (CorGK) <- (PropGK) <- (Count, OneChar)`, where OneChar uses an automorphy input `(G3)` for a residually reducible three-dimensional representation. Published Allen–Newton–Thorne Thm 1.1 really does require more than generic reducibility: (iv) each *individual* irreducible residual constituent is conjugate self-dual with cyclotomic^(−2) for dimension 3; (v) special local unramified cyclotomic string; (vi)(c) Steinberg seed. The human reconstruction does not establish these hypotheses and explicitly states that the direct application is unavailable. This is a bibliographic, conditional implication audit, **not an alleged flaw in the Lean proof**.

## Micro-pass 2 — exact character algebra obstruction strengthens the comparison

Specialize the HUMAN reconstruction to K=Q(sqrt(-3)), character psi=1, prime l>=5, even e>=2 with generic-position condition `(l−1) does NOT divide 2e`. Since K and Q(mu_l) are linearly disjoint for l>=5, the mod-l cyclotomic character chi restricted to G_K has exact order l−1. The residual triple `Psi ⊕ 1 ⊕ Psi^(-1)` for Psi=chi^e, normalized by chi^(-1) as in the manuscript, becomes

`chi^(e-1) ⊕ chi^(-1) ⊕ chi^(-e-1)`.

For any character `chi^a`, individual dimension-3 polarised conjugate self-duality requires `chi^a = (chi^a)^(-1)*chi^(-2)` (since chi^c=chi), equivalent to `l−1 | 2(a+1)`. For the two extreme characters this becomes `l−1|2e`, CONTRADICTING generic position. The middle chi^(-1) does satisfy it; the *whole triple* is polarized because the extremes swap. Hence **ANT Thm 1.1(iv) cannot be invoked as stated in this generic case**, even apart from Steinberg hypotheses. This is a rigorous finite-character algebra fact, not a contradiction to the human reconstruction (which explicitly marks G3 as not proved), nor to formally verified Lean RH. Independent exact modular regression 11,155 eligible (l,e) pairs with primes 5<=l<500 and even e<=250; each `[False,True,False]` constituentwise test and full triple CSD pairing PASS. Example l=7,e=2, exponents 1,5,3 mod6. Script and JSON locally saved (`allen_newton_thorne_generic_obstruction.py/.json`). Quantifier scope assumes the explicitly stated K and cyclotomic normalization; a DIFFERENT automorphy theorem might handle exchanged constituents.

## Micro-pass 3 — Vandiver-type bound is stronger but NOT full Vandiver

Incomplete human source defines `(V)`: for each even fixed e>=2, and any finite set L of primes l>=5 with `(l−1) not dividing 2e`, finite Sha_l(Q,e) and `sum_{l∈L} lambda(Sha_l(Q,e)) <= C(e+1)^A`. If omega^(−e) class-group eigenspace nonzero, at least `lambda>=log l`; so the bound forces vanishing when `log l > C(e+1)^A` for **fixed e**. This cannot be upgraded to full Vandiver uniformly over e growing with l. For example l=17, e=(l−1)/4=4 (even), generic condition holds; for arbitrary l=1 mod8 let e=(l−1)/4≈l/4. The mere existence of universal C,A does not force log l > C(e+1)^A in that moving-e regime. Finite test exact over all primes l<=20,000 and even e=2..800 checked 634 pairs where `(l−1)|2e` but `(l−1)∤e`: in all cases l=1 mod4, hence quadratic exception indeed Q(sqrt(l)); elementary proof d=l−1 even, d|2e and d∤e implies e odd*(d/2), and even e implies d divisible4. Script/JSON `vandiver_quantifier_audit.py/.json`.

## Micro-pass 4 — only the easy piece of the (Count) norm statement

At each Frobenius place with norm p and twist e, the human source uses target `t(z)=p^e*z+1+p^(−e)*z^(−1)` with |z|=1, and a normalized pure automorphic three-dimensional trace with absolute value <=3. Triangle inequality gives `|t(z)| >= p^e-1-p^(−e) >3` for p^e>=5, so the difference cannot vanish. For p=7,e=1 exact gap is `(7−1−1/7)−3 = 20/7`. Verified 80 exact rational (p,e) tests, script `automorphy_trace_quantifiers.py/.json`. This shows **nonvanishing only** assuming the indicated purity normalization. The hard part of Count is the common nonzero integer `NN`, uniform cardinality and bound `log|NN| <= poly(N(e+1))*log p`. Triangle nonvanishing alone does not produce that bound, nor G3.

## Micro-pass 5 — formally checkable divisor-sum consequences, finite falsification only

MIT independently combined the formal RH result with an older formalization of Robin/Lagarias inequalities, deriving their true universal statements. Recomputed divisor sums sigma_1(n) by an exact integer sieve through n=300,000 and evaluated real sides with float64 solely for a regression: 294,960 Robin `n>5040` instances and 300,000 Lagarias `n>=1` instances, no observed violations. The excluded Robin n=5040 fails by about 106.94 (as it should); Lagarias equality n=1; max observed Robin ratio at 10080 is ~0.9858186. This is **not independent proof**; floats near boundary not certificates. Scripts `robin_lagarias_independent_regression.py/.json`. It does not repeat or replace full Lean certified proof.

## Still unsolved, fails, and next distinct experiments

The independent human reconstruction has open G3, Selmer window bound, theta normalization, chain records; its author says this does not establish RH independent of Lean. A failed attempt to apply old ANT 2020 directly should not be retried without *a new theorem* removing (iv),(v),(vi)(c), with detailed proof and sources. Finite divisor-sum checks, modular examples or nonzero Frobenius differences prove no RH. Formal proof is independently kernel-checked, but not personally rebuilt here; no new independent RH proof/disproof. The previous Weil core/collar mixing obstacle remains.

Next highest-value: identify a genuinely published automorphy lifting result with swapped (rather than individually self-dual) residual constituents and no Steinberg seed; verify hypotheses directly or document its absence; distinguish “new theorem needed” from an alleged Lean bug. Separately, inspect (Count) integral conjugacy and polynomial Weyl-law cardinality quantitatively, then the human source `(G3)` compatibility with those bounds. For Weil, only resume with a certified operator complement/Schur argument, never 16D-only positivity. Check updated MIT verification after 14:35 UTC.


