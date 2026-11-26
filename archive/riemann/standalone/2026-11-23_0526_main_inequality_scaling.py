#!/usr/bin/env python3
"""Exact rational exponent audit for Rubinstein v2 §II.3 estimate (A)."""
from fractions import Fraction as F
import json, itertools
from time import monotonic
start=monotonic()
def score(a,b,c):
    terms={'x/m':1-a,'x*m/k':1+a-b,'m':a,'k/n^2':b-2*c}
    return max(terms.values()),terms
published=(F(1,2),F(9,2),F(2,1))
bound,terms=score(*published)
assert bound==F(1,2)
assert {x:str(y) for x,y in terms.items()}=={'x/m':'1/2','x*m/k':'-3','m':'1/2','k/n^2':'1/2'}
# Universal lower bound: max(a,1-a)>=1/2 for all a in R, independent of b,c.
# Symbolically check over a grid as a consistency check, not as a proof.
for a in [F(i,200) for i in range(-40,250)]:
    assert max(a,1-a)>=F(1,2)
# For fixed b=9/2,c=2, varying a yields min at a=1/2, with sharp third-fourth terms.
res=[(score(F(i,200),F(9,2),F(2))[0],F(i,200)) for i in range(-40,250)]
opt=min(x[0] for x in res)
assert opt==F(1,2)
# Loss if someone misreads 9/2 as 9/10: the xm/k term becomes x^0.6 for a=0.5.
wrong=score(F(1,2),F(9,10),F(2))[0]
assert wrong==F(3,5)
report={'source':'Rubinstein 22-Nov-2026 v2 PDF Part II section 3 Estimate (A), scanned PDF screenshot page 33','m_exponent':str(published[0]),'k_exponent':str(published[1]),'n_exponent':str(published[2]),'four_error_exponents':{t:str(v) for t,v in terms.items()},'leading_exponent':str(bound),'unconditional_structural_lower_bound':'max(a,1-a) >= 1/2, so this particular four-term error bound cannot by tuning m,k,n alone yield better than square-root cancellation','wrong_k_as_x_to_point9_exponent':str(wrong),'caveat':'only scale calculus of the quoted conditional inequality; (M) itself and its thirteen inputs are not independently proved here','elapsed_wall_seconds':monotonic()-start}
with open(__file__.replace('.py','.json'),'w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
