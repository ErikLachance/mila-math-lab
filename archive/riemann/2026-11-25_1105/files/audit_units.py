import numpy as np,sympy as s,json,sys
from pathlib import Path
p=7;I=np.eye(42,dtype=np.int64)
def rref(a):
 a=np.asarray(a,dtype=np.int64).copy()%p;i=0;piv=[]
 for j in range(a.shape[1]):
  z=np.flatnonzero(a[i:,j]);
  if not len(z):continue
  k=i+z[0];a[[i,k]]=a[[k,i]];a[i]=a[i]*pow(int(a[i,j]),-1,p)%p;c=a[:,j].copy();c[i]=0;a=(a-c[:,None]*a[i])%p;piv.append(j);i+=1
  if i==a.shape[0]:break
 return a,piv
def rank(a):return len(rref(a)[1])
def base(a):return a[:,rref(a)[1]]
def powm(a,k):
 b=np.eye(a.shape[0],dtype=np.int64)
 for _ in range(k):b=b@a%p
 return b
S=np.roll(I,-6,axis=0);D=sum(((-1)**(j+1)*pow(j,-1,p)*powm((S-I)%p,j) for j in range(1,7)),np.zeros_like(I))%p
assert not np.any(powm(D,7))
for q in (683,907):
 d=json.loads(Path(f'units_wide{q}.json').read_text());M=[s.Matrix(m) for m in d['matrices']];one=s.Matrix(d['one']);assert sum((v*m for v,m in zip(one,M)),s.zeros(21))==s.eye(21)
 assert all(m*one==s.eye(21)[:,j] for j,m in enumerate(M))
 for v,norm,_ in d['units']:
  N=sum((int(a)*m for a,m in zip(v,M) if a),s.zeros(21));assert N.det(method='domain-ge')==norm and abs(norm)==1
 a=json.loads(Path(f'partial_cert{q}_6.json').read_text());b=json.loads(Path(f'partial_cert{q}_7.json').read_text());assert a==b
 V=np.array(a['V'],dtype=np.int64).T;g=np.array(a['G'],dtype=np.int64);G=np.zeros_like(I)
 for j in range(7):G[(3*j%7)*6:(3*j%7+1)*6,j*6:(j+1)*6]=g
 assert np.array_equal(G@S%7,powm(S,3)@G%7) and np.array_equal(powm(G,6),I)
 U=base(np.hstack([powm(S,k)@V%7 for k in range(7)]));assert rank(np.hstack([U,G@U]))==U.shape[1];assert rank(np.hstack([U,S@U]))==U.shape[1]
 ranks=[rank(powm(D,k)@U) for k in range(8)];weights=[rank(sum((pow(w,-k,7)*powm(G,k) for k in range(6)),np.zeros_like(I))@U) for w in range(1,7)]
 assert sum(weights)==rank(U);print(q,'unit norms',len(d['units']),'rank',rank(U),'D restrictions',ranks,'weight dimensions',weights,'shortfall to target 20:',20-rank(U))
