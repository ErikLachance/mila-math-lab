import numpy as np
from itertools import product
p=7
# basis X0, D^j y1, D^j yeta, D^j ybeta
I=np.eye(22,dtype=np.int64); D=np.zeros_like(I)
for start in (1,8,15):
 for j in range(6):D[start+j+1,start+j]=1
weights=[3]+[w*pow(3,j,7)%7 for w in (1,6,5) for j in range(7)]
G=np.diag(weights);S=sum((pow(__import__('math').factorial(j),-1,7)*np.linalg.matrix_power(D,j) for j in range(7)),np.zeros_like(I))%7
assert np.array_equal(G@D%7,3*D@G%7)
assert np.array_equal(G@S%7,np.linalg.matrix_power(S,3)@G%7)
assert np.array_equal(np.linalg.matrix_power(S,7)%7,I)
def rank(A):
 a=np.array(A,dtype=np.int64).copy()%7;i=0
 for j in range(a.shape[1]):
  k=next((k for k in range(i,a.shape[0]) if a[k,j]),None)
  if k is None:continue
  a[[i,k]]=a[[k,i]];a[i]=a[i]*pow(int(a[i,j]),-1,7)%7
  for k in range(i+1,a.shape[0]):a[k]=(a[k]-a[k,j]*a[i])%7
  i+=1
  if i==a.shape[0]:break
 return i
# W consists of 7 copies of 6 local lines. Each maps equivariantly into M.
# u_theta=X0 + D*y1 + e*D^2*ybeta; u_theta2=D^2*y1+f*D^3*ybeta.
for e,f in product(range(7),repeat=2):
 V=np.column_stack([I[:,1],I[:,3]+f*I[:,18],I[:,0]+I[:,2]+e*I[:,17],I[:,5],I[:,15],I[:,8]])%7
 assert rank(V)==6 and np.array_equal(G@V%7,V*np.arange(1,7)%7)
 W=np.column_stack([np.linalg.matrix_power(S,i)@V%7 for i in range(7)])
 assert rank(W)==22
 assert [rank(np.linalg.matrix_power(D,i)) for i in range(1,8)]==[18,15,12,9,6,3,0]
print('49 synthetic equivariant quotients, including all zero/nonzero combinations, passed. Not Galois realizations.')

