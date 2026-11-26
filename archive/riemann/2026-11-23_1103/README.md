# Riemann Proof Watch — append-only checkpoint

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_1103_EST.md`. **Recorded time label:** 2026-11-23 11:03 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)

**Checkpoint time:** 2026-11-23 11:03:08 EST (`America/New_York`). This report supplements the checkpoints of 2026-11-23 10:32 and 10:38 EST. The scientific conclusion is NOT an independently discovered RH proof.

## Scientific continuity

Earlier Riemann checkpoint: November 8 at 15:30:58 EST: a claimed conditional, source-to-code-unreviewed exact-rational Weil lower bound on narrow endpoint collars of `L=0.81`, `w=1/12`, and earlier negative-index estimate ≤14. Those do NOT imply positivity on the whole window or the Riemann Hypothesis. Read the later checkpoint `RIEMANN_SUPPLEMENT_2026-11-23_1038_EST.md`, which already established an exact conditional semiconvexity/adaptive integer grid reformulation of H12 and audited the published 1986 Kaczorowski–Pintz one-sided interval criterion. This run explicitly did **not** duplicate that as new work.


## Fresh sources actually consulted

* Michael Rubinstein et al., *The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, working draft **v2 November 22 2026**, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf . The human guide **assumes** (M), H0–H12 and quotes deep statements from the Lean source; it is *not by itself a completed human proof*. Part II one-sided Landau criterion and Part III.8–III.11 exponent, frame, theta lift, and supply clauses were examined, with screenshots of crucial PDF pages (printed 139, 140, 212, 213). The geometry is fundamentally different from the project's old finite Weil Fourier compressions.
* Andrew Sutherland (MIT), independent verification https://math.mit.edu/~drew/grh/ , page last updated **Nov 23 14:35 UTC**. Reports compilation of **175,187** modules, successful full Lean export kernel replay (normal and paranoid with changed allocator), independent nanoda, con-leche and con-ron, lean4lean, matching original challenge, Comparator v4.33 end-to-end pass; some redundant current-version checks remained running as of page timestamp. Five headline propositions include Mathlib RH and Dirichlet-L zero statements, NOT general Hecke/automorphic GRH. This run **did not** compile 17M lines itself.
* Lean/Mathlib joint note **Nov 21 2026**, https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ . Claims the published formal artifact proves the intended RH theorem in Mathlib under only standard axioms. Distinguish this strong formal certification from the unfinished human readable guide and Clay administrative prize adjudication.
* Authoritative pre-formal positivity source **arXiv v2** (authors on v2 Xuefeng Zhu, unlike the changing arXiv default abstract metadata), https://arxiv.org/html/2608.24827v2 ; unconditional upper bound at L=.8 of `2.27e-17` and lower bound `8.9e-18`. See signed-even and odd Weil conventions. Historical primary Weil criterion https://en.wikipedia.org/wiki/Weil%27s_criterion ; independent Suzuki criterion https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms.12785 .


## Independent micro-pass A — exact error exponent feasibility / quantitative obstacle

From Part III (M): normalized error `E/B <= x^(C ε)*(x/m + xm/k + m + k/n²)`. Put `m=x^a`, `k=x^b`, `n=x^c`. With ONLY these four terms, smallest feasible exponent of the largest error is exactly

`t_bare(c)=max(1/2,(2-2c)/3)` for c≥0.

Proof: the inequalities `1-a<=t`, `a<=t`, `1+a-b<=t`, `b-2c<=t` yield `t>=1/2` and `3t>=2-2c`. Setting `a=1-t,b=2-2t` attains all bounds for this t. Exact Fraction sweep for 5 c and 41*121 rational pairs found no violation.

**Critical structural amendment:** The author guide, printed p.213, says the number-of-words/trace condition forces `k>=8 C_G m^5 f x^ε` **with `f=2n`**, not `f` independent of `n`. On leading exponents this is `b>=5a+c`. With this extra condition, the exact minimax becomes

`t_geometric(c)=max(1/2,(5-c)/6,(2-2c)/3)` for c≥0,

via the same inequalities plus `a<=(t+c)/5`; construct `a=1-t,b=max(1+a-t,5a+c)`. At `t=1/2` one must have `a=1/2`, `b>=5/2+c`, `b<=1/2+2c`, hence **c>=2**. At c=2 exact feasible b=9/2: `m~x^0.5`, `n~x^2`, `k~x^4.5`, matching the guide. Explicit exact rational minimax checks and 7*41*161 constrained grid evaluations passed, including negative-error exponents. **Not a proof that the required q,d, theta lifts or H12 data exist; this is only consistency of the power budget.** Source H12 supplies n a power of 2 near x^(2+8ε). No simplification from falsely treating n as x^1/4.

Script `error_exponents.py`, JSON report `error_exponents.json` (separate ZIP).

## Independent micro-pass B — EXACT test of finite trace/frame Lemma T1

To test the Hilbert–Schmidt trace/rank mechanics of Rubinstein Part III.8 Lemma T1, constructed `p+1` mutually unbiased orthonormal bases of C^p (p=3,5,7): p quadratic chirp bases `v_(a,b)(x)=p^(-1/2) ζ_p^(a x²+b x)` for a,b in F_p plus the computational basis. Verified EVERY ordered pair, with integer-only cyclotomic autocorrelation counting and reduction by `1+z+...+z^(p-1)`, that their inner product squared is 1 (same vector), 0 (different vector in same basis), or 1/p (different bases). For p=3,5,7 numbers of vectors W=12,30,56, and ordered Gram squared histograms respectively `{1:12, 0:24, 1/3:108}`, `{1:30, 0:120, 1/5:750}`, `{1:56, 0:336, 1/7:2744}`. Exact integer trace `Q=sum_v v v*= (p+1)I_p`, `tr Q=S=p(p+1)`, `tr Q²=S²/p`. With `D_*=D=p`, `κ=1/(p+1)≤1/4`, η0=η1=e0=0, the Lemma T1(a)–(c) Hilbert–Schmidt inequalities hold exactly. THIS IS AN ABSTRACT FINITE FRAME, **not** evidence that the automorphic theta lift trace formula (S), (I), (P), count of forms, or H12 is true.

A trivial initial script failure parsing Fraction string '1/3' via `int` was repaired (`Fraction(key)`) and completely rerun. Source PDF text extractor displayed a confusing adjoint order; screenshots of pp139–140 confirmed the actual correct definition `K_ww'=B_w^* B_w'`, thus **no source typo** is claimed. Script `trace_frame_exact.py`, JSON `trace_frame_exact.json`.

## Independent micro-pass C — Weil window spectral falsification

The 2026 arXiv v2 certified even-sector upper at L=.8 `λ_even*(.8) <=2.27×10^-17` (unconditional). Support inclusion implies `λ_even*(.81)<=λ_even*(.8)`. Therefore **any extrapolation of old finite 8-even compression margin 10^-14 into a full L=.81 global bound is FALSE**, with exact ratio `(10^-14)/(2.27×10^-17)=100000/227≈440.53` times too large. This is **not a contradiction** to the older certificate because it explicitly applies only to 8 Fourier modes and never claimed all functions. Exact Fraction audit in `weil_window_monotone_audit.py`. Empirical author frequency scale at L=.81 gives T*≈31.7495 and naive Shannon count≈16.372 (HEURISTIC, not completeness). This independently confirms source and old journal warnings about spectral pollution / missing tail.

## Independent micro-pass D — analytic / formal small checks

`analysis_passes.py`: separately checked hinge Mellin kernel `∫_n^∞(x/n−1)x^(−s−1)dx=n^(−s)/(s(s−1))` numerically for s=1.5,2,3.2 and n=2,7; computed G(x) for seven x≤200 and compared the first 60 positive zeta-zero truncated explicit formula (only numerical diagnostics, no infinite remainder control); evaluated source four error terms with explicit parameters. First run accidentally attempted to integrate an infinite-range G defined using Lambda sieve cut off at 300 (INVALID test; abandoned), and a 400-high-precision-zero run was too expensive (timed out); reran bounded tests, no proof claims.

`independent_audits.py`: gamma tail localization checks for Part II Landau proof at σ=252, selected U=1,2,5,10,20 with j≈1.25(σ−2)U: tail masses shrink from ~5e-4 to ~3e-50, below source `exp(−.008j)` for tested values. Tested p=3,5,7 finite coefficients of height-two formal logarithm from Lagrange inversion; toy integrality/valuation only, NOT deep theta input. `check_mellin_formal.py`: independent finite von Mangoldt Dirichlet series tails at s=2,3,4, N=1e5 (positive, dominated by elementary log-integral bounds), plus **exact Fraction** check `l(U(z))=z mod z^82` for formal `l(u)=u+u^9/3+u^81/9` at p=3. No new RH proof or uniform estimates produced.

## Critical logic / failed approaches / next experiments

* The published Lean artifact has been independently and formally verified, but the human expository draft *deliberately* assumes deep H0–H12 and (M); one should NOT misrepresent those assumptions as a flaw in the formal Lean theorem or as proofs.
* Prior Nov 23 10:38 secondary checkpoint already established a **conditional** finite-grid reformulation of H12. Current source trace shows `n~x²` and at least `k~x^(9/2)` forced by deeper structural constraints, so the smaller grid does NOT automatically reduce geometric construction complexity or establish the still missing uniform node-wise bounds.
* A full-window Weil lower bound 1e-14 at L=.81 would be mathematically refuted by existing unconditional variational upper bound; do NOT extrapolate finite Fourier certificates. Floating eigenvalue signs and finite zeta zero scans are NOT proofs.

* Next highest-value distinct angle: inspect exact H12 clauses and dependency graph for what remains nontrivial after restricting x to integer adaptive nodes; trace one of the deep quantified (H4)/(H5)/(H8) input theorems in the formal proof and distinguish quoted from demonstrated; independently reproduce frame inequality's rank-bound adversarial numerical experiments with correct Hilbert-Schmidt totals; compare same window λ*(L) profile to formal consequence RH⇒strict full-window positivity while avoiding numerical margin claims.

Companion ZIP contains actual scripts and JSON reports from the current run.
