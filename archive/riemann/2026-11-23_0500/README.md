# Riemann research checkpoint - November 23, 2026

> **Historical research record / Archive de recherche.** Imported on 26 November 2026. Mathematical claims, source reports and test outcomes below describe the historical checkpoint. They have not all been independently audited or rerun during this import. No proof of RH is claimed.
> Private operational sections and scheduling metadata have been omitted. All embedded code, data and output blocks have been extracted byte-for-byte into linked files. Source scripts retain their historical paths and dependencies; they are not automatically executed.

**Source record:** `RIEMANN_CHECKPOINT_2026-11-23_0500_EST.md`. **Recorded time label:** 2026-11-23 05:00 EST (from the filename).

[Archive index](../../README.md) · [Manifest](../../manifest.json) · [Verification scope](../../README.md#what-was-checked-during-import)


- Research objective: preserve a source-grounded verification milestone.


## Last prior Riemann checkpoint actually read

Earlier checkpoint `=== RIEMANN CHECKPOINT - 2026-11-08 15:30:58 EST America/Toronto - W12 RATIONAL SUPPORT CERTIFICATE ===`, read in full in the current review. It reported a conditional-on-the-stated-formula complete Weil form lower bound Q(f) > (1/1000)||f||_2^2 for complex smooth f supported only on two endpoint collars of width w=1/12 within (-0.81,0.81). The report used exact Fraction interval arithmetic with parity separation, prime-5 shift, density caps, segmented bins, and a Galerkin diagnostic. Limitations expressly stated there: the core/collar mixed coupling remains unbounded for whole-interval positivity, so there is NO global support positivity theorem and NO RH proof from that route. Earlier auxiliary negative-index bound <=14 remained separate. Scripts were named in that checkpoint and not rerun in this November 23 review; do not silently upgrade their validation status.

## New authoritative external development, November 20-23, 2026

1. On Nov 20 Levent Alpoge published `https://alpo.ge/remark.pdf`, a four-page announcement of a Lean formal proof of RH and of GRH for Dirichlet L-functions, with a 14-part Lean source release. The author explicitly credits Claude as a co-research tool and describes a descendant of Stepanov's method, a Fourier-analytic toy argument, and chaining theta lifts with a suggested length sqrt(X). This primary PDF was opened and its first page visually checked. This is not our group's or this assistant's proof.
2. Primary public verification: Lean FRO and the Mathlib Initiative, joint Nov 21 statement `https://leanprover-community.github.io/blog/posts/riemann-hypothesis/` says they have full confidence in the proof; compile, statement matching to Mathlib's pre-existing RiemannHypothesis, and multiple independent kernel checks satisfy all four verification criteria.
3. Independent detailed audit: Andrew Sutherland (MIT), `https://math.mit.edu/~drew/grh/`, last updated Nov 22 16:20 UTC; 175187 Lean modules compiled; five headline theorems depend only on standard `propext`, `Classical.choice`, `Quot.sound`; 175187 modules passed `leanchecker`; independent Rust kernels nanoda, con-leche, con-ron, lean4lean reported accepted full or module-by-module proofs. con-leche and con-ron comparison accepted all five challenge statements. Two slower full-export checks were still in progress at page-update time. Reported here from the cited primary log, not independently rerun in this container.
4. Primary Lean repository `https://github.com/leanprover-community/riemann-hypothesis` includes the theorem statements and a maintainable community formalization. Its `original` branch preserves the original release. Distinguish this proof from our earlier localized Weil calculations; these are very different strategies. We have NOT checked 17 million lines locally.
5. Clay Mathematics Institute `https://www.claymath.org/millennium/Riemann-Hypothesis/` still labels RH 'Unsolved' when checked on November 23. This official administrative status does NOT invalidate Lean's technical certification; mathematical understanding, traditional review and formal prize acceptance are distinct. Avoid either categorical dismissal or categorical 'Clay-recognized solved'.
6. Separately, Ravi Vakil announced Alessandro Maria Masullo's human-written proposed GRH proof: `https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/`. Vakil added a same-day update reporting problems identified in the draft, and explicitly did not vouch for its correctness. This is NOT independently validated corroboration of Alpoge's claim.

## Research/test passes and adversarial verification

- Source confirmation pass: compared author announcement, official Lean/Mathlib certification, MIT test matrix, community code repository, and Clay status. Result: high-confidence formally checked RH theorem, but formal validation must not be conflated with human explanation, peer review or Clay prize recognition.
- Statement pass: MIT audit shows `riemannHypothesis : RiemannHypothesis` using Mathlib's zeta and nontrivial-zero definition, plus an explicit restatement and Dirichlet L-function zero statements. Standard three logical axioms, no unexplained extra axioms per MIT audit. This report is sourced rather than rerunning kernels.
- Method pass: Stepanov / automorphic theta-lift strategy in author note differs materially from our prior L=0.81 local Weil positivity route. Do not force a nonexistent implication from finite or restricted-support matrices to the global RH statement.
- Critical source-discrepancy pass: a secondary page had claimed theta-lift chain length X; the actual author note on page 1 specifies sqrt(X). Favor primary note. Other early Nov20 sources calling the proof 'not verified' are stale relative to Nov21 Lean certification.
- Computational experiments this review: NONE. No new RH or GRH theorem derived here. No claim to have executed the 175187-module build, to have tested the full proof.
- No independent reproducible new mathematical lemma; the progress is substantial external literature and formal-verification news.

## Open gaps / next steps

- Review any new November 23+ primary verification updates, including whether the two slow full-export checks finish; update source dates accurately.
- Parse a readable explanation of the theta-lift / Stepanov architecture as mathematical papers are released. Extract independently checkable short lemmas, in contrast with 17 million raw lines.
- Acknowledge the strong public formal result while maintaining an adversarial attitude toward exact statement, trusted kernel base, imported axioms, and the distinction between RH and all possible generalized hypotheses.
- Do not repeat finite-dimensional Weil expansions as though they were global RH proofs. Our November 8 core/collar cross-form control remains unsolved and is now a separate methodological study, not a competitor to the formally checked Lean proof.


## Verification status

Live web searches, primary PDF inspection with page screenshot, and MIT/Lean/Clay cross-checks took place in the current conversational turn on November 23 2026. The snapshot is a report of sources actually consulted and tests actually performed, not a claimed new proof.

