# Beal — 36 auxiliary ternary cubics and nine 3-adic exclusions

Historical checkpoint: 8 November 2026 (research run 32). Public reconstruction: 26 November 2026.

**Conditional scope:** the historical descent for A^3+B^4=C^11 requires a rational root of a particular auxiliary equation and a sequence of ideal/class-group/unit arguments. The rational-root prerequisite is unproved. The descent itself has not been independently re-certified for this edition. The local calculation below proves a fact about explicit cubics, not exclusion of the full (3,4,11) signature or Beal's conjecture.

## Defined family

Work in the cubic algebra with basis 1,beta,beta^2 and beta^3=-15-9beta-4beta^2. Put p3=-2+2beta+beta^2, p5d=-2-beta, p5s=-5-beta-beta^2, p11=1+3beta+beta^2, e=26+15beta+2beta^2.

For u=1 let delta run over the eight positive divisors of 165; for u=5 let delta run over the four positive divisors of 33. For k=0,1,2 form H=p3^[3|delta] p5d^[5|delta] p11^[11|delta] p5s^[11*(u=5)] e^k. Define F_H as the beta^2 coefficient of H(x+y beta+z beta^2)^3. Divide the integer coefficient vector by its positive gcd to get the primitive polynomial. This defines 36 explicit cubics. All coefficients are available in the new JSON result.

With monomial order (x^3,x^2y,x^2z,xy^2,xyz,xz^2,y^3,y^2z,yz^2,z^3), the historical coordinate vectors for the cube are

G0=(1,0,0,0,-90,180,-15,180,-315,105),

G1=(0,3,0,0,-54,63,-9,63,-9,-42),

G2=(0,0,3,3,-24,21,-4,21,-21,25).

For H=(h0,h1,h2), the coefficient vector of F_H is h2 G0+(h1-4h2)G1+(h0-4h1+7h2)G2.

## Exhaustive local obstruction

Every projective Q3 point has a representative with integral 3-adic coordinates, at least one a unit. Normalize the first unit to 1. Modulo 27 there are exactly 1,053 canonical representatives: (1,y,z) with y,z arbitrary; (x,1,z) with x divisible by 3; and (x,y,1) with x,y divisible by 3. These three patches are disjoint.

The new verifier uses exact BigInt arithmetic to reconstruct H and the primitive coefficients, then evaluates every one of these classes for each cubic. It reproduces the nine zero-count twists:

| u | delta | k excluded |
|---:|---:|---|
| 1 | 33 | 0,1,2 |
| 5 | 3 | 0,1,2 |
| 5 | 33 | 0,1,2 |

Thus these nine explicit curves have no Q3 point, hence no rational point. The other 27 have primitive residues modulo 27; this **does not by itself prove Q3 solubility**. The historical checkpoint reports additional Hensel checks, which have not been repeated here. The stronger conclusions about conditional descent branches require verifying the full antecedent.

## What is still missing

The auxiliary rational-root assumption, global ideal/unit descent audit, and rational-point analysis of the 27 remaining twists are not closed. No claim that the general Beal conjecture is almost solved follows from this calculation. Other historical lines include (3,5,7), (3,17,19), and auditing claimed results. See [Beal's official conjecture page](https://www.bealbank.com/who-we-are/our-founder/the-beal-conjecture/) and the historical research lead [arXiv:2609.26996](https://arxiv.org/abs/2609.26996), which is not endorsed as a valid proof here.

Reproduce with node experiments/recheck-historical.mjs; the JSON includes all 36 cubics and counts. This is a public reconstruction of the local test, not the original checkpoint scripts or a certificate of the upstream descent.
