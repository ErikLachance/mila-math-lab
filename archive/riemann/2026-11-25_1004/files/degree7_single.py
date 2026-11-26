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
cands.sort(key=lambda a:a[0]); ks=[None,cands[0][1]];candidate=[0,1]
print('single monomial',ks[1], 'max arch heuristic',float(cands[0][0]))
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
