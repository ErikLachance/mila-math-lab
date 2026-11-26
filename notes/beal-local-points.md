# Local arithmetic of 36 auxiliary ternary cubics

**Research note ML-BEAL-003.** Historical checkpoints: 8 November 2026, runs 31–32. Reconstruction: 26 November 2026. Not peer reviewed.

## Abstract

For the 36 explicitly defined cubic forms from the project's conditional (3,4,11) descent, an exact local recheck constructs a strong Hensel witness over Q_3 for each of the 27 forms with nonzero primitive residue counts modulo 27. The other nine have no Q_3 point. For all 36 forms, simple-root witnesses are also exhibited at thirteen further primes. These are facts about the explicit auxiliary forms; the descent from a hypothetical generalized Fermat solution is not established by these tests.

## 1. Necessary hypotheses in the proposed descent

For a hypothetical primitive positive A^3+B^4=C^11, the historical argument assumes, additionally, that the rational function equation F(t)=A^3/C^11 has a rational root, where

$$
Q(t)=1+4t+10t^2+20t^3+35t^4+56t^5+84t^6+120t^7,\quad
F(t)=1-(1-t)^4 Q(t)=t^8(165-440t+396t^2-120t^3).
$$

The rational-root prerequisite remains unproved. The historical number-field descent also requires a verified ideal-factorization and unit-class analysis. It leads to the candidate family in [ML-BEAL-002](beal-advanced-20261108.md), not to a proven equivalence with the original equation. In particular, points on the auxiliary cubic must satisfy additional integrality, coprimality and fourth-power restrictions to be relevant to the original Diophantine equation.

## 2. Independent construction and local certificates

In the cubic ring with beta^3+4beta^2+9beta+15=0, the verifier constructs the coefficient of beta^2 in H(x+y beta+z beta^2)^3 by direct multiplication and reduction, using the explicit twists H of ML-BEAL-002. It divides the resulting coefficient vector by its gcd. The new construction was cross-checked against all 36 prior coefficient vectors and all prior modulo-27 counts.

Normalize the first unit coordinate of a projective residue to one. Over Z/27 Z this gives 27^2+9*27+9^2=1053 classes, all examined per cubic. The three pairs (u,delta)=(1,33),(5,3),(5,33) are excluded for every k=0,1,2. The absence of any primitive residue implies absence of Q_3 points, since any projective Q_3 point can be scaled to integral coordinates with a unit coordinate.

For each remaining curve, the new certificate fixes a unit coordinate equal to one and holds one of the other two coordinates constant. It exhibits an integer value x0 of the remaining coordinate such that

$$
v_3(F_H(x_0))>2v_3(F_H'(x_0)).
$$

The derivative is with respect to the free coordinate, not the normalized one. Strong Hensel's lemma gives a root in Z_3 while the unit coordinate stays one. A zero value of F_H is treated as infinite valuation. Thus each of the 27 surviving curves has a certified Q_3 point, not merely a solution modulo 27.

For example, on the twist u=1, delta=3, k=0, the normalized point (0,1,17) gives F_H=492318 and partial_z F_H=90873, of valuations five and two, respectively. This passes the strict Hensel inequality. The JSON contains values and derivative coordinates for every witness.

## 3. Additional local primes

For each of the 36 forms and each p in {2,5,7,11,13,17,19,23,29,31,37,41,43}, the verifier finds a normalized projective point modulo p with a nonzero partial derivative in a free coordinate. Ordinary Hensel lifting supplies a Q_p point. This is 468 explicit local certificates, not a test of every prime.

The global rational-point question for the 27 curves not excluded at p=3 remains unresolved by these checks. Local solubility at tested primes is not global solubility. Even a rational point on an auxiliary cubic would not establish a solution of the original generalized Fermat equation.

## 4. Research directions

Independently audit the rational-root prerequisite and all ideal/unit derivations before transferring the local exclusions upstream. For the remaining curves, investigate certified rational points or a descent with the additional fourth-power and integrality restrictions. Keep the separate (3,5,7) literature claim distinct: [Peter Chocian, arXiv:2609.26996](https://arxiv.org/abs/2609.26996) announces a computer-assisted result for that signature; this collection does not certify its full proof or claim that Beal follows.

**Reproduce:** node experiments/certificates-20261126.mjs; [exact output](../results/certificates-20261126.json), key beal_local. No special algebra system or GPU is needed.
