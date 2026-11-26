import sys,math,time,json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form as hnf
# Load helper definitions without executing main loop.
exec(Path('/mnt/data/riemann_1004/order7.py').read_text().split('for q in map(int,sys.argv[1:]):')[0])
class Split(Exception):pass
def kernel(M,m):
 a=[[int(z)%m for z in row] for row in M.tolist()];r,n=M.shape;i=0;piv=[]
 for j in range(n):
  ks=[k for k in range(i,r) if a[k][j]]
  if not ks:continue
  k=next((k for k in ks if math.gcd(a[k][j],m)==1),None)
  if k is None:raise Split(math.gcd(a[ks[0]][j],m))
  a[i],a[k]=a[k],a[i];v=pow(a[i][j],-1,m);a[i]=[x*v%m for x in a[i]]
  for k in range(r):
   if k!=i and a[k][j]:
    v=a[k][j];a[k]=[(x-v*y)%m for x,y in zip(a[k],a[i])]
  piv.append(j);i+=1
  if i==r:break
 cols=[]
 for j in range(n):
  if j not in piv:
   v=[0]*n;v[j]=1
   for k,l in enumerate(piv):v[l]=-a[k][j]%m
   cols.append(s.Matrix(v))
 R=s.Matrix.hstack(*cols) if cols else s.zeros(n,0)
 assert all(int(x)%m==0 for x in M*R)
 return R

def enlarge_composite(M,m):
 n=len(M);N=s.eye(n);T=s.Matrix([[s.trace(a*b) for b in M] for a in M]);K=kernel(T,m);print('modulus digits',len(str(m)),'trace kernel dimension',K.cols,flush=True)
 I=hnf((m*N).row_join(K));Ii=I.inv()
 MM=[Ii*a*I for a in M];assert all(x.q==1 for a in MM for x in a), 'trace-kernel preimage not ideal'
 E=s.Matrix.hstack(*[s.Matrix(list(a)) for a in MM]);J=kernel(E,m);print('idealizer kernel dimension',J.cols,flush=True)
 B=hnf((m*N).row_join(J))/m
 return B,change(M,B)
for q in map(int,sys.argv[1:]):
 t=time.monotonic();P=s.Poly(Path(f'/mnt/data/riemann_1004/poly{q}.txt').read_text(),x);expected=-7**4*q**3;d=int(P.discriminant());idx=math.isqrt(d//expected);assert idx**2*expected==d
 primes=[7,41,181,633877] if q==683 else [7,293]
 B,M,one,d=saturate(structure(P),primes,s.eye(7)[:,0]);m=math.isqrt(d//expected);assert m*m*expected==d
 queue=[m];success=True
 while queue:
  m=queue.pop()
  if m==1:continue
  try:
   A,MM=enlarge_composite(M,m);ii=int(1/abs(A.det()));assert ii>1 and (m%ii==0 or ii%m==0);print('integral enlargement index',ii,flush=True);M=MM;B=B*A;one=A.inv()*one;assert all(x.q==1 for x in one)
  except Split as ex:
   f=int(ex.args[0]);assert 1<f<m and m%f==0;print('nonunit pivot exposes factor',f,flush=True);queue.extend([f,m//f]);continue
  except AssertionError as ex:
   print('enlargement not certified',str(ex),flush=True);success=False;break
 final=disc(M);print('q',q,'final disc',final,'target',expected,'equal',final==expected,'elapsed',time.monotonic()-t,flush=True)
 if final==expected:
  assert all(v.q==1 for a in M for v in a);print('FULL integral order by discriminant equality',flush=True)
  data={'q':q,'poly':str(P.as_expr()),'B':[[str(x) for x in row] for row in B.tolist()],'one':[str(x) for x in one],'M':[[[int(x) for x in row] for row in a.tolist()] for a in M],'disc':final}
  Path(f'/mnt/data/riemann_1004/fullorder{q}.json').write_text(json.dumps(data))
