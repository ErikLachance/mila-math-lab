import math, json, mpmath as mp
from pathlib import Path
mp.mp.dps=65
root=Path('/mnt/data/riemann_20261123_0751')

def sieve(n):
    isprime=bytearray(b'\x01')*(n+1);isprime[:2]=b'\x00\x00'
    for k in range(2,math.isqrt(n)+1):
        if isprime[k]:isprime[k*k::k]=b'\x00'*((n-k*k)//k+1)
    return [p for p in range(2,n+1) if isprime[p]]

def ppowers(T):
    arr=[]
    for p in sieve(T):
        r=1;x=p
        while x<=T:
            arr.append((x,p,r))
            r+=1;x*=p
    return sorted(arr)

def diag(T,y):
    arr=ppowers(T)
    E=mp.mpf(0);O={}
    for n,p,r in arr:
        w=mp.log(p)*min(1,mp.mpf(y)/n)
        if r%2==0:E+=w
        else:O[p]=O.get(p,mp.mpf(0))+w
    return E*E+sum((v*v for v in O.values()),mp.mpf(0)),arr,len(O)

case=[]
for T in (30,80,200,500):
    arr=ppowers(T)
    for y in (2,3,5,8,20,50,100):
        if y>T:continue
        pred,_,np=diag(T,y)
        brute=mp.mpf(0)
        weights=[(n,mp.log(p)*min(1,mp.mpf(y)/n)) for n,p,r in arr]
        for n,wn in weights:
            for m,wm in weights:
                r=math.isqrt(n*m)
                if r*r==n*m:brute+=wn*wm
        err=abs(pred-brute)
        assert err<mp.mpf('1e-55'),(T,y,err)
        case.append({'T':T,'y':y,'pairs':len(arr)**2,'ratio_diagonal_over_ylogy':mp.nstr(pred/(y*mp.log(y)),18),'error':mp.nstr(err,3)})

# Finite T=100000; even and odd full upper: D <=400 y log y for all T and y>=2, using
# Chebyshev psi(x)<=5x, theta(x)<=3ln2*x, integration by parts.
ratios=[]
for y in (2,10,100,1000,10000):
    D,arr,np=diag(100000,y)
    assert D<=400*y*mp.log(y)
    ratios.append({'y':y,'D_T_100000':mp.nstr(D,25),'D_div_ylogy':mp.nstr(D/(y*mp.log(y)),18),'odd_prime_classes':np})

# Explicit symbolic constant:
# E <= 15 sqrt(y), E^2 <=225*y.
# O_p<=3 log y for p<=y, sum_p<=y O_p <= (5+4ln2)*y < 8y -> sum O_p^2 <=24 y log y.
# For p>y: O_p <=(4/3)y log p/p; 
# sum_{p>y} log^2(p)/p^2 <=(3ln2)(2log y+1)/y.
# sum O_p^2 <=(16/9)*(3ln2)*(2+1/ln2) y log y.
# 225y<=225/ln2*ylogy for y>=2.
C=225/mp.log(2)+24+(mp.mpf(16)/9)*(3*mp.log(2))*(2+1/mp.log(2))
assert C<mp.mpf(400)

out={'structural_exact_identity':'For prime-power terms a(p^r)=ln(p)*min(1,y/p^r), the square-class portion of sum_{n,m<=T}a(n)a(m) 1[n*m is square] equals E_T(y)^2 + sum_p O_{p,T}(y)^2; E counts even exponents, O_p counts odd exponents for one prime.','rigorous_bound_for_y>=2':'D_T(y) <= 400*y*log(y), uniform all cutoffs T>=2. This uses elementary Chebyshev theta(x)<=3 log2*x, psi(x)<=5*x, by binomial primorial recurrence and partial summation. The weaker exact upper coefficient before rounding: 225/log2 + 24 +(16/9)*(3log2)*(2+1/log2).','bound_constant':mp.nstr(C,35),'brute_pair_checks':len(case),'brute_examples':case[:9],'larger_tests':ratios,'context':'This proves a bound for square-coherent diagonal terms only; the actual mean-square prime progression theorem also needs difficult cancellation for non-square nm (quadratic reciprocity, large sieve/zero-density), not established here.','status':'elementary analytic proof of toy diagonal input, not RH proof'}
(root/'square_class_diagonal_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('brute_examples',)},indent=2))
