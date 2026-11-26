# MILA Mathematical Research Lab

Independent AI-assisted mathematical research / Recherche mathématique indépendante assistée par IA.

**Research collection 0.4.0 — 26 November 2026.** [Scientific website](https://eriklachance.github.io/mila-math-lab/) · [Research catalog](https://eriklachance.github.io/mila-math-lab/catalog.html) · [Reproducibility](https://eriklachance.github.io/mila-math-lab/methods.html) · [Bibliography](https://eriklachance.github.io/mila-math-lab/references.html)

No solution of P vs NP, Beal's conjecture, or the Riemann hypothesis is claimed. Research notes are not peer reviewed; novelty and prize eligibility are not established. We distinguish elementary proofs, finite certificates, conditional deductions, formal arguments and unresolved steps.

## Research notes

| Identifier | Research note | Historical source date |
|---|---|---|
| ML-PNP-004 | [Exact integer recursion for fixed rational bilinear matrix identities](notes/pnp-rational-recursion.md) | 2026-11-09 |
| ML-BEAL-004 | [Valuation obstructions to the rational-root reduction for (3,4,11)](notes/beal-rational-root-obstruction.md) | 2026-11-08 |
| ML-RH-004 | [A Carleman obstruction at a spatial interface in the Weil form](notes/riemann-carleman-obstruction.md) | 2026-11-08 |
| ML-PNP-003 | [Prime-power Tseitin constraints in matching characteristic](notes/pnp-tseitin.md) | 2026-11-08 |
| ML-BEAL-003 | [Local arithmetic of 36 auxiliary ternary cubics](notes/beal-local-points.md) | 2026-11-08 |
| ML-RH-003 | [Rational enclosures for a compact-window Weil-form estimate](notes/riemann-intervals.md) | 2026-11-08 |
| ML-PNP-002 | [Formal contraction bounds and finite Boolean generators](notes/pnp-advanced-20261109.md) | 2026-11-09 |
| ML-BEAL-002 | [Thirty-six auxiliary cubics and nine 3-adic exclusions](notes/beal-advanced-20261108.md) | 2026-11-08 |
| ML-RH-002 | [A compact-window spectral candidate: codimension 361](notes/riemann-advanced-20261108.md) | 2026-11-08 |
| ML-PNP-001 | [SAT enumeration and decision versus counting](notes/p-vs-np.md) | 2026-11-26 |
| ML-BEAL-001 | [Exponent signatures, fixed bases and an abc obstruction](notes/beal.md) | 2026-11-07 |
| ML-RH-001 | [Exact Möbius and Mertens computations](notes/riemann.md) | 2026-11-26 |

Public reconstruction and verification: 26 November 2026. See [research archive index](notes/research-archive.md) for the selected scope. The private research journal is not published.

## Reproduction

Python 3.10+ and Node.js with BigInt support; standard libraries only.

```sh
python3 experiments/verify.py
node experiments/recheck-historical.mjs
node experiments/certificates-20261126.mjs
node experiments/frontier-20261126.mjs
```

Verification outputs: [frontier arguments and countertests](results/frontier-20261126.json) (including illustrative floating-point quadrature), [finite checks](results/independent-reproduction.json), [historical rechecks](results/historical-recheck-20261126.json), [explicit certificates](results/certificates-20261126.json). The original [Mertens scripts](experiments/mertens/) are provided for deliberate reproduction. The [compute pilot](notes/compute.md) is supporting technical documentation, not a mathematical publication.

## Integrity and contributions

Finite tests do not establish asymptotic theorems. Static certificate degree is not dynamic polynomial-calculus degree; local solubility is not global solubility; a fixed-window estimate is not RH. Corrections and independent checks are welcome in [Issues](https://github.com/ErikLachance/mila-math-lab/issues) or pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md), and [CITATION.cff](CITATION.cff).

[Apache License 2.0](LICENSE). Independent project; no affiliation with OpenAI, Clay Mathematics Institute or the Beal prize.
