# Beal — signature enumeration, special cases and an obstruction

**Date:** 2026-11-26. **Status:** exact finite arithmetic and an elementary fixed-base argument; no general proof or primitive counterexample.

Beal's conjecture concerns positive integers A,B,C with A^x+B^y=C^z and x,y,z>2. It asserts that A,B,C have a common prime divisor. For a potential primitive positive counterexample put c=C^z, R=rad(ABC), and sigma=1/x+1/y+1/z. Since A^x and B^y are each strictly below c, R<=ABC<c^sigma.

## 1. Exact exponent enumeration

For unordered exponents 3<=x<=y<=z, requiring sigma>=71/105 gives precisely 115 triples:

| Family | Range of z | Count |
|---|---:|---:|
| (3,3,z) | 3..105 | 103 |
| (3,4,z) | 4..10 | 7 |
| (3,5,z) | 5..7 | 3 |
| (4,4,z) | 4..5 | 2 |

This enumeration is reproducible using exact rational inequalities. A threshold t bounds x by floor(3/t), y by floor(2/(t-1/x)), and z by floor(1/(t-1/x-1/y)) when the denominators are positive, as they are in these enumerations. The threshold 89/132 gives 143 triples. The historical journal (7 November 2026) proposes that known generalized Fermat results eliminate many of these signatures; checking the literature, sign conventions, and all reductions remains necessary before asserting a global frontier. **The count of triples is verified; elimination of every corresponding equation is not certified here.**

## 2. Fixed bases 2, 3 and 5

Claim: neither 2^m+3^n=5^k nor 2^m+5^n=3^k has a solution with m,n,k>=3.

Proof: in either orientation, reduction modulo 8 forces n and k even, because odd powers of 3 and 5 have distinct residues and even powers both equal 1 modulo 8. Write U^2-V^2=2^m, where U and V are powers of the distinct odd primes 3 and 5, each with exponent at least 2. The positive integers (U-V)/2 and (U+V)/2 are coprime, since any common divisor divides both U and V. Their product is 2^(m-2). The smaller factor must be 1. Thus U=V+2 and V+1=2^(m-2). Yet V+1 is 2 or 4 modulo 8 if V is a power of 3, and 2 or 6 modulo 8 if V is a power of 5. It is strictly larger than 4 and cannot be a power of 2. Contradiction. This is an elementary special case, not an originality claim. A separate bounded regression checks all exponents 3..59.

## 3. An obstruction to an overstrong abc argument

The exact identity 2+109*3^10=23^5=6,436,343 has radical 15,042. Integer arithmetic verifies 6,436,343^71 > 15,042^105. Therefore the unconditional inequality c<=rad(abc)^(105/71) cannot hold for all coprime positive abc triples. A proof specific to Beal would need additional structure, since these terms are not all perfect powers of exponent at least 3.

## 4. Literature audit and next step

Historical leads: signatures (3,5,7) and (3,4,11), and a claimed result [arXiv:2609.26996](https://arxiv.org/abs/2609.26996) noted in the journal. The claim and its hypotheses have not been independently accepted in this collection. Review [Laishram and Shorey, Explicit abc-related work](https://www.isid.ac.in/~shanta/PAPERS/ABCExplicitI.pdf), separating conditional from unconditional statements. See [Beal Bank's conjecture and prize page](https://www.bealbank.com/who-we-are/our-founder/the-beal-conjecture/) for status. The enumeration, fixed-base regression, and abc identity are verified by the public script; the proposed literature-based frontier is not a proved result here.
