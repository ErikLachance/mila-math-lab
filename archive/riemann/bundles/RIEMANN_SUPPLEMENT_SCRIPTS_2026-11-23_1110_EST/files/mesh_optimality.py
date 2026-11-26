"""Exact integer-only adaptive mesh, finite lower bound within curvature-budget framework."""
from fractions import Fraction
from math import isqrt,log
import json

def nodes(m,p,q):
    assert m>=2 and 0<p<q
    a=m*m;upper=m*m*m
    # max integer h satisfying h^(2q) <= 8^q a^(p+q)
    # binary search monotonically without floating point
    out=[a]
    while a<upper:
        target=(8**q)*pow(a,p+q)
        lo,hi=1,min(upper-a+1,2*a+1)
        while lo<hi:
            md=(lo+hi+1)//2
            if pow(md,2*q)<=target:lo=md
            else:hi=md-1
        h=min(lo,upper-a)
        assert h>=1
        assert pow(h,2*q)<=target
        if a+h<upper:
            assert pow(h+1,2*q)>target
        a+=h
        out.append(a)
    return out

cases=[]
for p,q in [(3,5),(11,20),(13,25),(100,199)]:
    for m in [30,100,300,1000,3000]:
        nds=nodes(m,p,q)
        T=m**3
        late_gaps=sum(1 for a,b in zip(nds,nds[1:]) if b>T//2)
        theta=Fraction(p,q)
        lower_constant=(m**(3*(1-float(theta))/2))/(2*8**.5)
        assert len(nds)-1>=lower_constant-1
        cases.append({'p':p,'q':q,'m':m,'intervals':len(nds)-1,
                      'last_half_intervals':late_gaps,'analytic_lower_bound':lower_constant,
                      'actual_over_lower':(len(nds)-1)/lower_constant})

# Analytic lower bound for every partition satisfying h_i^2<=8*a_i^(1+theta),
# because each h_i<=sqrt8*T^((1+theta)/2), and at least T/2 of total
# interval length lies in [T/2,T]. This is Omega(T^((1-theta)/2)).
print(json.dumps(cases,indent=2))
with open('/mnt/data/riemann_runs/20261123_1047/mesh_optimality.json','w') as f:json.dump(cases,f,indent=2)
