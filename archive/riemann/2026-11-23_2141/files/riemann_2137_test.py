import numpy as np, math, time, json, random
from fractions import Fraction as Q
from scipy.integrate import quad
start=time.monotonic(); rng=random.Random(20261123)
N=math.ceil(math.exp(14)); prime=np.ones(N+1,dtype=bool);prime[:2]=False
for p in range(2,math.isqrt(N)+1):
 if prime[p]:prime[p*p::p]=False
p=np.flatnonzero(prime); lp=np.log(p.astype(np.longdouble));w=lp/np.sqrt(p.astype(np.longdouble));A=(np.sinh(np.longdouble(.25))/.25)**2

def k(v):return np.maximum(0,1-np.abs(v))
def H(v):
 v=np.clip(v,-1,1);return np.where(v<=0,(1+v)**2/2,1-(1-v)**2/2)
def P(t):
 a,b=np.searchsorted(lp,[t-1,t+1]);return A*np.exp(np.longdouble(t)/2)-np.sum(w[a:b]*k(lp[a:b]-t))
def F(t,t0=2):
 b=np.searchsorted(lp,t+1);return 2*A*(np.exp(np.longdouble(t)/2)-np.exp(np.longdouble(t0)/2))-np.sum(w[:b]*(H(t-lp[:b])-H(t0-lp[:b])))-(t-t0)/2
err=0
for t in np.linspace(2.1,7.0,40):
 knots=np.unique(np.concatenate([lp-1,lp,lp+1])); knots=knots[(knots>2)&(knots<t)]
 ref=quad(lambda x:float(P(x)-.5),2,t,points=list(map(float,knots)),limit=len(knots)+100,epsabs=1e-9)[0]
 err=max(err,float(abs(F(t)-ref)))
assert err<1e-8
# Exact rational antiderivative check, split piecewise polynomial independent trapezoid.
def h(v):return Q(0) if v<=-1 else (1+v)**2/2 if v<=0 else 1-(1-v)**2/2 if v<=1 else Q(1)
for i in range(1000):
 a,b=sorted([Q(rng.randrange(-100,101),32) for _ in range(2)]);cuts=[a]+[Q(j) for j in [-1,0,1] if a<j<b]+[b];
 val=sum((y-x)*(max(0,1-abs(x))+max(0,1-abs(y)))/2 for x,y in zip(cuts,cuts[1:]));assert val==h(b)-h(a)
# Prime power contamination on log scale (fixed r), exact sum of enumerated primes, compare to analytic main.
rows=[]
for t in [4,6,8,10,12,14,16,20,24,26]:
 a={}
 for r in [2,3,4,5]:
  lo,hi=np.searchsorted(lp,[(t-1)/r,(t+1)/r]);z=lp[lo:hi];v=np.sum(z*np.exp(-r*z/2)*k(r*z-t));d=1/r-.5;K=1 if d==0 else (math.sinh(d/2)/(d/2))**2; main=math.exp(d*t)*K/r
  a[str(r)]={'actual':float(v),'main':main,'ratio':float(v/main)}
 rows.append({'t':t,'powers':a})
# Tail transform bound log-stable, includes hypothetical off-line points and k up to 100.
maxdelta=-float('inf');n=0
for r in [1,2,3,10,30,100]:
 for _ in range(100):
  sigma=rng.uniform(-.5,.5);gamma=rng.uniform(2*r,100*r);z=complex(sigma,gamma)/(2*r)
  import cmath
  lhs=2*r*math.log(abs(cmath.sinh(z)/z));rhs=abs(sigma)+2*r*math.log(2*r/gamma)
  assert lhs<=rhs+1e-10;maxdelta=max(maxdelta,lhs-rhs);n+=1
# Dyadic majorant series closed form check with independent partial sum.
for r in range(1,31):
 q=2.**(1-2*r);L=math.log(4*10**6);lhs=sum(q**j*(L+j*math.log(2)) for j in range(120));rhs=L/(1-q)+math.log(2)*q/(1-q)**2;assert abs(lhs-rhs)<1e-12
out={'prime_count':len(p),'prime_limit':N,'integral_checks':40,'max_integral_abs_error':err,'exact_CDF_checks':1000,'power_samples':rows,'complex_tail_checks':n,'max_log_bound_slack':maxdelta,'dyadic_checks':30,'elapsed_s':time.monotonic()-start}
print(json.dumps(out,indent=2));open('/mnt/data/riemann_2137_results.json','w').write(json.dumps(out,indent=2))

