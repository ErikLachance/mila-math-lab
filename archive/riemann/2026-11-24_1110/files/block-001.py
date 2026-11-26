from itertools import product
from random import Random
from time import monotonic
from math import gcd
rng=Random(24111029); start=monotonic()
# Cohomology of cyclic p-groups with rank-one finite coefficients Z/p^k.
cyclic=0; sharp1=sharp2=0
for p in (3,5,7):
 for k in range(1,5):
  m=p**k
  for a in range(1,4):
   n=p**a
   for u in range(1,m):
    if pow(u,n,m)!=1:continue
    # norm via doubling (a sum of geometric progression, no division)
    def geo(j):
     if j==0:return (1,0)
     v,s=geo(j//2); w=v*v%m; z=s*(1+v)%m
     return (w*u%m,(z+w)%m) if j%2 else (w,z)
    norm=geo(n)[1]
    fixed=gcd(u-1,m); nk=gcd(norm,m)
    h1=nk*fixed//m; h2=fixed*nk//m
    assert nk*fixed%m==0 and 1<=h1<=n and 1<=h2<=n
    sharp1+=h1==n;sharp2+=h2==n;cyclic+=1
# R=Z/3^a[zeta_3], zeta^2+zeta+1=0. Enumerate modules with T^3=1.
# Use diagonal and triangular actions T=((zeta^i,b),(0,zeta^j)) for i != j;
# T^3=1 by geometric sum; include scalar/trivial and cyclic permutation examples.
cases=0; strict=0; max_excess=0; fourier_checks=0
for a in (1,2):
 m=3**a
 R=list(product(range(m),repeat=2)); zero=(0,0); one=(1,0); z=(0,1); z2=(m-1,m-1); roots=(one,z,z2)
 def add(x,y):return ((x[0]+y[0])%m,(x[1]+y[1])%m)
 def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%m)
 def vmul(c,x):return tuple(mul(c,y) for y in x)
 def vadd(x,y):return tuple(add(v,w) for v,w in zip(x,y))
 V=list(product(R,repeat=2)); Z=(zero,zero)
 for i,j in product(range(3),repeat=2):
  for b in ([zero] if i==j else [zero,one,z]+[rng.choice(R) for _ in range(3)]):
   def T(x):return (add(mul(roots[i],x[0]),mul(b,x[1])),mul(roots[j],x[1]))
   eig=[set() for _ in roots]
   for x in V:
    tx=T(x); t2=T(tx); assert T(t2)==x
    for h,root in enumerate(roots):
     if tx==vmul(root,x):eig[h].add(x)
    # unnormalized projectors P_h and sum P_h=3I
    ps=[vadd(vadd(x,vmul(roots[(-h)%3],tx)),vmul(roots[(-2*h)%3],t2)) for h in range(3)]
    assert all(T(y)==vmul(roots[h],y) for h,y in enumerate(ps))
    assert vadd(vadd(ps[0],ps[1]),ps[2])==vmul((3%m,0),x)
    fourier_checks+=1
   sz=1
   for E in eig:sz*=len(E)
   assert sz>=len(V)
   if sz>len(V):strict+=1
   q=sz//len(V); excess=0
   while q>1:
    assert q%3==0;q//=3;excess+=1
   max_excess=max(max_excess,excess);cases+=1
print(dict(cyclic_cohomology_cases=cyclic,sharp_H1=sharp1,sharp_H2=sharp2,cyclotomic_matrix_cases=cases,strict_overcounts=strict,max_excess_O_length=max_excess,Fourier_vector_checks=fourier_checks,seconds=monotonic()-start))

