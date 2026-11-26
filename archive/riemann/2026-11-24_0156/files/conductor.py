from math import gcd,lcm
from fractions import Fraction as F
from sympy import primitive_root,totient
import json,time
start=time.monotonic();odd=dyad=0;vals=0
for p in [3,5,7,11,13]:
 for v in range(1,4):
  if p**v>400:continue
  M=p**v;N=int(totient(M));g=int(primitive_root(M));log={pow(g,t,M):t for t in range(N)}
  def cond(k):
   global vals
   for j in range(v+1):
    m=p**j;ph={};ok=True
    for a,t in log.items():
     key=a%m;z=k*t%N;vals+=1
     if key in ph and ph[key]!=z:ok=False;break
     ph[key]=z
    if ok:return j
   raise AssertionError
  c=[cond(k) for k in range(N)]
  for m in range(1,N+1):
   if N%m:continue
   measured=F(sum(c[k] for k in range(0,N,N//m)),m)
   a=0;t=m
   while t%p==0:a+=1;t//=p
   expected=F(a+1)-F(1,m)-(1-F(1,p**a))/(p-1)
   assert measured==expected,(p,v,m,measured,expected)
   odd+=1
for e in range(1,7):
 M=2**(e+2);N=2**e;log={((-1)**s*pow(5,t,M))%M:(s,t) for s in range(2) for t in range(N)}
 for signs in [(0,),(0,1)]:
  cs=[]
  for s0 in signs:
   for k in range(N):
    for j in range(e+3):
     ph={};ok=True
     for a,(s,t) in log.items():
      key=a%(2**j);z=(s*s0*(N//2)+t*k)%N;vals+=1
      if key in ph and ph[key]!=z:ok=False;break
      ph[key]=z
     if ok:cs.append(j);break
  expected=F(e+1)-F(1,N) if len(signs)==1 else F(e+1)
  assert F(sum(cs),len(cs))==expected
  dyad+=1
print(json.dumps(dict(odd_local_subgroups=odd,dyadic_local_subgroups=dyad,phase_comparisons=vals,seconds=time.monotonic()-start)))

