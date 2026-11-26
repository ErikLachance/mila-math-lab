import itertools, random, time, math, json
from fractions import Fraction as Q
import mpmath as mp
start=time.monotonic(); rng=random.Random(20261123)
# Exact Gram inequality with one exceptional Walsh coefficient, other correlations small.
checks=0; strict=0
for d in range(2,7):
 signs=list(range(1<<d)); N=len(signs)
 def walsh(x,s):return (-1)**((x&s).bit_count()&1)
 for i in range(35):
  e=rng.randrange(1,N); bias=Q(rng.randrange(-8,9),8); noise=Q(rng.randrange(0,5),10)
  perturb=[rng.randrange(1,10) for _ in signs]; total=sum(perturb)
  w=[(1-noise)*(1+bias*walsh(x,e))/N+noise*Q(perturb[x],total) for x in signs]
  assert sum(w)==1 and min(w)>=0
  corr=[sum(w[x]*walsh(x,s) for x in signs) for s in signs]
  eta=max(abs(corr[s]) for s in signs if s not in (0,e))
  a=[rng.randrange(-5,6) for s in signs]
  direct=sum(w[x]*sum(a[s]*walsh(x,s) for s in signs)**2 for x in signs)
  gram=sum(a[s]*a[t]*corr[s^t] for s in signs for t in signs)
  assert direct==gram
  bound=sum(v*v for v in a)+abs(corr[e])*sum(abs(a[s]*a[s^e]) for s in signs)+eta*sum(map(abs,a))**2
  assert direct<=bound<=2*sum(v*v for v in a)+eta*sum(map(abs,a))**2
  checks+=1;strict+=direct<bound
# Conditional sampling event intersection; exact finite model including counterexample at equality.
intersections=0
for i in range(200):
 n=20; m=15
 qbad=set(rng.sample(range(n),rng.randrange(n+1))); dbad={q:set(rng.sample(range(m),rng.randrange(m+1))) for q in range(n)}
 host={(q,d) for q in range(n) for d in range(m) if rng.randrange(3)==0}
 deltaq=Q(len(qbad),n); deltad=max(Q(len(v),m) for v in dbad.values()); good={(q,d) for q,d in host if q not in qbad and d not in dbad[q]}
 assert Q(len(good),n*m)>=Q(len(host),n*m)-deltaq-(1-deltaq)*deltad
 intersections+=1
# Numerical independent ramp/triangular differential relation using actual prime powers.
mp.mp.dps=45
limit=10000
prime=[True]*(limit+1);prime[0]=prime[1]=False
for p in range(2,math.isqrt(limit)+1):
 if prime[p]:prime[p*p::p]=[False]*((limit-p*p)//p+1)
terms=[]
for p in range(2,limit+1):
 if prime[p]:
  v=p; l=mp.log(p)
  while v<=limit:terms.append((mp.log(v),l/mp.sqrt(v)));v*=p
terms.sort(); A=(mp.sinh(mp.mpf(1)/4)/(mp.mpf(1)/4))**2
# Rather than integrate piecewise huge sums, analytic convolution of individual ramp terms.
def k(u):return max(mp.mpf(0),1-abs(u))
def g(t):return mp.exp(t/2)*(1+mp.euler-t)+sum(w*2*mp.sinh((t-a)/2) for a,w in terms if a<t)
def B(t):return A*mp.exp(t/2)-sum(w*k(t-a) for a,w in terms if abs(t-a)<1)
def primitive_exp(c,u):return mp.exp(c*u)/c
# integrate k(u)*exp(c*u) and k(u)*u*exp(c*u) via elementary moments
# on subinterval where k(u)=a+b*u.
def moments(c,l,r,a,b):
 def F(u):return mp.exp(c*u)*(a/c+b*(u/c-1/c**2))
 def J(u):return mp.exp(c*u)*(a*(u/c-1/c**2)+b*(u*u/c-2*u/c**2+2/c**3))
 return F(r)-F(l),J(r)-J(l)
def H(t):
 h=mp.mpf(0)
 for l,r,a,b in [(-1,0,1,1),(0,1,1,-1)]:
  I,J=moments(mp.mpf('.5'),l,r,a,b); h+=mp.exp(t/2)*((1+mp.euler-t)*I-J)
  for v,w in terms:
   low=max(l,v-t)
   if low>=r:continue
   P,_=moments(mp.mpf('.5'),low,r,a,b); M,_=moments(mp.mpf('-.5'),low,r,a,b)
   h+=w*(mp.exp((t-v)/2)*P-mp.exp(-(t-v)/2)*M)
 return h
errs=[]
for i in range(30):
 t=mp.mpf(2)+mp.mpf(i)/10
 result=H(t)/4-g(t+1)+2*g(t)-g(t-1)
 errs.append(abs(result-B(t)))
assert max(errs)<mp.mpf('1e-37')
# Independently integrate g*k over all knots in a smaller interval as check of H calculation.
t=mp.mpf('2.6'); knots=sorted(set([-1,0,1]+[a-t for a,w in terms if -1<a-t<1])); active=[(a,w) for a,w in terms if a<t+1]
def smallg(z):return mp.exp(z/2)*(1+mp.euler-z)+sum(w*2*mp.sinh((z-a)/2) for a,w in active if a<z)
quad=mp.quad(lambda u:k(u)*smallg(t+u),knots); qe=abs(quad-H(t)); assert qe<mp.mpf('1e-37')
print(json.dumps({'exact_gram_checks':checks,'strict':strict,'exact_host_intersection_checks':intersections,'prime_powers':len(terms),'ramp_relation_checks':len(errs),'max_abs_error':str(max(errs)),'independent_quadrature_error':str(qe),'runtime_sec':time.monotonic()-start},indent=2))

