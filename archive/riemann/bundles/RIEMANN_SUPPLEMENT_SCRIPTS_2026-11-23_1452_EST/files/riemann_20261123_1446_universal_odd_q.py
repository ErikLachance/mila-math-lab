"""Odd quadratic Dirichlet witness independent of auxiliary odd prime q, d>37.
For d prime 3mod4, chi_-d(d-4)=chi_-d(d-36)=-1. Their difference
32 cannot be divisible by odd q simultaneously. Hence a q-free odd
negative-character n<d has an odd prime factor p!=q with chi=-1.
"""
from sympy import primerange, kronecker_symbol, factorint
from mpmath import mp
import json
mp.dps=70
checks=0; cases=[]
for d in primerange(41,2000):
    if d%4!=3: continue
    for q in primerange(3,37):
        if q==d: continue
        n=d-4 if (d-4)%q else d-36
        assert n>1 and n%2==1 and n%q!=0 and n<d
        assert int(kronecker_symbol(-d,n))==-1
        factors=list(factorint(n).keys())
        bad=[p for p in factors if int(kronecker_symbol(-d,p))==-1 and p!=q]
        assert bad
        p=bad[0]
        val=2*mp.log(p)*(mp.mpf(1)/p-mp.mpf(1)/(2*d))
        assert val>=mp.log(d)/d
        checks+=1
        if d in (43,67,127,223) and q in (3,5,7):
            cases.append(dict(d=d,q=q,n=n,witness_prime=p,term=mp.nstr(val,25),bound=mp.nstr(mp.log(d)/d,25)))
print('PASS cases',checks)
with open('/mnt/data/riemann_20261123_1451_universal_odd_q.json','w') as f: json.dump({'all_passed':True,'cases_checked':checks,'examples':cases},f,indent=2)
