from fractions import Fraction as F
from random import Random
from itertools import product
from math import sqrt, log1p
import time,json
start=time.monotonic(); rng=Random(202611240348)
# exact clipped slope integral, including upper positive thresholds
count=0; sharp=0; full=0
for n in range(1,7):
 for v in product(range(-2,3),repeat=n):
  if sum(v)<0: continue
  U=max(0,max(v));
  for S in range(1,5):
   neg=F(sum(min(S,max(0,-x)) for x in v),n)
   harmonic=F(U*S,U+S)
   assert neg<=harmonic
   if neg==harmonic and neg>0: sharp+=1
   # Integral of f over [s-S,s+U], exact step function
   pts=sorted(set([-S,U]+[x for x in v if -S<x<U])); integ=F(0)
   for a,b in zip(pts,pts[1:]):
    integ+=F(sum(2*x<a+b for x in v),n)*(b-a)
   assert integ==F(sum(min(S+U,U-x) for x in v),n)
   assert integ<=U
   count+=1; full+=1
# coordinate frames, retained threshold subspaces and target maximal compatible slopes
trials=0; exact=0; floatchecks=0; biggest=0.; tight=0
for trial in range(3500):
 D=rng.randrange(1,10); R=rng.randrange(1,30)
 coords=[rng.randrange(D) for j in range(R)]
 weights=[F(rng.randrange(2,7),4) for j in range(R)]
 e=sum((w-1)**2 for w in weights)/R
 if e>F(1,4): continue
 x=[rng.randrange(-6,7) for j in range(R)]
 mean=F(sum(x),R); x=[F(v)-mean for v in x]; U=max(x); S=F(rng.randrange(1,8))
 # Target threshold must contain retained coordinate images; choose minimal compatible y.
 y=[max([-S]+[x[j] for j in range(R) if coords[j]==i]) for i in range(D)]
 Q=[sum((weights[j] for j in range(R) if coords[j]==i),F(0)) for i in range(D)]
 T=sum(Q); eta=D*sum(w*w for w in Q)/T**2-1
 H=U*S/(U+S); B=(eta*S+3*H+e/(1-e)*S)/(1+eta)
 assert -sum(y)/D<=B
 # pointwise rational linearized bound at every distinct midpoint (both threshold signs)
 pts=sorted(set([-S,U]+[v for v in x if -S<v<U]+[v for v in y if -S<v<U])); loss=F(0)
 for a,b in zip(pts,pts[1:]):
  t=(a+b)/2; rem=[j for j in range(R) if x[j]<t]; f=F(len(rem),R)
  q=sum((weights[j] for j in rem),F(0))/T
  z=F(sum(v<t for v in y),D)
  assert (1-e)*(q-f)**2<=e*f*(1-f)
  assert (1-q)**2<=(1-z)*(1+eta)
  assert z*(1+eta)<=eta+3*f+e/(1-e)*(1-f)
  loss+=z*(b-a); exact+=3
 assert loss==F(sum(U-min(U,v) for v in y),D)
 assert loss-U==-sum(y)/D
 Fbar=U/(U+S)
 qstar=min(1,float(Fbar)+sqrt(float(e/(1-e)*Fbar*(1-Fbar))))
 et=float(eta); Z=(2*qstar+et+sqrt(et*et+4*et*qstar*(1-qstar)))/(2*(1+et))
 signed=float(U+S)*min(1,Z)-float(U)
 assert float(-sum(y)/D)<=signed+1e-10
 old=(4*float(U)*log1p(float(S/U)) if U else 0)+(et+4*sqrt(float(e)))*float(S)
 if old>0: biggest=max(biggest,1-signed/old)
 if abs(float(-sum(y)/D)-signed)<1e-12:tight+=1
 trials+=1;floatchecks+=1
# simultaneous equality in discarded-mass and complement inequality, exact fractions
f=F(1,3); e=F(1,9); q=F(1,2); z=F(2,3); eta=F(1,8)
assert (1-e)*(q-f)**2==e*f*(1-f)
assert (z-q)**2==eta*z*(1-z)
# explicit Q diag 4/3,4/3,8/3: 2 discarded columns, 4 retained columns
Q=[F(4,3),F(4,3),F(8,3)]; assert 3*sum(v*v for v in Q)/sum(Q)**2-1==eta
assert (2*(F(4,3)-1)**2+4*(F(2,3)-1)**2)/6==e
# surrogate e'=(e/3)^2: exact rational size budget and order
budget=0
for i in range(2501):
 e=F(i,10000); ep=(e/3)**2
 assert e/(1-e)<=4*e/3 and ep<=F(1,4)
 assert 16*ep==(4*e/3)**2
 budget+=1
print(json.dumps(dict(negative_tail_checks=count,positive_threshold_integral_checks=full,harmonic_sharp_cases=sharp,frame_trials=trials,exact_frame_comparisons=exact,signed_bound_float_checks=floatchecks,simultaneous_equality_exact=4,budget_checks=budget,seconds=time.monotonic()-start),indent=2))

