"""Exact rational Taylor bounds for elementary sufficient Robin inequalities
on integers with prime support included in {2,3,5} (n>=5041) or
{2,3,5,7} (n>=1_000_000). This does not prove RH.

Euler gamma lower bound H100 - log(101), and log(101)<4.617,
are standard classical inequalities. The latter is certified here via exp.
"""
from fractions import Fraction as F
from math import factorial
import json

def esum(x,N):
    return sum((x**k/F(factorial(k))) for k in range(N+1))
def exp_upper(x,N):
    assert x >= 0 and F(N+2)>x
    tail_first=x**(N+1)/F(factorial(N+1))
    return esum(x,N)+tail_first/(1-x/F(N+2))
checks={
    'H100_gt_5.187':sum(F(1,k) for k in range(1,101))>F(5187,1000),
    'exp_4.617_gt_101':esum(F(4617,1000),32)>101,
    'gamma_gt_0.57_from_two_inequalities':sum(F(1,k) for k in range(1,101))-F(4617,1000)>F(57,100),
    'exp_0.57_gt_1.765':esum(F(57,100),4)>F(353,200),
    'exp_8.5_lt_5041':exp_upper(F(17,2),60)<5041,
    'exp_2.13_lt_8.5':exp_upper(F(213,100),25)<F(17,2),
    'support_235_margin':F(353,200)*F(213,100)>F(15,4),
    'exp_13_lt_1e6':exp_upper(F(13),90)<1000000,
    'exp_2.5_lt_13':exp_upper(F(5,2),30)<13,
    'support_2357_margin':F(353,200)*F(5,2)>F(35,8),
}
assert all(checks.values()),checks
print(json.dumps({'verified_exact_rational_checks':checks,'numerical_margins':{
 '235':str(F(353,200)*F(213,100)-F(15,4)),
 '2357':str(F(353,200)*F(5,2)-F(35,8)),
 },'proof_note':'Euler bound H100-ln101<gamma classical; all exp comparisons are certified via Taylor partial sum and tail bound'},indent=2))
