#!/usr/bin/env python3
"""Exact exponent feasibility audit of the printed four-term error of (M), not a proof of H12."""
from fractions import Fraction as F
from itertools import product
import json

def exponent(a,b,c):
    return max(1-a,1+a-b,a,b-2*c)

def candidate(c):
    t=max(F(1,2),(2-2*c)/3)
    a=1-t
    b=2-2*t
    assert exponent(a,b,c)==t
    assert a>=0 and b>=0
    return t,a,b

rows=[]
for c in [F(0),F(1,20),F(1,10),F(1,5),F(1,4),F(1,2),F(1),F(2)]:
    t,a,b=candidate(c)
    assert 3*t>=2-2*c and t>=F(1,2)
    rows.append(dict(c=str(c),optimal_t=str(t),a=str(a),b=str(b),four_terms=list(map(str,[1-a,1+a-b,a,b-2*c]))))

# Exhaustive rational-grid falsification of analytic optimum under b>=0,a>=0
for c in [F(0),F(1,10),F(1,4),F(1,2),F(1)]:
    t,_,_=candidate(c)
    for ia,ib in product(range(41),range(121)):
        a=F(ia,20);b=F(ib,20)
        assert exponent(a,b,c)>=t, (a,b,c)

# Structural source budget (III.8, page 213): k >= 8 C_G m**5 f x**eps and f=2n.
# Leading exponents obey b>=5a+c. This is distinct from bare (M).
def geometric_candidate(c):
    t=max(F(1,2),(F(5)-c)/6, (F(2)-2*c)/3)
    a=1-t
    b=max(1+a-t,5*a+c)
    assert b<=t+2*c
    assert exponent(a,b,c)==t
    assert b>=5*a+c
    return t,a,b
geo_rows=[]
for c in [F(0),F(1,4),F(1,2),F(1),F(3,2),F(2),F(3)]:
    t,a,b=geometric_candidate(c)
    geo_rows.append(dict(c=str(c),minimax_t=str(t),a=str(a),b=str(b)))
    for ia,ib in product(range(41),range(161)):
        a2=F(ia,20);b2=F(ib,20)
        if b2>=5*a2+c:
            assert exponent(a2,b2,c)>=t,(a2,b2,c)
# t=1/2 forces a=1/2, b>=5/2+c and b<=1/2+2c -> c>=2.
assert F(5,2)+F(2)==F(1,2)+2*F(2)
assert exponent(F(1,2),F(9,2),F(2))==F(1,2)
report={
 'claim':'For 4 abstract monomial error exponents and n=x^c, minimax t(c)=max(1/2,(2-2c)/3). This is independent of existence/geometric constraints.',
 'proof':'If each term <=x^t, then a>=1-t; a<=t; b>=1+a-t; b<=t+2c. Combining gives t>=1/2, 3t>=2-2c. Feasible constructive a=1-t,b=2-2t for c>=0.',
 'table':rows,'geometric_constraint_table':geo_rows,'geometry_audit':'If source k>=8 C_G m^5 f x^eps with f=2n, t=1/2 forces c>=2 (not c>=1/4). This is a conditional exponent budget only. The working guide H12 chooses n near x^(2+8epsilon); it does not establish existence of such arithmetic data in the guide itself.',
 'finite_grid_check':'Tested 5 values of c, all 41*121 rational (a,b) pairs each; no counterexample.',
 'source':'Rubinstein working v2 Nov22 2026 Part II, eq (M) and Part III Section III.8 page around 148 where k>=C m^5 f x^eps appears.'}
path='/mnt/data/riemann_runs/20261123_1047/error_exponents.json'
with open(path,'w') as f: json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
