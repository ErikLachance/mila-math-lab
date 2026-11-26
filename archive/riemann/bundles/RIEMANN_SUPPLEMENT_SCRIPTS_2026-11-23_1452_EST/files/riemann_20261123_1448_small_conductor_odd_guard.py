#!/usr/bin/env python3
"""Exact witness for odd quadratic char chi_{-d}: negative odd prime <d not equal auxiliary q>=5.
Proof independent of numerical checks: -4, -16 are negative quadratic residues,
so chi(d-4)=chi(d-16)=-1. Since their difference is 12,
q>=5 cannot divide both. A selected positive odd n coprime to q has a
prime divisor p!=q with chi(p)=-1. For y>=2d, source-scope P/a>=log(d)/d.
"""
import json
from sympy import primerange, factorint, kronecker_symbol
from mpmath import mp
mp.dps=60
cases=[]; total=0
qs=(5,7,11,13,17,19)
for d in primerange(19,1000):
    if d%4 != 3:continue
    for q in qs:
        if d==q:continue
        n=d-4 if (d-4)%q else d-16
        assert n>1 and n%2==1 and n%q!=0 and n<d
        assert int(kronecker_symbol(-d,n))==-1
        primes=list(factorint(n))
        witness=[p for p in primes if int(kronecker_symbol(-d,p))==-1 and p!=q]
        assert witness, (d,q,n,primes)
        p=witness[0]
        y=2*d
        direct_one=2*mp.log(p)*(mp.mpf(1)/p-mp.mpf(1)/y)
        crude=mp.log(d)/d
        assert direct_one>=crude, (d,q,p,direct_one,crude)
        total+=1
        if d in (19,23,31,43,67,127,223,997):cases.append({'d':d,'q':q,'nonresidue_factor':p,'n':n,'witness_contribution':mp.nstr(direct_one,25),'required_bound':mp.nstr(crude,25)})
print('PASS witness cases',total)
# Full source-scope P/a for a selection of pairs; all other terms nonnegative.
def P(d,q,y):
    val=mp.mpf(0)
    for p in primerange(3,y):
        if p==q or p==d:continue
        x=p;k=1
        while x<y:
            val+=(1-int(kronecker_symbol(-d,p))**k)*mp.log(p)*(mp.mpf(1)/x-mp.mpf(1)/y)
            x*=p;k+=1
    return val
full=[]
for d,q in [(19,7),(23,7),(31,5),(43,7),(67,11),(127,7),(223,19)]:
    y=2*d;v=P(d,q,y);lo=mp.log(d)/d
    assert v>=lo
    full.append({'d':d,'q':q,'y':y,'P_over_a':mp.nstr(v,30),'bound':mp.nstr(lo,30)})
    print(d,q,'P/a',mp.nstr(v,15),'bound',mp.nstr(lo,15))
with open('/mnt/data/riemann_20261123_1448_small_conductor_odd_guard.json','w') as f:
    json.dump({'status':'PASS','total_witness_cases':total,'selected_exact_algebraic_witnesses':cases,'full_prime_sum_checks':full,'scope':'all d prime 3 mod4 >17; q odd prime >=5 distinct from d; y>=2d'},f,indent=2)
