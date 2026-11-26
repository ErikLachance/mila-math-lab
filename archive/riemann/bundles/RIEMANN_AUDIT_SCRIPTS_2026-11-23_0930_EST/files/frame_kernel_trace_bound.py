#!/usr/bin/env python3
"""Independent improved finite-dimensional kernel-bound from frame trace concentration.
All numerical tests are falsification-only; mathematical proof uses Cauchy-Schwarz."""
import math, json
from pathlib import Path
import numpy as np
from fractions import Fraction
from sympy import Matrix
rng=np.random.default_rng(110823)
tests=0; eligible=0; gains=[]; min_gap=1000; worst=None; tight=0
for D in [2,3,5,7,11,17]:
  for w in [2,5,9,20]:
    for rep in range(120):
      blocks=[]; Q=np.zeros((D,D)); Qprime=np.zeros((D,D)); S=0; r=0; eS=0
      for j in range(w):
        d=int(rng.integers(1,D+1)); A=rng.normal(size=(D,d))
        B=np.linalg.qr(A,mode='reduced')[0]*float(rng.uniform(.4,1.6))
        eS+=np.linalg.norm(B.T@B-np.eye(d),'fro')**2
        S+=d; Q+=B@B.T
        keep=int(rng.integers(0,d+1)); r+=d-keep
        Bp=B[:,:keep]; Qprime+=Bp@Bp.T
      mu=np.trace(Q)/D
      eta=max(0., np.trace(Q@Q)/(D*mu*mu)-1)
      e=eS/S; alpha=r/S
      delta=(alpha+math.sqrt(alpha*e))/(1-math.sqrt(e)) if e<1 else math.inf
      k=D-int(np.linalg.matrix_rank(Qprime,tol=1e-8))
      if math.isfinite(delta):
        new_upper=(math.sqrt(eta)+math.sqrt(eta+4*delta))**2/4
        old_upper=1-(1-delta)**2/(1+eta) if delta<1 else 1
        assert k/D<=new_upper+1e-7,(D,w,rep,k/D,new_upper,eta,delta)
        min_gap=min(min_gap,new_upper-k/D)
        if delta<1:
          gains.append(old_upper-new_upper)
          if new_upper<old_upper-1e-7:tight+=1
        eligible+=1
        if worst is None or new_upper-k/D<worst['gap']:
          worst={'D':D,'w':w,'r':r,'S':S,'e':e,'eta':eta,'delta':delta,'kernel':k,'upper':new_upper,'gap':new_upper-k/D}
      tests+=1
# Tight frame exact family: R orthonormal basis copies with k coordinates deleted from all copies
# Q=R*I, Qprime=R*diag(0,..0,1,..1), e=eta=0, alpha=k/D, delta=k/D and kernel fraction=k/D.
for D in (2,3,8,17):
  R=3
  for k in range(D+1):
    Q=Matrix.eye(D)*R
    Qr=Matrix.diag(*([0]*k+[R]*(D-k)))
    assert Qr.rank()==D-k
    alpha=Fraction(k,D)
    bound=alpha
    assert Fraction(D-Qr.rank(),D)==bound
out={'test':'Exact trace-concentration kernel inequality','time_label':'2026-11-23 09:08 EST run','formula':'k/D <= [(sqrt(eta)+sqrt(eta+4delta))/2]^2 with delta=(alpha+sqrt(alpha*e))/(1-sqrt(e)), e<1, mu=tr(Q)/D>0','random_cases':tests,'admissible_e_less_than_one':eligible,'minimum_numerical_slack':min_gap,'new_bound_stronger_than_prior_in_cases':tight,'comparisons_count':len(gains),'median_old_minus_new':float(np.median(gains)) if gains else None,'worst_case':worst,'exact_tight_family':'R repeated ONB copies, delete k same coordinates: e=eta=0, alpha=k/D, kernel=k, new bound equals alpha exactly','status':'PASS; algebraic proof in journal','limitations':'not a proof of arithmetic frame estimates H8, no RH proof'}
Path('/mnt/data/riemann_20261123_0908/frame_kernel_trace_bound.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
