import sys,json,time,itertools,math
from pathlib import Path
import sympy as s, mpmath as mp, numpy as np
from order7 import change,lin,structure,disc,x,C,saturate
q=int(sys.argv[1]);start=time.monotonic();root=Path(__file__).parent;mp.mp.dps=350
read=lambda n:json.loads((root/n).read_text()); a=read(f'fullorder{q}.json');b=read(f'fullorder21_{q}.json');P=s.Poly(a['poly'],x)
B=s.Matrix(a['B']);M=[s.Matrix(v) for v in a['M']];one=s.Matrix(a['one']).applyfunc(s.Rational)
T=s.kronecker_product(B,s.eye(3))*s.Matrix(b['B']);MM=[s.Matrix(v) for v in b['M']];oo=s.Matrix(b['one']).applyfunc(s.Rational)
# Normalize input polynomial for numerical embeddings only. Exact norms and integral bases do not rely on numerical precision.
scale=10**(max(1,len(str(abs(int(P.nth(0)))))//7)); Q=s.Poly(P.as_expr().subs(x,x*scale)/scale**7,x); roots=Q.nroots(n=300,maxsteps=1000); roots=[mp.mpc(str(s.re(z)),str(s.im(z)))*scale for z in roots if s.im(z)>=0];cs=[mp.mpf(str(z)) for z in C.nroots(n=300)];assert len(roots)==4 and roots[0].imag==0

def em(bs,deg):
 rows=[]
 for a in roots:
  for c in (cs if deg==21 else [1]):
   row=[a**i*c**j for i in range(7) for j in range(deg//7)]
   rows.append([mp.re(z)*(1 if a.imag==0 else mp.sqrt(2)) for z in row])
   if a.imag:rows.append([mp.im(z)*mp.sqrt(2) for z in row])
 return mp.matrix(rows)*mp.matrix([[mp.mpf(str(v.p))/int(v.q) for v in row] for row in bs.tolist()])
def reduce(E):
 scale=10**200 if E.cols==7 else 10**40;A=s.Matrix([[int(mp.nint(E[j,i]*scale)) for j in range(E.rows)] for i in range(E.cols)]);L,U=A.lll_transform(delta=s.Rational(3,4));assert L==U*A and abs(U.det())==1
 print('LLL',E.cols,'norms',[round(float(mp.sqrt(sum(int(z)**2 for z in L.row(i)))/scale),3) for i in range(E.cols)],flush=True);return U.T
# Find a simple primitive generator with index prime to 7.
U=reduce(em(B,7)); B=B*U;M=change(M,U);one=U.inv()*one
cand=[]
for k in (1,2,3):
 for inds in itertools.combinations(range(7),k):
  for signs in itertools.product([-1,1],repeat=k-1):
   v=s.zeros(7,1)
   for i,sgn in zip(inds,(1,)+signs):v[i]=sgn
   N=lin(M,v);ps=[one]
   for _ in range(6):ps.append(N*ps[-1])
   S=s.Matrix.hstack(*ps);ind=abs(int(S.det()))
   if not ind or ind%7==0:continue
   poly=s.Poly(N.charpoly(x).as_expr(),x);assert poly.discriminant()==int(a['disc'])*ind**2
   cand.append((max(abs(int(z)) for z in poly.all_coeffs()),ind,poly,S,v))
_,ind,poly,S,v=min(cand,key=lambda z:(z[0],z[1]));assert poly.is_irreducible
print('smallgen',poly.as_expr(),'index',ind,'candidates',len(cand),'mod7',s.factor_list(poly,modulus=7),flush=True)
(root/f'smallgen{q}.json').write_text(json.dumps({'poly':[int(z) for z in poly.all_coeffs()],'old_power_to_new':[[str(z) for z in row] for row in (S.inv()*B.inv()).tolist()]}))
M3=structure(C); MM=[s.kronecker_product(a,b) for a in M for b in M3]; oo=s.kronecker_product(one,s.eye(3)[:,0]); BB,MM,oo,dd=saturate(MM,[7],oo); assert dd==-7**14*q**9; T=s.kronecker_product(B,s.eye(3))*BB; E=em(T,21); U=reduce(E);MM=change(MM,U);oo=U.inv()*oo;T=T*U;E=em(T,21);mats=np.array([m.tolist() for m in MM],dtype=np.int64)
print('max structure coeff',np.max(np.abs(mats)),flush=True)
def detmod(a,p):
 a=a.copy()%p;n=a.shape[0];v=1
 for i in range(n):
  j=next((j for j in range(i,n) if a[j,i]),None)
  if j is None:return 0
  if j!=i:a[[j,i]]=a[[i,j]];v=-v
  z=int(a[i,i]);v=v*z%p
  if i+1<n:a[i+1:]=(a[i+1:]-(a[i+1:,i]*pow(z,-1,p)%p)[:,None]*a[i])%p
 return v%p
def save():
 (root/f"units{q}.json").write_text(json.dumps({"basis":[[str(v) for v in row] for row in T.tolist()],"units":units,"matrices":mats.tolist(),"one":[int(v) for v in oo]}))
units=[];attempts=0;passfilter=0;t=time.monotonic();limit=int(sys.argv[2]) if len(sys.argv)>2 else 60
for k in range(1,6):
 for inds in itertools.combinations(range(21),k):
  for signs in itertools.product([-1,1],repeat=k-1):
   if len(units)>=40 or time.monotonic()-t>limit:break
   v=[0]*21
   for i,sgn in zip(inds,(1,)+signs):v[i]=sgn
   mat=np.tensordot(v,mats,axes=1);attempts+=1
   if any(detmod(mat,p) not in (1,p-1) for p in (3,5,7,11,13)):continue
   passfilter+=1;norm=int(s.Matrix(mat.tolist()).det(method='domain-ge'))
   if abs(norm)!=1:continue
   logs=[mp.log(abs(sum(E[j,i]*v[i] for i in range(21)))) for j in range(3)]
   logs += [mp.log((sum(E[j,i]*v[i] for i in range(21))**2+sum(E[j+1,i]*v[i] for i in range(21))**2)/2)/2 for j in range(3,21,2)]
   if max(map(abs,logs))<mp.mpf('1e-60'):continue
   units.append((v,norm,[float(z) for z in logs]));print('unit',len(units),inds,signs,'norm',norm,'logrank',np.linalg.matrix_rank(np.array([a[2] for a in units]),tol=1e-9),flush=True);save()
  if len(units)>=40 or time.monotonic()-t>limit:break
 if len(units)>=40 or time.monotonic()-t>limit:break
print('attempts',attempts,'passfilter',passfilter,'unit count',len(units),'elapsed',time.monotonic()-start,flush=True)
(root/f'units{q}.json').write_text(json.dumps({'basis':[[str(v) for v in row] for row in T.tolist()],'units':units,'matrices':mats.tolist(),'one':[int(v) for v in oo]}))
