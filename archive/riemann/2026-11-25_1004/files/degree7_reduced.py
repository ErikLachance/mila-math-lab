import math, sympy as s, mpmath as m, itertools,time,sys,os
from fractions import Fraction as F
start=time.monotonic();m.mp.dps=100; q0=int(sys.argv[1]); N=7*q0; res={i*i%q0 for i in range(1,q0)}; eta=lambda a: 1 if a%q0 in res else -1; g=next(i for i in range(2,N) if math.gcd(i,N)==1 and (i%7)*(eta(i))%7==5)
H=[a for a in range(1,N) if math.gcd(a,N)==1 and (a%7,eta(a)) in [(1,1),(6,-1)]]
C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]
e=[1,-2,-3,-1,2,3];r=[pow(3,j,7) for j in range(6)]
logs=[sum(m.log(2*abs(m.sin(m.pi*a/N))) for a in c) for c in C]
print('q,g',q0,g,flush=True);print('u logs',[float(v) for v in logs]); print('b logs',[float(sum(e[l]*logs[(l+j)%6] for l in range(6))/7) for j in range(6)])
# Try short integer combinations of trace vectors; heuristic basis selection.
E=[[e[(l-j)%6] for l in range(6)] for j in range(6)]
d=[[ (E[j][l]-r[j]*e[l])//7 for l in range(6)] for j in range(6)]
zeta=m.exp(2j*m.pi/7)
def values(k):
 bs=[m.exp(sum(e[l]*logs[(l+j)%6] for l in range(6))/7+k*logs[j]) for j in range(6)]
 return [sum(bs[j]*zeta**(i*r[j]) for j in range(6)) for i in range(4)]
def vec(v):return [m.re(v[0])]+[a for x in v[1:] for a in (m.sqrt(2)*m.re(x),m.sqrt(2)*m.im(x))]
# search unit exponent vector k_j with small max archimedean bound
cands=[]
for k in itertools.product(range(-1,2),repeat=5):
 k=k+(0,)
 bs=[m.exp(sum(e[l]*logs[(l+j)%6] for l in range(6))/7+sum(k[l]*logs[(l+j)%6] for l in range(6))) for j in range(6)]
 cands.append((max(bs),k,vec([sum(bs[j]*zeta**(i*r[j]) for j in range(6)) for i in range(4)])))
cands.sort(key=lambda a:a[0]); scale=10**60
# Pick a basis certified over a finite field, so exact algebraic relations cannot masquerade as tiny real singular values.
for k in range(2,100000):
 ell=N*k+1
 if not s.isprime(ell):continue
 ell=int(ell);z=pow(int(s.primitive_root(ell)),k,ell);zz=pow(z,q0,ell)
 us=[math.prod((1-pow(z,a,ell))%ell for a in c)%ell for c in C];al=math.prod(pow(u,v,ell) for u,v in zip(us,e))%ell
 if pow(al,(ell-1)//7,ell)!=1:continue
 b=int(s.nthroot_mod(al,7,ell));bs=[pow(b,r[j],ell)*math.prod(pow(u,v,ell) for u,v in zip(us,d[j]))%ell for j in range(6)]
 break
rows=[[1]+[a for i in range(3) for a in (m.sqrt(2),0)]];ks=[None];rr=[[1]*7]; piv=[0]
def rank7(rr):
 a=[x[:] for x in rr];i=0
 for j in range(7):
  k=next((k for k in range(i,len(a)) if a[k][j]%ell),None)
  if k is None:continue
  a[k],a[i]=a[i],a[k];a[i]=[x*pow(a[i][j],-1,ell)%ell for x in a[i]]
  for k in range(i+1,len(a)):
   z=a[k][j];a[k]=[(x-z*y)%ell for x,y in zip(a[k],a[i])]
  i+=1
 return i
for _,k,v in cands:
 cs=[math.prod(pow(us[(l+j)%6],v,ell) for l,v in enumerate(k))%ell for j in range(6)]
 vz=[sum(pow(zz,i*r[j],ell)*bs[j]*cs[j] for j in range(6))%ell for i in range(7)]
 if rank7(rr+[vz])==len(rr):continue
 rr.append(vz);rows.append(v);ks.append(k)
 if len(rr)==7:break
assert len(rr)==7 and rank7(rr)==7
print('basis certified at',ell,'exponents',ks)
def lll_exact(A):
 B=[list(map(int,row)) for row in A.tolist()]; d=len(B); U=[[int(i==j) for j in range(d)] for i in range(d)]
 def gs():
  Q=[]; norms=[]; mu=[[F(0) for j in range(d)] for i in range(d)]
  for i,b in enumerate(B):
   v=list(map(F,b))
   for j,q in enumerate(Q):
    z=sum(F(x)*y for x,y in zip(b,q))/norms[j];mu[i][j]=z;v=[x-z*y for x,y in zip(v,q)]
   Q.append(v);norms.append(sum(x*x for x in v)); assert norms[-1]>0
  return mu,norms
 k=1; steps=0
 while k<d:
  mu,norms=gs()
  for j in range(k-1,-1,-1):
   z=(mu[k][j]+F(1,2))//1
   if z:
    B[k]=[a-z*b for a,b in zip(B[k],B[j])];U[k]=[a-z*b for a,b in zip(U[k],U[j])];mu,norms=gs()
  if norms[k]>=(F(3,4)-mu[k][k-1]**2)*norms[k-1]:k+=1
  else:B[k],B[k-1]=B[k-1],B[k];U[k],U[k-1]=U[k-1],U[k];k=max(1,k-1)
  steps+=1;assert steps<10000
 assert s.Matrix(U)*A==s.Matrix(B);assert abs(s.Matrix(U).det())==1
 return s.Matrix(B),s.Matrix(U)
A=s.Matrix([[int(m.nint(t*scale)) for t in row] for row in rows]); L,U=lll_exact(A)
print('norms',[float(m.sqrt(sum(m.mpf(int(x))**2 for x in L.row(i)))/scale) for i in range(7)])
candidate=next(list(map(int,U.row(i))) for i in range(7) if any(U.row(i)[1:]))
print('reduced candidate',candidate)
# Rational interval for pi from Machin formula, using alternating atan series.
def atan_interval(z,n=80):
 v=sum((-1)**i*z**(2*i+1)/F(2*i+1) for i in range(n)); w=v+(-1)**n*z**(2*n+1)/F(2*n+1)
 return min(v,w),max(v,w)
l,h=atan_interval(F(1,5)); l2,h2=atan_interval(F(1,239)); pl,ph=16*l-4*h2,16*h-4*l2
# pi bounds rounded outward, and sine alternating Taylor on [0,pi/2].
M0=2**64; pl=F((pl*M0)//1,M0); ph=F(-((-ph*M0)//1),M0)
def sin_lo_hi(x,n=18):
 v=sum((-1)**i*x**(2*i+1)/math.factorial(2*i+1) for i in range(n)); w=v+(-1)**n*x**(2*n+1)/math.factorial(2*n+1)
 return min(v,w),max(v,w)
# Use a rational lower/upper bound on each positive |1-zeta^a|.
# ph*a/N < pi/2 for odd N and a <= (N-1)/2, sine monotone.
Ulo=[];Uhi=[]; cache={}
for group in C:
 lo=hi=1
 for a in group:
  a=min(a,N-a)
  if a not in cache:
   x=pl*a/N;y=ph*a/N
   l=2*sin_lo_hi(x)[0];h=2*sin_lo_hi(y)[1]
   l=int(l*M0//1);h=int(-((-h*M0)//1));assert 0<l<=h
   cache[a]=(l,h)
  l,h=cache[a];lo*=l;hi*=h
 Ulo.append(lo);Uhi.append(hi)
DEN=M0**len(C[0])
def trace_bound(k):
 exp=[e[j]+7*k[j] for j in range(6)]; maxb=0
 for j in range(6):
  num=den=1
  for l,x in enumerate(exp):
   if x>=0:num*=Uhi[(l+j)%6]**x;den*=DEN**x
   else:den*=Ulo[(l+j)%6]**(-x);num*=DEN**(-x)
  root=int(s.integer_nthroot(num//den,7)[0])+1
  maxb=max(maxb,root)
 return 6*maxb
boundroot=abs(candidate[0])+sum(abs(c)*trace_bound(k) for c,k in zip(candidate[1:],ks[1:]) if c)
bound=max(math.comb(7,k)*boundroot**k for k in range(8));print('rootbound',boundroot,'coeffbound',bound)
M=1; coeff=[0]*8;pr=[]
for k in range(2,100000):
 q=N*k+1
 if not s.isprime(q):continue
 q=int(q);z=pow(int(s.primitive_root(q)),k,q);zz=pow(z,q0,q)
 us=[math.prod((1-pow(z,a,q))%q for a in c)%q for c in C];al=math.prod(pow(u,v,q) for u,v in zip(us,e))%q
 if pow(al,(q-1)//7,q)!=1:continue
 b=int(s.nthroot_mod(al,7,q));bs=[pow(b,r[j],q)*math.prod(pow(u,v,q) for u,v in zip(us,d[j]))%q for j in range(6)]
 cs=[sum(c*math.prod(pow(us[(l+j)%6],v,q) for l,v in enumerate(k)) for c,k in zip(candidate[1:],ks[1:]))%q for j in range(6)]
 zs=[(candidate[0]+sum(pow(zz,i*r[j],q)*bs[j]*cs[j] for j in range(6)))%q for i in range(7)]
 c=[1]
 for v in zs:
  cc=[0]*(len(c)+1)
  for j,a in enumerate(c):cc[j]=(cc[j]-v*a)%q;cc[j+1]=(cc[j+1]+a)%q
  c=cc
 if M>2*bound:
  assert all((a if 2*a<=M else a-M)%q==b for a,b in zip(coeff,c));print('extra prime',q);break
 coeff=[a+M*((b-a)*pow(M,-1,q)%q) for a,b in zip(coeff,c)];M*=q;pr.append(q)
assert M>2*bound
coeff=[a if 2*a<=M else a-M for a in coeff];x=s.symbols('x');P=s.Poly(sum(a*x**i for i,a in enumerate(coeff)),x)
print('certified poly',P.as_expr());assert P.is_irreducible;print('disc',P.discriminant());open(f'/mnt/data/riemann_1004/poly{q0}.txt','w').write(str(P.as_expr()));print('CRT primes',pr,'elapsed',time.monotonic()-start)
