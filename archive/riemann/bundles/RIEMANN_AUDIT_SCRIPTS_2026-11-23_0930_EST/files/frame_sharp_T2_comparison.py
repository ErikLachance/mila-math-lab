#!/usr/bin/env python3
"""Sharp abstract frame-kernel bound inserted into Rubinstein Corollary T2 assumptions."""
from mpmath import mp
import json
from pathlib import Path
mp.dps=75
rows=[]
for kappa_s in ['0.25','0.01','0.0001','0.00000001']:
 k=mp.mpf(kappa_s)
 for a_s in ['0','0.01','0.1','1','3']:
  a=k*mp.mpf(a_s);e0=k*k/4; eta=5*k
  delta=(a+mp.sqrt(a*e0))/(1-mp.sqrt(e0))
  orig=eta+4*a+4*mp.sqrt(e0)
  oldratio=1-(1-delta)**2/(1+eta) if delta<1 else mp.mpf(1)
  sharp=(2*delta+eta+mp.sqrt(eta**2+4*eta*delta*(1-delta)))/(2*(1+eta)) if delta<1 else mp.mpf(1)
  assert sharp<=oldratio+mp.mpf('1e-65')
  best=min(mp.mpf(1),sharp,orig)
  rows.append({'kappa':mp.nstr(k,8),'alpha':mp.nstr(a,8),'e0':mp.nstr(e0,10),'eta':mp.nstr(eta,10),'delta':mp.nstr(delta,10),'published_bound_D':mp.nstr(orig,12),'previous_trace_bound_D':mp.nstr(oldratio,12),'new_sharp_bound_D':mp.nstr(sharp,12),'improvement_factor':mp.nstr(orig/best,12) if best>0 else 'undefined'})
res={'source':'Rubinstein v2 III.8 Cor T2, with its η=5κ,e0<=κ²/4, α=α_ram+α_prime','status':'PASS','rows':rows,'warning':'Illustrative upper-bound parameter substitutions, not actual source parameter verification; delta_p projection multiplies all by 1/(1-delta_p). The sharpened bound cannot replace proofs of S/I/P/H8 or (M).'}
Path('/mnt/data/riemann_20261123_0908/frame_sharp_T2_comparison.json').write_text(json.dumps(res,indent=2))
print(json.dumps({'rows':len(rows),'sample':rows[:6],'most_improved':max(rows,key=lambda x:float(x['improvement_factor']))},indent=2))
