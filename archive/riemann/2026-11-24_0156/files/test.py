from math import gcd,prod
from itertools import product
from sympy import primerange, factorint, Matrix
from random import Random
import time,json
s=time.monotonic()
# Direct global residue enumeration versus local decomposition in a cyclotomic quotient.
def leg(a,p):
 x=pow(a%p,(p-1)//2,p);return -1 if x==p-1 else x

def power_set(p,m):
 a=1%m;out=set()
 while a not in out:out.add(a);a=a*p%m
 return out

def locals(p,m):
 v=1
 while m%p==0:v*=p;m//=p
 return v,m

def enc(a,S,q,d,mode):
 x=a%S
 if mode=='real':x=min(x,S-x)
 return (x,leg(a,q),leg(a,d))

cases=[]
for S in (16,32,48,80):
 for q,d in product([3,11,19,43],[7,23,71,103]):
  if gcd(S,q*d)!=1 or leg(q,d)!=1 or any(leg(p,d)!=1 for p in factorint(S)):continue
  if S*q*d>140000:continue
  cases.append((S,q,d))
local_checks=global_units=0;min_f_d=100000
for S,q,d in cases:
 M=S*q*d; U=[a for a in range(1,M) if gcd(a,M)==1];global_units+=len(U)
 for mode in ('real','full'):
  C=enc(-1,S,q,d,mode);G={enc(a,S,q,d,mode) for a in U}
  for p in factorint(M):
   pp,m=locals(p,M);P=power_set(p,m)
   I={enc(a,S,q,d,mode) for a in U if a%m==1%m}
   D={enc(a,S,q,d,mode) for a in U if a%m in P}
   # Independent local-coordinate construction: independently vary the ramified factor
   # and lift each compatible unramified residue via CRT.
   inv=pow(m,-1,pp)
   def lift(b,c):return c+m*((b-c)*inv%pp)
   B=[b for b in range(pp) if gcd(b,pp)==1]
   assert I=={enc(lift(b,1),S,q,d,mode) for b in B}
   assert D=={enc(lift(b,c),S,q,d,mode) for b,c in product(B,P)}
   assert C not in D and C not in I
   assert len(G)%len(D)==0 and len(D)%len(I)==0
   if p==d:
    assert I=={(1,1,1),(1,1,-1)}
    assert len(D)//len(I)%2==0
    min_f_d=min(min_f_d,len(D)//len(I))
   else:assert all(t[2]==1 for t in D)
   local_checks+=1
# Search a counterexample when d=15 mod16, leaving other split conditions intact.
ce=None
for d in primerange(7,150):
 if d%16!=15:continue
 for q in primerange(3,100):
  if q%8!=3 or q==d or leg(q,d)!=1:continue
  S=16;M=S*q*d;m=S*q;P=power_set(d,m)
  C=enc(-1,S,q,d,'real')
  D={enc(a,S,q,d,'real') for a in range(1,M) if gcd(a,M)==1 and a%m in P}
  if C in D:
   ce=dict(S=S,q=q,d=d,D_size=len(D),c=C);break
 if ce:break
assert ce
# Riemann form exact arithmetic on O_K, omega=(1+sqrt(-d))/2, omega^2=omega-(d+1)/4.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y,d):return (x[0]*y[0]-(d+1)//4*x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def conj(x):return (x[0]+x[1],-x[1])
def h(x,y,d):
 v=(0,0)
 for a,b in zip(x,y):v=add(v,mul(a,conj(b),d))
 return v
rng=Random(20261124);forms=entries=0
for d,g in product([7,23,31,71],range(1,5)):
 for _ in range(12):
  T=[[(int(i==j),0) for j in range(g)] for i in range(g)]
  if g>1:
   for k in range(5):
    i,j=rng.sample(range(g),2);a=(rng.randrange(-2,3),rng.randrange(-2,3))
    T[i]=[add(x,mul(a,y,d)) for x,y in zip(T[i],T[j])]
  V=[v for row in T for v in (row,[mul((0,1),x,d) for x in row])]
  A=Matrix([[-h(x,y,d)[1] for y in V] for x in V]);assert A.T==-A and A.det()==1
  # Compare entries to standard symplectic form in original integral coordinates.
  B=Matrix([[z for x in row for z in x] for row in V]);J=Matrix(2*g,2*g,lambda i,j: 1 if i%2==0 and j==i+1 else -1 if i%2==1 and j==i-1 else 0)
  assert B.det() in (1,-1) and A==B*J*B.T
  forms+=1;entries+=(2*g)**2
print(json.dumps(dict(host_cases=len(cases),unit_residues=global_units,local_group_checks=local_checks,min_residue_degree_d=min_f_d,counterexample_without_d_mod16_7=ce,riemann_forms=forms,alternating_entries=entries,seconds=time.monotonic()-s),indent=2))

