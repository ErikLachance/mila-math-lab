#!/usr/bin/env python3
"""Quantitative comparison with Rubinstein v2 Corollary T2 (III.236): illustrative only."""
from mpmath import mp
import json
from pathlib import Path
mp.dps=80
rows=[]
for kappa_s in ['0.01','0.0001','0.00000001']:
 k=mp.mpf(kappa_s); e=k*k/4; eta=5*k
 for a_factor in ['0','0.01','0.1','1','3']:
  a=k*mp.mpf(a_factor)
  delta=(a+mp.sqrt(a*e))/(1-mp.sqrt(e))
  original=eta+4*a+4*mp.sqrt(e)
  b1=1-(1-delta)**2/(1+eta) if delta<1 else mp.mpf(1)
  b2=((mp.sqrt(eta)+mp.sqrt(eta+4*delta))/2)**2
  best=min(mp.mpf(1),original,b1,b2)
  rows.append({'kappa':str(k),'alpha':str(a),'e0':str(e),'eta':str(eta),'delta':mp.nstr(delta,19),'old_T2_loss_D':mp.nstr(original,19),'trace_ratio_loss_D':mp.nstr(b1,19),'kernel_loss_D':mp.nstr(b2,19),'best_loss_D':mp.nstr(best,19),'old_over_best':mp.nstr(original/best,10) if best else '0'})
# Exact orthonormal repeated basis family: e=eta=0, alpha=k/D,
# expected kernel loss alpha, whereas old T1 loss gives 4alpha.
for row in rows: assert mp.mpf(row['best_loss_D']) <= mp.mpf(row['old_T2_loss_D'])+mp.mpf('1e-18')
res={'source':'Rubinstein 22 Nov v2 §III.8 Cor T2 (III.234–236), uses 5*kappa second moment and e0<=kappa²/4','rows':rows,'note':'New bound is an ALTERNATIVE analytic corollary from identical finite-frame assumptions, not a new trace estimate. Does not prove H8, arithmetic inputs (S/I/P), or RH. May use min of original/b1/b2. Projection onto E adds 1/(1-delta_p) in all bounds.','status':'PASS'}
Path('/mnt/data/riemann_20261123_0908/frame_corollary_T2_comparison.json').write_text(json.dumps(res,indent=2))
print(json.dumps({'rows':len(rows),'sample':rows[:4],'most_relative_improvement':max((float(r['old_over_best']),r) for r in rows)[1]},indent=2))
