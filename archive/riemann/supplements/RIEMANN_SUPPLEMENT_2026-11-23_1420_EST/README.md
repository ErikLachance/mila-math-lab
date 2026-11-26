# Riemann Proof Watch — third append-only checkpoint on 23 November 2026, 14:20 EST

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_SUPPLEMENT_2026-11-23_1420_EST.md`. **Recorded time label:** 2026-11-23 14:20 EST (from the filename).

[Archive index](../../../README.md) · [Manifest](../../../manifest.json) · [Verification scope](../../../README.md#what-was-checked-during-import)


## Distinct rigorous source-fidelity pass 9: Laurent limit of psi

Source of *classical* external input listed in third-party 21-Nov manuscript EXTERNAL_THEOREMS.md: `integral_1^infinity (psi(u)-u) du/u^2 = -1-EulerGamma`. I independently reconstructed an analytic proof with explicit convergence requirement:
- For Re s>1, `-zeta'(s)/zeta(s) = s integral_1^infty psi(u) u^(−s−1) du`. Therefore `integral_1^infty (psi(u)−u) u^(−s−1)du = -(zeta'/zeta)(s)/s − 1/(s−1)`.
- A **strong unconditional prime number theorem error** `psi(u)−u = O(u exp(−c sqrt(log u)))` for large u ensures absolute integrability of `(psi(u)−u)/u²`, allowing s down to1 by dominated convergence. The ordinary PNT `psi(u)=u+o(u)` alone does NOT justify this interchange.
- Laurent `−ζ'/ζ(s) =1/(s−1)−γ+O(s−1)` then yields `−1−γ` (not `−γ`).
- Exact finite cutoff identity: `I(X)=integral_1^X(psi(u)−u)/u² du = sum_{n<=X}Lambda(n)/n−psi(X)/X−log X` by Tonelli finite sums. Independently implemented a prime-power sieve up to1,000,000, evaluated six cutoff checkpoints, and independently integrated the actual step function up to1000. The two independent finite computations agreed to <1e−23. At X=1e6 computed −1.577204624465..., ∼1.1e−5 above limit −1−γ. Near-s=1 Laurent test with eps1e−8 checked. All numerical tests PASS but **do not prove infinite limiting statement**; analytic proof depends on unconditional standard PNT zero-free-region estimate, not RH. `riemann_20261123_psiintegral_laurent.py/.json`.

## Pass 10: check actual November-23 human 225-page reconstruction *source* rather than summaries

Fetched 2026-11-23 public TeX directly through GitHub connector from `jimjamzola/RH-Alpoge-Reconstruction`: `manuscript/main.tex`, `sec2_criterion.tex`, `sec19_frontier.tex`, `sec11_lifts.tex`, `sec12_loss.tex`, `sec14_bessel.tex`, `sec15_heights.tex`, `sec16_local.tex`, `sec17_twisted.tex`, `sec18_assembly.tex`; content read, no PR/issues/writes. Verified abstract source warning via `sec19_frontier`: class (P) proved in human paper, (X) reduced to published, (O) unproved conventional internal statements, (U) source verification incomplete. Selected seven sections have respective source textual counts of `\notgiven{` 1,8,1,11,2,7,2 (total32), and explicit `\begin{hypothesis}` 3,1,13,13,2,2,2 (total36), although many are repeated/aggregated and **are not 68 independent mathematical gaps**. No claim of independent human proof. Earlier 66-page Nov21 document is superseded; Nov23 version 225 pages and still incomplete conventionally. Independent formal Lean checking externally accepted, not executed in this run.

## Pass 11: localized Selmer descent and a surplus assertion in a human draft, NOT a counterexample to Lean

Source `manuscript/sec17_twisted.tex`, GitHub SHA 921ea3252c143adbeca0b7af1281865cf8d2b566, proposition labeled `w4:prop:res`: for `E subset Q(mu_N)`, odd l∤N and e≥1 with l−1 not dividing e, it states restriction `Sha_l(Q,e) -> Sha_l(E,e)` is injective **onto Gal(E/Q)-fixed classes**. The displayed proof establishes injection and that the image is fixed, but **does not justify the converse** that *every fixed Sha_E class descends satisfying all local Sha_Q conditions* (although global H1-invariants descend because `M_e^{G_E}=0`). This is an expository proof gap unless an additional argument is supplied, not a demonstrated false proposition.

Local obstruction to a naive local-descending argument: take l=3,N=7,e=1 and E=Q(zeta7)^+ (real cyclic degree3). At local v=7, E_w/Q_7 is cyclic, totally ramified of degree3. The cyclotomic character is unramified at7, Frob residue value7, so `M_e^{G_Ew}` is Z/3 because v_3(7^1−1)=1. The inertia quotient C3 acts trivially. Then `H^1(C3,Z/3) = Hom(C3,Z/3) = Z/3`, injecting by local inflation-restriction into kernel `H^1(Q_7,M_e)->H^1(E_w,M_e)`. This exhibits a genuine **local restriction kernel**, so the global Sha descent cannot be deduced from mere local restriction injectivity. It does **not** construct a global Gal-invariant Sha_E class outside image, hence does NOT disprove the global surjectivity claim. The **weaker injection** and consequent `len Sha_l(Q,e) <= len Sha_l(E,e)` are actually all that the manuscript subsequently uses (checked precise reference at later line); those *are proved* in the source. Thus no defect identified in the route to RH or formal proof. Exact finite C3 cocycle enumeration 3 classes and ramification arithmetic PASS; script `riemann_20261123_local_selmer_descent_guard.py/.json`.

Editorial warning: `sec17_twisted.tex` duplicates an identical definition with label `r5:def:eta` twice; this can produce LaTeX duplicate-label warnings, but is only an editor issue, not a mathematical argument defect.

## Status and next

No independent RH proof/disproof, no assertion of a Lean defect. Most promising next work: scrutinize the *specific* high-value new human mathematical assumptions in `sec17_twisted` (not the safe injection), or verify the form of a published theorem on its 23-Nov external boundary against its source. Avoid repeating partial Weil finite-mode work. Do not report the local Sha observation as a verified error in the formally certified Lean archive or notify any author without explicit permission.
