#!/usr/bin/env python3
"""Exact coefficient calculation of [p]_F(X)=sl(p*l(X)), l'=1/sqrt(1-X^4)."""
from fractions import Fraction as F
from math import comb
import json

def multiply(a,b,K):
    c=[F(0)]*(K+1)
    for i,ai in enumerate(a[:K+1]):
        if ai==0:continue
        for j,bj in enumerate(b[:K+1-i]):c[i+j]+=ai*bj
    return c

def run(p, N):
    K=(N-1)//4
    a=[F(comb(2*k,k),4**k*(4*k+1)) for k in range(K+1)]
    # sl(X)=X sum c_k X^{4k}
    c=[F(1)]; sq=[F(1)]
    for k in range(K):
        cc= -2*sum(c[i]*sq[k-i] for i in range(k+1))/F((4*k+5)*(4*k+4))
        c.append(cc)
        sq.append(sum(c[j]*c[k+1-j] for j in range(k+2)))
    a2=multiply(a,a,K)
    a4=multiply(a2,a2,K)
    v=[F(0)]+[p**4*a4[k-1] for k in range(1,K+1)]
    H=[F(0)]*(K+1)
    H[0]=c[K]
    for k in range(K-1,-1,-1):
        H=multiply(v,H,K)
        H[0]+=c[k]
    g=multiply([p*x for x in a],H,K)
    residues=[]
    for k,x in enumerate(g):
        assert x.denominator%p!=0,('non p integral',p,k,x)
        residues.append((x.numerator%p)*pow(x.denominator,-1,p)%p)
    return {'p':p,'N':N,'K':K,'residues':residues,'first_nz':next(((4*k+1,v) for k,v in enumerate(residues) if v),None),'nonzero_count':sum(v!=0 for v in residues)}

results=[]
for p,N in [(3,9),(7,49),(11,121),(5,5),(13,13),(17,17)]:
    r=run(p,N)
    print(r['p'],r['N'],r['first_nz'],r['nonzero_count'])
    if p%4==3:
        assert r['nonzero_count']==1
        assert r['first_nz']==(p*p,p-1)
    else:
        assert r['first_nz'][0]==p and r['first_nz'][1]!=0
    results.append(r)
with open('/mnt/data/riemann_20261123_0936/lemniscate_formal_p_series.json','w') as f:json.dump({'computed':[{'p':r['p'],'N':r['N'],'first_nonzero_degree_mod_p':r['first_nz'],'nonzero_count':r['nonzero_count']} for r in results],'warnings':'finite p-adic modular checks; not proof for all primes; exact Fraction coefficients, polynomial ring Z_(p)[[X]] truncated'},f,indent=2)
print('PASS all 6 prime cases')
