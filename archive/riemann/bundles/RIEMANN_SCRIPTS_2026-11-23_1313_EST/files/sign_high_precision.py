from sympy import primerange
from mpmath import mp
import json
mp.dps=70
C=mp.dirichlet(1,[0,1,0,-1],1)/mp.dirichlet(1,[0,1,0,-1])
queries=[100,274,275,276,355,356,1000,20000,21318,21319,21320,22833,22834,50000,100000,200000]
X=max(queries)
seq=[]
for p in primerange(2,X+1):
  k=int(p)
  while k<=X:
    seq.append((k,int(p)))
    k*=int(p)
seq.sort()
A=B=Ac=Bc=mp.mpf(0)
idx=0;out={}
for x in queries:
  while idx<len(seq) and seq[idx][0]<=x:
    n,p=seq[idx];lam=mp.log(p);h=0 if n%2==0 else (1 if n%4==1 else -1)
    A+=lam/n;B+=lam;Ac+=h*lam/n;Bc+=h*lam;idx+=1
  g1=x*(A-mp.log(x)+1+mp.euler)-B
  g4=x*(Ac+C)-Bc
  out[x]={'G1':mp.nstr(g1,32),'G4':mp.nstr(g4,32)}
print(json.dumps(out,indent=2))
open('/mnt/data/riemann_20261123_1253/sign_high_precision.json','w').write(json.dumps(out,indent=2))
