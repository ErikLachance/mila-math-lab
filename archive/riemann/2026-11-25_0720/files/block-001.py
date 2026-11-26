import json,re,itertools,sys
from pathlib import Path
import numpy as np
p=7
src=Path('/mnt/data/RIEMANN_CHECKPOINT_2026-11-25_0619_EST.md').read_text()
old=json.loads(re.search(r'### Certificat F7.*?```json\n(.*?)\n```',src,re.S).group(1));new=json.loads(Path('/mnt/data/riemann_0720/riemann_embed_run11_certificate.json').read_text())
# independent integer-only Gauss-Jordan implementation (no numerical rank).
def reduce(a):
 a=[[int(z)%7 for z in row] for row in a];m=len(a);n=len(a[0]);piv=[]
 for j in range(n):
  k=next((k for k in range(len(piv),m) if a[k][j]),None)
  if k is None:continue
  i=len(piv);a[i],a[k]=a[k],a[i];a[i]=[v*pow(a[i][j],-1,7)%7 for v in a[i]]
  for k in range(m):
   if k!=i and a[k][j]:
    c=a[k][j];a[k]=[(u-c*v)%7 for u,v in zip(a[k],a[i])]
  piv.append(j)
  if len(piv)==m:break
 return a,piv
def rank(a):return len(reduce(a)[1])
def null(a):
 a,piv=reduce(a);n=len(a[0]);cols=[]
 for j in range(n):
  if j in piv:continue
  v=[0]*n;v[j]=1
  for i,k in enumerate(piv):v[k]=-a[i][j]%7
  cols.append(v)
 return np.array(cols,dtype=np.int64).reshape(-1,n).T
def mp(a,k):
 b=np.eye(a.shape[0],dtype=np.int64)
 for _ in range(k):b=b@a%7
 return b
def h(*a):return np.hstack(a)%7
I=np.eye(42,dtype=np.int64);S0=np.roll(I,-6,axis=0)
results=[]
for name,cert in [('prior',old),('fresh',new)]:
 V=np.array(cert['V']).T;G=np.array(cert['G']);U=h(*[mp(S0,i)@V for i in range(7)]);assert rank(U)==20
 def eig(w):
  v=null(G-w*np.eye(6,dtype=np.int64));assert v.shape==(6,1)
  return np.vstack([v,np.zeros((36,1),dtype=np.int64)])
 y1,yb,u2=eig(1),eig(5),eig(2)
 for k in range(1,7):
  S=mp(S0,k);T=(S-I)%7;D=sum(((-1)**(j+1)*pow(j,-1,7)*mp(T,j) for j in range(1,7)),np.zeros_like(I))%7
  R=h(U,mp(D,4));d1=mp(D,2)@y1%7;d2=mp(D,3)@yb%7
  assert [rank(A) for A in [R,h(R,d1),h(R,d1,d2),h(R,d1,u2),h(R,d1,d2,u2)]]==[29,30,31,31,31]
  # dual witness kills R,d1, sends d2 to 1; then must send u2 to nonzero.
  N=null(h(R,d1).T);w=next(N[:,i] for i in range(N.shape[1]) if int(N[:,i]@d2[:,0])%7)
  w=w*pow(int(w@d2[:,0])%7,-1,7)%7;assert not np.any(w@R%7) and int(w@d1[:,0])%7==0 and int(w@d2[:,0])%7==1
  e=int(w@u2[:,0])%7;assert e!=0
  hits=[(a,b) for a,b in itertools.product(range(7),repeat=2) if rank(h(R,u2-a*d1-b*d2))==29];assert len(hits)==1 and hits[0][1]==e
  results.append(dict(certificate=name,generator=k,coefficients=hits[0],witness=w.tolist(),u2_local=u2[:6,0].tolist()))
  print(name,k,'coefficients',hits[0],'dual dot',e)
# verify all 36 mixed leading directions and 6 nonzero B coefficients; no floats
E=lambda i,j:np.eye(3,dtype=np.int64)[:,i:i+1]@np.eye(3,dtype=np.int64)[j:j+1,:]
U=E(0,1)+E(1,2);L=E(2,0);V=E(0,2);C=lambda a,b:(a@b-b@a)%7
n=0
for a,b,v in itertools.product(range(1,7),repeat=3):
 X=a*L+b*U;Y=v*V;Z=C(X,C(X,C(X,Y)))
 assert np.array_equal(Z,3*a*a*b*v*(E(2,1)-E(1,0))%7) and Z[1,0] and Z[2,1]
 assert np.array_equal(C(X,C(X,Y)),v*(a*b*U-2*a*a*L)%7)
 assert np.array_equal(C(Y,C(X,Y)),2*a*v*v*V%7)
 n+=1
print('mixed commutator cases',n)
json.dump(results,open('/mnt/data/riemann_0720/order8_witnesses.json','w'),indent=2)

