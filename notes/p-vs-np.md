# P vs NP — exact finite experiments and decision versus counting

**Date:** 2026-11-26. **Status:** reproducible finite tests and elementary reduction; no solution of P vs NP.

## 1. Structured 3-CNF instance

Let b_1,...,b_18 be Boolean variables and let F be the conjunction of 16 clauses (b_i OR b_(i+1) OR NOT b_(i+2)), for i=1,...,16. Encode b_i as bit i-1 of integer x in [0,2^18). The full truth table is reproduced by the verifier using both ordinary clause evaluation and the independent compact expression

```
((x | (x >> 1) | ~(x >> 2)) & 65535) == 65535
```

Of 262,144 assignments, 10,945 satisfy the formula and 251,199 do not. The SHA-256 of the sequence of little-endian uint32 Boolean outputs (0 or 1, increasing x) is 5af5b258801a1138709617d3dceb6c4a669ea2b1139f4fea366e7f4b2259657d. Both P106-090 GPUs independently returned this digest in a bounded GPU arithmetic test on 2026-11-26, with host-side verification. The public verifier independently reproduces it. This highly structured instance is not a hard-instance benchmark or evidence of polynomial-time SAT solving.

## 2. Easy decision does not automatically provide easy counting

For a finite simple graph G=(V,E), construct the negative monotone 2-CNF formula

$$ F_G = \bigwedge_{uv\in E}(\neg x_u\lor\neg x_v). $$

The all-zero assignment satisfies F_G. For every assignment, S={v : x_v=1} is an independent set if and only if F_G is true. This is a bijection. Consequently the number of satisfying assignments equals the number of independent sets of G, a #P-complete counting problem under standard counting reductions. Decision restricted to this family is trivial, while exact counting is #P-complete. This does not prove FP differs from #P, and does not resolve what P=NP would imply about exact counting.

The historical journal entry dated 2026-11-08 reports a 198-graph test. A fresh replication, not a recreation of the historical random sample, checks 33 structured graphs and 165 deterministic random graphs of sizes 2 through 12, evaluating independent sets and Boolean assignments independently. All 198 agree; complete graphs have n+1 independent sets, paths have F_(n+2), and stars have 2^(n-1)+1.

## 3. Research directions, not results

Compare SAT solvers and exhaustive enumeration on families of increasing size, preserving satisfiable and unsatisfiable instances, seeds, input size, verified witnesses, and resource use. Audit arithmetic-circuit-to-Boolean complexity transfers and restrictions on proof systems. A result for a restricted circuit family, a finite exact rank, or a speedup in arithmetic operations alone cannot establish P != NP. More specialized historical candidate bounds and circuit arguments need separate independent review.

## References

- [Clay Mathematics Institute, P vs NP](https://www.claymath.org/millennium/p-vs-np/).
- N. Linial, *Hard Enumeration Problems in Geometry and Combinatorics*, SIAM Journal on Algebraic and Discrete Methods (1986), [DOI 10.1137/0607036](https://doi.org/10.1137/0607036). Bibliographic source recorded in the historical journal; primary text not re-audited for this collection.
- [Chukhin et al., arXiv:2611.07972](https://arxiv.org/abs/2611.07972), historical research lead, not a theorem endorsed here.
