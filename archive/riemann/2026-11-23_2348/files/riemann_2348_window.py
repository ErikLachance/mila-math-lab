from fractions import Fraction as F
import json,time
start=time.monotonic(); checks=0; sharp=0; dyadic=0
# For alpha=p/q in (1,2), (kW)^alpha<=W^2 iff W^(2q-p)>=k^p.
for p,q in [(3,2),(4,3),(5,3),(7,4),(9,5),(11,6),(19,10)]:
 for k in range(1,31):
  r=2*q-p
  # exact integer search for minimum W
  lo,hi=0,k**p
  while hi-lo>1:
   m=(lo+hi)//2
   if m**r>=k**p:hi=m
   else:lo=m
  assert (k*hi)**p<=hi**(2*q)
  if hi>1:assert (k*(hi-1))**p>(hi-1)**(2*q)
  sharp+=1
  for W in [hi,hi+1,2*hi, max(1,hi-1)]:
   assert ((k*W)**p<=W**(2*q))==(W**r>=k**p);checks+=1
# eps=1/80, a=21/10. Minimal dyadic exponent via integer inequalities.
for c in [1,2,3,5,17,128,567]:
 for x in range(3,1500):
  if x**21<c**10:continue
  e=0
  while (c*2**e)**10<x**21:e+=1
  assert x**21<=(c*2**e)**10<2**10*x**21
  if e:assert (c*2**(e-1))**10<x**21
  dyadic+=1
# General rank cutoff rescaling: (k*x')^B <= x'^A iff x'^(A-B)>=k^B.
coh=0
for A,B in [(5,4),(11,8),(51,50),(401,400)]:
 for k in range(1,9):
  lo,hi=0,k**B
  while hi-lo>1:
   m=(lo+hi)//2
   if m**(A-B)>=k**B:hi=m
   else:lo=m
  for z in [max(1,hi-1),hi,hi+1]:
   assert ((k*z)**B<=z**A)==(z**(A-B)>=k**B);coh+=1
print(json.dumps(dict(cohomology_cutoff_checks=coh,window_exact_equivalences=checks,sharp_threshold_checks=sharp,dyadic_rank_checks=dyadic,runtime_seconds=time.monotonic()-start),indent=2))

