#!/usr/bin/env python3
"""Independent finite check of Rubinstein III.1 Step2 reciprocity reduction with m0 multiple of 8."""
import math, json
from itertools import product
from sympy import primerange, legendre_symbol, jacobi_symbol, factorint
from pathlib import Path

Z=42
pp=[]
for p in primerange(2,Z+1):
 n=int(p)
 while n<=Z:pp.append(n);n*=int(p)

def sf_outside(num,m):
 s=1
 for p,e in factorint(num).items():
  if m%p!=0 and e%2:s*=int(p)
 return s

progressions=0; pairs=0; primechecks=0; signs=0; qrecords=[]
for m in [8,24,40,56,120,168]:
 for a in range(1,m):
  if math.gcd(m,a)!=1:continue
  qs=[int(q) for q in primerange(2000,20000) if int(q)%m==a]
  if len(qs)<2:continue
  progressions+=1
  for n,np in product(pp[:18],pp[:18]):
   num=n*np;s=sf_outside(num,m)
   vals=set()
   for q in qs[:4]:
    if q<=num:continue
    lhs=int(legendre_symbol(num,q))
    rhs=int(jacobi_symbol(q,s)) if s>1 else 1
    assert lhs in [-1,1] and rhs in [-1,1]
    vals.add(lhs*rhs)
    primechecks+=1
   assert len(vals)==1,(m,a,n,np,s,vals)
   pairs+=1
  qrecords.append({'modulus':m,'class':a,'primes_available':len(qs)})
res={'progressions_checked':progressions,'primepower_pairs_checked':pairs,'legendre_jacobi_tests':primechecks,'status':'PASS','proof':'Quadratic reciprocity for odd p and supplements for p=2; q fixed modulo 8m forces all signs from prime factors dividing m and reciprocity parity to be constant. Remaining factors are s and give Jacobi(q,s).','scope':'Toy finite progressions q 2000..20000; no prime-counting equidistribution, character cancellation or RH conclusion','example_progressions':qrecords[:7]}
Path('/mnt/data/riemann_20261123_0908/quadratic_reciprocity_progression.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
