import numpy as np
from itertools import product
from math import factorial
from time import monotonic
s=monotonic(); p=7; n=8
I=np.eye(3,dtype=np.int64); O=np.zeros((3,3),dtype=np.int64); J=np.fliplr(I)
def E(i,j):
 a=O.copy();a[i,j]=1;return a
U=E(0,1)+E(1,2); V=E(0,2); L=E(2,0)
def poly(*terms):
 r=np.zeros((n,3,3),dtype=np.int64)
 for k,a in terms:r[k]=a%p
 return r
def mul(A,B):return np.array([sum((A[i]@B[k-i] for i in range(k+1)),O.copy())%p for k in range(n)])
Id=poly((0,I))
def power(A,k):
 R=Id.copy()
 while k:
  if k&1:R=mul(R,A)
  A=mul(A,A);k//=2
 return R
def inv(A):
 Y=(Id-A)%p;P=Id.copy();R=P.copy()
 for _ in range(7):P=mul(P,Y);R=(R+P)%p
 assert np.array_equal(mul(A,R),Id)
 return R
def ad(A,Z):return mul(mul(A,Z),inv(A))
def sign(A):return np.array([J@z.T@J%p for z in inv(A)])
def delta(A,b,w):
 d=np.diag([pow(w,2,p),1,pow(w,-2,p)])
 di=np.diag([pow(w,-2,p),1,pow(w,2,p)])
 if b:A=sign(A)
 return np.array([d@z@di%p for z in A])
def eq(A,B):assert np.array_equal(A%p,B%p)
def order(Z):return next((j for j in range(n) if np.any(Z[j]%p)),n)
def rank(rows):
 M=np.array([r.reshape(-1) for r in rows],dtype=np.int64)%p;i=0
 for j in range(M.shape[1]):
  a=next((k for k in range(i,len(M)) if M[k,j]),None)
  if a is None:continue
  M[[a,i]]=M[[i,a]];M[i]=M[i]*pow(int(M[i,j]),-1,p)%p
  for k in range(len(M)):
   if k!=i:M[k]=(M[k]-M[k,j]*M[i])%p
  i+=1
  if i==len(M):break
 return i
def iterate(f,Z,k):
 for _ in range(k):Z=f(Z)
 return Z
checks=0
for a,b in product(range(1,7),repeat=2):
 X=a*L+b*U; c=a*b*b%p
 eq(np.linalg.matrix_power(X,3),c*I)
 # Artin-Hasse E_7(z) through degree 7: 1/7!+1/7 = 103/720.
 C=[pow(factorial(k),-1,p) for k in range(7)]+[103*pow(720,-1,p)%p]
 A=poly(*[(k,C[k]*np.linalg.matrix_power(X,k)) for k in range(8)])
 eq(power(A,7),poly((0,I),(7,c*c*X)));eq(power(A,49),Id)
 for e,w in product(range(2),range(1,7)):
  theta=(-1 if e else 1)*w*w%p
  eq(delta(A,e,w),power(A,pow(theta,7,49)))
  checks+=1
 for j in (4,5):
  B=poly((j,V));T=lambda Z:(ad(A,Z)-Z)%p
  D=lambda Z:sum((pow(k,-1,p)*(-1)**(k+1)*iterate(T,Z,k) for k in range(1,8-j)),np.zeros_like(Z))%p
  # leading double commutator, regardless of higher coefficients
  Z=D(D(B)); assert order(Z)==j+2
  eq(Z[j+2],a*b*U-2*a*a*L)
  # the theta sector at j=4 cannot cancel an order-six lower entry
  if j==4:
   for k in (5,6,7):
    W=poly((k,U));assert rank([Z,W,poly((7,c*c*X))])==3
  if j==5:
   W=poly((7,U));eq((-c*c*pow(2*a%p,-1,p))*Z+(3*c*c*b*pow(2,-1,p))*W,poly((7,c*c*X)))
   assert rank([B,D(B),Z,W])==4
   assert rank([B,D(B),Z,poly((7,c*c*X))])==4
   eq(D(W),np.zeros_like(W))
   # exact invariance of two inertia generators under Delta, incl signed action
   for e,w in product(range(2),range(1,7)):
    beta=(-1 if e else 1)*pow(w,4,p)%p;theta=(-1 if e else 1)*w*w%p
    eq(delta((Id+B)%p,e,w),(Id+beta*B)%p)
    eq(delta((Id+W)%p,e,w),(Id+theta*W)%p)
    checks+=2
