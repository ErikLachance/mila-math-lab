# Riemann Proof Watch — append-only checkpoint, 2026-11-23 13:13:14 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1313_EST.md`. **Recorded time label:** 2026-11-23 13:13 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

The companion ZIP contains the Python scripts and JSON reports for the computations recorded below.

## Scientific continuity

Earlier Riemann checkpoint: **2026-11-08 15:30:58 EST**, a claimed conditional-on-formula exact rational certificate for positivity of a signed Weil quadratic form on *restricted endpoint collars*, L=81/100, w=1/12, not the full interval and not RH. Other earlier partial results: 16D positive Fourier principal compression and ≤14 candidate negative directions; uncontrolled mixed core/collar and complementary Schur terms remain the obstruction. No verification of those older claims was rerun here.

Preceding Riemann research checkpoints:
- `RIEMANN_SUPPLEMENT_2026-11-23_1245_EST.md`: character-selector ramified-prime boundary corrections, finite twisted prime integration, Thorner–Zaman Cor1.4 source match, possible printed partial-summation endpoint typo pending visual inspection.
- `RIEMANN_SUPPLEMENT_2026-11-23_1237_EST.md`: Jutila's original 1977 distinction between fixed-modulus all-character count and aggregate primitive-character count; induction multiplicity counterexample; inert/split prime power identity.
- `RIEMANN_CHECKPOINT_2026-11-23_1232_EST.md`: separate small countermodels for auxiliary mesh/height quantifiers, classical prime sums, and Lean verification overview.
Do NOT relabel results from these prior snapshots as this run's original work. Distinct micro-passes performed here appear below.


## Authoritative/contextual sources actually consulted

1. Lean & Mathlib joint announcement (2026-11-21): https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ — the Alpöge–Claude proof's *formal statement* and checking were independently certified. This run did NOT compile the ~17 million lines.
2. Andrew Sutherland's MIT verification logs, status on 2026-11-23: https://math.mit.edu/~drew/grh/ — 175,187 imported modules, independent kernel and definition/axiom checks, formal RH and Dirichlet-GRH headline statements; avoid conflating the claim with every automorphic GRH variant.
3. Michael Rubinstein's ongoing readable explanatory guide https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ ; some named intermediate estimates are not proved *in that human guide*. The guide PDF v2 was inaccessible for direct page-63 screenshot this run, so no erratum claim on its possible (III.6) endpoint typo.
4. Classical von Mangoldt explicit formula and relation to RH: https://mathworld.wolfram.com/MangoldtSummatoryFunction.html ; Riesz-weighted inverse Mellin framework https://en.wikipedia.org/wiki/Riesz_mean ; these are **background and independently checked via algebra**, not presented as new theorems.
5. Jutila primary original source 1977 https://journals.msp.org/mscand/article/view/1943 — its primitive-character distinction was audited in *earlier fallback*, not repeated here.
6. Recent external reconstruction dependency ledger https://github.com/jimjamzola/RH-Alpoge-Reconstruction, useful context but not a substitute for formal kernel checking.

## Fresh mathematical pass 1: centered Riesz-type prime sum, exact Mellin normalization

Define for primitive Dirichlet χ (nonprincipal)
`Sχ(x) = sum_{n<=x} Λ(n) χ(n) (x/n−1)`, `cχ=L'(1,χ)/L(1,χ)`, and `Gχ(x)=Sχ(x)+cχ*x`.
For Re(s)>1, exact integration by summing prime powers:
`∫_{1}^∞ Sχ(x) x^(−s−1) dx = −[L'(s,χ)/L(s,χ)]/[s(s−1)]`.
Adding `cχ*x` cancels the s=1 simple pole. For principal ζ case define `G1=S1−x log x+(1+EulerGamma)x` to remove the double pole at s=1. Its regular Mellin finite value at s=1 is `1+EulerGamma+2*StieltjesGamma1+EulerGamma² = 1.7647618977418980852...`. Odd χ4 has `c4≈0.24560958477731417`, regular Mellin value `c4−(L'/L)'(1)≈0.5021929919461827112`. Independent exact finite-cutoff step-function integration to X=100,1000,10000,100000,1000000 approaches the predicted limits; finite convergence does not prove RH. `mellin_regularized_test.py/.json`.

## Fresh pass 2: real sign changes falsify a naive positivity argument

