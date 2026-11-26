# exact linear algebra over F7 for the conditional A-module calculation
import numpy as np
p=7

def rank(A):
 A=np.array(A,dtype=np.int64).copy()%p
 if A.ndim!=2:raise ValueError(A.shape)
 r=0
 for j in range(A.shape[1]):
  c=next((i for i in range(r,A.shape[0]) if A[i,j]),None)
  if c is None:continue
  A[[r,c]]=A[[c,r]];A[r]=A[r]*pow(int(A[r,j]),-1,p)%p
  for i in range(A.shape[0]):
   if i!=r:A[i]=(A[i]-A[i,j]*A[r])%p
  r+=1
 return r

def chains(lengths,weights):
 n=sum(lengths);D=np.zeros((n,n),dtype=np.int64);w=[];o=0
 for l,a in zip(lengths,weights):
  w += [(a+j)%6 for j in range(l)]
  for j in range(l-1):D[o+j+1,o+j]=1
  o+=l
 return D,w
# W=A^6 and H=A^3+1; standard kernel includes D A(theta)
D,w=chains([7]*6,list(range(6)))
U=np.eye(42,dtype=np.int64)[:,[7*a+j for a in (2,4) for j in range(7)]+[7+j for j in range(1,7)]]
assert rank(U)==20 and rank(D@U)==17
print('kernel dim',rank(U),'top dim',rank(U)-rank(D@U))
for c in (1,2,3,6):
 fixed=[j for j in range(U.shape[1]) if all(w[i]%c==0 for i in np.flatnonzero(U[:,j]))]
 # subgroup order c, theta acts by primitive cth root
 V=U[:,fixed];B=np.concatenate([np.linalg.matrix_power(D,j)@V for j in range(7)],axis=1)
 print('subgroup order',c,'fixed dim',len(fixed),'orbit span',rank(B))
 if c==2:assert rank(B)==20
 if c==6:assert rank(B)<20
for m in range(1,8):
 idx=[7*a+j for a in range(6) for j in range(m)]
 r=rank(U[idx,:]);assert r==3*m-1
 print('depth',m,'relation rank',r,'quotient rank',6*m-r)
# Test canonical invariant line recovery from H/T^(m+1) to H/T^m
for m in range(1,7):
 J,weights=chains([1]+[m+1]*3,[1,0,3,5]);J2,_=chains([1]+[m]*3,[1,0,3,5]);
 inds=[0]+[1+a*(m+1)+j for a in range(3) for j in range(m)]
 ker=np.eye(len(J),dtype=np.int64)[:,np.flatnonzero(np.all(J==0,axis=0))]
 assert rank(ker[inds,:])==1 and ker[0,0]==1
 print('depth',m,'invariant image rank',rank(ker[inds,:]),'kernel dim',ker.shape[1])
# Adversarial synthetic local map: e independently varies; rank test distinguishes all choices,
# including arbitrary nonzero normalization of X0,y1,ybeta and arbitrary d.
J,weights=chains([1,3,3,3],[1,0,3,5]);I=np.eye(10,dtype=np.int64);n=0
for c in range(1,7):
 for d in range(7):
  for e in range(7):
   for a in range(1,7):
    u=(c*I[:,0]+d*I[:,2]+e*I[:,9])%7
    r=rank(np.column_stack([I[:,0],a*I[:,2],u]));assert (r==2)==(e==0);n+=1
print('synthetic exact rank checks',n)

