"""Exact exponent bookkeeping only: Rubinstein Part II estimate (A),
together with PageWin in the Lean source. This checks a CONDITIONAL
implication, NOT (M) itself and NOT the truth of its prerequisites.
"""
import json
from fractions import Fraction as Q
out=[]
for eps in (Q(1,1000),Q(1,200),Q(1,52),Q(1,32),Q(1,16)):
    m=Q(1,2)-eps/16
    n=2+8*eps
    k=Q(9,2)+10*eps
    E=[1-m,1+m-k,m,k-2*n]
    target=Q(1,2)+eps/16
    assert E[0]==target
    assert E[1]==-3-Q(161,16)*eps
    assert E[2]==Q(1,2)-eps/16
    assert E[3]==Q(1,2)-6*eps
    assert all(e<=target for e in E)
    out.append({'epsilon':str(eps),'m_exp':str(m),'n_exp':str(n),'k_exp':str(k),'A_term_exponents':[str(x) for x in E],'A_total_upper_exponent':str(target),'bound':'x/m + x*m/k + m + k/n^2 <= 7*x^(1/2+epsilon/16) for x>=1, assuming PageWin factor-2 bounds'})
print(json.dumps({'exact_fraction_epsilon_cases':len(out),'passed':True,'caution':'Exponent arithmetic only; does not establish the main analytic bound (M) or hypotheses H0-H12.','cases':out},indent=2))
