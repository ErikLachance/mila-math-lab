from math import gcd,lcm
from itertools import product
import json,time
start=time.monotonic();checks=0;residue_pairs=0;explicit_c2=0;examples=[]
# Represent all characters of U(2^v) x U(p) as rational phases with common denominator D.
for v in range(0,6):
 for p in [3,5,13,17]:
  u2=1<<v; cyc=1<<max(0,v-2)
  g=next(x for x in range(2,p) if len({pow(x,t,p) for t in range(p-1)})==p-1)
  logp={pow(g,t,p):t for t in range(p-1)}
  if v<=1: log2={1%u2:(0,0)}; ss=[0]
  else:
   log2={((-1)**s*pow(5,t,u2))%u2:(s,t) for s in range(2) for t in range(cyc)};ss=[0,1]
  assert len(log2)==max(1,u2//2)
  D=lcm(2,cyc,p-1)
  for e in [max(1,v-2),max(1,v-2)+1]:
   W=2**(e+2); assert W>=u2
   rows=[(min(a,W-a),*log2[a%u2],t) for a in range(1,W,2) for t in logp.values()]
   for s0,k,j in product(ss,range(cyc),range(p-1)):
    im={(a,(s*s0*(D//2)+t*k*(D//cyc)+z*j*(D//(p-1)))%D) for a,s,t,z in rows}
    c=lcm(2 if s0 else 1,(p-1)//gcd(j,p-1))
    assert len(im)==(2**e)*c,(v,p,e,s0,k,j,len(im),c)
    kerim={phase for a,phase in im if a==1}; assert len(kerim)==c
    checks+=1; residue_pairs+=len(rows)
    if c==2 and j==0 and s0:explicit_c2+=1
# Example with q,d factors: directly count CRT units for a small case, using all residues.
# e=1,W=8, odd base p=5, q=11,d=7, character at 5 of order 4.
W=8;p=5;q=11;d=7;N=W*p*q*d
l5={pow(2,t,p):t for t in range(4)}
leg=lambda a,r: 1 if pow(a%r,(r-1)//2,r)==1 else -1
im=set();ker=0;units=0
for a in range(1,N):
 if gcd(a,N)!=1:continue
 units+=1;w=a%W
 z=(min(w,W-w),l5[a%p],leg(a,q),leg(a,d));im.add(z)
 if z==(1,0,1,1):ker+=1
assert len(im)==4*2*4 and units==ker*len(im)
print(json.dumps(dict(character_cases=checks,unit_pair_evaluations=residue_pairs,odd_dyadic_only_factor2_cases=explicit_c2,full_crt_units=units,full_crt_image=len(im),full_crt_kernel=ker,seconds=time.monotonic()-start),indent=2))
