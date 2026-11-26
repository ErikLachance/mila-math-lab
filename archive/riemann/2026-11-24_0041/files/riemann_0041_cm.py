from itertools import combinations,product
from math import isqrt,prod
import json,time
start=time.monotonic()
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def sc(a,k):return (a[0]*k,a[1]*k)
def norm(a):return a[0]**2+a[1]**2
def exactdiv(a,k):assert a[0]%k==a[1]%k==0;return (a[0]//k,a[1]//k)
def fieldmul(v,w,m):
 a,b=v;c,d=w;k=(m-1)//4
 return add(mul(a,c),sc(mul(b,d),k)),add(add(mul(a,d),mul(b,c)),mul(b,d))
def trace(v):return add(sc(v[0],2),v[1])
def gram(v,w,m):return exactdiv(trace(fieldmul(v,tuple(map(conj,w)),m)),m)
ps=[5,13,17,29,37,41,53,61,73,89,97,101]
fac={p:next((a,isqrt(p-a*a)) for a in range(1,isqrt(p)+1) if isqrt(p-a*a)**2==p-a*a) for p in ps}
checks=0;matrix_entries=0;normone=0;maxm=0
for k in range(1,5):
 for subset in combinations(ps,k):
  m=prod(subset);maxm=max(maxm,m);r=(m+1)//2
  assert (r*r-r-(m-1)//4)%m==0
  for signs in product((1,-1),repeat=k):
   pi=(1,0)
   for p,s in zip(subset,signs):pi=mul(pi,(fac[p][0],s*fac[p][1]))
   assert norm(pi)==m
   v=((conj(pi)),(0,0));w=((-r,0),(1,0))
   G=[[gram(x,y,m) for y in (v,w)] for x in (v,w)]
   assert G==[[(2,0),neg(conj(pi))],[neg(pi),((m+1)//2,0)]]
   matrix_entries+=4
   assert add(mul(G[0][0],G[1][1]),neg(mul(G[0][1],G[1][0])))==(1,0)
   # nearest Gaussian integer to pi/2; tie picks floor
   a=(pi[0]//2,pi[1]//2);b=(1,0)
   t=tuple(add(mul(a,x),mul(b,y)) for x,y in zip(v,w))
   assert gram(t,t,m)==(1,0)
   normone+=1
   # explicit orthogonal split: second vector z=e1-h(e1,t)*t
   e1=v;h=gram(e1,t,m);z=tuple(add(x,neg(mul(h,y))) for x,y in zip(e1,t))
   assert gram(z,t,m)==(0,0) and gram(z,z,m)==(1,0)
   # basis transform [[a,1],[1-ha,-h]] has determinant -1
   assert add(mul(a,neg(h)),neg(add((1,0),neg(mul(h,a)))))==(-1,0)
   checks+=1
print(json.dumps(dict(families=checks,gram_entries=matrix_entries,norm_one_and_orthogonal_basis=normone,largest_m=maxm,seconds=time.monotonic()-start),indent=2))
