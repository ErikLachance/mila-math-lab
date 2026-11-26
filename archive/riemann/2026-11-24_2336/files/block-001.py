import sympy as s
from math import gcd,prod
from time import monotonic
start=monotonic()
m=553;p=7
# F=L^+: chars even, kernel of eta and omega on L, extended by -1.
units=[a for a in range(1,m) if gcd(a,m)==1]
H=[a for a in units if (a%7==1 and s.kronecker_symbol(-79,a)==1) or (a%7==6 and s.kronecker_symbol(-79,a)==-1)]
assert len(H)==78
assert all(a*b%m in H for a in H for b in H)
g=next(a for a in units if len({pow(a,j,m) for j in range(1,7)} & set(H))==1 and pow(a,6,m) in H and all(pow(a,j,m) not in H for j in range(1,6)))
cosets=[sorted({h*pow(g,j,m)%m for h in H}) for j in range(6)]
assert sorted(sum(cosets,[]))==units
print('H size',len(H),'g',g,'coset reps',list(map(min,cosets)))
def rank(M,p):
 M=[list(map(lambda x:x%p,r)) for r in M];i=0
 for j in range(len(M[0])):
  k=next((k for k in range(i,len(M)) if M[k][j]),None)
  if k is None:continue
  M[k],M[i]=M[i],M[k];v=pow(M[i][j],-1,p);M[i]=[v*x%p for x in M[i]]
  for k in range(len(M)):
   if k!=i:
    v=M[k][j];M[k]=[(x-v*y)%p for x,y in zip(M[k],M[i])]
  i+=1
  if i==len(M):break
 return i
rows=[]
for k in range(1,1000):
 q=m*k+1
 if not s.isprime(q):continue
 a=int(s.primitive_root(q));z=pow(a,(q-1)//m,q);r=pow(a,(q-1)//7,q)
 assert pow(z,m,q)==1 and pow(z,7,q)!=1 and pow(z,79,q)!=1
 logs={pow(r,j,q):j for j in range(7)}
 U=[prod((1-pow(z,b,q))%q for b in C)%q for C in cosets]
 assert prod(U)%q==1
 ell=[logs[pow(u,(q-1)//7,q)] for u in U]
 M=[[ell[(i+j)%6] for j in range(5)] for i in range(6)]
 rows+=M
 print('q',q,'primitive',a,'z',z,'r',r,'U',U,'ell',ell,'rank',rank(M,7),'combined',rank(rows,7))
 if rank(rows,7)==5:break
print('seconds',monotonic()-start)
# independent certificate prime q=3319 and exact minor
q=3319
assert all(q%d for d in range(2,58))
assert pow(6,3318,q)==1 and all(pow(6,3318//r,q)!=1 for r in (2,3,7,79))
assert int(s.Matrix(M[:5]).det())==-180
# Independently compute minus valuation using p-adic Teichmuller via a^(7^3)
def vp(n):
 assert n
 j=0
 while n%7==0:n//=7;j+=1
 return j
vals=[]
for b in (0,1):
 for j in range(6):
  if (b+j)%2!=1:continue
  f=(79 if b else 1)*(7 if j else 1)
  n=sum(a*(int(s.kronecker_symbol(-79,a)) if b else 1)*(pow(a,343*j,2401) if j else 1) for a in range(1,f+1) if gcd(a,f)==1)%2401
  vals.append((b,j,n,vp(n)-int(f%7==0)))
assert 1+sum(x[3] for x in vals)==1
print('minus independent',vals)
# Centralizer on upper triangular matrices and actual iterated group commutator.
import numpy as np
from itertools import product
I=np.eye(3,dtype=np.int64);O=np.zeros((3,3),dtype=np.int64)
def E(i,j):
 a=O.copy();a[i,j]=1;return a
upper=[E(i,j) for i in range(3) for j in range(i,3)]
def poly(*terms):
 r=np.zeros((8,3,3),dtype=np.int64)
 for k,A in terms:r[k]=A%7
 return r
def mul(A,B):
 return np.array([sum((A[i]@B[k-i] for i in range(k+1)),O.copy())%7 for k in range(8)])
Id=poly((0,I))
def inv(A):
 Y=(Id-A)%7; P=Id.copy(); S=P.copy()
 for _ in range(7):P=mul(P,Y);S=(S+P)%7
 assert np.array_equal(mul(A,S),Id)
 return S
def comm(A,B):return mul(mul(mul(A,B),inv(A)),inv(B))
for a,b in product(range(1,7),repeat=2):
 X=a*E(2,0)+b*(E(0,1)+E(1,2))
 matrix=np.array([(X@Y-Y@X).reshape(-1) for Y in upper]).T
 assert rank(matrix.tolist(),7)==5
 # U=I+tX, V=I+t^5 E13; [U,[U,V]] has exact leading coefficient t^7 ad_X^2 E13.
 U=poly((0,I),(1,X));V=poly((0,I),(5,E(0,2)))
 W=comm(U,comm(U,V));Y=X@E(0,2)-E(0,2)@X;Z=(X@Y-Y@X)%7
 assert np.array_equal(W,poly((0,I),(7,Z)))
 assert Z[2,0]==(-2*a*a)%7!=0
 P=Id.copy()
 for _ in range(7):P=mul(P,U)
 assert np.array_equal(P,poly((0,I),(7,np.linalg.matrix_power(X,7)%7)))
print('36 centralizer ranks, 36 commutators, 36 seventh powers checked; seconds',monotonic()-start)
# Filtration obstruction: E31 of a commutator with strictly upper triangular B is zero.
# Exhaustive B, basis Y; bilinearity then covers every Y.
checks=0
for b,c,d in product(range(7),repeat=3):
 B=b*E(0,1)+c*E(0,2)+d*E(1,2)
 for i,j in product(range(3),repeat=2):
  Y=E(i,j)
  assert (Y@B-B@Y)[2,0]%7==0
  checks+=1
print('filtration coordinate checks',checks,'script total seconds',monotonic()-start)

