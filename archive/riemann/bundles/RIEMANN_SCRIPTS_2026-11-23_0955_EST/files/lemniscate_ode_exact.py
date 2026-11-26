#!/usr/bin/env python3
"""Independent exact recurrence for lemniscatic sine and inert-prime valuations."""
import json, math, sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as F
from sympy import primerange
KMAX=500
c=[F(1)]
sq=[F(1)]
A={1:1}
for K in range(KMAX):
    # In s(t)=sum c_k t^(4k+1), coeff s^3 at t^(4K+3)
    tot=sum(c[i]*sq[K-i] for i in range(K+1))
    ck= -2*tot/F((4*K+5)*(4*K+4))
    c.append(ck)
    sq.append(sum(c[j]*c[K+1-j] for j in range(K+2)))
    n=4*K+5
    an=math.factorial(n)*ck
    assert an.denominator == 1, (n,an)
    A[n]=an.numerator
expected={1:1,5:-12,9:3024,13:-4390848,17:21224560896}
assert all(A[k]==v for k,v in expected.items())

def vp(x,p):
    if x==0:return None
    x=abs(x); z=0
    while x%p==0:x//=p;z+=1
    return z
inert=list(p for p in primerange(3,75) if p%4==3)
split=list(p for p in primerange(5,75) if p%4==1)
fail=[]; cases=0; bound_slack=[]; positives=[]
for n,an in A.items():
    if n<=1:continue
    for p in inert:
        actual=vp(an,p); target=n*p//(p*p-1);cases+=1
        if actual<target:fail.append((n,p,actual,target))
        bound_slack.append((actual-target,n,p,actual,target))
        positives.append((actual,n,p))
assert not fail, fail[:15]
assert all(vp(A[n],p)==0 for n in (5,9,13,17,49,101,201) for p in (5,13,17,29)), 'Unexpected split divisibility'
for n in (17,49,101,201):
    print('TABLE',n,{p:{'actual':vp(A[n],p),'floor_target':n*p//(p*p-1)} for p in (3,7,11)}, 'digits',len(str(abs(A[n]))))
print('Max extra inert valuation slack',max(bound_slack));print('Minimum',min(bound_slack))
res={'ODE':'sl_second_derivative=-2 sl_cubed; c_0=1; c_(K+1)=-2 sum_{i+j+l=K} c_i*c_j*c_l/((4K+5)(4K+4))', 'largest_n':max(A),'coefficients_checked':len(A),'inert_primes':inert,'inert_pairs':cases,'failed':fail, 'min_slack':min(bound_slack),'max_slack':max(bound_slack),'selected':{str(n):{'A_digits':len(str(abs(A[n]))),'A_exact':str(A[n]) if n<=17 else None,'v3':vp(A[n],3),'v7':vp(A[n],7),'v11':vp(A[n],11),'v5':vp(A[n],5),'v13':vp(A[n],13)} for n in (1,5,9,13,17,49,101,201,1001,2001)}}
with open('/mnt/data/riemann_20261123_0936/lemniscate_ode_exact.json','w') as f:json.dump(res,f,indent=2)
print('PASS',cases,'inert-prime comparisons all bound; max n',max(A))
