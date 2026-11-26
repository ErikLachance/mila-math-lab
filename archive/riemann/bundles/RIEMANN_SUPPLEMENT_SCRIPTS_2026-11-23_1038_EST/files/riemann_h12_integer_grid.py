#!/usr/bin/env python3
"""Exact-big-integer rational-exponent grid, with integer endpoints Y=m^2, Y^(3/2)=m^3."""
from pathlib import Path
import math,json,hashlib,random,bisect

def max_safe_integer_step(a,p,q):
    # h^(2q) <= 8^q * a^(p+q), iff h^2 <= 8*a^(1+p/q).
    target=(8**q)*(a**(p+q))
    lo,hi=1,2
    while hi**(2*q)<=target:lo,hi=hi,2*hi
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**(2*q)<=target:lo=mid
        else:hi=mid
    assert lo**(2*q)<=target<(lo+1)**(2*q)
    return lo

def make(m,p,q):
    assert 1/2<p/q<1
    end=m**3
    nodes=[m*m]
    while nodes[-1]<end:
        a=nodes[-1]
        h=max_safe_integer_step(a,p,q)
        b=min(end,a+h)
        assert b>a and (b-a)**(2*q)<=(8**q)*(a**(p+q))
        nodes.append(b)
    return nodes

N=260000
lam=[0.0]*(N+1);flags=bytearray(b'\x01')*(N+1);flags[0]=flags[1]=0
for p in range(2,N+1):
    if flags[p]:
        if p*p<=N:flags[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
        v=p
        while v<=N:lam[v]=math.log(p);v*=p
A=[0.0]*(N+1);B=[0.0]*(N+1)
for i in range(2,N+1):
    A[i]=A[i-1]+lam[i]/i;B[i]=B[i-1]+lam[i]
def G(x):
    n=int(math.floor(x));return x*A[n]-B[n]-x*math.log(x)+(1+0.57721566490153286)*x

def d(a,b,x):
    t=(x-a)/(b-a);return (1-t)*a*math.log(a)+t*b*math.log(b)-x*math.log(x)

rng=random.Random(530599)
rows=[]
for m,p,q in [(10,3,5),(30,11,20),(60,13,25),(1000,3,5)]:
    nodes=make(m,p,q)
    theta=p/q
    if m**3>N:
        rows.append({'m':m,'theta':f'{p}/{q}','n_intervals':len(nodes)-1,'upper':m**3,'integer_mesh_proof':'PASS by exact big integers, prime-sum diagnostics skipped (range exceeds sieve)'})
        continue
    vals=[G(float(n)) for n in nodes]
    C=max(0,max(v/n**theta for v,n in zip(vals,nodes)))
    max_err=-float('inf');bad=0;count=0
    for i in range(len(nodes)-1):
        a,b=nodes[i:i+2];ga,gb=vals[i:i+2]
        for _ in range(500):
            x=a+(b-a)*rng.random();t=(x-a)/(b-a)
            exact=(1-t)*ga+t*gb+d(a,b,x)
            max_err=max(max_err,G(x)-exact)
            if G(x)>exact+5e-6 or G(x)>(C+1)*x**theta+5e-6:bad+=1
            count+=1
    assert bad==0,(m,bad)
    rows.append({'m':m,'theta':f'{p}/{q}','n_intervals':len(nodes)-1,'upper':m**3,'samples':count,'C_finite':C,'max_G_minus_exact_interpolant':max_err,'violations':bad,'integer_mesh_proof':'PASS, exact integer power comparisons on every edge'})
result={'proof':'For fixed rational theta=p/q with 1/2<p/q<1, Y=m^2 and upper=m^3 are integers. For each a, choose maximum positive integer h with h^(2q) <= 8^q a^(q+p), then b=min(m^3,a+h). These purely integer comparisons verify h^2 <= 8 a^(1+theta), so the semiconvex finite-grid lemma applies without floating node-rounding risks. There are asymptotically O(m^(3*(1-theta)/2)) nodes, equivalent to O(Y^(3*(1-theta)/4)).','tests':rows,'quantifier':'Combined with the source one-sided Landau interval criterion and theta arbitrarily close to 1/2, a uniform-in-m bound G(node)<=C_theta node^theta for arbitrarily large m along these integer meshes implies RH. Conversely RH implies it. These are equivalent unsolved node estimates, NOT computational proof by the finite tests.'}
out=Path('/mnt/data/riemann_current/riemann_h12_integer_grid.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(rows,indent=2))
for z in [Path(__file__),out]:print('SHA256',z.name,hashlib.sha256(z.read_bytes()).hexdigest())
