#!/usr/bin/env python3
"""Falsification tests for an independent elementary finite-net sufficient criterion for G(x)."""
from bisect import bisect_right
import math, json, random, hashlib
from pathlib import Path

def mangoldt_upto(N):
    v=[0.0]*(N+1)
    for p in range(2,N+1):
        if all(p%d for d in range(2,math.isqrt(p)+1)):
            k=p
            while k<=N:
                v[k]=math.log(p)
                k*=p
    return v

N=40000
v=mangoldt_upto(N)
A=[0.0]*(N+1);B=[0.0]*(N+1)
for i in range(2,N+1):
    A[i]=A[i-1]+v[i]/i
    B[i]=B[i-1]+v[i]
gamma=0.5772156649015328606

def G(x):
    j=min(N,int(x));return x*A[j]-B[j]-x*math.log(x)+(1+gamma)*x

def deriv(x):return A[min(N,int(x))]-math.log(x)+gamma

def bound(z):return (math.log(z)**2)+2*math.log(z)+1

rng=random.Random(230711)
checks=0; worst=0
for _ in range(6000):
    x=2+ rng.random()*(N-3)
    j=int(x)
    if j==int(x+1e-5):
        d=(G(x+1e-5)-G(x))/1e-5
        err=abs(d-deriv(x))
        worst=max(err,worst)
        assert err<0.003, (x,d,deriv(x),err)
        checks+=1
    assert abs(deriv(x))<=bound(N)

cases=[]
for Y,theta in [(40,.55),(100,.6),(200,.53),(1000,.6)]:
    U=Y**1.5; M=bound(U); h=Y**theta/M
    n=math.ceil((U-Y)/h)
    xs=[Y+(U-Y)*i/n for i in range(n+1)]
    values=[G(x) for x in xs]
    C=max(0.0,max(g/max(1,x**theta) for x,g in zip(xs,values)))
    failures=0; max_slack=-1e100
    for _ in range(2500):
        x=Y+rng.random()*(U-Y)
        j=min(n-1,int((x-Y)/(U-Y)*n))
        left=xs[j]
        assert left<=x and x-left<=h+1e-8
        assert G(left)<=C*left**theta+1e-8
        upper=C*x**theta+M*h
        slack=G(x)-upper
        max_slack=max(max_slack,slack)
        if slack>1e-7:failures+=1
    assert failures==0
    cases.append(dict(Y=Y,U=U,theta=theta,h=h,n_grid_intervals=n,max_G_ratio_C=C,largest_tested_G_minus_proved_envelope=max_slack,failures=failures))

result={
 'claim':'For x>=2, G(x)=sum_{n<=x} Lambda(n)(x/n-1)-x log x+(1+gamma)x is continuous piecewise differentiable and |G\'(x)| <= log(x)^2+2log(x)+1, away from prime powers; hence is globally Lipschitz on [Y,Y^{3/2}] with M(Y)=(3logY/2)^2+3logY+1.',
 'proof':'A(x)=sum_{n<=x} Lambda(n)/n <= log(x) * sum_{n<=x}1/n <= log(x)*(1+log x). Piecewise G\'=A(x)-log x+gamma. At jumps S(x) has new factor (x/n-1)=0, so continuous. Each piece satisfies |G\'| <= log^2 x+2log x+1 for x>=2. Then integration over finitely many breaks gives Lipschitz bound. If a left-anchored h-net with h<=Y^theta/M has G(x_j)<=C*x_j^theta at each node, then G(x)<=C*x^theta+Y^theta <=(C+1)*x^theta for all x; theta>0, C>=0. Node count O(Y^{3/2-theta} log^2 Y).',
 'scope':'This elementary discretization reduces a continuous scalar bound to finitely many scalar bounds at each chosen window Y. It does NOT establish (M), H12, control uniform constants, or RH. Additional arithmetic data may vary with x; the lemma alone cannot furnish them.',
 'derivative_checks':checks,'max_differencing_error':worst,'tests':cases}
p=Path('/mnt/data/riemann_current/riemann_h12_grid_audit.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k in ('derivative_checks','max_differencing_error','tests')},indent=2));print('SHA256 CODE',hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print('SHA256 JSON',hashlib.sha256(p.read_bytes()).hexdigest())
