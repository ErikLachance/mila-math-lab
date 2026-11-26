#!/usr/bin/env python3
"""Adaptive finite-net certificate for one-sided von Mangoldt sum and adversarial prime-power probes."""
from __future__ import annotations
import math,json,random,hashlib,bisect
from pathlib import Path
N=400000
is_prime=bytearray(b'\x01')*(N+1);is_prime[0]=is_prime[1]=0
lam=[0.0]*(N+1)
for p in range(2,N+1):
    if is_prime[p]:
        if p*p<=N:
            is_prime[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
        n=p
        while n<=N:
            lam[n]=math.log(p);n*=p
A=[0.0]*(N+1);B=[0.0]*(N+1)
for n in range(2,N+1):
    A[n]=A[n-1]+lam[n]/n;B[n]=B[n-1]+lam[n]
gamma=0.577215664901532860606512090082

def G(x:float)->float:
    assert 1.0<x<N
    n=int(math.floor(x))
    return x*A[n]-B[n]-x*math.log(x)+(1+gamma)*x

def d(a,b,x):
    t=(x-a)/(b-a)
    return (1-t)*a*math.log(a)+t*b*math.log(b)-x*math.log(x)

def grids(Y,theta):
    end=Y**1.5
    max_uniform_h=math.sqrt(8*Y**(1+theta))
    n=math.ceil((end-Y)/max_uniform_h)
    uniform=[Y+(end-Y)*i/n for i in range(n+1)]
    adaptive=[float(Y)]
    while adaptive[-1]<end:
        a=adaptive[-1]
        h=math.sqrt(8)*a**((1+theta)/2)
        next_v=min(end,a+h)
        assert next_v>a
        adaptive.append(next_v)
    return uniform,adaptive

rng=random.Random(202611231031)
report=[]
for Y,theta in [(100,.52),(1000,.57),(5000,.60),(20000,.505)]:
    end=Y**1.5
    if end>N:continue
    uni,ad=grids(Y,theta)
    vals=[G(x) for x in ad]
    C=max(0.0,max(v/x**theta for v,x in zip(vals,ad)))
    errors=0;tests=0;max_err=-1e40;max_dratio=0.;max_defect=0.
    samples=[]
    for i in range(len(ad)-1):
        a,b=ad[i],ad[i+1]
        samples.extend(a+(b-a)*rng.random() for _ in range(200))
        # Adversarially place test points near every von Mangoldt jump in cell
        for n in range(math.ceil(a),min(N,math.floor(b))+1):
            if lam[n]>0:
                samples.extend([float(n),n-1e-7,n+1e-7])
        samples.append((a+b)/2)
    for x in samples:
        if not (Y<x<end):continue
        i=min(len(ad)-2, max(0,bisect.bisect_right(ad,x)-1))
        a,b=ad[i],ad[i+1];t=(x-a)/(b-a)
        delta=d(a,b,x)
        exact=(1-t)*vals[i]+t*vals[i+1]+delta
        slack=(b-a)**2/(8*a)
        g=G(x)
        max_err=max(max_err,g-exact)
        max_defect=max(max_defect,delta)
        max_dratio=max(max_dratio,delta/slack)
        if (g>exact+3e-6 or delta>slack+3e-6 or g>(C+1)*x**theta+3e-6):
            errors+=1
        tests+=1
    assert errors==0,(Y,errors,max_err)
    assert all((b-a)**2/(8*a)<=a**theta*(1+1e-12) for a,b in zip(ad[:-1],ad[1:]))
    report.append({'Y':Y,'theta':theta,'upper':end,'uniform_steps':len(uni)-1,'adaptive_steps':len(ad)-1,'samples_including_prime_power_knots':tests,'C_from_adaptive_nodes':C,'max_G_minus_exact_interpolant':max_err,'max_defect_over_local_quadratic_bound':max_dratio,'worst_defect':max_defect,'violations':errors})
result={'claim':'For a>1, b>a and 0<theta<1, the one-sided interpolant G(x)<=chord(G endpoints)+D where D=chord(xlogx)-xlogx<= (b-a)^2/(8a). Choosing b-a<=sqrt(8*a^(1+theta)) makes D<=a^theta<=x^theta; G at adaptive grid nodes<=C node^theta implies G(x)<=(C+1)x^theta, with C independent of the window scale.','asymptotics':'Adaptive step length ~a^((1+theta)/2), so grid count O(Y^((3/2)*(1-theta)/2)) = O(Y^(3*(1-theta)/4)) on [Y,Y^1.5]. This is conditional sampling complexity, not a method to prove bounds at each node.','proof':'Positive Lambda(n)/n implies S(x)=sum Lambda(n)/n*(x-n)_+ is convex. Since G=S-xlogx+(1+gamma)x, Jensen S(x)<=chord(S) (FALSE: convex S(x) <= its chord: YES). D>=0 from convexity xlogx; D <= (b-a)^2/(8a) from upper second derivative 1/a. Concavity of x^theta gives chord(x^theta)<=x^theta. The adaptive step ensures D <= x^theta. A dyadic grouping over [Y,Y^1.5] yields O(Y^(3*(1-theta)/4)) cells; no PNT is required.','tests':report,'warning':'No proof of RH. Error checks are float-only and do not certify an infinite set; formal inequalities are unconditional basic convexity.'}
out=Path('/mnt/data/riemann_current/riemann_h12_adaptive_semiconvex.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(report,indent=2))
for path in [Path(__file__),out]: print('SHA256',path.name,hashlib.sha256(path.read_bytes()).hexdigest())
