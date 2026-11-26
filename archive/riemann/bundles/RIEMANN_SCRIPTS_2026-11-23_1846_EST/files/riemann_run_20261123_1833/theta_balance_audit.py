"""Exact integer samples supporting, but NOT proving, the symbolic PageWin
bound. Proof is elementary and recorded in the Riemann supplement.
For epsilon in {1/4,1/8,1/16} write epsilon=8/q and use x=t^(2q),
then delta=x^(-epsilon/8)=t^(-2), A=sqrt(x delta)=t^(q-1),
and X/A+A=t^(q+1)+t^(q-1). 3*x^(1/2+epsilon/16)=3t^(q+1).
For m in [A,2A], x/m+m <= 3t^(q+1) for t>=2.
"""
from fractions import Fraction as F
import json
cases=[]
for q in (32,64,128):
  eps=F(8,q)
  for t in (2,3,5):
    x=t**(2*q)
    A=t**(q-1)
    upper=3*t**(q+1)
    for mult in (F(1,1),F(3,2),F(2,1)):
      m=A*mult
      lhs=F(x,1)/m + m
      passed=lhs<=upper
      assert passed
      cases.append({'epsilon':str(eps),'t':t,'m_multiplier':str(mult),'passed':passed,'exact_slack_positive':upper>=lhs})
print(json.dumps({'exact_integer_fraction_checks':len(cases),'all_pass':all(k['passed'] for k in cases),'cases':cases},indent=2))
