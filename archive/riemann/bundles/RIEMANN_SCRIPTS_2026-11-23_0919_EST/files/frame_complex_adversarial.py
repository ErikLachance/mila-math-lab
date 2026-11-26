#!/usr/bin/env python3
"""Complex/Hermitian stress tests for trace/rank bounds with arbitrary deleted subspaces."""
import math,json
from pathlib import Path
import numpy as np
rng=np.random.default_rng(202611230914)
checked=0; eligible=0; strong=0; worstold=None; loewner=0; failures=[]
for D in [2,4,8,12]:
 for w in [2,5,14,34]:
  for j in range(100):
   Q=np.zeros((D,D),complex);Qp=np.zeros((D,D),complex);S=0;r=0;err=0
   for i in range(w):
    d=int(rng.integers(1,D+1));Z=(rng.standard_normal((D,d))+1j*rng.standard_normal((D,d)))/math.sqrt(2)
    U,_=np.linalg.qr(Z,mode='reduced')
    B=U*float(rng.uniform(.7,1.3))
    K=np.eye(d)-B.conj().T@B
    S+=d;err+=float(np.linalg.norm(K,'fro')**2)
    Q+=B@B.conj().T
    keep=int(rng.integers(d+1)); r+=d-keep
    W=(rng.standard_normal((d,d))+1j*rng.standard_normal((d,d)))/math.sqrt(2)
    V,_=np.linalg.qr(W)
    BU=B@V[:,:keep]
    Qp+=BU@BU.conj().T
   mu=float(np.trace(Q).real)/D; e=err/S; alpha=r/S
   eta=max(0.,float(np.trace(Q@Q).real)/(D*mu**2)-1)
   lam=np.linalg.eigvalsh(Q-Qp)
   if min(lam)<-1e-10:failures.append(('Loewner',D,w,j,float(min(lam))))
   if min(lam)>-1e-10:loewner+=1
   k=D-int(np.linalg.matrix_rank(Qp,tol=1e-8))
   if e<1:
    delta=(alpha+math.sqrt(alpha*e))/(1-math.sqrt(e))
    upper=(math.sqrt(eta)+math.sqrt(eta+4*delta))**2/4
    if k/D>upper+1e-8:failures.append(('Kernel',D,w,j,k/D,upper))
    if delta<1:
      upperOld=1-(1-delta)**2/(1+eta)
      if upper<upperOld-1e-8:strong+=1
    eligible+=1
   checked+=1
assert not failures,failures[:3]
out={'complex_cases':checked,'e_less_than_one_cases':eligible,'new_tighter_than_old_cases':strong,'psd_Q_minus_Qprime_cases':loewner,'failures':failures,'status':'ALL PASS','limitation':'floating point falsification only, no Lean verification'}
Path('/mnt/data/riemann_20261123_0908/frame_complex_adversarial.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
