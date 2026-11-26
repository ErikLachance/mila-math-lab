from fractions import Fraction as Q
from math import factorial,isqrt
from functools import lru_cache
import json,time
from pathlib import Path
BASE=Path(__file__).parent
start=time.monotonic()
B=48; D=1<<B; N=8

def fl(q): return q.numerator*D//q.denominator

def ce(q): return -fl(-q)

def roundout(a,b): return Q(fl(a),D),Q(ce(b),D)

def log_unit(r):
    assert 1<=r<=2
    z=(r-1)/(r+1); z2=z*z; v=z; total=Q(0)
    for j in range(24):
        total+=2*v/(2*j+1); v*=z2
    return total,total+2*v/(49*(1-z2))

LOG2=log_unit(Q(2))
@lru_cache(None)
def log_bound(r):
    r=Q(r); assert r>0
    e=0
    while r>=2:r/=2;e+=1
    while r<1:r*=2;e-=1
    l,h=log_unit(r)
    if e>=0:l+=e*LOG2[0];h+=e*LOG2[1]
    else:l+=e*LOG2[1];h+=e*LOG2[0]
    return roundout(l,h)

@lru_cache(None)
def invsqrt(n):
    a=isqrt(n*D*D)
    return roundout(Q(D,a+1),Q(D,a))

def coeffs(N):
    c=[1]
    for j in range(1,N+1):
        s=1<<(N-j)
        for _ in range(2):
            a=[0]*(len(c)+s)
            for i,v in enumerate(c):a[i]+=v;a[i+s]-=v
            c=a
    return c

C=coeffs(N); C2=1<<(N*(N-1)); shift=Q(2)-Q(1,2**(N-1)); step=Q(1,2**(N-1)); stepD=D//2**(N-1); shiftD=fl(shift)
var=Q(2,9*4**N); error4=32*var**2
# Exact k_N and its second derivative at dyadic point q/D (even functions).
def dens(q,der=0):
    q=-abs(q); a=q+shiftD; d=2*N-1-der
    if a<=0:return Q(0)
    total=sum(c*(a-i*stepD)**d for i,c in enumerate(C) if a>i*stepD and c)
    return Q(total*C2,factorial(d)*D**d)

def kb(n,x):
    lo,hi=log_bound(Q(n,x)); assert hi-lo<=Q(2,D)
    if lo>=2 or hi<=-2:return Q(0),Q(0)
    mid=(fl(lo)+ce(hi))//2; radius=max(abs(Q(mid,D)-lo),abs(hi-Q(mid,D)))
    v=dens(mid)+var*dens(mid,2)/2
    er=error4+(2+16*var)*radius
    return roundout(max(Q(0),v-er),max(Q(0),v+er))

# independent exact integrated truncated powers; normalization and variance
# integral v^r (v-a)_+^d = sum binomial(r,l) a^(r-l) (b-a)^(d+l+1)/(d+l+1)
from math import comb
for r in (0,1,2,4):
    d=2*N-1; b=shift; result=Q(0)
    for i,c in enumerate(C):
        a=-shift+i*step
        if a>=b or not c:continue
        result+=c*sum(Q(comb(r,l))*a**(r-l)*(b-a)**(d+l+1)/(d+l+1) for l in range(r+1))
    result*=Q(C2,factorial(d))
    vv=sum(Q(2,3*4**j) for j in range(1,N+1))
    expected={0:Q(1),1:Q(0),2:vv,4:3*vv**2-Q(4,15)*sum(Q(1,16**j) for j in range(1,N+1))}[r]
    assert result==expected,(r,result,expected)

@lru_cache(None)
def H_real(s):
    # Factors 1 <= sinh(w)/w <= exp(w^2/6); all terms positive.
    hn=32; l=h=Q(1)
    for j in range(1,hn+1):
        w2=s*s/4**j; term=Q(1); t=Q(1)
        for k in range(1,49):
            term*=w2/((2*k)*(2*k+1));t+=term
        first=term*w2/(98*99); ratio=w2/(100*101); assert ratio<1
        lo,hi=roundout(t,t+first/(1-ratio))
        l,h=roundout(l*lo,h*hi)
    u=s*s/Q(18*4**hn);assert u<1
    return roundout(l,h/(1-u))

# Prime-power list verified with trial divisions in independent check below.
def primes_to(m):
    a=bytearray(b'\x01')*(m+1); a[:2]=b'\0\0'
    for p in range(2,isqrt(m)+1):
        if a[p]: a[p*p::p]=b'\0'*((m-p*p)//p+1)
    return [p for p in range(2,m+1) if a[p]]

def run(x):
    root=isqrt(x);assert root*root==x and x>=16
    a,b=H_real(Q(1,2));lo=root*a*a;hi=root*b*b
    pl=ph=Q(0); used=0; omitted=0; primepowers=0
    for p in primes_to(8*x):
        n=p
        while n<=8*x:
            if 8*n>=x:
                primepowers+=1
                kl,kh=kb(n,x)
                if kh==0:omitted+=1
                else:
                    used+=1; ll,lh=log_bound(Q(p));sl,sh=invsqrt(n)
                    l,h=roundout(ll*sl*kl,lh*sh*kh);pl+=l;ph+=h
            n*=p
    # Trivial-zero correction: s=2m+1/2, m>=1. x perfect square.
    el=eh=Q(0);M=12
    for m in range(1,M+1):
        l,h=H_real(Q(4*m+1,2)); den=root*x**(2*m)
        el+=l*l/den;eh+=h*h/den
    r=Q(8,x);tail=r**(2*M+2)/(1-r*r)
    L,U=lo-ph-eh-tail,hi-pl-el
    assert L<=U
    return dict(x=x,primepowers=primepowers,used=used,outside_support=omitted,lower=float(L),upper=float(U),width=float(U-L),trivial_tail_bound=float(tail),lower_exact=str(L),upper_exact=str(U))

if __name__=='__main__':
    rows=[run(x) for x in [16,64,256,1024]]
    report={'N':N,'dyadic_bits':B,'exact_moment_checks':4,'pointwise_density_taylor_error':str(error4),'rows':rows,'elapsed_code_seconds':time.monotonic()-start}
    (BASE/'certified_bump.json').write_text(json.dumps(report,indent=2));print(json.dumps({**report,'rows':[{k:v for k,v in r.items() if not k.endswith('_exact')} for r in rows]},indent=2))

