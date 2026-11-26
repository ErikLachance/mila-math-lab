# Riemann Proof Watch — append-only checkpoint, 23 November 2026 at 14:52 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1452_EST.md`. **Recorded time label:** 2026-11-23 14:52 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Pass A: Source size constraints materially narrow our previous odd-character extremal counterfamily

Directly fetched the current Nov23 **independent human reconstruction** from GitHub `jimjamzola/RH-Alpoge-Reconstruction`, file `manuscript/sec16_local.tex` SHA `96e49a132f32d4d660ea12cc8efd9c96216229fc`, *Lemma r5:lem:primesizes* lines 175-197, and `manuscript/sec12_loss.tex` SHA `5d1a0cec6eb545abd9fe9468f3d58ef4aa7b89e6`, initial scale equations. For **admissible data** under its stated hypotheses (NOT an independent proof that all such data exist), source says for fixed `0<epsilon<1/52` and x sufficiently large:

- `log d <= x^(epsilon/5) * (log x)^2`, a sharper bound than its also-stated `log d <= x^epsilon`.
- `X' = exp(x^(epsilon/3))` and `X'' = x*n*X'`. Thus `log X' = x^(epsilon/3)` and `log (X'/d) >= x^(epsilon/3)-x^(epsilon/5)*(log x)^2 -> +infinity`, because their ratio `x^(2epsilon/15)/(log x)^2 -> +infinity`.