Computed the exact piecewise identity `Sχ(x)=x*sum_{n<=x}Λ(n)χ(n)/n − sum_{n<=x}Λ(n)χ(n)`. Direct signed scan x=1..200000 found 15 sign switches in G1 and 21 in Gχ4. Confirmed with mpmath high precision Gχ4(274)>0, Gχ4(275)<0, G1(21318)>0, G1(21319)<0. Therefore **an argument requiring global pointwise Gχ≥0 is false for these centered individual sums**. This does **not** invalidate Alpöge–Claude's Landau positivity application: their specially selected *nonnegative combination* is not the same Gχ. These are numerical sign tests at concrete finite points, not interval-rational certificates. Scripts `centered_sign_and_mellin.py/.json`, `sign_high_precision.py/.json`.

## Fresh pass 3: ζ smoothed explicit formula and sharp conditional constant

Residue identity (for x≥1, smoothing makes the zero sum absolutely convergent):
`G1(x) = log(2π) − sum_{ρ_zeta} x^ρ/[ρ(ρ−1)] − T_even(x)`, with
`T_even(x)=sum_{k≥1} x^(−2k)/[2k(2k+1)]`.
Zero-count N(T)=O(T logT) controls the absolute sum because 1/[ρ(ρ−1)]=O(|Im ρ|^-2) at high heights. Under RH, every ρ=1/2+iγ and `ρ(ρ−1)=−(γ²+1/4)`; consequently
`|G1(x)−log(2π)+T_even(x)| <= C_zeta*sqrt(x)`,
`C_zeta=sum_ρ 1/(γ²+1/4) = 2+EulerGamma−log(4π) ≈0.0461914179322420676`.
**SHARP at x=1** (all x^ρ=1), hence cannot reduce its universal prefactor without shrinking domain. Classical conditional corollary/equivalent form of RH, **not a proof** or a claimed novel result. Numeric prime sums x=1..100000 satisfy proposed bound; first 80 zeta zeros contribute only C80≈0.03913241499166053, residual C−C80≈0.00705900294 not independently certified as a finite zero tail. Scripts `explicit_formula_zeros.py/.json`, `sharp_rh_smoothed_bound.py/.json`.

## Fresh pass 4: odd and even primitive quadratic characters require different residues

For odd primitive χ4 mod4, `L(0,χ4)≠0`. Let c0χ=L'(0)/L(0), T_odd(x)=sum_{k>=0} x^(−(2k+1))/[(2k+1)(2k+2)]. The s=0 residue is *constant* c0χ, so
`Gχ4(x)=c0χ4 − T_odd(x) − sum_ρ x^ρ/[ρ(ρ−1)]`.
Under Dirichlet-GRH, bound `|Gχ4(x)−c0χ4+T_odd(x)|<=C4 sqrt(x)`, with `C4≈0.155567979923585929`, equality at x=1; high precision tests x1..1e5 PASS. χ4 `c0≈0.78318878541367355`.

For *even* primitive χ5 mod5, `L(0,χ5)=0` is a simple **trivial zero**, resulting in a **double pole** of Mellin kernel at s=0. Define `dχ=L''(0)/(2L'(0))≈−0.0220246578387269184`. Correct constant is `log x + 1+dχ`, not the odd constant c0χ. Thus
`Gχ5(x)=log x+1+dχ−T_even(x)−sum_ρ x^ρ/[ρ(ρ−1)]`,
`|Gχ5(x)−log x−(1+dχ)+T_even(x)|<=C5 sqrt(x)` under Dirichlet-GRH, `C5≈0.156556953994286497`, sharp at x1, high-precision x1..1e5 tests PASS. This fixes a genuine elementary parity bookkeeping hazard, not a challenge to the Lean proof. `even_dirichlet_parity_audit.py/.json`, `beta_sharp_bound.py/.json`.

Additional primitive character q3 parity odd tested, C3≈0.113229969857472342. A preliminary q8 numerical routine suffered unstable second derivative at s=0 and apparent 1e−12 numerical mismatch: **DO NOT count q8 as verified**. Replacing `mp.diff(mp.dirichlet)` with high precision Hurwitz-zeta derivatives repaired χ5 q5 to residual <1e−65. `quadratic_char_parity_general.py/.json` retains negative test transparently.

## Fresh pass 5: genuinely complex χ, correct conjugation in spectral constant

For primitive quartic odd χ5 mod5 with χ(2)=i, χ(3)=−i, χ(4)=−1, independently use Hurwitz generalized Stieltjes data to compute
`cχ≈0.15786453544818350655−0.08833613256665016766 i`,
`c0χ≈0.64779028342859446302−0.08833613256665016766 i`,
`Cχ=log(5/π)+ψ(1)+2*Re(cχ)≈0.20322143257953435`.
Under Dirichlet-GRH, `|Gχ(x)−c0χ+T_odd(x)|<=Cχ sqrt(x)` sharp x1. Numeric x=1,2,3,5,10,100,1000,10000 all pass within derivative precision; the x1 difference was ≈7.5e−37 due finite 35-digit estimates, not a mathematical violation. **Critical:** formula requires 2Re(cχ), NOT 2cχ. This is a *consistency check*; formal Lean proof unaffected. `complex_character_conjugation.py/.json`.

