import numpy as np
from fractions import Fraction as F
from math import sqrt
from time import monotonic
from random import Random
import json
start=monotonic(); rng=np.random.default_rng(202611240520); rr=Random(20261124)
# Gaussian integer complex column frames; exact moments via real and imaginary integer arrays.
def gram(a,b):
 return a@a.T+b@b.T,b@a.T-a@b.T
def tr(A): return int(np.trace(A[0]))
def norm2(A): return int(np.sum(A[0]**2)+np.sum(A[1]**2))
def inner(A,B): return int(np.sum(A[0]*B[0])+np.sum(A[1]*B[1]))
checks=0; noncomm=0; improvement=[]
for i in range(6000):
 d=int(rng.integers(2,13)); n=int(rng.integers(2,45)); k=int(rng.integers(1,n))
 a=rng.integers(-3,4,(d,n)); b=rng.integers(-3,4,(d,n)); Q=gram(a,b); R=gram(a[:,:k],b[:,:k]); P=gram(a[:,k:],b[:,k:]); T=tr(Q); L=tr(R)
 if not L or not T: continue
 r=F(L,T); q=1-r; eta=F(d*norm2(Q),T*T)-1; v=F(d*norm2(R),L*L)-1
 assert eta>=0 and v>=0 and inner(P,R)>=0
 assert norm2(R)<=inner(Q,R)
 # exact squared inequality, only when left nonnegative
 assert r*v<=q or (r*v-q)**2<=eta*v
 old=(1+eta)/r**2-1
 assert v<=old
 # prove exact new bound <= old by polynomial test
 assert r*old-q>=0 and (r*old-q)**2>=eta*old
 bound=((sqrt(float(eta))+sqrt(float(eta+4*r*q)))/(2*float(r)))**2
 assert float(v)<=bound+1e-9 and bound<=float(old)+1e-9
 # rational Young envelope
 assert v<=2*q/r+eta/r**2
 C=Q[0]@R[0]-Q[1]@R[1]-R[0]@Q[0]+R[1]@Q[1]; J=Q[0]@R[1]+Q[1]@R[0]-R[0]@Q[1]-R[1]@Q[0]
 noncomm+=bool(np.any(C) or np.any(J)); checks+=1
 if old>0: improvement.append(1-bound/float(old))
# Exact sharpness: disjoint supports, uniform on each, r>=k/d.
sharp=0
for d in range(2,45):
 for k in range(1,d):
  v=F(d-k,k)
  for j in range(11):
   r=F(k,d)+(1-F(k,d))*F(j,10); q=1-r
   eta=F(d,k)*r*r+F(d,d-k)*q*q-1
   assert r*v-q>=0 and (r*v-q)**2==eta*v
   sharp+=1
# exact deleted trace fraction bound, random real rational diagonal weights.
mass=0
for i in range(6000):
 n=rr.randrange(2,50); k=rr.randrange(n); w=[F(rr.randrange(2,7),4) for _ in range(n)]
 e=sum((x-1)**2 for x in w)/n; f=F(k,n); q=sum(w[:k])/sum(w)
 assert (1-e)*(q-f)**2<=e*f*(1-f)
 # avoid square roots in regression of linear upper envelope q<=2f+e/(4(1-e))
 h=2*f+e/(4*(1-e)); assert q<=h
 mass+=1
print(json.dumps(dict(complex_frames=checks,noncommuting_frames=noncomm,exact_sharpness_cases=sharp,exact_mass_cases=mass,mean_relative_improvement_vs_old_trace_bound=float(np.mean(improvement)),seconds=monotonic()-start),indent=2))

