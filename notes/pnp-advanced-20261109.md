# P vs NP — formal contraction bounds and finite Boolean generator certificates

Historical research checkpoints: 9 November 2026. Public reconstruction and rechecks: 26 November 2026. These notes are not peer reviewed. **No separation of P and NP, new general PIT algorithm, or asymptotic circuit lower bound is established.**

## P7: sharp bound for a specified formal exponent envelope

Let a,b,b',c be nonnegative, d=a+b+b'+c>0, with d/3<a+b,a+b'<=2d/3. For a sorted triple x>=y>=z>=0 define U=x+y if z(x+y)<=xy, and U=(xy+yz+zx)^2/(4xyz) otherwise. Define

- E1=max(U(a,b,c),U(a,b',c),a+c);
- E2=max(U(b,a,b'),U(b,c,b'),b+b');
- E=min(E1,E2).

Here U is symmetric by sorting its arguments. With A=max(a,c), B=max(b,b'), t=min(a,b,b',c), coordinatewise monotonicity and the pair-sum lower bounds of U yield E=U(A,B,t). This reduction was independently checked by enumerating the admissible integer profiles.

Set s=A+B. The admissibility inequalities and their complements give d/2<=s<=2d/3, and t<=(d-s)/2, t<=min(A,B). In the active branch U=s+(ts-AB)^2/(4ABt). Since AB=t(s-t)+(A-t)(B-t)>=t(s-t) and 0<ts-AB<=t^2,

$$ E\le s+\frac{t^2}{4(s-t)}\le s+\frac{(d-s)^2}{8(3s-d)}. $$

The inactive branch E=s satisfies the same bound. For u=s/d in [1/2,2/3], f(u)=u+(1-u)^2/[8(3u-1)] has derivative (5u-1)(15u-7)/[8(3u-1)^2]>0. Thus E<=49d/72. Equality is attained at (a,b,b',c)=(d/2,d/6,d/6,d/6). Relative to a formal 5d/6 cost, this is an improvement of 11d/72 in the exponent; it is **not a verified algorithmic speedup**.

Current recheck: 312,850 admissible integer quadruples for d=2..72 passed the exact integer comparisons, including the reduction and equality-profile checks. The formula's bounded-integer arithmetic is exactly representable in JavaScript Number on this finite domain.

The historical checkpoint cites [Chukhin et al. arXiv:2611.07972](https://arxiv.org/abs/2611.07972), [Amanov, van den Berg and Zuiddam arXiv:2610.30054](https://arxiv.org/abs/2610.30054), and [Pass arXiv:2610.28627](https://arxiv.org/abs/2610.28627) as the research context. These papers' complete hypotheses and implications are not re-certified here. The bridge to a uniform bit-complexity algorithm with rational bilinear identities, coefficient growth and one-sided cutoff remains open.

## P3: exact minimum annihilator degrees for a fixed 13-to-14 Boolean map

Over F2 let F be the triangular bijection on 13 bits with first-three-bit permutation [5,3,1,4,6,7,0,2] (little-endian indexing), and y_i=x_i+x_a*x_b for i=3,...,12. The ordered pairs (a,b) are (2,0),(3,1),(2,3),(5,3),(6,5),(6,0),(8,6),(9,8),(10,9),(11,4).

Append a bit z=g(x2,x8,x12), with g interpreted as an eight-bit truth table. For g=60,105,150,195, the original checkpoint found an exact degree-four annihilator and no degree-at-most-three annihilator. A common multiplier B(y) consists of the sum of squarefree monomials with masks [0,2,4,8,16,5,10,18,12,20,21,14]. Put h(y)=g(F^-1(y)) and reduce A=hB modulo y_i^2=y_i. Then Q(y,z)=zB(y)+A(y) is nonzero and vanishes on the graph. The current verifier reconstructs A by the Boolean Möbius transform, checks every one of the 8,192 graph points, and independently ranks all 470 degree-at-most-three evaluation columns. Full rank excludes a lower degree relation.

| Truth table g | Terms in A | Rank through degree 3 | Exact minimum degree |
|---:|---:|---:|---:|
| 60 | 24 | 470 | 4 |
| 105 | 32 | 470 | 4 |
| 150 | 44 | 470 | 4 |
| 195 | 36 | 470 | 4 |

For a different appended bit z=g(x10,x11,x12) with g=23, Q=z*y9*y10*y12*(1+y8) vanishes at all 8,192 graph points. The rank of the 1,471 degree-at-most-four monomials is 1,471; the minimum degree is exactly five. Both findings were freshly rechecked, not merely copied. They concern this explicit map only. No general NC0 hardness or growing-family lower bound follows. Context: [Gajulapalli et al. arXiv:2303.05044](https://arxiv.org/abs/2303.05044).

## Further historical work not yet reproduced in this public collection

The later 9 November checkpoint reports 100 exact four-index contraction/Strassen comparisons, 240 rational-scaling multiplication cases with 55,872 exact integer divisions, and a Tseitin encoding of IP_b with 4b-1 variables and 7b-4 clauses, uniquely extended for each original input. It also records characteristic-p cancellation: a satisfiable formula with exactly p solutions has count zero mod p, while a generating polynomial with distinct assignment monomials need not vanish identically. These are historical records; their original scripts have not been recovered for this edition. No one of them proves a general complexity separation.

## Reproduce

Run node experiments/recheck-historical.mjs from the repository root. See the matching JSON in results/. This is an independent reconstruction, not the original historical scripts. The novelty of these finite/elementary findings is not asserted.
