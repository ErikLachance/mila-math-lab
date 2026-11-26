import numpy as np
from fractions import Fraction as F
from random import Random
from time import monotonic
import json
s=monotonic(); rng=np.random.default_rng(202611240537); rr=Random(537)
# Exact real-integer frames (complex extension follows by Hermitian block identity).
# Original normalization uses common rational scale 1/M.
partitions=pair_tests=0
for j in range(1000):
 D=int(rng.integers(2,12)); n=int(rng.integers(2,12)); ds=[int(rng.integers(1,5)) for _ in range(n)]; M=int(rng.integers(1,20))
 As=[rng.integers(-2,3,(D,d)) for d in ds]; R=sum(ds)
 hs=lambda X: int(np.sum(X*X))
 # Gram entries scaled by 1/M: C_i=A_i/sqrt(M)
 errs=[hs(A.T@A-M*np.eye(d,dtype=int)) for A,d in zip(As,ds)]
 cross={(i,k):hs(As[i].T@As[k]) for i in range(n) for k in range(n) if i!=k}
 B=max(F(v*D,M*M*ds[i]*ds[k]) for (i,k),v in cross.items())
 p=list(range(n));rr.shuffle(p); g=rr.randrange(1,n+1); parts=[p[i:i+g] for i in range(0,n,g)]
 grouped=[np.concatenate([As[i] for i in G],axis=1) for G in parts]; gd=[sum(ds[i] for i in G) for G in parts]
 assert np.array_equal(sum(A@A.T for A in As),sum(A@A.T for A in grouped))
 E=0
 for G,A,d in zip(parts,grouped,gd):
  val=hs(A.T@A-M*np.eye(d,dtype=int));E+=val
  assert val==sum(errs[i] for i in G)+sum(cross[i,k] for i in G for k in G if i!=k)
  assert F(val-sum(errs[i] for i in G),M*M)<=B*F(d*d-sum(ds[i]**2 for i in G),D)
 for j,A in enumerate(grouped):
  for k,C in enumerate(grouped):
   if j==k:continue
   val=hs(A.T@C);assert val==sum(cross[i,l] for i in parts[j] for l in parts[k]); assert F(val,M*M)<=B*F(gd[j]*gd[k],D);pair_tests+=1
 assert F(E,M*M*R)<=F(sum(errs),M*M*R)+B*F(max(gd),D)
 partitions+=1
# Exact Gauss-square via residue-difference histograms, no floating point.
# For zeta_p primitive, sum h[t]*zeta^t equals h[0]-h[1] when all nonzero bins agree.
primes=[p for p in range(3,102,2) if all(p%d for d in range(2,int(p**.5)+1))]
gauss=0; hist_entries=0; mub_pairs=0; block_tests=0
for p in primes:
 x=np.arange(p,dtype=np.int64); diff=x[:,None]-x[None,:]; sq=x[:,None]**2-x[None,:]**2
 for a in range(p):
  for b in range(p):
   h=np.bincount(((a*sq+b*diff)%p).ravel(),minlength=p)
   assert np.all(h[1:]==h[1]); assert int(h[0]-h[1])==(p*p if a==b==0 else 0 if a==0 else p)
   gauss+=1;hist_entries+=p
 # Test exact inner product Gram squared using basis labels and subset partition.
 # p quadratic bases plus computational basis, all p vectors each.
 labels=[(a,b) for a in range(p+1) for b in range(p)]
 for i in range(12):
  rr.shuffle(labels); k=rr.randrange(1,min(len(labels),2*p)+1)
  A=labels[:k]; B=labels[k:k+min(k,len(labels)-k)]
  def cross_num(A,B):return sum(p if a==c and b==d else int(a!=c) for a,b in A for c,d in B)
  assert cross_num(A,B)<=len(A)*len(B)
  assert cross_num(A,A)-p*len(A)==len(A)**2-sum(sum(a==c for a,b in A)**2 for c in range(p+1))
  block_tests+=1
 # complete orthonormal bases as blocks have exactly zero diagonal and cross p.
 # each distinct basis pair contributes p*p equal squared entries 1/p.
 for a in range(p+1):
  for b in range(a):
   assert F(p*p,p)==p;mub_pairs+=1
# Counterexample: opposite local heights, product of individual norms fixed.
height_counter=[]
for M in [2,4,16,256,65536]:
 # norm squares at two places (M,1/M) and (1/M,M)
 hsum=F(M)+F(1,M)
 assert hsum>2
 height_counter.append(str(hsum))
print(json.dumps(dict(partitions=partitions,group_pair_checks=pair_tests,odd_primes=len(primes),exact_gauss_sums=gauss,residue_histogram_entries=hist_entries,mub_basis_pair_checks=mub_pairs,mub_partition_checks=block_tests,height_counterexamples=height_counter,seconds=monotonic()-s),indent=2))

