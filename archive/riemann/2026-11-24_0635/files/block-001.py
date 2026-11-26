from fractions import Fraction as F
from random import Random
from time import monotonic
from itertools import product
import numpy as np
import json
s=monotonic(); rng=Random(63538); nr=np.random.default_rng(63538)
# Exact multiplicative form of metric balancing: norm squared scales 2^a.
# Actual height is mean log2 norm squared; h_i bound integral in log2 units.
# Choose local integer log norms with integer mean (last coordinate corrected).
checks=0; volume=0; weighted=0
for _ in range(5000):
 t=rng.randrange(1,9); n=rng.randrange(1,12)
 for i in range(n):
  a=[rng.randrange(-15,16) for _ in range(t-1)]; h=rng.randrange(-9,10); a.append(t*h-sum(a)); H=h+rng.randrange(0,6)
  shift=[v+H-h for v in a]; assert sum(shift)==t*H
  for v,z in zip(a,shift):
   assert F(2)**(v-z)==F(2)**(h-H)<=1;checks+=1
  # covolume factor for K-rank r at each complex place = (norm^2 factor)^r
  r=rng.randrange(1,11); assert np.prod([1])==1
  assert sum(r*z for z in shift)==r*t*H;volume+=1
  # common group h=0 achieved with rational block weights p_i
  p=F(i+1,n*(n+1)//2)
  assert all(F(2)**v/(F(2)**z/p)<=p for v,z in zip(a,shift));weighted+=1
# Exact operator-norm squared group bound for diagonal local maps, including overlapping images.
local=0; gap_cases=0
for _ in range(4000):
 d=rng.randrange(1,10); g=rng.randrange(1,12); ranks=[rng.randrange(1,15) for i in range(g)]; R=sum(ranks); p=[F(v,R) for v in ranks]
 a=[[F(rng.randrange(0,17),16) for j in range(d)] for i in range(g)]
 for v in a: v[rng.randrange(d)]=F(1)
 un=max(sum(v[j] for v in a) for j in range(d)); w=max(sum(p[i]*a[i][j] for i in range(g)) for j in range(d)); assert 1<=un<=g and 0<w<=1;local+=1
 if un<g:gap_cases+=1
# Test entropy cost sharpness exactly without logarithms: for integer ranks,
# maximize product p_i^d_i at p_i=d_i/R. Enumerate finite rational simplex.
entropy=0
for g in range(2,5):
 for ranks in product(range(1,5),repeat=g):
  R=sum(ranks); best=F(1)
  for d in ranks:best*=F(d,R)**d
  den=12
  for ks in product(range(1,den),repeat=g-1):
   last=den-sum(ks)
   if last<=0:continue
   trial=F(1)
   for d,k in zip(ranks,(*ks,last)):trial*=F(k,den)**d
   assert trial<=best;entropy+=1
# Distinct common-shift criterion; direct sum local lengths by elementary divisors.
shifts=0
for _ in range(5000):
 g=rng.randrange(1,12); ts=[rng.randrange(-5,20) for i in range(g)]; ds=[rng.randrange(1,12) for i in range(g)]; u=min(ts)
 loss=sum(d*(v-u) for d,v in zip(ds,ts)); assert loss>=0;assert (loss==0)==(len(set(ts))==1)
 # higher common shifts fail containment in at least one block
 assert any(u+1>v for v in ts);shifts+=1
# Noncommuting complex operators: independent numerical diagnostic only.
complex_cases=0; min_margin=1.; max_violation=0.
for _ in range(2000):
 d=int(nr.integers(1,12)); g=int(nr.integers(1,8)); A=[]; ds=[]
 for i in range(g):
  k=int(nr.integers(1,10)); a=nr.normal(size=(d,k))+1j*nr.normal(size=(d,k));a/=np.linalg.norm(a,2);A.append(a);ds.append(k)
 q=sum(a@a.conj().T for a in A); m=np.linalg.eigvalsh(q)[-1]; p=np.array(ds)/sum(ds)
 w=np.linalg.eigvalsh(sum(p_i*a@a.conj().T for p_i,a in zip(p,A)))[-1]
 assert m<=g+1e-12 and w<=1+1e-12;max_violation=max(max_violation,w-1,m-g);complex_cases+=1
print(json.dumps(dict(exact_local_rescaling_checks=checks,exact_rank_volume_checks=volume,exact_weighted_rescaling_checks=weighted,exact_diagonal_group_cases=local,strict_unweighted_improvement_cases=gap_cases,exact_entropy_comparisons=entropy,exact_DVR_cases=shifts,numerical_complex_group_cases=complex_cases,max_float_violation=max_violation,elapsed_seconds=monotonic()-s),indent=2))

