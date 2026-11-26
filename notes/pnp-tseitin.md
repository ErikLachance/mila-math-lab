# Prime-power Tseitin constraints in matching characteristic

**Research note ML-PNP-003.** Historical argument: 8 November 2026. Reconstruction and exact certificate checks: 26 November 2026. Not peer reviewed. No general circuit lower bound or P vs NP resolution is claimed.

## Abstract

For flow constraints over Z/p^k Z, encoded by base-p digits and local forbidden-tuple indicators over F_p, a nonzero total charge yields an explicit bounded-degree certificate in the finite-field function ring. An exact computation for K4 with Z/4 Z edge values distinguishes odd total charge from charge two: the minimum degree in a specified static monomial-multiple filtration is respectively six and seven. This is an encoding-dependent statement, not a lower bound for arbitrary polynomial-calculus derivations.

## 1. Statement and encoding

Orient a finite simple graph of maximum degree Delta. Assign an element of Z/q Z, q=p^k, to each edge, with p prime. At vertex v require signed outgoing-minus-incoming flow equal to charge b_v. Suppose C=sum_v b_v is nonzero modulo q. Encode every edge by k digits in F_p. Work in the quotient by all digit relations x^p=x. For each forbidden local digit tuple a use its indicator delta_(v,a), the product over incident digits of 1-(x-a)^(p-1). The indicator has syntactic degree at most D=(p-1)k Delta.

Define the degree of a static certificate as a bound on the degrees of the products of coefficients and original indicators before reduction by the digit relations. In the quotient a certificate is an identity 1=sum f_(v,a) delta_(v,a). This definition does not identify the minimum such degree with the degree of arbitrary dynamic polynomial calculus.

## 2. Constructive certificate bound

For any digit index j (0<=j<k) such that digit_j(-C mod q) is nonzero, the following construction gives a certificate of degree at most D p^j.

Let r_v be the residue of the signed local flow minus b_v in [0,q), and r_(v,i) its i-th base-p digit. Each r_(v,i) is a function of the local edge digits. It has an interpolating polynomial of degree at most D, namely sum_a r_(v,i)(a) delta_(v,a) over forbidden tuples only. Valid tuples contribute zero.

For a variable X define the coefficient extraction

$$
P_j=[X^{p^j}]\prod_{v}\prod_{i=0}^j
\left(\sum_{t=0}^{p-1}\binom{r_{v,i}}{t}X^{t p^i}\right).
$$

Here binomial(z,t) is the degree-t polynomial z(z-1)...(z-t+1)/t! over F_p. On actual digit valuations, the product equals (1+X)^(sum_v r_v) through the required coefficient, using (1+X)^(p^i)=1+X^(p^i) in characteristic p. Lucas' digit formula makes P_j the j-th digit of sum_v r_v in F_p. Signed incidence cancels globally, so sum_v r_v is congruent to -C modulo q on every valuation. Therefore P_j is the specified nonzero constant in the finite-field function ring.

P_j has degree at most p^j in the residue digits and vanishes if all residue digits are zero. Substituting their indicator expansions, dividing by the nonzero constant, and grouping terms by one indicator factor yields the claimed static certificate of degree at most D p^j. Reduction by x^p=x does not increase degree. For fixed p,k,Delta this bound is independent of graph size. It does not transfer across characteristics or unrelated encodings without a proof.

## 3. K4 over Z/4 Z: exact finite span

Use vertices 0,1,2,3 and orient edges from lower to higher index, in lexicographic order. Edge i uses bits 2i and 2i+1. At each vertex there are 64 local assignments, 16 valid and 48 forbidden. Hence there are 192 degree-six forbidden-tuple polynomials. In the Boolean quotient, V_6 is their linear span; V_7 additionally includes each indicator multiplied by each of its six external variables. Products by local variables reduce to zero or the same indicator. The filtration uses original product degrees, not arbitrary derived low-degree polynomials.

| Charges | rank V_6 | 1 in V_6? | rank V_7 | Static minimum degree |
|---|---:|---|---:|---:|
| (1,0,0,0) | 192 | yes | not needed | 6 |
| (2,0,0,0) | 191 | no | 1227 | 7 |
| (3,0,0,0) | 192 | yes | not needed | 6 |

An independent GF(2) elimination in coefficient-bitset representation reconstructs these results. The middle row uses 1,344 rows (192 original, 1,152 external-variable multiples) and produces a sum of 384 rows equal to the constant polynomial 1. For each odd-charge example the explicit certificate uses 128 rows. All combinations are checked coefficient by coefficient. Full certificates, generator indices and multiplier bits are recorded in the JSON output; a multiplier index of -1 denotes the original indicator. Generators are ordered by vertex then local integer assignment, skipping valid assignments.

For the upper bound seven in the middle case, there is also a direct identity. Write b_v=c_v+2d_v, low/high edge bits u_e,w_e, t_v=sum_(e incident v)u_e, z_v=sum_(e<f incident v)u_e u_f in F_2. Put L_v=t_v+c_v and H_v=sum_inc w_e+sum_in u_e+z_v+d_v. Both vanish on valid local assignments. In the Boolean quotient,

$$
\sum_v d_v+\sum_{v<w}c_v c_w
=\sum_v H_v+\sum_{v<w}(L_vt_w+c_vL_w).
$$

Indeed sum_v t_v=0, and sum_(v<w)t_v t_w=sum_e u_e+sum_v z_v by counting incidences modulo two. If C=2 mod 4 the left side is one. If C is odd, sum_v L_v=1. Expressing the local L_v,H_v as combinations of forbidden indicators gives static degrees at most 2Delta+1 and 2Delta respectively.

## 4. Limitations and next work

The exact lower bound here is nonmembership in V_6. Dynamic polynomial calculus can multiply polynomials after cancellations; no claim about its minimum derivation degree follows just from this finite span calculation. Neither this matching-characteristic construction nor the small K4 examples establish a separation of P and NP. A novelty review and a comparison with other encodings and proof systems remain necessary.

Background: Buss, Grigoriev, Impagliazzo and Pitassi, [Linear gaps between degrees for the polynomial calculus modulo distinct primes](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/lineargaps/index.html); see also the project's [formal contraction and Boolean generator note](pnp-advanced-20261109.md). The construction and finite certificate check above are presented with their own definitions, not attributed to that background paper.

**Reproduce:** run node experiments/certificates-20261126.mjs. The result key tseitin contains all three certificates. See [exact output](../results/certificates-20261126.json).
