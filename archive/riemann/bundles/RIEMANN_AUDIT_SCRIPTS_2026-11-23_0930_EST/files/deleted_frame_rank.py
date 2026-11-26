import numpy as np, json, math, hashlib
from fractions import Fraction
from pathlib import Path
p=Path('/mnt/data/riemann_20261123_0908')
rng=np.random.default_rng(20261123)
passed=0
useful=0
maxgap=-1e100
min_gap=1e100
worst=None
examples=[]
# Exact toy cases supplement random double tests.
for D in [3,4,7,11]:
  for w in [3,6,15]:
    for t in range(100):
      blocks=[]
      proj=[]
      e_sum=0.
      total=0
      removed=0
      Q=np.zeros((D,D))
      Qr=np.zeros((D,D))
      for k in range(w):
        d=int(rng.integers(1,D+1))
        A=rng.normal(size=(D,d))
        B=np.linalg.qr(A,mode='reduced')[0][:,:d]
        # Perturb by scaling, so the diagonal defect is nonzero in some cases.
        scale=float(rng.uniform(.95,1.05) if t%3 else rng.uniform(.5,1.5))
        B=B*scale
        total+=d
        Gr=B.T@B
        e_sum+=np.linalg.norm(Gr-np.eye(d),'fro')**2
        Q+=B@B.T
        rd=int(rng.integers(0,d+1))
        removed+=rd
        U=B[:,:(d-rd)]
        Qr+=U@U.T
      # Test Loewner monotonicity for trace square, even when matrices do not commute.
      tsum=float(np.trace(Q))
      ts2=float(np.trace(Q@Q))
      trs=float(np.trace(Qr))
      trs2=float(np.trace(Qr@Qr))
      assert trs2<=ts2+1e-7*max(1,ts2)
      e=e_sum/total
      alpha=removed/total
      eta=D*ts2/(tsum*tsum)-1
      assert eta>=-1e-10
      delta=(alpha+math.sqrt(alpha*e))/(1-math.sqrt(e)) if math.sqrt(e)<1 else math.inf
      rank=int(np.linalg.matrix_rank(Qr,tol=1e-8))
      if delta<1:
        lower=D*(1-delta)**2/(1+max(0,eta))
        gap=rank-lower
        min_gap=min(min_gap,gap)
        maxgap=max(maxgap,gap)
        assert gap>=-1e-8,(D,w,t,gap)
        useful+=1
        if len(examples)<7: examples.append({'D':D,'w':w,'alpha':alpha,'e':e,'eta':eta,'delta':delta,'rank':rank,'lower':lower,'gap':gap})
      passed+=1
# Exact rational toy, B1=I_2, B2=I_2, U1=span(e1), U2=span(e1)
# Q=2I, Qr=diag(2,0), S=4, removed=2, e=eta=0, delta=1/2,
# rank=1, bound=2*(1/2)^2=1/2.
from sympy import Matrix
I=Matrix.eye(2)
P=Matrix([[1,0],[0,0]])
Q=I*I.T+I*I.T
Qr=I*P*I.T+I*P*I.T
assert Q==Matrix.diag(2,2) and Qr==Matrix.diag(2,0)
assert Qr.rank()==1
result={'run':'2026-11-23 09:08 EST','test':'derived exact deleted-frame rank inequality','random_cases':passed,'nontrivial_delta_less_than_one':useful,'minimum_rank_minus_bound':min_gap,'max_gap':maxgap,'sample_cases':examples,'exact_toy':{'D':2,'rank':1,'certified_lower_bound':str(Fraction(1,2))},'status':'PASS; mathematical proof requires separate trace/Cauchy-Schwarz derivation','limitations':'Toy arbitrary finite matrices, no theta lift or trace formula verified'}
(p/'deleted_frame_rank.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
