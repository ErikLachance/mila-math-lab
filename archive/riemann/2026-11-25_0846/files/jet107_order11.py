import numpy as np
p=7; n=12
I=np.eye(3,dtype=np.int64);Z=np.zeros((n,3,3),dtype=np.int64);one=Z.copy();one[0]=I
X=np.array([[0,1,0],[0,0,1],[1,0,0]],dtype=np.int64)
# c,e and u4 coefficient in cert1 k=1, place0
c,e,f=3,2,3

def mul(A,B):
 C=Z.copy()
 for i in range(n):
  for j in range(n-i): C[i+j]=(C[i+j]+A[i]@B[j])%p
 return C

def power(A,k):
 B=one.copy()
 for _ in range(k): B=mul(B,A)
 return B

def inv(A):
 T=(A-one)%p;R=one.copy();B=one.copy()
 for j in range(1,n): B=mul(B,T);R=(R+(-1)**j*B)%p
 assert np.array_equal(mul(A,R),one)
 return R

def RREF(A):
 A=A.copy()%p;i=0;cols=[]
 for j in range(A.shape[1]-1):
  q=np.flatnonzero(A[i:,j]);
  if not len(q):continue
  k=i+q[0];A[[i,k]]=A[[k,i]];A[i]=A[i]*pow(int(A[i,j]),-1,p)%p
  cc=A[:,j].copy();cc[i]=0;A=(A-cc[:,None]*A[i])%p;cols.append(j);i+=1
  if i==len(A):break
 if np.any(A[i:,-1]):return None,i
 sol=np.zeros(A.shape[1]-1,dtype=np.int64);sol[cols]=A[:i,-1];return sol,i

for model in ('linear','truncated_exp'):
 A=one.copy()
 if model=='linear':A[1]=X
 else:
  import math
  for j in range(1,7):A[j]=np.linalg.matrix_power(X,j)*pow(math.factorial(j),-1,p)%p
 AI=inv(A)
 def T(B):return (mul(mul(A,B),AI)-B)%p
 def D(B):
  Q=Z.copy();C=B.copy()
  for j in range(1,7):C=T(C);Q=(Q+(-1)**(j+1)*pow(j,-1,p)*C)%p
  return Q
 def DP(B,k):
  for _ in range(k):B=D(B)
  return B
 def forbidden(B):return B[:,np.tril_indices(3)[0],np.tril_indices(3)[1]].flatten()
 def constraints(B):return np.concatenate([forbidden(e*DP(B,2)%p),forbidden(f*DP(B,5)%p)])
 # A^7-1 has order7, so logarithm is itself to order10
 C=(power(A,7)-one)%p
 lead=Z.copy();lead[5,0,2]=c*pow(2*e,-1,p)%p
 rhs=(-np.concatenate([forbidden(c*C%p),np.zeros(6*n,dtype=np.int64)])-constraints(lead))%p
 basis=[];cols=[]
 for j in range(6,n):
  for a,b in [(0,1),(0,2),(1,2)]:
   v=Z.copy();v[j,a,b]=1;basis.append(v);cols.append(constraints(v))
 M=np.column_stack(cols);sol,r=RREF(np.column_stack([M,rhs]));print(model,'rank',r,'consistent',sol is not None)
 if sol is None:continue
 B=(lead+sum((s*v for s,v in zip(sol,basis)),Z.copy()))%p
 assert not np.any(forbidden((c*C+e*DP(B,2))%p));assert not np.any(forbidden(f*DP(B,5)%p))
 # group exponential of B (log) exact through degree10
 BG=(one+B+pow(2,-1,p)*mul(B,B))%p
 assert np.array_equal((BG-one-pow(2,-1,p)*mul(BG-one,BG-one))%p,B)
 print('B log nonzero coefficients',[(i,int(a),int(b),int(B[i,a,b])) for i in range(n) for a,b in zip(*np.nonzero(B[i]))]);print('u_theta',[(i,int(a),int(b),int(v[a,b])) for i,v in enumerate((c*C+e*DP(B,2))%p) for a,b in zip(*np.nonzero(v))]);print('u_4',[(i,int(a),int(b),int(v[a,b])) for i,v in enumerate(f*DP(B,5)%p) for a,b in zip(*np.nonzero(v))])
 # all H conjugates really commute modulo t^11, exponent7
 gen=[C+one]+[mul(mul(power(A,i),BG),inv(power(A,i))) for i in range(7)]
 for a in gen:
  for b in gen:
   comm=mul(mul(mul(a,b),inv(a)),inv(b))-one
   comm%=p
   assert not np.any(comm[:11])
   assert all(not comm[11,i,j] for i in range(3) for j in range(3) if (i,j)!=(0,2))
 assert all(np.array_equal(power(a,7),one) for a in gen)

