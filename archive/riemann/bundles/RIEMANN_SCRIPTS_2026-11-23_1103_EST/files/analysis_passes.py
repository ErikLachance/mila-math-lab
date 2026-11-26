#!/usr/bin/env python3
"""Reproducible, falsification-oriented micro-passes, not a new proof of RH."""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt, log, sqrt
import json, math, time, hashlib
import mpmath as mp

getcontext().prec=60
mp.mp.dps=32

def von_mangoldt_table(N):
    # True natural logs are kept as mpmath; prime powers computed by sieve.
    ps=[True]*(N+1)
    if N>0: ps[0]=False
    if N>1: ps[1]=False
    for p in range(2,isqrt(N)+1):
        if ps[p]:
            for k in range(p*p,N+1,p): ps[k]=False
    lam=[mp.mpf('0')]*(N+1)
    for p in range(2,N+1):
        if ps[p]:
            pow=p
            while pow<=N:
                lam[pow]=mp.log(p)
                pow*=p
    return lam

lam=von_mangoldt_table(300)
z=[mp.zetazero(j) for j in range(1,61)]
zero_conj=[mp.conj(v) for v in z]

def G(x):
    x=mp.mpf(x)
    prime_sum=sum(lam[n]*(x/n-1) for n in range(2,int(x)+1))
    return prime_sum-x*mp.log(x)+(1+mp.euler)*x

def trivials(x):
    x=mp.mpf(x)
    return mp.fsum(x**(-2*k)/((2*k)*(2*k+1)) for k in range(1,60))

def explicit_approx(x,K):
    x=mp.mpf(x)
    rho_sum=mp.fsum(2*mp.re(x**z[j]/(z[j]*(z[j]-1))) for j in range(K))
    return mp.log(2*mp.pi)-trivials(x)-rho_sum

out={'precision_decimal':mp.mp.dps,'formula_tests':[], 'balances':[], 'mellin':{},'notes':[]}
for X in [2,3,5,10,20,50,100,200]:
    a=G(X)
    e20=explicit_approx(X,20)
    e400=explicit_approx(X,60)
    out['formula_tests'].append({'X':X,'G':mp.nstr(a,22),'approx_20zeros':mp.nstr(e20,22),'approx_60zeros':mp.nstr(e400,22),'error_20':mp.nstr(a-e20,18),'error_60':mp.nstr(a-e400,18)})
# Algebraic case audit for x/m + m: minimum at m=sqrt(x). Consider extra rank terms.
for X in [10**2, 10**4, 10**6, 10**8]:
    mm=isqrt(X)
    k=mp.mpf(X)**mp.mpf('4.5')
    n=mp.mpf(X)**2
    E=mp.mpf(X)/mm + mp.mpf(X)*mm/k + mm + k/n**2
    E1=mp.mpf(X)/mm + mm
    # Taking n~x^2, k~x^4.5 gives k/n^2=x^0.5, not smaller. xm/k=x^(-3) near.
    out['balances'].append({'x':X,'m':mm,'terms':{'x/m':mp.nstr(mp.mpf(X)/mm,12),'xm/k':mp.nstr(mp.mpf(X)*mm/k,12),'m':mm,'k/n^2':mp.nstr(k/n**2,12)},'sum':mp.nstr(E,18),'sum_over_sqrt_x':mp.nstr(E/mp.sqrt(X),14)})
# verify Mellin kernel for a single term and the weighted Dirichlet series analytically and numerically
for s in [mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3.2')]:
    for n in [2,7]:
        integrand=mp.quad(lambda x: (x/n-1)*x**(-s-1), [mp.mpf(n),mp.inf]); rhs=mp.mpf(n)**(-s)/(s*(s-1))
        out.setdefault('kernel_integrals',[]).append({'s':str(s),'n':n,'lhs':mp.nstr(integrand,24),'rhs':mp.nstr(rhs,24),'difference':mp.nstr(integrand-rhs,10)})
# The infinite G Mellin integral is NOT evaluated numerically (would require all prime powers).
out['mellin']={'analytic_identity':'M_G(s)=-zeta_prime(s)/(zeta(s)*s*(s-1))-(s-1)^(-2)+(1+gamma)/(s-1), initially Re s>1; if |G(X)|<<X^(theta) then M_G holomorphic Re s>theta, excludes zeta zeros to right of theta, except zeta pole at s=1.','scope':'Algebraic derivation; numerical kernel checks only.'}
out['notes']=['Initial trial incorrectly attempted numerical Mellin quadrature to infinity using a prime table capped at 300. That timed out and would be invalid even if it finished; the flawed trial was removed. No Mellin integral value claimed.','Zeros truncated at 60 positive heights; partial explicit formula is numerical diagnostics, not a RH certificate.','At prime-power endpoints G is continuous, since (X/n-1)_+ vanishes at X=n.']
path='/mnt/data/riemann_runs/20261123_1047/analysis_passes.json'
with open(path,'w') as f:json.dump(out,f,indent=2)
print(json.dumps({'file':path, 'data':out},indent=2)[:13000])
