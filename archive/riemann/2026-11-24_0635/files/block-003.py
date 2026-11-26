from fractions import Fraction as F
from math import log
from random import Random
from time import monotonic
import numpy as np
from scipy.optimize import minimize_scalar
import json
s=monotonic(); rng=Random(635); nr=np.random.default_rng(635)
# Rational two rank-one projections, equal weights.  For v=(c,s), u=e1,
# Z is projection onto (u+v) direction, rational entries even if normalized vector irrational.
# Exact certificate S<=I, Z has trace1 and tr(ZM_i)=(1+c)/2.
two=0
for a in range(1,100):
 for b in range(0,a+1):
  c=F(a*a-b*b,a*a+b*b); ss=F(2*a*b,a*a+b*b); assert c*c+ss*ss==1
  M=[[F(1)+c*c,c*ss],[c*ss,ss*ss]]; t=1/(1+c)
  Z=[[F(1+c,2),ss/2],[ss/2,F(1-c,2)]]
  assert Z[0][0]+Z[1][1]==1 and Z[0][0]*Z[1][1]==Z[0][1]**2
  assert Z[0][0]==(1+c)/2
  assert Z[0][0]*c*c+2*Z[0][1]*c*ss+Z[1][1]*ss*ss==(1+c)/2
  A=1-t*M[0][0]; B=1-t*M[1][1]; C=-t*M[0][1]; assert A>=0 and B>=0 and A*B==C*C
  two+=1
# Orthogonal classes: t_i=p_i/P_class; dual density diagonal P_class.
classes=0; class_checks=0
for _ in range(5000):
 n=rng.randrange(1,30); k=rng.randrange(1,n+1); rs=[rng.randrange(1,30) for i in range(n)]; P=[F(r,sum(rs)) for r in rs]; cls=[rng.randrange(k) for i in range(n)]; masses=[sum((p for p,c in zip(P,cls) if c==j),F(0)) for j in range(k)]
 t=[p/masses[c] for p,c in zip(P,cls)]; assert sum(masses)==1
 for j,m in enumerate(masses):
  assert sum((v for v,c in zip(t,cls) if c==j),F(0))==int(m>0);class_checks+=1
 classes+=1
# Numerical dual optimisation and primal/dual certificates for arbitrary complex PSD contractions.
# For any density Z, candidate t=p/a; scale by lambda_max(S) for primal feasibility.
# True optimal objective lies between dual and dual-log(lambda_max(S)).
rows=[]
for _ in range(100):
 D=int(nr.integers(2,7)); g=int(nr.integers(2,9)); Ms=[]
 for i in range(g):
  A=nr.normal(size=(D,D))+1j*nr.normal(size=(D,D))
  A=A[:,:int(nr.integers(1,D+1))]; M=A@A.conj().T; Ms.append(M/np.linalg.eigvalsh(M)[-1])
 M=np.array(Ms); p=nr.integers(1,12,g).astype(float);p/=p.sum(); Z=np.eye(D,dtype=complex)/D
 def vals(Z):return np.einsum('ij,kji->k',Z,M).real
 for j in range(250):
  a=vals(Z); t=p/a; S=np.einsum('k,kij->ij',t,M); ev,V=np.linalg.eigh(S); lam=ev[-1]
  if lam-1<1e-8:break
  W=np.outer(V[:,-1],V[:,-1].conj()); b=vals(W)
  f=lambda z:-np.dot(p,np.log(np.maximum((1-z)*a+z*b,1e-300)))
  opt=minimize_scalar(f,bounds=(0,1),method='bounded',options={'xatol':1e-12}); z=opt.x;Z=(1-z)*Z+z*W
 a=vals(Z);t=p/a;lam=np.linalg.eigvalsh(np.einsum('k,kij->ij',t,M))[-1];scale=max(1.,lam);lo=np.dot(p,np.log(t/scale));hi=np.dot(p,np.log(t)); H=-np.dot(p,np.log(p)); assert lo<=hi+1e-12 and hi>=-H-1e-10 and lo<=1e-10
 rows.append((hi-lo,-hi,H,j+1))
print(json.dumps(dict(exact_two_projection_certificates=two,exact_orthogonal_class_cases=classes,exact_class_checks=class_checks,numerical_cases=len(rows),largest_numerical_duality_gap=max(r[0] for r in rows),median_numerical_duality_gap=float(np.median([r[0] for r in rows])),median_cost_fraction_of_entropy=float(np.median([r[1]/r[2] for r in rows])),elapsed_seconds=monotonic()-s),indent=2))

