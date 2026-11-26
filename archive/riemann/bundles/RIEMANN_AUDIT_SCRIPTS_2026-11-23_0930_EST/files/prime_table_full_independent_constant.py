#!/usr/bin/env python3
"""Tie together independently computed L'/L(1,chi_d) and full prime-power cell sum."""
import json
from pathlib import Path
from mpmath import mp
mp.dps=55
base=Path('/mnt/data/riemann_20261123_0908')
p=json.loads((base/'prime_cell_table_reconstruction.json').read_text())
d=json.loads((base/'dirichlet_logderivative_gamma.json').read_text())
r1=mp.mpf(d['Lprime_over_L_at_1'])
a=mp.mpf(10000)
M=a*(mp.log(a)-1-mp.euler+r1-(mp.log(10)+7*mp.log(mp.mpf('0.05')))/8)
refs=[mp.mpf('237.6375'),mp.mpf('-300.2570'),mp.mpf('-176.7314'),mp.mpf('229.1329')]
rows=[]
for rec,ref in zip(p['records'],refs):
  P=mp.mpf(rec['P']); excess=P-M
  assert abs(excess-ref)<mp.mpf('.00005'), (rec['class'],str(excess-ref))
  rows.append({'class':rec['class'],'P':mp.nstr(P,40),'difference_P_minus_M':mp.nstr(excess,38),'difference_vs_report':mp.nstr(excess-ref,12)})
out={'M_from_independently_evaluated_quadratic_Lprime_over_L':mp.nstr(M,46),'rows':rows,'mean_excess':mp.nstr(mp.fsum(mp.mpf(r['difference_P_minus_M']) for r in rows)/4,36),'status':'PASS all four reported 4-decimal excesses and M from independent Dirichlet L function gamma sum.','interpretation':'Finite pedagogical table only; source explicitly says q,d are too small to satisfy theorem M size and congruence hypotheses.'}
(base/'prime_table_full_independent_constant.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
