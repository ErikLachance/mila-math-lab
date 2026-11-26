from riemann_order_run11 import *
import mpmath as mp, itertools, json, random
mp.mp.dps=100
B,M,one,d=saturate(structure(P),[2,7,79,38737,13513109],s.eye(7)[:,0]); M3=structure(C); MM=[s.kronecker_product(a,b) for a in M for b in M3]; oo=s.kronecker_product(one,s.eye(3)[:,0]); BB,MM,oo,dd=saturate(MM,[7,79],oo)
T=s.kronecker_product(B,s.eye(3))*BB
# Minkowski embedding real and one from each complex pair, times all real cubic roots
roots=P.nroots(n=85,maxsteps=500); roots=[mp.mpc(str(s.re(z)),str(s.im(z))) for z in roots if s.im(z)>=0]; cs=[mp.mpf(str(z)) for z in C.nroots(n=85)]
rows=[]
for a in roots:
 for b in cs:
  row=[a**i*b**j for i in range(7) for j in range(3)]
  rows.append([mp.re(z) * (1 if a.imag==0 else mp.sqrt(2)) for z in row]);
  if a.imag!=0:rows.append([mp.im(z)*mp.sqrt(2) for z in row])
assert len(rows)==21
E=mp.matrix(rows)*mp.matrix([[mp.mpf(str(v.p))/int(v.q) for v in row] for row in T.tolist()]); scale=10**32
A=s.Matrix([[int(mp.nint(E[j,i]*scale)) for j in range(21)] for i in range(21)])
L,U=A.lll_transform(delta=s.Rational(3,4)); assert L==U*A and abs(U.det())==1
print('LLL norms',[round(float(mp.sqrt(sum(int(z)**2 for z in L.row(i)))/scale),3) for i in range(21)],flush=True)
MM=change(MM,U.T);oo=U.T.inv()*oo;T=T*U.T;E=E*mp.matrix(U.T.tolist())
# Norm mod small primes used as filter, exact determinant for candidates passing filter.
import numpy as np
mats=np.array([m.tolist() for m in MM],dtype=np.int64)
def detmod(a,p):
 a=a.copy()%p; n=a.shape[0];v=1
 for i in range(n):
  j=next((j for j in range(i,n) if a[j,i]),None)
  if j is None:return 0
  if j!=i:a[[j,i]]=a[[i,j]];v=-v
  x=int(a[i,i]);v=v*x%p
  if i+1<n:a[i+1:]=(a[i+1:]-(a[i+1:,i]*pow(x,-1,p)%p)[:,None]*a[i])%p
 return v%p
units=[];attempts=0;passfilter=0;seen=set();t=time.monotonic()
for k in range(1,5):
 for inds in itertools.combinations(range(21),k):
  for signs in itertools.product([-1,1],repeat=k-1):
   if len(units)>=19 or time.monotonic()-t>30:break
   v=[0]*21
   for i,sgn in zip(inds,(1,)+signs):v[i]=sgn
   mat=np.tensordot(v,mats,axes=1);attempts+=1
   if any(detmod(mat,p) not in (1,p-1) for p in (3,5,7,11,13)):continue
   passfilter+=1; norm=int(s.Matrix(mat.tolist()).det(method='domain-ge'))
   if abs(norm)!=1:continue
   logs=[]
   for j in range(0,3):logs.append(mp.log(abs(sum(E[j,i]*v[i] for i in range(21)))))
   for j in range(3,21,2):logs.append(mp.log((sum(E[j,i]*v[i] for i in range(21))**2+sum(E[j+1,i]*v[i] for i in range(21))**2)/2)/2)
   if max(map(abs,logs))<mp.mpf('1e-60'):continue
   units.append((v,norm,[float(z) for z in logs]));print('unit',len(units),inds,signs,'norm',norm,'logrank',np.linalg.matrix_rank(np.array([a[2] for a in units]),tol=1e-9),flush=True)
  if len(units)>=19 or time.monotonic()-t>30:break
 if len(units)>=19 or time.monotonic()-t>30:break
print('attempts',attempts,'passfilter',passfilter,'unit count',len(units),'seconds',time.monotonic()-t,flush=True)
json.dump({'basis':[[str(v) for v in row] for row in T.tolist()],'units':units,'matrices':mats.tolist(),'one':[int(v) for v in oo]},open('/mnt/data/riemann_units_run11.json','w'))

