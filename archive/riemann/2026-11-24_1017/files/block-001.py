from itertools import product
from random import Random
from time import monotonic
rng=Random(241017); t=monotonic()
# finite mixed torsion modules, near-identity lift B=I+p^b C preserving relations
cases=steps=0
for _ in range(300):
 p=rng.choice([2,3,5]); b=2 if p==2 else 1
 ex=[rng.randint(1,4),rng.randint(1,3)]; m=[p**a for a in ex]
 # B maps each relation m[j]e_j into the relation lattice.
 B=[[int(i==j)+p**max(b,ex[i]-ex[j])*rng.randint(-3,3) for j in range(2)] for i in range(2)]
 def mul(A,C):return [[sum(A[i][k]*C[k][j] for k in range(2))%m[i] for j in range(2)] for i in range(2)]
 def power(A,k):
  z=[[1,0],[0,1]]
  while k:
   if k&1:z=mul(z,A)
   A=mul(A,A);k//=2
  return z
 def image(A):return {tuple(sum((A[i][j]-int(i==j))*x[j] for j in range(2))%m[i] for i in range(2)) for x in product(*(range(a) for a in m))}
 im=image(B)
 for k in range(1,4):
  actual=image(power(B,p**k)); expected={tuple(p**k*x[i]%m[i] for i in range(2)) for x in im}
  assert actual==expected
  assert len(im)<=p**(2*k)*len(actual)
  steps+=1
 cases+=1
# exact local prefix bound: arbitrary scalar p-adic centers incl. exact resonances
prefix=0
for _ in range(3000):
 p=rng.choice([2,3,5,7]); T=rng.randint(2,300); M=rng.randint(1,T); c=rng.randint(-T*T,T*T)
 def vp(a):
  if not a:return 10**9
  v=0
  while a%p==0:a//=p;v+=1
  return v
 vals=[vp(r-c) for r in range(1,T+1)]; i=max(range(T),key=vals.__getitem__)+1
 K=0; q=1
 while q*p<=T-1:q*=p;K+=1
 V=[vals[r-1] for r in range(1,M+1) if r!=i]
 assert all(v<=K for v in V)
 assert sum(V)*(p-1)<=M+K*(p-1)
 prefix+=1
# H1(C2, cyclic 2-primary module) = ker(1+a)/image(a-1)
cyclic=0
for k in range(1,12):
 m=2**k
 for a in range(1,m,2):
  if a*a%m!=1:continue
  ker=sum((1+a)*x%m==0 for x in range(m)); im=len({(a-1)*x%m for x in range(m)})
  assert ker%im==0 and ker//im<=2
  cyclic+=1
print(dict(mixed_torsion_cases=cases,exact_image_growth_checks=steps,prefix_bounds=prefix,cyclic_H1_checks=cyclic,seconds=monotonic()-t))
