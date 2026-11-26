# Riemann Proof Watch — append-only fallback checkpoint — 2026-11-23 07:29:01 EST (America/New_York)

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0729_EST.md`. **Recorded time label:** 2026-11-23 07:29 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

## Scientific continuity

No independent proof of RH is claimed.

Earlier Riemann checkpoint **2026-11-08 15:30:58 EST**, partial positive Weil form on two endpoint collars at L=.81, w=1/12, reported >0.001||f||^2 for functions supported there; negative index bound <=14 separately. Full-window cross-terms and complement not certified. This earlier claim is as stated in that checkpoint and not independently re-executed here. Rejected routes from that checkpoint: extrapolating finite-dimensional Weil compressions; a naive mixed collar/core IMS estimate; float64 sign tests near tiny eigenvalues.


Relevant preceding research checkpoints: `RIEMANN_CHECKPOINT_2026-11-23_0709_EST.md` and `RIEMANN_CHECKPOINT_2026-11-23_0718_EST.md`; avoid reporting their work as first discovery. They already contained a symbolic Lipschitz/G(x) criterion, adaptive maillages, an exact p-adic cancellation counterexample for lemniscatic derivatives, exact exceptional-index interval selection, finite-character tests and review of VWinAt. This run builds on that audit, rather than repeats it.

## Primary/formal sources inspected this run

1. Levent Alpoege/Lean repository, public pinned copy at commit `a6ac91a412dcbaab31801355ec5707024a71bf65`, complete raw module source:
   - `.../CharacterBoxes/ExistsPageN.lean` (excerpt as published at https://alexisdpc.github.io/riemann/sources.html , `VWinAt`, `VAt`, `WinPair`, `IsChiField`).
   - `.../CharacterBoxes/SupplyChi.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/CharacterBoxes/SupplyChi.lean
   - `.../CharacterBoxes/HostOfField.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean
   - `.../CharacterBoxes/WinPairs.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/CharacterBoxes/WinPairs.lean
   - `.../ShortNorms/supplyOfAdmOf.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/ShortNorms/supplyOfAdmOf.lean
   - `.../MeanSquareBounds/pairEx.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/MeanSquareBounds/pairEx.lean
   - `.../CoprimeRanks/AdmChi.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/CoprimeRanks/AdmChi.lean
   - `.../ShortNorms/Primes.lean` https://raw.githubusercontent.com/TomasOrtega/RH/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/Development/AutomorphicArithmetic/ShortNorms/Primes.lean
2. Independent verification published and time-stamped 2026-11-22 16:20 UTC by Andrew Sutherland (MIT), https://math.mit.edu/~drew/grh/ : all 175,187 Lean modules accepted, standard axioms only, multiple independent kernel replay, theorem corresponds to Mathlib's RH and *Dirichlet* GRH; two redundant single-threaded verification paths pending as of last update; NOT independently compiled here.
3. Lean / Mathlib formal certification 2026-11-21, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ .
4. Source-linked secondary technical guide 2026-11-23 https://alexisdpc.github.io/riemann/technical.html and https://alexisdpc.github.io/riemann/sources.html ; source curator explicitly did not recompile full Lean.
5. Independent reading project blueprint https://nasqret.github.io/riemann-rev/book/blueprint.html and partial-kernel proof audits https://nasqret.github.io/riemann-rev/book/formalization.html . These are secondary, distinguish from formal source.

## Micro-pass A — exact quantifiers and possible vacuity: upstream resolved at selected call sites

`VWinAt psi Ct` is `forall eps ... forall e ... exists J>=1, X0, forall X>=X0, forall q,d, WinPair eps (X^(1/J)) q d -> exists Y, X^(1/J)<=Y and Y^2<=X and forall x in [Y,Y^2], VAt psi eps Ct q d (e x) x`. Two potential vacuity hazards require source-level tracing:
- Quantification `forall q,d, WinPair -> ...` does **not** itself guarantee existence of admissible prime q,d.
- `VAt` is `forall E, IsChiField ... E -> VVle ... E`, and thus is vacuous for hypothetical nonexistent fields E.

**Actual source trace resolves both at the USE in the analyzed branch**, not via VWinAt alone: `WinPairs.lean` lines 8–33 calls `QH.pairEx` to construct q,d at scale `X^(1/J)`; `pairEx.lean` lines 106–134 constructs prime pair from `pair_exists` and verifies q mod8=3, d mod16=7, q|(d+1), and all small odd primes divide d+1. `supplyOfAdmOf.lean` lines 90–129 builds field/frame `H` and invokes `isChiField ψ ...` at line 126, then applies the window bound `hW.bound H.E hCF` at line 128 to an **explicit existing field**. Thus neither apparent vacuity is established at this junction. This is a **positive rigorous source-audit finding**, not a proof by this researcher that upstream `QH.pairEx` or any needed input is mathematically sound; external Lean verifiers cover the complete formal proof. Next: inspect `pair_exists` quantitative prime-in-progressions dependency and hidden assumptions in its exact types, as well as downstream transfer of host windows into entire power intervals.

Additional necessary consequence of the `VWinAt` inequalities: for X>1 and Y>=X^(1/J)>0, Y^2<=X implies J>=2 by taking real logarithms; declared J>=1 can be sharpened at any **actual** admissible pair and X>1. If no pair, this logical inference is unavailable. Not a contradiction since existential J may be larger than 2.

## Micro-pass B — exact p-adic inverse-series lemma with self-contained proof

Consider the independent **toy model** (not the actual theta construction) `l_p(t)=t+sum_{j>=1}p^{-j} t^(p^(2j))` over Q_p[[t]], for integer prime p>=2. Its unique compositional inverse `U(z)=sum_{n>=1}u_n z^n` exists since l'_p(0)=1. Let L=p²−1. The identity `U=z−sum_j p^{-j}U^(p^(2j))` implies a recurrence for u_n in terms of smaller-degree coefficients. Inductively, each contribution of j with r=p^(2j) factors and n1+...+nr=n, n_i>=1, has p-valuation at least
`−j − sum_i (n_i−1)/L = −j −(n−r)/L >= −(n−1)/L`, since r−1=p^(2j)−1>=j(p²−1). The ultrametric triangle inequality completes the induction. Therefore for all n>=1:
`v_p(u_n) >= −(n−1)/(p²−1)`.
For *any* F(t)∈Z_p[[t]], degree-n coefficients of F(U(z)) satisfy the same bound for n>=1, by decomposing monomials with r>=1 factors. Hence
`v_p((d^n/dz^n)F(U)(0)) >= v_p(n!)-(n−1)/(p²−1) = (n−s_p(n))/(p−1)−(n−1)/(p²−1)`, where s_p(n) is the base-p digit sum. This yields exact `n*p/(p²−1)−s_p(n)/(p−1)+1/(p²−1)`, explaining a derivative divisibility mechanism without illegitimate termwise 1/n denominators from Lagrange inversion.
Exact independent Lagrange coefficients computed in `/mnt/data/riemann_research_20261123/padic_inverse_symbolic_audit.py` and `.json`: p=3,n=1..193 (25 nonzero); p=5,n=1..201 (9 nonzero); all exact rational `Fraction` valuations meet the lemma, 0 failures. Demonstration is the recurrence, not the finite tests. This is a **toy lemma**, not proof of the full lemniscatic or theta theorem and not a result on RH.

## Micro-pass C — elementary CRT shows no congruence contradiction, not quantitative prime existence

For finite odd prime set P and M=prod(P), the simultaneous congruences d=7 mod16 and d=-1 mod M have the unique solution `d=7+16t`, `t=-8*16^-1 mod M` modulo 16M. The residue is coprime to 16M. Dirichlet's classical prime progression theorem implies infinitely many primes in this progression for **fixed M**, but not the difficult simultaneous `log d` and `log q` windows, q|(d+1), or uniformity as M grows with Y. Exact CRT/elementary primality example script `/mnt/data/riemann_research_20261123/winpair_crt_sanity.py` and `.json`: bounds {3,5,7,11,13,17}; examples first prime d={23,359,839,9239,840839,2042039} for corresponding residue classes, all satisfy necessary congruences. This is falsification of an elementary incompatibility suspicion ONLY; does not prove PairEx nor RH.

## Known limitations and next experiments

Formal theorem external verification is strong, but **no independent full Lean recompilation in this run**, and no new mathematical proof of RH originated here. The published human-readable guide 22 November still misses a fully narrated proof of the main arithmetic hypotheses: a gap in exposition is not a kernel gap. Do not extrapolate this toy p-adic coefficient recurrence to the real elliptic theta construction. Do not mix claims across pinned Lean versions; one secondary PDF excerpt appears to use an alternate VWinAt upper endpoint `x<=X` rather than `x<=Y²`, whereas pinned source here uses `Y²`; base conclusions only on pinned source.

Next highest-value reading and tests: `Development.AutomorphicArithmetic.MeanSquareBounds.PairExists` exact input for `QH.pairEx`; `UpperTheory.Top.winPairs` bridge (quantifier order), `UpperTheory.Top.isChiField` construction, then `UpperTheory.Top.eFamC_of_cls` and the formal source of full power-interval bound; compare with Rubinstein 2026-11-22 guide H12 and verify where constants/prime supply remain uniform. A separate mathematical task is to find a genuinely independently auditable finite lemma with potential falsifying test, not repeat previous huge prime-sum sweeps.


