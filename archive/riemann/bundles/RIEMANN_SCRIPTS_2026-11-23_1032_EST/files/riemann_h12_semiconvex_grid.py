#!/usr/bin/env python3
"""Finite tests and analytic certificate for a semiconvex interpolation criterion on G(x)."""
import math, random, json, hashlib
from bisect import bisect_right
from pathlib import Path
N=360000
prime=bytearray(b'\x01')*(N+1);prime[0]=prime[1]=0
v=[0.0]*(N+1)
for p in range(2,N+1):
    if prime[p]:
        if p*p<=N:
            prime[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
        m=p
        while m<=N:
            v[m]=math.log(p);m*=p
A=[0.0]*(N+1); B=[0.0]*(N+1)
for n in range(2,N+1):
    A[n]=A[n-1]+v[n]/n
    B[n]=B[n-1]+v[n]
gamma=0.5772156649015328606

def G(x):
    n=math.floor(x)
    return x*A[n]-B[n]-x*math.log(x)+(1+gamma)*x

def D(a,b,x):
    t=(x-a)/(b-a)
    return (1-t)*a*math.log(a)+t*b*math.log(b)-x*math.log(x)

rng=random.Random(202611231026)
results=[]
for Y,theta in [(100,.52),(1000,.57),(5000,.60)]:
    U=Y**1.5; h=math.sqrt(8*Y**(1+theta)); n=math.ceil((U-Y)/h)
    nodes=[Y+(U-Y)*i/n for i in range(n+1)]
    gs=[G(x) for x in nodes]; C=max(0,max(g/x**theta for g,x in zip(gs,nodes)))
    tests=0; bad_exact=bad_simple=bad_global=0
    max_excess_exact=-1e100; max_D_over_bound=0
    for k in range(n):
        a=nodes[k]; b=nodes[k+1];ga=gs[k];gb=gs[k+1]
        for _ in range(150):
            x=a+(b-a)*rng.random(); t=(x-a)/(b-a)
            d=D(a,b,x)
            exact=(1-t)*ga+t*gb+d
            simple=(1-t)*ga+t*gb+(b-a)**2/(8*Y)
            bound=(C+1)*x**theta
            g=G(x)
            max_excess_exact=max(max_excess_exact,g-exact)
            max_D_over_bound=max(max_D_over_bound,d/((b-a)**2/(8*Y)))
            if g>exact+5e-7:bad_exact+=1
            if g>simple+5e-7:bad_simple+=1
            if g>bound+5e-7:bad_global+=1
            tests+=1
    assert bad_exact==bad_simple==bad_global==0,(Y,bad_exact,bad_simple,bad_global)
    results.append({'Y':Y,'upper':U,'theta':theta,'mesh_bound':h,'actual_steps':n,'sample_count':tests,'C_from_nodes_only':C,'max_G_minus_exact_interpolant':max_excess_exact,'max_D_over_h2_over_8Y':max_D_over_bound,'violations':[bad_exact,bad_simple,bad_global]})

report={
 'exact_one_sided_interpolation':'For any 1<=a<x<b, t=(x-a)/(b-a), let S(x)=sum_n (Lambda(n)/n)*(x-n)_+, convex since Lambda>=0. Thus S(x)<=(1-t)S(a)+t S(b). For G=S-x log x+(1+gamma)x, conclude G(x)<=(1-t)G(a)+tG(b)+D(a,b;x), D=(1-t)a log a+t b log b -x log x >=0.',
 'rigorous_semiconvex_bound':'For a,b>=Y>=2, 0<=D(a,b;x)<= (x-a)(b-x)/(2Y) <=(b-a)^2/(8Y). This follows from convexity of G(x)+x^2/(2Y): distributional G second derivative is sum_n Lambda(n)/n delta_n-1/x dx, bounded below by -1/Y.',
 'finite_net_lemma':'If 0<theta<1, C>=0, Y>=2, nodes cover [Y,Y^(3/2)] with each gap h<=sqrt(8Y^(1+theta)) and G(node)<=C node^theta for every node, then G(x)<=(C+1)x^theta for every x in the window: concavity of x^theta ensures chord(node^theta)<=x^theta and interpolation defect <=Y^theta<=x^theta.',
 'mesh_cardinality':'Number of nodes O(Y^(1-theta/2)), versus O(Y^(3/2-theta)) for constant-Lipschitz first-derivative grid, and O(Y^(3/2-theta)*log^2Y) for purely elementary first-derivative grid. No PNT or RH assumption is needed for the semiconvex lemma.',
 'tests':results,
 'limitations':'This is a mathematical reduction of continuous one-sided G bounds to finite, but Y-growing, testing grids with a UNIFORM C for arbitrarily large Y. It does not prove those bounds, does not yield the arithmetic H12 data, and does not prove/disprove RH. Numerical tests are illustrative; the analytic convexity argument proves the finite-net implication.'}
p=Path('/mnt/data/riemann_current/riemann_h12_semiconvex_grid.json');p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(results,indent=2));print('SHA256 CODE',hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print('SHA256 JSON',hashlib.sha256(p.read_bytes()).hexdigest())