print('36 mixed X; 432 Artin-Hasse covariance tests and 864 inertia covariance tests; 108 exact rank-3 exclusion checks, 72 rank-4 checks; all passed; covariance count',checks,'seconds',monotonic()-s)
# Character bookkeeping: exponents (eta,omega) with moduli (2,6).
chars=list(product(range(2),range(6)))
add=lambda x,y:((x[0]+y[0])%2,(x[1]+y[1])%6)
neg=lambda x:((-x[0])%2,(-x[1])%6)
th=(1,2);be=(1,4);ch=(0,2);om=(0,1)
Sunit={z:int(sum(z)%2==0)+int(z==om) for z in chars}
Kummer={z:Sunit[z]+int(z==th) for z in chars}
H1={z:Kummer[add(om,neg(z))] for z in chars}
assert sum(H1.values())==8
assert H1[th]==H1[be]==1 and H1[ch]==H1[(0,4)]==0
for z,k in product((th,be,ch),range(5)):
 c0=z
 for _ in range(k):c0=add(c0,th)
 assert (c0==th)==((z,k) in ((th,0),(be,2),(ch,3)))
print('12 global H1 character dimensions',H1)
# Regressions for degree 3 exclusion and degree 2 escape via commutators.
def bracket(A,B):return (mul(mul(mul(A,B),inv(A)),inv(B))-Id)%p
def groupcomm(A,B):return (Id+bracket(A,B))%p
for a,b in product(range(1,7),repeat=2):
 X=a*L+b*U;c=a*b*b%p
 C=[pow(factorial(k),-1,p) for k in range(7)]+[103*pow(720,-1,p)%p]
 A=poly(*[(k,C[k]*np.linalg.matrix_power(X,k)) for k in range(8)])
 # degree 3: actual N commutators from grade3 and grade4 land in E13 at grade7
 B=poly((3,V));T=lambda Z:(ad(A,Z)-Z)%p
 D=lambda Z:sum((pow(k,-1,p)*(-1)**(k+1)*iterate(T,Z,k) for k in range(1,5)),np.zeros_like(Z))%p
 Z=D(D(B));assert order(Z)==5;eq(Z[5],a*b*U-2*a*a*L)
 for k in (4,5,6,7):
  W=poly((k,U));assert rank([Z,W,poly((7,V)),poly((7,c*c*X))])==4
 for W in (E(0,1),E(1,2),V,np.diag([-a,0,a])):
  R=bracket((Id+B)%p,(Id+poly((4,W)))%p)
  assert order(R)>=7
  assert rank([R,poly((7,V))])==1
 # degree 2: actual group nested commutators produce X^7 in [N,N]
 B=(Id+poly((2,V)))%p;B1=groupcomm(A,B);B2=groupcomm(A,B1);B3=groupcomm(A,B2)
 K=bracket(B,B3);M=bracket(B1,B2)
 eq(K,poly((7,3*a*a*b*U)))
 eq(M,poly((7,-a*a*b*U-4*a*a*a*L)))
 assert rank([K,M])==2
 assert rank([K,M,poly((7,c*c*X))])==2
 x=(-c*c*pow(4*a*a%p,-1,p))%p
 y=((c*c*b+x*a*a*b)*pow(3*a*a*b%p,-1,p))%p
 eq(x*M+y*K,poly((7,c*c*X)))
print('144 degree-3 rank exclusions, 144 degree-3 central commutator tests, 36 degree-2 commutator escape certificates; all passed; total seconds',monotonic()-s)
