from itertools import product
from random import Random
from math import factorial
from time import monotonic
import json
rng=Random(24110846); start=monotonic()
def mm(a,b):
 n=len(a);return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def power(a,k):
 z=eye(len(a))
 while k:
  if k&1:z=mm(z,a)
  k//=2
  if k:a=mm(a,a)
 return z
def det(a):
 if len(a)==1:return a[0][0]
 return sum((-1)**j*x*det([row[:j]+row[j+1:] for row in a[1:]]) for j,x in enumerate(a[0]))
def vp(a,p):
 if not a:return None
 a=abs(a);v=0
 while a%p==0:a//=p;v+=1
 return v
def diff(a,k,u):
 n=len(a);b=power(a,k);return [[u*b[i][j]-int(i==j) for j in range(n)] for i in range(n)]
checks=0; singular=0; sums=0; counts=0; max_ratio=0
for _ in range(450):
 p=rng.choice([2,3,5]); b=2 if p==2 else 1; n=rng.randrange(1,4); g=1+p**b
 # Mod-p upper unitriangular, so action is pro-p. Integer lifts need only determinant prime to p.
 A=[[int(i==j)+(rng.randrange(p) if i<j else 0)+p*rng.randrange(-2,3) for j in range(n)] for i in range(n)]
 s=0; pp=1
 while pp<n:pp*=p;s+=1
 if p==2:s+=1
 P=power(A,p**s); assert all((P[i][j]-int(i==j))%p**b==0 for i in range(n) for j in range(n))
 T=rng.randrange(n+1,18); vals=[]
 for r in range(1,T+1):
  v=vp(det(diff(A,p**s,g**(r*p**s))),p);vals.append(v)
  w=vp(det(diff(A,p**(s+1),g**(r*p**(s+1)))),p)
  assert (w is None if v is None else w==v+n); checks+=1;singular+=v is None
 # Without finding individual roots, removing n largest total valuations can only improve on removing their individual maximizers (pad with arbitrary indices).
 rem=sorted(vals,key=lambda x:float('inf') if x is None else x)[:T-n]
 assert all(v is not None for v in rem)
 assert sum(rem)*(p-1)<=n*((b+s)*(T-1)*(p-1)+T-1); sums+=1
 k=0; q=1
 while q*p<=T-1:q*=p;k+=1
 assert max(rem)<=n*(b+s+k);counts+=1
# Torsion module M=(Z/p^a)^n; image cardinal by enumeration; compare to free determinant if nonsingular.
torsion=0; singular_finite=0
for _ in range(500):
 p=rng.choice([2,3]); b=2 if p==2 else 1; n=rng.randrange(1,3); a=rng.randrange(1,5); m=p**a;g=1+p**b
 A=[[int(i==j)+p**b*rng.randrange(-2,3) for j in range(n)] for i in range(n)]
 r=rng.randrange(1,6);D=diff(A,1,g**r);v=vp(det(D),p)
 im={tuple(sum(D[i][j]*x[j] for j in range(n))%m for i in range(n)) for x in product(range(m),repeat=n)}
 size=m**n//len(im); assert m**n%len(im)==0
 if v is None:singular_finite+=1
 else:assert size<=p**v
 torsion+=1
print(json.dumps(dict(lifting_determinant_checks=checks,singular_free_cases=singular,aggregate_bounds=sums,pointwise_bounds=counts,torsion_quotient_checks=torsion,singular_free_finite_torsion=singular_finite,seconds=monotonic()-start),indent=2))

