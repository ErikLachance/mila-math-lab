#!/usr/bin/env python3
"""Sharp two-moment upper bound on kernel fraction under positive compression and trace loss."""
from fractions import Fraction
from sympy import Matrix, Rational
from pathlib import Path
import numpy as np,json, math
rng=np.random.default_rng(20261123)
count=0; check=0; better=0; min_slack=100
worst=None
for D in [2,3,4,5,7,11,16]:
 for w in [2,4,10,25]:
  for i in range(125):
   Bblocks=[];Q=np.zeros((D,D),dtype=complex);Qp=np.zeros_like(Q);S=0;r=0;eS=0
   for j in range(w):
    d=int(rng.integers(1,D+1)); raw=rng.standard_normal((D,d))+1j*rng.standard_normal((D,d));B=np.linalg.qr(raw,mode='reduced')[0]*float(rng.uniform(.85,1.15))
    eS+=np.linalg.norm(B.conj().T@B-np.eye(d),'fro')**2;S+=d
    Q+=B@B.conj().T
    keep=int(rng.integers(0,d+1));r+=d-keep
    U=np.linalg.qr(rng.standard_normal((d,d))+1j*rng.standard_normal((d,d)))[0]
    BP=B@U[:,:keep];Qp+=BP@BP.conj().T
   e=eS/S
   if e>=1:continue
   alpha=r/S
   mu=float(np.trace(Q).real)/D
   eta=max(0.,float(np.trace(Q@Q).real)/(D*mu*mu)-1)
   delta=(alpha+math.sqrt(alpha*e))/(1-math.sqrt(e))
   k=D-int(np.linalg.matrix_rank(Qp,tol=1e-9));t=k/D
   if delta<1:
    bh=(2*delta+eta+math.sqrt(eta*eta+4*eta*delta*(1-delta)))/(2*(1+eta))
    old=1-(1-delta)**2/(1+eta)
    assert t<=bh+1e-8,(D,w,i,k,delta,eta,bh)
    assert bh<=old+1e-9,(D,w,i,bh,old)
    check+=1;min_slack=min(min_slack,bh-t)
    if old-bh>1e-8:better+=1
    if worst is None or bh-t<worst['slack']:
      worst={'D':D,'w':w,'k':k,'delta':delta,'eta':eta,'new':bh,'old':old,'slack':bh-t}
   count+=1
# Exactly tight abstract example: D=4, k=2, Q=(1/2,1/2,3/2,3/2), Qprime=(0,0,3/2,3/2).
Q=Matrix.diag(Rational(1,2),Rational(1,2),Rational(3,2),Rational(3,2)); Qp=Matrix.diag(0,0,Rational(3,2),Rational(3,2));D=4
mu=Q.trace()/D; eta=(Q*Q).trace()/(D*mu*mu)-1;delta=(Q-Qp).trace()/Q.trace();t=Fraction(D-Qp.rank(),D)
assert eta==Rational(1,4) and delta==Rational(1,4) and t==Fraction(1,2)
from sympy import sqrt
bound=(2*delta+eta+sqrt(eta**2+4*eta*delta*(1-delta)))/(2*(1+eta))
assert bound==Rational(1,2)
res={'run':'2026-11-23 09:08 EST','theorem':'Let Qp<=Q be PSD on C^D, mu=trQ/D>0, eta=trQ²/(Dmu²)-1>=0, tr(Q-Qp)/trQ<=delta<1. Then dim kerQp /D <= [2delta+eta+sqrt(eta²+4eta delta(1-delta))]/[2(1+eta)].','proof':'P=projection ker Qp, t=rank P/D; 0<=tr(PQ)<=tr(Q-Qp). Centered Hilbert-Schmidt Cauchy implies tr(PQ)>=mu D[t-sqrt(eta*t*(1-t))]. Thus t-sqrt(eta*t*(1-t))<=delta. Solve quadratic in t; valid for delta<1, eta>=0.','sharp_abstract_rational_example':{'D':4,'kernel_dim':2,'delta':str(delta),'eta':str(eta),'bound':str(bound),'Q_diagonal':['1/2','1/2','3/2','3/2'],'Qprime_diagonal':['0','0','3/2','3/2']},'cases':count,'bounded_delta_cases':check,'new_tighter_than_uncentered_Cauchy_bound':better,'min_slack':min_slack,'worst':worst,'limitation':'Sharp in abstract Q/Qp trace moments. Not proven optimal under the stronger decomposed-frame constraints, and not a proof of H8 or RH.','status':'PASS'}
Path('/mnt/data/riemann_20261123_0908/frame_sharp_kernel_bound.json').write_text(json.dumps(res,indent=2))
print(json.dumps({k:v for k,v in res.items() if k not in ('proof','theorem')},indent=2))