## Fresh passes 6–8: exact imprimitive Euler factor correction and conductor-sensitive log x drift

If χ modulo m is induced from primitive χ*, and p divides m but not its conductor q*, write a=χ*(p), |a|=1. Then `L(s,χ)=L(s,χ*)*(1−a p^(−s))`, where cχ−cχ*=`a log(p)/(p−a)`.
For m=floor(log_p x), exactly (as rational/complex coefficient of log p):
`[Gχ(x)−Gχ*(x)]/log p = [x*a/(p−a)]*(a/p)^m + sum_{k=1}^m a^k`.
**Proof:** subtract missing p-power contributions from the two arithmetic S functions and add the derivative centering correction, then finite geometric summation. If a=1, RHS=`m+(x/p^m)/(p−1)`, i.e. `(log x)/(log p)+O_p(1)`, so Δ=`log x+O_p(1)`; if a≠1, the finite geometric sum is bounded and Δ=`O_{p,a}(log p)`. Analytically this matches the extra zero of `(1−a p^(−s))` at s=0 **iff a=1**, not merely the existence of zeros elsewhere on Re(s)=0. Distinguished real a=1 p5/p11 and a=−1 p3/p7: 651 exact Fraction cases PASS (including boundaries), script `imprimitive_centering_dichotomy.py/.json`. Complex a=i,p2: exact Q(i) gaussian-rational coefficient identities for m0..40 and x=p^m,p^m+1,p^(m+1)−1, plus |Δ/log2|<5/2, all PASS; `gaussian_missing_euler.py/.json`.

For multiple **distinct** new primes p|m, Δ is sum of the exact single-p corrections. Hence the exact number of missing split primes with χ*(p)=1 equals coefficient of `log x` in the centering correction, independent of *powers* p^k dividing the modulus; missing inert or complex phases contribute bounded oscillations. Independently evaluated real primitive χ4 induced to moduli 20,12,140,260,6500,84. **66 exact Fraction tests** of direct χ modulo m primepower enumeration vs closed formula PASS. Classification: m20 and140 correction 1logx+O(1); m260 and6500 correction 2logx+O(1), despite extra p5 powers; m12 and84 correction O(1). First implementation failed at x=1 by omitting the necessary `cχ−cχ*` derivative normalization; corrected and reran, old failure excluded. `missing_euler_multi_and_boundary.py/.json`. All are elementary **fixed-conductor** results; no uniform bound as modulus grows with x, and they neither prove RH/GRH nor a new theorem beyond classical Euler-product algebra.

## Adversarial caveats / known limits

- Smooth Riesz sum and all these inequalities are **conditional on RH or Dirichlet-GRH**. Testing finitely many x, 80 ζ zeros or ten beta zeros does NOT prove any GRH.
- Many numeric outcomes use mpmath 35–70-digit, not interval-certified. Claims of exact fractions apply only to algebraic and prime-power coefficient comparisons, not the analytic zero sums, c values, or formal identity over all complex s.
- No proof/replay of Alpöge–Claude's 175187-module Lean code was executed; independent community certificate is evidence. Human-readable guide remains incomplete by its own admission. Its unpublished source typo conjecture remains NOT visually checked this run.
- No link between above newly checked classical conditional inequalities and the missing H0–H12 derivations was established. Replacing the author proof with them would be circular.
- Inverse Mellin and contour shifts require polynomial bounds in strips, convergence of high-zero tails and correct handling of exceptional trivial zeros. The smooth `x/n−1` kernel is helpful but not a license to exchange uncontrolled sums or use partial zero lists to prove a global estimate.
- Main Google Doc write failure remains; NOT solved by this work. No other project or task state changed.

## Next distinct research experiments

1. Generalize missing Euler correction to arbitrary complex roots-of-unity `a`, including multiple primes with fixed/unbounded conductors, retaining exact character terms, and track how constants deteriorate as conductor grows.
2. Check the boundary zero multiplicity criterion through Mellin residues and confirm the full correction to nonprincipal imprimitive `L` at s0; add independent primepower spotchecks (not just closed-form algebra).
3. Audit uniformity: under a conductor q=q(x) growing with x, `O_q(1)` is not uniform. Calculate explicit p and phase dependence; test if the working draft ever promotes a fixed conductor estimate to uniform conductor using a quantifier swap.


**STATUS:** No independent RH proof/disproof.
