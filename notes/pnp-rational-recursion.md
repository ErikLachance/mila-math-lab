# Exact integer recursion for fixed rational bilinear matrix identities

**ML-PNP-004.** Historical research question: 9 November 2026. Reconstruction and extension: 26 November 2026. Not peer reviewed.

## Abstract

A fixed rational bilinear matrix multiplication identity can be implemented recursively over integers by clearing denominators in each of its three linear maps and normalizing exactly at every node. We give a magnitude bound for all intermediate data, including partial sums with cancellation, and a corresponding bit-complexity bound. The conclusion is conditional on a specified fixed identity and does not construct an improved polynomial identity testing algorithm.

The denominator-clearing recursion and logarithmic growth of intermediate bit lengths already appear in [Pass, Section 4.3](https://arxiv.org/html/2610.28627v2#S4.SS3). This note is a reconstruction and elaboration with a rectangular formulation, an explicit magnitude guard, and additional exact tests. The underlying simulation principle is not claimed as a new discovery.

## 1. Base identity and normalization

Fix positive integer dimensions a,b,c and a rank-r rational identity for multiplying a-by-b by b-by-c matrices. Flatten input and output blocks in row-major order. Let U and V be the r-by-ab and r-by-bc linear maps, and W the ac-by-r recombination map. The identity is

$$
(XY)_j=\sum_{i=1}^r W_{ji}(UX)_i(VY)_i.
$$

Choose positive integers D_U,D_V,D_W clearing the denominators separately in the three maps. Write the corresponding integer matrices U',V',W', and D=D_U D_V D_W. The numerator identity with these maps equals D times the output. It can be checked on all pairs of input basis matrices, by bilinearity. It also holds for rectangular matrix blocks under ordinary block multiplication: the order of the left and right factors is unchanged.

At depth h multiply matrices of dimensions a^h by b^h and b^h by c^h. At each node use U',V' to form integer blocks, recursively multiply, use W' to recombine, and divide each output entry by D. Induction on depth proves exactness of every division and equality to ordinary integer matrix multiplication. No assumption of exact floating arithmetic is required.

## 2. Bound on intermediate magnitude

Let A,B,C be the maximum absolute row sums of U',V',W' respectively, each increased to at least one. Let M>=1 bound the absolute input entries. At recursion depth d, the input entries are bounded by A^d M and B^d M. This follows by applying the triangle inequality to each row, even during partial sums. Each recursively computed child product at depth d+1 has inner dimension b^(h-d-1), hence entries bounded by b^(h-d-1)(AB)^(d+1) M^2.

During recombination at depth d, each coefficient multiplication and partial sum has magnitude at most

$$
C b^{h-d-1}(AB)^{d+1}M^2.
$$

Thus all input, product and recombination intermediates (apart from fixed identity constants) are bounded by

$$
H=C M^2(ABb)^h.
$$

For a signed integer representation the bit length, including a sign allowance, is O(log M + h) with constants depending only on the fixed identity. An implementation can also include D in its guard bound. This bound does not require positive matrix entries or the absence of cancellation.

## 3. Operation and bit complexity

For one fixed identity the scalar arithmetic cost satisfies a recursion with r children and overhead O((ab)^(h-1)+(bc)^(h-1)+(ac)^(h-1)), with fixed identity-dependent constants. The rank of the multiplication tensor is at least each of ab, bc and ac by its three flattenings. Summing the recursion therefore gives O((h+1)r^h) scalar operations, including exact divisions by the fixed integer D. With schoolbook integer arithmetic on O(log M+h)-bit values, a sufficient bit-cost bound is

$$
O((h+1)r^h(1+\log M+h)^2).
$$

This is a fixed-identity simulation statement. To transfer the formal envelope of ML-PNP-002 to a particular uniform algorithm, one still needs the appropriate rational identities, a fixed-epsilon construction, input-size and padding accounting, and the exact cutoff and promise handling of that algorithm. We do not infer an improved PIT theorem or a circuit lower bound from this lemma alone.

## 4. Exact reproduction

The new verifier rescales individual rank terms by unequal signed rational factors: the left and right linear forms are scaled and the output weights divided by their product. It clears all three maps independently, checks the base tensor on every basis pair, then compares recursively normalized products with ordinary integer multiplication. Tested identities: Strassen's 2-by-2 square identity and classical rectangular identities with dimensions (2,3,2), (2,2,3), (3,2,2). Depths 1 through 3, 8- and 40-bit magnitude bounds, and random, zero, alternating-sign and sparse inputs are covered.

The exact test results are in the companion JSON. Each checked scalar division is exact; coefficient products and partial sums are checked against H. These finite tests illustrate the general bound, not a claim to have constructed asymptotically fast rectangular identities.

## References and remaining work

Rafael Pass, [Matrix Multiplication from Polynomial Packings](https://arxiv.org/abs/2610.28627), v2, 30 October 2026; Alimzhan Amanov, Maxim van den Berg and Jeroen Zuiddam, [Multiplying matrices via polynomials: exposition and barriers](https://arxiv.org/abs/2610.30054), 21 October 2026; Nikolai Chukhin et al., [A Little Derandomization Goes a Long Way](https://arxiv.org/abs/2611.07972), 5 November 2026. These sources motivate the problem; the lemma here does not certify all their claims or imply a new result about P vs NP. The prior historical test used scaled square identities only; the current reconstruction includes rectangular block shapes and independently cleared maps.

**Reproduce:** node experiments/frontier-20261126.mjs; [results](../results/frontier-20261126.json), key matrix. See [ML-PNP-002](pnp-advanced-20261109.md).
