#!/usr/bin/env python3
"""Reproduce sign-extreme local construction within source family chi_{-d}, d=3 mod4 prime.
Checks are finite rational identities; infinitude is via CRT+Dirichlet (not computation).
"""
import json
from sympy import primerange,isprime,kronecker_symbol,mod_inverse
from sympy.ntheory.modular import crt
from mpmath import mp
mp.dps=60

def choose_residue(p, sign):
    if p==2: return 7 if sign==1 else 3,8
    for x in range(1,p):
        if int(kronecker_symbol(-x,p))==sign:
            return x,p
    raise AssertionError

def construct(bound, sign):
    ps=list(primerange(1,bound+1))
    rs,mods=zip(*(choose_residue(p,sign) for p in ps))
    x,M=crt(mods,rs,check=True)
    x=int(x);M=int(M)
    if x==0:x=M
    for trial in range(10000):
        d=x+trial*M
        if d>bound and d>3 and int(d%4)==3 and isprime(d):
            assert all(int(kronecker_symbol(-d,p))==sign for p in ps)
            return int(d), int(M),ps,trial
    raise RuntimeError('No representative found in finite scan; not a theorem issue')

def prime_sum(bound,d,omit={2,7}):
    out=mp.mpf('0')
    for p in primerange(2,bound):
        if p in omit:continue
        power=p;k=1
        while power<bound:
            out+=(1-int(kronecker_symbol(-d,p))**k)*mp.log(p)*(mp.mpf(1)/power-mp.mpf(1)/bound)
            power*=p;k+=1
    return out

def theoretical_max(bound,omit={2,7}):
    out=mp.mpf('0')
    for p in primerange(2,bound):
        if p in omit:continue
        power=p;k=1
        while power<bound:
            if k%2==1:out+=2*mp.log(p)*(mp.mpf(1)/power-mp.mpf(1)/bound)
            power*=p;k+=1
    return out

report=[]
for bound in [10,30,100]:
    plus,M,ps,t1=construct(bound,+1)
    minus,M2,ps,t2=construct(bound,-1)
    assert M==M2
    lo=prime_sum(bound,plus)
    hi=prime_sum(bound,minus)
    target=theoretical_max(bound)
    assert lo==0 and abs(hi-target)<mp.mpf('1e-55')
    report.append({'bound':bound,'num_primes':len(ps),'chi_positive_d':str(plus),'chi_negative_d':str(minus),'progression_modulus_digits':len(str(M)),'scan_steps_positive':t1,'scan_steps_negative':t2,'exact_lower_zero':lo==0,'max_bound':mp.nstr(target,36),'max_error':mp.nstr(hi-target,5)})
    print(bound, 'plus d',plus,'minus d',minus,'source-scope max',mp.nstr(target,24))
path='/mnt/data/riemann_20261123_1441_odd_quadratic_extremes.json'
with open(path,'w') as f:json.dump({'result':'PASS','scope':'d prime 3 modulo 4; chi_{-d} primitive odd real quadratic','cases':report},f,indent=2)
print('PASS',path)
