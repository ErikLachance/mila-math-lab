import sympy as s, time
from sympy.matrices.normalforms import hermite_normal_form as hnf
x=s.symbols('x'); P=s.Poly(x**7 - 819*x**5 - 132370*x**4 + 7939358*x**3 - 67624354*x**2 + 4300177441*x + 57532485313,x)
C=s.Poly(x**3+x**2-2*x-1,x)
def nullmod(M,p):
 a=[[int(z)%p for z in row] for row in M.tolist()]; m,n=M.shape; piv=[]; i=0
 for j in range(n):
  k=next((k for k in range(i,m) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i]; v=pow(a[i][j],-1,p); a[i]=[z*v%p for z in a[i]]
  for k in range(m):
   if k!=i and a[k][j]:
    v=a[k][j];a[k]=[(b-v*c)%p for b,c in zip(a[k],a[i])]
  piv.append(j);i+=1
  if i==m:break
 cols=[]
 for j in range(n):
  if j not in piv:
   v=[0]*n;v[j]=1
   for k,l in enumerate(piv):v[l]=-a[k][j]%p
   cols.append(s.Matrix(v))
 return s.Matrix.hstack(*cols) if cols else s.zeros(n,0)
def structure(P):
 n=P.degree(); a=[s.eye(n)[:,i] for i in range(n)]; coeff=s.Matrix([-P.nth(i) for i in range(n)])
 for _ in range(n-1):
  v=a[-1];a.append(s.Matrix([0]+list(v[:-1]))+v[-1]*coeff)
 return [s.Matrix.hstack(*a[i:i+n]) for i in range(n)]
def lin(M,v):return sum((c*m for c,m in zip(v,M) if c),s.zeros(*M[0].shape))
def change(M,B):
 Bi=B.inv();N=[Bi*lin(M,B[:,i])*B for i in range(B.cols)];assert all(v.q==1 for m in N for v in m);return N
def disc(M):
 T=s.Matrix([[s.trace(a*b) for b in M] for a in M]);return int(T.det())
def mulmod(M,a,b,p):return (lin(M,a)*b).applyfunc(lambda z:int(z)%p)
def power(M,a,k,p,one):
 v=one
 while k:
  if k&1:v=mulmod(M,v,a,p)
  k//=2
  if k:a=mulmod(M,a,a,p)
 return v
def enlarge(M,p,one):
 n=len(M);N=s.eye(n); q=p
 while q<n:q*=p
 F=s.Matrix.hstack(*[power(M,N[:,i],q,p,one) for i in range(n)])
 K=nullmod(F,p);I=hnf((p*N).row_join(K));Ii=I.inv()
 MM=[Ii*m*I for m in M];assert all(v.q==1 for m in MM for v in m)
 E=s.Matrix.hstack(*[s.Matrix(list(m)) for m in MM]);J=nullmod(E,p)
 if J.cols==0:return None,K.cols
 B=hnf((p*N).row_join(J))/p
 assert abs(B.det())==s.Rational(1,p**J.cols)
 return B,K.cols
def saturate(M,primes,one):
 n=len(M);B=s.eye(n);d=disc(M);print('initial disc',d,flush=True)
 for p in primes:
  while True:
   A,r=enlarge(M,p,one);print('p',p,'radical dimension',r,'step index',None if A is None else 1/abs(A.det()),flush=True)
   if A is None:break
   d1=d*A.det()**2;assert d1.q==1
   M=change(M,A);one=A.inv()*one;assert all(v.q==1 for v in one);B=B*A;d=int(d1)
 assert disc(M)==d
 print('final disc',d,flush=True);return B,M,one,d
if __name__=='__main__':
 t=time.monotonic(); M=structure(P);assert P.is_irreducible;B,M,one,d=saturate(M,[7,107,373599001,47447980890086283233],s.eye(7)[:,0]);print('basis',B.tolist(),flush=True);print('degree7 seconds',time.monotonic()-t,flush=True)
 M3=structure(C);MM=[s.kronecker_product(a,b) for a in M for b in M3]; oo=s.kronecker_product(one,s.eye(3)[:,0]);dd=disc(MM);assert dd==d**3*49**7
 BB,MM,oo,dd=saturate(MM,[7,107],oo);print('degree21 index',1/abs(BB.det()),'basis',BB.tolist(),flush=True)
 print('total seconds',time.monotonic()-t,flush=True)

