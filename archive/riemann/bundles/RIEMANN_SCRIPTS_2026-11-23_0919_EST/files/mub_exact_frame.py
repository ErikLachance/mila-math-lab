import json, math
from pathlib import Path
import numpy as np
res=[]
for p in (3,5,7,11,13):
  z=np.exp(2j*np.pi/p)
  vec=[]
  labels=[]
  for b in range(p):
    e=np.zeros(p,complex);e[b]=1
    vec.append(e);labels.append(('standard',b))
  for a in range(p):
    for b in range(p):
      v=np.array([z**int((a*x*x+b*x)%p) for x in range(p)],complex)/math.sqrt(p)
      vec.append(v);labels.append((a,b))
  M=np.array(vec).T
  G=M.conj().T @ M
  Q=M @ M.conj().T
  target=(p+1)*np.eye(p)
  diagerr=float(np.max(abs(np.diag(G)-1)))
  maxerr=0.
  for i in range(len(labels)):
    for j in range(len(labels)):
      if i==j: continue
      target_abs=0 if labels[i][0]==labels[j][0] else 1/p
      maxerr=max(maxerr,abs(abs(G[i,j])**2-target_abs))
  spec=np.linalg.eigvalsh(Q)
  err=float(np.max(abs(Q-target)))
  eta=p*np.trace(Q@Q).real/(np.trace(Q).real**2)-1
  # For finite frames the off-diagonal squared HS upper bound is (d_i d_j)/D.
  assert diagerr<1e-12 and maxerr<5e-13 and err<5e-12 and abs(eta)<5e-12
  res.append({'prime_dimension':p,'bases':p+1,'vectors':p*(p+1),'frame_operator_eigen_min':float(spec.min()),'frame_operator_eigen_max':float(spec.max()),'max_overlap_squared_error':maxerr,'frame_operator_error':err,'second_moment_defect_eta':float(eta)})
Path('/mnt/data/riemann_20261123_0908/mub_exact_frame.json').write_text(json.dumps({'proof':'Odd finite field Gauss sums: for a!=0 mod p, |sum_x exp(2pi i (a*x*x+b*x)/p)|^2=p, since shifting by h leaves only h=0 after x sum; equal-a distinct-b geometric sums vanish. This proves the frame and overlaps exactly for all odd primes p.','status':'PASS','experimental_checks':res,'limits':'Finite-dimensional toy illustrating block correlations; does not verify theta lift bounds LinkS or Riemann'},indent=2))
print(json.dumps(res,indent=2))
