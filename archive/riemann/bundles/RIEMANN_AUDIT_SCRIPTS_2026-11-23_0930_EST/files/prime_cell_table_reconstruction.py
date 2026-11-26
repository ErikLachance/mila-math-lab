#!/usr/bin/env python3
"""Independent reconstruction of Rubinstein's p36 toy table (q=11,d=1319,N=16,a=10000)."""
import json
from pathlib import Path
from sympy import primerange, legendre_symbol
from mpmath import mp
mp.dps=40
q=11;d=1319;N=16;a=mp.mpf(10000)
U=[1,3,5,7];P={u:mp.mpf(0) for u in U}; entries=0; nonzero=0
for p_ in primerange(3,200001):
 p=int(p_)
 if p==q:continue
 ell=mp.log(p)
 s=int(legendre_symbol(p,d)) if p!=d else 0
 t=int(legendre_symbol(p,q))
 r=p;j=1
 while r<=200000:
  coeff=(1 if p==d else (1-s**j))*ell
  if coeff:
   chi_q=t**j
   v=(1+chi_q)//2
   r16=r%16
   h=min(r16,16-r16)
   assert h in U
   for u in U:
    w=mp.mpf('10') if v==1 and h==u else mp.mpf('0.05')
    z=a/r-w
    if z>0:P[u]+=coeff*z
   nonzero+=1
  entries+=1
  j+=1;r*=p
M=a*(mp.log(a)-1-mp.euler+mp.mpf('-1.520227887516')-(mp.log(10)+7*mp.log(mp.mpf('.05')))/8)
reported_P=[mp.mpf('84701.0317')]
reported_diff=[mp.mpf('237.6375'),mp.mpf('-300.2570'),mp.mpf('-176.7314'),mp.mpf('229.1329')]
records=[]
for u,ref in zip(U,reported_diff):
 delta=P[u]-M
 records.append({'class':u,'P':mp.nstr(P[u],32),'P_minus_M_with_paper_c':mp.nstr(delta,22),'paper_P_minus_M':str(ref),'difference_to_paper':mp.nstr(delta-ref,12)})
 assert abs(delta-ref)<mp.mpf('0.00015'),(u,delta,ref)
assert abs(P[1]-reported_P[0])<mp.mpf('0.0001')
out={'source':'Rubinstein v2 II.4.2 pp35-37; p36 P_[1]=84701.0317','rprimepowers_seen':entries,'rprimepowers_with_nonzero_coeff':nonzero,'P1':mp.nstr(P[1],35),'M_from_12_digit_reported_logderivative':mp.nstr(M,32),'records':records,'mean_excess':mp.nstr(sum((P[u]-M for u in U),mp.mpf(0))/4,20),'status':'PASS four translate computations','texterratum':'Guide prose II.4.1 says v=(1+chi_q)/2 equals 1 for nonsquare, but mathematically v=1 for square chi_q=+1; table (p=23) uses the formula, so apparent prose typo, not computational contradiction','limitations':'Finite example explicitly violates full proof size hypotheses; reproduces a toy table, not inequality M, source Lprime/L rounded constant used'}
Path('/mnt/data/riemann_20261123_0908/prime_cell_table_reconstruction.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
