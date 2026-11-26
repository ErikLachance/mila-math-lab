import numpy as np, sympy as s, itertools,time
start=time.monotonic();p=7;n=14
I=np.eye(3,dtype=np.int64);O=np.zeros((n,3,3),dtype=np.int64);one=O.copy();one[0]=I
V=np.zeros((3,3),dtype=np.int64);V[0,2]=1
lower=np.tril_indices(3,-1)
def mul(A,B):
 C=O.copy()
 for i in np.flatnonzero(np.any(A,axis=(1,2))):
  for j in np.flatnonzero(np.any(B[:n-i],axis=(1,2))):C[i+j]=(C[i+j]+A[i]@B[j])%p
 return C
def inv(A):
 R=one.copy()
 for k in range(1,n):R[k]=-sum((A[i]@R[k-i] for i in range(1,k+1)),np.zeros((3,3),dtype=np.int64))%p
 assert np.array_equal(mul(A,R),one);return R
def comm(A,B):return mul(mul(mul(A,B),inv(A)),inv(B))
def powr(A,k):
 R=one.copy()
 for _ in range(k):R=mul(R,A)
 return R
def br(X,Y):return (X@Y-Y@X)%p
# Symbolic first lower term in commutators of finite differences.
a,b,v=s.symbols('a b v');X=s.Matrix([[0,b,0],[0,0,b],[a,0,0]]);Vs=s.Matrix(V.tolist());U=X*Vs-Vs*X;W=X*U-U*X;C=U*W-W*U
assert C[2,0]==-4*a**3 and C[1,0]==C[2,1]==0
print('symbolic [ad_X V, ad_X^2 V] =',C,flush=True)
rng=np.random.default_rng(20261125);tests=0;pairs=0
for aa,bb,vv in itertools.product(range(1,7),repeat=3):
 X=np.array([[0,bb,0],[0,0,bb],[aa,0,0]],dtype=np.int64)
 A=one.copy();A[1]=X;A[2:]=rng.integers(0,7,size=(n-2,3,3));AI=inv(A)
 B=one.copy();B[5]=vv*V;B[6:]=np.triu(rng.integers(0,7,size=(n-6,3,3)),1)
 bs=[B]
 for i in range(2):bs.append(mul(mul(A,bs[-1]),AI))
 C1=mul(bs[1],inv(bs[0]));C2=mul(mul(bs[2],powr(inv(bs[1]),2)),bs[0])
 assert np.array_equal(C1[6],vv*br(X,V)%7);assert not np.any(C1[1:6]);assert np.array_equal(C2[7],vv*br(X,br(X,V))%7);assert not np.any(C2[1:7])
 C=comm(C1,C2);assert not np.any(C[1:13]);assert C[13,2,0]==(-4*aa**3*vv**2)%7!=0
 # Other commutators cannot have lower entries before degree13.
 A7=powr(A,7)
 for i,j in ((0,1),(0,2),(1,2)):
  W=comm(bs[i],bs[j]);assert not np.any(W[1:11]);assert not np.any(W[:13,lower[0],lower[1]]);pairs+=1
 for bi in bs:
  W=comm(A7,bi);assert not np.any(W[1:12]);assert not np.any(W[:13,lower[0],lower[1]]);pairs+=1
 tests+=1
print('exact randomized higher corrections for all nonzero leading triples',tests,'pair tests',pairs,'elapsed',time.monotonic()-start)
