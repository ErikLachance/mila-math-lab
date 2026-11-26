#!/usr/bin/env python3
"""Independent finite arithmetic audit of Rubinstein III.1 exceptional squareclass pair contribution.
No assumptions about actual distribution of primes in progressions; purely combinatorial/finitary."""
import math, json
from collections import defaultdict
from sympy import primerange, factorint

# c_n=Lambda(n)*min(1,y/n). n is a prime power <=Z.
def pp_terms(y,Z):
    out=[]
    for p in primerange(2,Z+1):
        n=p
        while n<=Z:
            out.append((int(n),int(p),math.log(int(p))*min(1.,y/int(n))))
            n*=int(p)
    return out

def sf_outside(n,m0):
    result=1
    for p,e in factorint(int(n)).items():
        if m0%p and e%2: result*=p
    return result

records=[]
for Z in [25,50,120,250,800]:
    for y in [2,5,11,29,59,155]:
        if y>Z: continue
        terms=pp_terms(y,Z)
        for m0 in [8,24,40,8*3*5*7]:
            R=sum(c for n,p,c in terms if sf_outside(n,m0)==1)
            s_classes=defaultdict(float)
            for n,p,c in terms:
                for k,r,d in terms:
                    s_classes[sf_outside(n*k,m0)]+=c*d
            available=[p for p in primerange(2,Z+1) if m0%int(p)!=0]
            scenarios=available[:min(6,len(available))]
            scenarios += [available[i]*available[j] for i in range(min(4,len(available))) for j in range(i+1,min(5,len(available)))]
            scenarios += [2*3*5*7,3*5*7,11*13*17,4,9,1]
            for s in scenarios:
                if s<=1 or len(factorint(s))>2 or any(e!=1 for e in factorint(s).values()) or math.gcd(s,m0)>1:
                    # A non-squarefree or source-excluded-prime exceptional label cannot be produced
                    if s>1 and (any(e!=1 for e in factorint(s).values()) or math.gcd(s,m0)>1):
                        assert abs(s_classes.get(s,0.))<1e-12,(Z,y,m0,s)
                    continue
                bound=(6*math.log(y)*R if len(factorint(s))==1 else 18*math.log(y)**2)
                actual=s_classes.get(s,0.)
                assert actual<=bound+1e-10,(Z,y,m0,s,actual,bound,R)
                records.append({'Z':Z,'y':y,'m0':m0,'s':s,'actual':actual,'bound':bound,'ratio':actual/bound if bound else 0.})
            # Structural: any two terms have squarefree part either 1, 1 prime, or 2 primes outside m0.
            for s in s_classes:
                assert len(factorint(s))<=2 and all(e==1 for e in factorint(s).values())
summary={'source':'Rubinstein v2 section III.1 Step 2, page 64','cases_checked':len(records),'max_ratio':max(x['ratio'] for x in records),'worst_case':max(records,key=lambda x:x['ratio']),'all_pass':True,'identity':'s(n*nprime) outside m0 is 1, a single prime, or a product of two different primes','bound':'exceptional class s*=p: ≤6 log(y)*R; s*=pr: ≤18 log(y)^2','limitation':'finite combinatorics only; DOES NOT bound nonexceptional character sums, supply primes, zero-density, or RH'}
with open('/mnt/data/riemann_20261123_0908/exceptional_squareclass_audit.json','w') as f: json.dump(summary,f,indent=2)
print(json.dumps(summary,indent=2))