Therefore **d is eventually far smaller than X' and X''**, and at any SINGLE COMMON scalar cutoff `y>=X'/2`, we eventually have `y>=2d`. This corrects the precise scope of our previous CRT extremal constructions which intentionally chose d>y and hence do **not** satisfy this source scale at those large y. It would be incorrect to cite the CRT examples as a counterexample to the **source's conductor-constrained** H12 data. However source weights are cell dependent: *thick* weights w~b give cutoff y~x, potentially below d, while *thin* weights w~w'' give cutoff y~xnX' well above d; this is a statement only about particular scalar cutoffs, NOT positivity of the whole original cell-sum. The source's original (D1) existence hypothesis is part of the uncompleted human reconstruction, and formal Lean has not been compiled by us.

Numeric asymptotic sanity checks used only **log x=t**, never x itself: for epsilon=0.005 at t=64000, epsilon=.01 at t=16000, epsilon=.018 at t=8000, the ratio `exp(2epsilon*t/15)/t^2` was respectively `8.27e8`, `7.19`, `3.41`; as t grows it diverges by elementary exponential domination of polynomial. This illustrates, rather than proves, the asymptotic calculation. Script `riemann_20261123_1446_conductor_size_comparison.py/.json`.

## Pass B: Rigorous odd-character nonresidue witness with any auxiliary odd prime excluded

Let d>37 be PRIME, d=3 mod4, let chi=chi_{-d} be the primitive odd real Dirichlet character of conductor d, and let q be ANY ODD PRIME different from d. Then there is an odd prime p<d, p != q, with chi(p)=-1.

**Elementary proof:** n1=d−4 and n2=d−36 are positive odd integers >1 and below d. Using the primitive odd Kronecker character, chi(n1)=chi(-4)=-1 and chi(n2)=chi(-36)=-1 because (-1/d)=-1 and squares have character+1. Since n1−n2=32, an odd prime q cannot divide both n1 and n2. Select n from {n1,n2} not divisible by q. It factors into odd primes p<d, all distinct from q; its character is -1, so at least one prime factor must satisfy chi(p)=-1. No PNT, Burgess bounds, Linnik bound, GRH, or algebraic geometry needed.

For **uniform positive weight** `a>0` with `y=a/w>=2d`, and with the original prime exclusions p=2,q,d, consider `P/a = sum_{p^k<y; p notin {2,q,d}}(1-chi(p)^k)*log p*(1/p^k-1/y)`. Every summand is nonnegative. The witness prime p<d contributes `2log p(1/p-1/y) >= log p/p >= log d/d`, since y>=2d>=2p and log t/t decreases on t>=e. Consequently a NEW **conditional-on-the-common-weight-model** unconditional elementary lower bound holds:

`P/a >= (log d)/d > 0` for every d>37 prime 3 mod4, any q odd prime !=d, and y>=2d.

This is distinct from the old extremal zero achieved by arbitrarily large d>y: the source size restriction excludes that regime at large cutoff y. The lower bound is weak, vanishes as d grows, and gives no cell-distribution or theta-lift compatibility. It cannot be inserted into (M) without controlling the actual varying cell weights and excluded primes. It is **not RH/GRH proof or any alleged Lean flaw**.

Exact SymPy factorization, Kronecker, Fraction/positive-term reasoning and mpmath checks: first model for q∈{5,7,11,13,17,19} and d19..1000 in correct family passed 503 cases and seven full prime-power sums y=2d satisfied the bound; improved universally odd q∈[3,37], prime d41..2000, passed **1,490 exact factor/sign/witness cases**. Numerical selected e.g d43 q7 P/a≈1.95352 vs log(d)/d≈.08747; d127 q7 P/a≈2.83811 vs bound≈.03814. Scripts `riemann_20261123_1448_small_conductor_odd_guard.py/.json`, `riemann_20261123_1446_universal_odd_q.py/.json`. The universal proof does not depend on tests.

## Pass C: Exact algebraic source regression of the orbit gain formulas

Read live `manuscript/sec12_loss.tex` §§r2:g0,r2:g1, r2:ask and the author's own derivation around line510. With `gamma_p=p/(p²−1)=sum_{e odd>=1}p^(−e)`, positive adjusted weights `al(s)=a_s−2c_G`, nonnegative caps `cap_j(s,e)=w_j(π_p(s,e))−kappa_j+c_G` and the indicated Excl(s,e) omissions, the difference before price is EXACTLY:

`g1−g0 = sum_{s odd} sum_{e odd, Excl(s,e)} max(al(s)/p^e−cap_j(s,e),0) + sum_{s even} [gamma_p*al(s)−sum_{e odd, not Excl} max(al(s)/p^e−cap_j(s,e),0)] >=0`.

Every bracket nonnegative since max(v−c,0)≤v for v,c≥0. The common `digit loss` cancels. In classII, all tops are called even; identity still holds. **This algebra and the identity min+max=v were already explicitly used in the 225-page source around line510; it is an independent regression check, NOT a new author-level theorem.** Crucial: it does NOT imply a positive served-orbit gain after subtracting the nonnegative price Pr, and it says nothing about the required strong local `LP(...)` nondegeneracy hypotheses. Code `riemann_20261123_1450_orbit_gain_identity.py` checked 5,000 exact Fraction cases with constant caps; a separate `riemann_20261123_1452_orbit_periodic_caps.py` checked 5,000 *periodic e-dependent* cap cases, independently summing `min` via finite terms plus exact geometric tail and `max` via finite positive terms. Both 100% PASS; no counterexample found to the author's identity.

## Pass D: Exact Lean source-level theorem bridge (read, not executed)

Fetched source from `tamnd/riemann-lean` mirror, which states it matches Alpöge's November-20 release but was **not independently rebuilt by us**:

- `lean/src/Main.lean` SHA `dbd5db70bc11b35f18fa5751216ab335321e7bfc` states exactly five headline theorems, including `theorem riemannHypothesis : RiemannHypothesis := rhOfAll`.
- `lean/src/Statements.lean` SHA `1cd1bce93344065936b2b392b23306254e0785ef` explicitly defines the other four statements for zeta and Dirichlet L-functions.
- `lean/src/Supplements/Kernels/MainTheorems.lean` SHA `6a542d7ce969a791fd12ce575f587e6bc29044bf` shows `allChi : UpperTheory.EveryCharacter := UpperTheory.FinalTheorems.everyCharacter` and `rhOfAll := Formalism.VW.rh_of_every allChi`.
- `lean/src/Formalism/GammaFactorNonvanishing/RhOfRight.lean` SHA `3604637147a33e72248faddd775ea750e7846ead`, `CritLine.lean` SHA `95fa4da5c50119db164aa93944d106f22fdb576d`: nonvanishing right of line plus zeta functional equation gives RH, including explicit exclusions of trivial zeros; primitive Dirichlet strip reflection uses nonzero gamma factors for 0<Re s<1.
- `lean/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean` SHA `ee340012ab19713a8acfecf8adc6a331cbc2f1a4`: `EveryCharacter` is discharged by `everyCharacter_of_row` and a named `galoisLocalGlobalStrong_recParameter` theorem; another imported `EveryCharacter.lean` constructs the `EveryCharacter` predicate.

The final bridge is recognizable ordinary complex analysis; the truly deep part is the large theorem `UpperTheory.FinalTheorems.everyCharacter` and its antecedents. Names like `LiteratureTheorems` or intermediate `Hyps` do not themselves mean unsupported external axioms; the full independent proof kernel checks are **reported externally** by Lean/Mathlib and MIT, not replicated here. We found no evidence from these small files of a circular RH assumption. This is a source-level audit, not verification of all 175,187 modules and not an independently new proof.

## Status and next

No RH/GRH proof or disproof created; no new gap established in formally checked Lean material. The old fixed-window Weil mixed core/collar terms remain unresolved, and full human exposition's 13 H conditions remain incomplete. Distinguish the source-size conditional elementary prime witness from the original full theta/lattice analysis. Do not treat the finite CRT extreme characters from the previous supplement as source-valid for all cutoffs; corrected by (A)-(B). Distinct next experiment: map which actual cells have weight small enough to place p<d under their individual cutoff, and whether their Frobenius cell positions are among the served orbits; without this, no global positivity assertion. For proof audit, inspect published local Langlands/nondegeneracy input before claiming to have closed the human paper gaps.
