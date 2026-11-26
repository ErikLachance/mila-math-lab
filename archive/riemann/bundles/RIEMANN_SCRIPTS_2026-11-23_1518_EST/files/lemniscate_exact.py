#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, log
from sympy import primerange
import json,time
start=time.monotonic()
K=50
c=[Fraction(1)]
a=[]
for k in range(1,K+1):
  r=k-1
  triple=sum((c[i]*c[j]*c[r-i-j] for i in range(r+1) for j in range(r-i+1)),Fraction(0))
  ck=Fraction(-2, (4*k+1)*4*k)*triple
  c.append(ck)
for k,v in enumerate(c):
  n=4*k+1
  x=v*factorial(n)
  assert x.denominator==1,(k,x)
  a.append(int(x))

def vp(z,p):
  if z==0: return 10**9
  n=0
  while z%p==0:
    z//=p; n+=1
  return n
bad=[]; min_gap=10**9; tight=[]
for k in range(1,K+1):
  n=4*k+1
  for p in primerange(3,n+1):
    if p%4!=3: continue
    bound=n*p//(p*p-1)
    v=vp(a[k],p)
    if v<bound:bad.append({'n':n,'p':p,'v':v,'bound':bound})
    min_gap=min(min_gap,v-bound)
    if v==bound:tight.append([n,p,v])
print(json.dumps({'K':K,'max_n':4*K+1,'first_coefficients':a[:5], 'tested':sum(1 for k in range(1,K+1) for p in primerange(3,4*k+2) if p%4==3),'violations':bad[:10],'all_pass':not bad,'min_gap':min_gap,'tight_count':len(tight),'first_tight':tight[:12],'runtime_s':round(time.monotonic()-start,3),'largest_coefficient_digits':len(str(abs(a[-1])))}))
with open('/mnt/data/riemann_run_20261123_1457/lemniscate_exact.json','w') as f:json.dump({'K':K,'first_coefficients':a[:5], 'tested':sum(1 for k in range(1,K+1) for p in primerange(3,4*k+2) if p%4==3),'violations':bad,'min_gap':min_gap,'tight':tight,'largest_coefficient_digits':len(str(abs(a[-1])))} ,f,indent=2)
