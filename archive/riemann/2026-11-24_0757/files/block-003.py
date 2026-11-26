from fractions import Fraction as F
from random import Random
from math import prod
from time import monotonic
import json
s=monotonic();rng=Random(241124)
def val(x,p,cap):
    if x==0:return cap
    k=0
    while x%p==0:x//=p;k+=1
    return k
cases=0; residues=0; nonexceptional=0; max_ratio=F(0); power_checks=0
# finite p-adic precision; truncated valuations; max chosen among actual truncated values.
for _ in range(6500):
    p=rng.choice([2,3,5,7,11]); b=2 if p==2 else 1; prec=rng.randrange(5,17); mod=p**prec; g=1+p**b
    u=1+p**b*rng.randrange(mod//p**b); t=rng.randrange(2,151)
    w=u*g%mod; vals=[]
    for r in range(1,t+1):
        vals.append(val((w-1)%mod,p,prec)); w=w*g%mod
    j=max(range(t),key=vals.__getitem__); remaining=vals[:j]+vals[j+1:]
    assert sum(remaining)<=b*(t-1)+F(t-1,p-1)
    assert all(p**(v-b)<=t-1 for v in remaining)
    for k in range(b+1,prec+1):
        indices=[r for r,v in enumerate(vals,1) if v>=k]
        assert len(indices)<=1+(t-1)//p**(k-b)
        if indices:assert all((r-indices[0])%p**(k-b)==0 for r in indices)
        residues+=1
    if vals[j]<prec:
        u0=u*pow(g,j+1,mod)%mod
        for n in range(4):
            assert val((pow(u0,p**n,mod)-1)%mod,p,prec)==min(prec,vals[j]+n);power_checks+=1
    max_ratio=max(max_ratio,F(sum(remaining),t-1));nonexceptional+=len(remaining);cases+=1
print(json.dumps(dict(exact_twist_families=cases,congruence_checks=residues,nonexceptional_twists=nonexceptional,power_lifting_checks=power_checks,max_mean_valuation=str(max_ratio),elapsed_seconds=monotonic()-s),indent=2))

