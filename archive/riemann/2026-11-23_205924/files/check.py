import math,time,json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.integrate import quad
start=time.monotonic(); M=400; N=math.ceil(math.e*(M+1)**2)
# Prime power enumeration by sieve.
prime=np.ones(N+1,dtype=bool);prime[:2]=False
for p in range(2,math.isqrt(N)+1):
 if prime[p]:prime[p*p::p]=False
lam=np.zeros(N+1,dtype=np.longdouble)
for p in np.flatnonzero(prime):
 p=int(p);n=p
 while n<=N:lam[n]=np.log(np.longdouble(p));n*=p
ns=np.flatnonzero(lam); ln=np.log(ns.astype(np.longdouble)); w=lam[ns]/np.sqrt(ns.astype(np.longdouble)); P=np.r_[np.longdouble(0),np.cumsum(w)]; R=np.r_[np.longdouble(0),np.cumsum(w*ln)]
A=(np.sinh(np.longdouble(.25))/.25)**2

def B(y):
 y=np.longdouble(y); u=2*np.log(y); a,b,c=np.searchsorted(ln,[u-1,u,u+1]);
 return A*y-((1-u)*(P[b]-P[a])+R[b]-R[a]+(1+u)*(P[c]-P[b])-R[c]+R[b])

def direct(y):
 y=np.longdouble(y);u=2*np.log(y);return A*y-np.sum(w*np.maximum(0,1-np.abs(ln-u)))
maxdiff=0
for m in range(2,M+1):
 for y in [m,m+.37]:maxdiff=max(maxdiff,float(abs(B(y)-direct(y))))
assert maxdiff<1e-10
# J(t) = integral of triangular log kernel from zero to t; independent direct integration below.
lo=np.exp(np.longdouble(-.5));hi=np.exp(np.longdouble(.5));
def J(t):
 t=np.asarray(t,dtype=np.longdouble);v=np.clip(t,lo,hi)
 return np.where(v<=1,2*v*np.log(v)-v+2*lo,3*v-2*v*np.log(v)-4+2*lo)
# constant C(M) = A/2*(M^2-4) - sum lambda*(J(M/sqrt(n))-J(2/sqrt(n))).
roots=np.sqrt(ns.astype(np.longdouble)); l=lam[ns]; J2=J(2/roots)

def C(y):return A/2*(np.longdouble(y)**2-4)-np.sum(l*(J(y/roots)-J2))
# Check J endpoints and direct integration, independent Simpson/Gauss quad on split support.
assert abs(J(hi)-A/2)<1e-15
jerr=0
for t in np.linspace(.3,2,101):
 ref=quad(lambda z:max(0,1-abs(2*math.log(z))),float(lo),max(float(lo),min(t,float(hi))),points=[1] if t>1 else None,epsabs=1e-12)[0]
 jerr=max(jerr,float(abs(J(t)-ref)))
assert jerr<1e-12
# For each interval, exact measure formula for B'' variation upper bound:
# continuous part <= 2/m^2 sum active weights; jump atoms exact magnitudes.
knots=[np.sqrt(ns.astype(np.longdouble)/np.exp(np.longdouble(1))),roots,np.sqrt(ns.astype(np.longdouble)*np.exp(np.longdouble(1)))]
maxratio=0; maxerr=0; totalerr=0; maxquad=0; totalvar=0
for m in range(2,M):
 left,right=np.longdouble(m),np.longdouble(m+1)
 a=np.searchsorted(ln,2*np.log(left)-1); b=np.searchsorted(ln,2*np.log(right)+1,side='right')
 bound=2*(P[b]-P[a])/left**2
 pieces=[]
 for kk,amp in zip(knots,[2,4,2]):
  ia=np.searchsorted(kk,left,side='right');ib=np.searchsorted(kk,right,side='left');
  bound+=np.sum(amp*w[ia:ib]/kk[ia:ib]);pieces.extend(map(float,kk[ia:ib]))
 exact=C(right)-C(left); trap=(B(left)+B(right))/2; err=abs(exact-trap)
 assert err<=bound/8+1e-9,(m,err,bound)
 maxratio=max(maxratio,float(8*err/bound)); maxerr=max(maxerr,float(err));totalerr+=float(err);totalvar+=float(bound)
 if m<32:
  val=quad(lambda y:float(B(y)),m,m+1,points=sorted(set(pieces)),epsabs=1e-10,limit=max(100,len(pieces)+10))[0]
  maxquad=max(maxquad,float(abs(val-exact)))
assert maxquad<1e-9
# Exact rational Peano kernel identity for piecewise linear functions with signed atoms.
# f(x)=a+b*x+sum c*(x-t)_+; integral minus trapezoid = -sum c*t*(1-t)/2.
import random
rng=random.Random(20261123)
for i in range(500):
 a,b=Q(rng.randint(-9,9)),Q(rng.randint(-9,9));atoms=[(Q(rng.randint(0,32),32),Q(rng.randint(-15,15),7)) for _ in range(12)]
 f=lambda x:a+b*x+sum(c*max(Q(0),x-t) for t,c in atoms)
 integral=a+b/2+sum(c*(1-t)**2/2 for t,c in atoms);err=integral-(f(Q(0))+f(Q(1)))/2
 assert err==-sum(c*t*(1-t)/2 for t,c in atoms)
 assert abs(err)<=sum(abs(c) for t,c in atoms)/8
report=dict(M=M,sieve_limit=N,prime_powers=len(ns),prefix_direct_checks=2*(M-1),max_prefix_direct_diff=maxdiff,J_checks=101,max_J_quad_diff=jerr,peano_exact_cases=500,intervals=M-2,max_trap_error=maxerr,max_fraction_of_variation_bound=maxratio,total_absolute_trap_error=totalerr,total_variation_upper_estimate=totalvar,split_quad_checks=30,max_split_quad_diff=maxquad,elapsed_seconds=time.monotonic()-start,selected=[dict(m=m,B=float(B(m)),C=float(C(m))) for m in [2,5,10,20,50,100,200,400]])
print(json.dumps(report,indent=2));Path(__file__).with_name('report.json').write_text(json.dumps(report,indent=2))

