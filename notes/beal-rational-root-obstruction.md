# Valuation obstructions to the rational-root reduction for (3,4,11)

**ML-BEAL-004.** Historical descent prerequisite: 8 November 2026. Explicit image-obstruction reconstruction: 26 November 2026. Not peer reviewed.

## Abstract

The polynomial used in our proposed conditional reduction of the generalized Fermat signature (3,4,11) is not surjective on the rational points of the open unit interval, even when its argument is allowed to range over all rational numbers. A simple valuation calculation gives necessary restrictions on its rational image. In particular, a hypothetical primitive solution with a denominator base divisible by 2 or 3 cannot satisfy the proposed additional rational-root hypothesis. This is an obstruction to the method, not to those solutions of the original equation.

## 1. The polynomial and its rational image

Put

$$
F(t)=t^8(165-440t+396t^2-120t^3).
$$

The auxiliary identity from ML-BEAL-003 is F(t)=1-(1-t)^4Q(t), where Q(t)=1+4t+10t^2+20t^3+35t^4+56t^5+84t^6+120t^7. The derivative is F'(t)=1320t^7(1-t)^3, so F is strictly increasing from 0 to 1 on (0,1). This real surjectivity does not imply rational surjectivity.

For t=m/n in lowest terms with n>0, define P_h(n,m)=165n^3-440n^2m+396nm^2-120m^3. Then F(m/n)=m^8 P_h(n,m)/n^11. For a prime p write v_p for its normalized valuation; v_p(0)=infinity.

## 2. Exact necessary valuations

If 2 does not divide n, F(m/n) is 2-adically integral. If 2 divides n, then m is odd. If v_2(n)>=2, the term -120m^3 has valuation 3, while all other terms have valuation at least 4. If v_2(n)=1, the first, third and fourth terms each have valuation 3 and the second has higher valuation. Dividing by 8 leaves the sum of three odd integers and one even integer, which is odd. Thus in either case v_2(P_h)=3.

Similarly, if 3 divides n, m is a 3-adic unit. The last term has valuation 1, and each other term has valuation at least 2. Thus v_3(P_h)=1. If 3 does not divide n, the value is 3-adically integral.

Consequently every nonzero value r=F(t) for rational t satisfies

$$
v_2(r)<0\ \Longrightarrow\ v_2(r)=3-11a,\quad a\ge1,
$$
$$
v_3(r)<0\ \Longrightarrow\ v_3(r)=1-11b,\quad b\ge1,
$$

for integers a,b. In particular 1/2 has no rational preimage, since its 2-adic valuation is -1. The obstruction holds for t outside (0,1) as well, so allowing signed numerators does not fix this example.

## 3. Consequence for the proposed descent

Suppose a hypothetical primitive positive solution satisfies A^3+B^4=C^11. Then gcd(A,C)=1, because a prime dividing both must divide B as well. If p=2 or 3 divides C, the ratio r=A^3/C^11 has valuation -11v_p(C). This is incompatible with the corresponding necessary image condition above.

Therefore the additional hypothesis F(t)=A^3/C^11 with t rational is impossible in those cases. It does **not** follow that C must be coprime to 6 for every primitive solution of the original equation. It only follows for solutions in the restricted rational-root branch. A global proof by this descent needs an independent argument covering all primitive solutions, including the cases outside the rational image.

Even the perfect-power ratio 1/2^11 lies outside the rational image; it is not asserted to be associated with a Beal solution. These examples expose why real intermediate-value arguments are insufficient.

## 4. Verification and boundary of the result

The verifier checks the polynomial identity with Q_h and the valuation statements over signed numerators of magnitude at most 128 and positive denominators at most 128, restricted to coprime pairs. The decisive proof is the elementary valuation argument above, not that finite range. It does not certify the existence or nonexistence of a rational root for every admissible primitive solution with C coprime to 6. The 36 auxiliary cubics in ML-BEAL-002/003 remain a restricted conditional family.

**Reproduce:** node experiments/frontier-20261126.mjs; [results](../results/frontier-20261126.json), key rational_root. See [ML-BEAL-003](beal-local-points.md).
