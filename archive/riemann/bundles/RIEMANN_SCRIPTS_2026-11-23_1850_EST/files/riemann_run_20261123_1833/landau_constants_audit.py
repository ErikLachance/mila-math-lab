"""Independent exact-rational check of the numerical choices in
Rubinstein 2026-11-22 Part II §1 sparse-window Landau argument:
eta=max((4/5)e^(1/5),(6/5)e^(-1/5)), c=1/125, sigma>=252.
Only finite constant inequalities, NOT the analytic lemma or RH.
"""
from fractions import Fraction as F
from math import factorial
import json

def esum(x,N):return sum((x**k/F(factorial(k))) for k in range(N+1))
def exp_upper(x,N):
    assert x>=0 and F(N+2)>x
    return esum(x,N)+(x**(N+1)/F(factorial(N+1)))/(1-x/F(N+2))
c=F(1,125)
checks={
    'eta_right_branch_max':exp_upper(F(2,5),12)<F(3,2),
    'c_smaller_than_log_ratio': F(6,5)*(2*exp_upper(c,10)-1)<esum(F(1,5),10),
    'sigma252_dominates_theta0_ratio':esum(c,2)>F(126,125),
    'eta_less_than_one': F(6,5)<esum(F(1,5),7),
}
assert all(checks.values()),checks
print(json.dumps({'verified_exact_fractional':checks,'consequence':'eta=(6/5)e^(-1/5) dominates the left eta branch; c=0.008 is below log((1+eta)/(2eta)); sigma>=252 ensures (sigma-theta)/(sigma-2) < exp(c) for 0<theta<1.','limitation':'Does not establish Mellin transform, Cauchy estimates, localization, theta lifts, or RH.'},indent=2))
