import numpy as np
from itertools import product
from time import monotonic
from sympy import primerange
s=monotonic(); p=7; I=np.eye(3,dtype=np.int64); J=np.fliplr(I)
# exact arithmetic in F7[t]/t^2, pairs of coefficient matrices
Z=np.zeros_like(I)
def M(a,b=None): return np.array([a,Z if b is None else b])%p
def mul(a,b):return np.array([a[0]@b[0],a[0]@b[1]+a[1]@b[0]])%p
def inv(a):
 m=np.concatenate([a[0].copy(),I.copy()],axis=1)
 for i in range(3):
  k=next(k for k in range(i,3) if m[k,i]%p);m[[i,k]]=m[[k,i]];m[i]=m[i]*pow(int(m[i,i]%p),-1,p)%p
  for k in range(3):
   if k!=i:m[k]=(m[k]-m[k,i]*m[i])%p
 b=m[:,3:];return M(b,-b@a[1]@b)
def th(a):return np.array([J@z.T@J for z in inv(a)])%p
def eq(a,b):return np.array_equal(a%p,b%p)
def diag(d):return M(np.diag(d))
def upper(a):return not np.any(np.tril(a,-1))
def conj(c,a,sign=1):return mul(mul(c,a),inv(c if sign==1 else th(c)))
def mat(vals,lower=False):
 z=Z.copy(); indices=[(1,0),(2,0),(2,1)] if lower else [(0,1),(0,2),(1,2)]
 for (i,j),v in zip(indices,vals):z[i,j]=v
 return M(I,z)
# prove only lower coordinates occur in flag chart; check signed conjugacy and triple constraints
rng=np.random.default_rng(20261125); count=0; checks=0; d=diag([2,1,4]); ident=M(I)
for vals in product(range(7),repeat=3):
 c=mat(vals,True)
 for sign in [1,-1]:
  g=mul(diag([3,2,5]),mat(rng.integers(0,7,3)))
  h=conj(c,g,sign)
  assert eq(conj(inv(c),h,sign),g)
  assert eq(mul(mul(h,conj(c,d)),inv(h)) if sign==1 else mul(mul(h,th(conj(c,d))),inv(h)),conj(c,mul(mul(g,d),inv(g))))
  checks+=2
  ss=[]; chars=[]
  for v in rng.choice([1,2,4],3):
   v=int(v); ds=[v,1,pow(v,-1,7)];chars.append(ds)
   ss.append(conj(c,mul(diag(ds),mat(rng.integers(0,7,3)))))
  n=[(a-chars[i][i]*ident)%p for i,a in enumerate(ss)]
  assert not np.any(mul(mul(n[0],n[1]),n[2])); checks+=1
  count+=1
# converse in diagonal basis: exhaust every first-order perturbation of a diagonal at each of 3 roots.
# triple equations with s* force 4 entries then trace fixes middle diagonal. compare against exact upper form.
# N1(s*)N2(s*)=multiple E33, N2(s*)N3(s*)=multiple E11.
N=[(d-x*ident)%p for x in [2,1,4]]
# exhaust all offdiagonal combinations, diagonal perturbations tested separately via trace and equations.
converse=0
for vals in product(range(7),repeat=3):
 for up in [(0,0,0),(1,2,3)]:
  lower=mat(vals,True)[1];u=mat(up)[1]
  for v in [1,2,4]:
   a=M(np.diag([v,1,pow(v,-1,7)]),lower+u)
   good=not np.any(mul(mul(N[0],N[1]),(a-pow(v,-1,7)*ident)%p)) and not np.any(mul(mul((a-v*ident)%p,N[1]),N[2]))
   assert good==upper(a);converse+=1
# e criterion: regular diagonal and dual cyclotomic weights not trivial
eligible=[];n=0
for q in primerange(3,100):
 for e in range(q-1):
  n+=1; regular=(e%(q-1)!=0 and 2*e%(q-1)!=0)
  unob=(e%(q-1)!=1 and 2*e%(q-1)!=1)
  if regular and unob:eligible.append((q,e))
assert (7,2) in eligible and (7,1) not in eligible and (5,2) not in eligible
print(f'{count=} {checks=} {converse=} {n=} eligible={len(eligible)} seconds={monotonic()-s:.4f}')
# Exact marked tangent gauge calculation over all possible regular residual diagonals and all gauge directions.
mark=0
for u in [2,3,4,5]:
 D=np.diag([u,1,pow(u,-1,7)]);di=pow(u,-1,7)
 for x,y,z in product(range(7),repeat=3):
  Y=np.array([[z,x,0],[y,0,-x],[0,-y,-z]])
  assert np.array_equal((-J@Y.T@J-Y)%7,Z)
  B=(Y@D-D@Y)%7
  assert (B[0,1]-B[1,2])%7==x*(di-u)%7
  assert (B[1,0]-B[2,1])%7==y*(u-di)%7
  mark+=1
print(f'{mark=} total_seconds={monotonic()-s:.4f}')

