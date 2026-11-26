# MILA Mathematical Research Lab

Independent AI-assisted mathematical research and reproducible computational experiments. / Laboratoire indépendant de recherche mathématique assistée par IA.

**Initial research collection — 26 November 2026.** No solution of P vs NP, the Riemann hypothesis, or Beal's conjecture is claimed. These are research notes, not peer-reviewed publications. Novelty and prize eligibility have not been established.

[Project homepage source](docs/index.html) · [Reproduction output](results/independent-reproduction.json)

## Research programs

| Program | Public notes | Status |
|---|---|---|
| P vs NP | [SAT and counting](notes/p-vs-np.md) | Exact finite tests; elementary reduction; no asymptotic separation |
| Beal | [Signatures and fixed bases](notes/beal.md) | Exact enumeration and special cases; literature frontier under audit |
| Riemann | [Möbius and Mertens](notes/riemann.md) | Finite exact calculations; no global conclusion |
| Computing | [Two-GPU validation](notes/compute.md) | Local 120-second prototype succeeded; no unattended service claimed |

## Reproduce

Python 3.10+; standard library only:

```sh
python3 experiments/verify.py
```

The verifier evaluates a structured 18-variable SAT instance in two ways, checks 198 graphs in a fresh deterministic replication, enumerates Beal signatures with rational arithmetic, and computes Mertens endpoints up to 100 million. It does not independently check every Möbius value to 100 million.

The original two CPU Mertens scripts are also in [experiments/mertens/](experiments/mertens/). The larger script uses Linux fork multiprocessing and substantial CPU/RAM resources; run it intentionally, not as an automatic install.

## Research integrity

Distinguish elementary proofs, cited results, finite experiments, conjectures, conditional arguments and rejected approaches. Report inputs, scope, method, reproducibility evidence and limitations. Faster exhaustive search is not a polynomial-time algorithm. A finite test cannot establish an unbounded conjecture.

The historical research journal is private; only reviewed research excerpts and selected sanitized results are included here. Further historical arguments require independent mathematical and privacy review. Corrections and replication reports are welcome through Issues or pull requests.

## Citation and license

MILA Mathematical Research Lab, *Initial research collection*, 2026-11-26, version 0.1.0, AI-assisted research notes and code. Human-maintained independent project, not affiliated with OpenAI, Clay Mathematics Institute, or the Beal prize.

See [LICENSE](LICENSE) for Apache License 2.0. External works are cited for reference and remain subject to their own rights.
