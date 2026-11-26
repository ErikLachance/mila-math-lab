import time, math, json
from fractions import Fraction as F
from random import Random
import numpy as np
from itertools import product
rng=Random(2611240313); s=time.monotonic(); exact=0; tight=0; rejected=0
# Coordinate frame matrices: all columns are scaled coordinate unit vectors.
# Exact trace moments and exact variance inequalities, arbitrary retained mask.
for trial in range(4000):
 D=rng.randrange(1,17); R=rng.randrange(1,80)
 coords=[rng.randrange(D) for _ in range(R)]
 w=[F(rng.randrange(3,6),4) for _ in range(R)]
 retain=[rng.randrange(2) for _ in range(R)]
 Q=[sum((w[j] for j in range(R) if coords[j]==i),F(0)) for i in range(D)]
 T=sum(Q); err=sum((x-1)**2 for x in w); e=err/R
 eta=D*sum(x*x for x in Q)/T**2-1
 h=R-sum(retain); f=F(h,R)
 P=[i for i in range(D) if not any(retain[j] and coords[j]==i for j in range(R))]
 z=F(len(P),D); mass=sum((Q[i] for i in P),F(0))/T
 rem=sum((w[j] for j in range(R) if not retain[j]),F(0))/T
 assert mass<=rem
 assert (mass-z)**2<=eta*z*(1-z)
 assert (1-rem)**2 <= (1-z)*(1+eta)
 assert (sum((w[j]-1 for j in range(R) if not retain[j]),F(0)))**2<=h*err
 q=min(1,float(f)+math.sqrt(float(e*f*(1-f)/(1-e))))
 root=(2*q+float(eta)+math.sqrt(float(eta)**2+4*float(eta)*q*(1-q)))/(2*(1+float(eta)))
 assert float(z)<=root+1e-12
 assert (1-e)*(rem-f)**2<=e*f*(1-f)
 exact+=5
 if z>0 and eta>0 and abs(float(z)-root)<1e-12:tight+=1
# Dense non-coordinate, complex frames, rank by independent SVD. Remove whole
# subspace dimensions after random unitary basis change of each source block.
rg=np.random.default_rng(261124); dense=0; gap=0
for _ in range(600):
 D=int(rg.integers(3,22)); dims=[int(rg.integers(1,D+1)) for j in range(int(rg.integers(1,8)))]; A=[]; kept=[]; err=0; h=0; R=sum(dims)
 for d in dims:
  Z=rg.normal(size=(D,d))+1j*rg.normal(size=(D,d)); V=np.linalg.qr(Z)[0]; V=V*np.sqrt(rg.uniform(.6,1.4,d)); W=np.linalg.qr(rg.normal(size=(d,d))+1j*rg.normal(size=(d,d)))[0]
  V=V@W; k=int(rg.integers(0,d+1)); A.append(V); kept.append(V[:,:k]); h+=d-k; err+=np.linalg.norm(V.conj().T@V-np.eye(d),'fro')**2
 B=np.concatenate(A,axis=1); C=np.concatenate(kept,axis=1); Q=B@B.conj().T; T=np.trace(Q).real; e=err/R; eta=max(0,D*np.linalg.norm(Q,'fro')**2/T**2-1)
 z=1-(np.linalg.matrix_rank(C) if C.shape[1] else 0)/D; f=h/R
 q=min(1,f+math.sqrt(e*f*(1-f)/(1-e))); root=(2*q+eta+math.sqrt(eta*eta+4*eta*q*(1-q)))/(2*(1+eta))
 assert z<=root+1e-9
 old=min(1,eta+4*f+4*math.sqrt(e)); assert root<=old+1e-9
 gap+=old-root; dense+=1
# Exact normalized chain error identity, arbitrary admissible positive rational parameters.
chain=0
for _ in range(2000):
 x,b,k,L,m,n=[rng.randrange(1,1000) for j in range(6)]; t=rng.randrange(1,n+1); t2=rng.randrange(1,n+1); p=F(t,n); q=F(t2,n); a=x*b
 B=t*a*(1+F(m*m,k))+2*n*m*m*b*L+F(m*t2*k*b*L*L,n*n)
 div=F(t*m*b*t2,2*n)
 assert B/div==2*x/(m*q)+2*x*m/(q*k)+4*m*L/(p*q)+2*k*L*L/(p*n*n)
 chain+=1
# O_K/2 multiplication: w^2=w-(1+d)/4. Test all 4 residues for both
# congruence types, not just chosen prime examples.
mod=0; split=0; inert=0
for d in range(3,10000,4):
 c=(1+d)//4
 def mul(x,y):
  a,b=x;u,v=y;return ((a*u-b*v*c)%2,(a*v+b*u+b*v)%2)
 pts=list(product(range(2),repeat=2)); good=[v for v in pts if mul((0,1),v)!=(0,0) and mul((1,1),v)!=(0,0)]
 if d%8==7: assert good==[(1,0)];split+=1
 else: assert len(good)==3;inert+=1
 mod+=len(pts)
print(json.dumps(dict(exact_frame_inequalities=exact,frame_trials=4000,dense_complex_trials=dense,mean_capped_codimension_bound_improvement=gap/dense,chain_identities=chain,torsion_residues=mod,split_congruences=split,inert_congruences=inert,seconds=time.monotonic()-s),indent=2))
