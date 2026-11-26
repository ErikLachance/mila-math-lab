"""Exactly stated asymptotic reduction from C9 to the dyadic consequence
used in the incomplete human RH manuscript; does NOT prove the source C9 theorem.
"""
import mpmath as mp,json
from pathlib import Path
mp.mp.dps=65

def margin(y,A,cp):
 # lower log count: y + ln cp - 10A*y^.4 - log y
 # desired log count .9*y
 return mp.mpf('0.1')*y-10*A*y**mp.mpf('.4')-mp.log(y)+mp.log(cp)
res=[]
for A in [1,2,5,10]:
 for cp in ['1','0.001']:
  lo=mp.mpf('1e-3');hi=mp.mpf('1')
  while margin(hi,A,mp.mpf(cp))<0:hi*=2
  # Find upper root using valid large side (not necessarily monotone before)
  for _ in range(250):
   mid=(lo+hi)/2
   if margin(mid,A,mp.mpf(cp))>0:hi=mid
   else:lo=mid
  y=(lo+hi)/2
  res.append({'A':A,'cPrime':cp,'largeRootLogX':mp.nstr(y,20),'log10X':mp.nstr(y/mp.log(10),20),'positiveAboveRoot':margin(2*y,A,mp.mpf(cp))>0})
# For C9 assumption log Q<=c sqrt(logX) and weaker logQ<=10(logX)^.4,
# sufficient: (logX)^.1>=10/c, or logX>=(10/c)^10.
for c in [mp.mpf(1),mp.mpf('.5'),mp.mpf('.1')]:
 pass
R={'source':'RH-Alpoge-Reconstruction manuscript/sec5_auxiliary.tex (C9), source explicitly applies h=1 with logQ<=10*(logX)^(2/5) and X=(kb)^8.','needed':'Only the DYADIC count for X<g<=2X under logQ<=10*(logX)^(2/5) is used; the separately stated uniformity for all h as small as exp(-c sqrt(logX)) is not needed for that application.','conditionalFromC9':'Assuming C9, count>=cPrime*X/(Q^A logX). Let y=log X. It exceeds X^(9/10) whenever y/10 >= 10A y^(2/5)+log y-log cPrime. For any fixed A,cPrime>0 this holds for sufficiently large y. Moreover logQ<=10 y^(2/5) implies logQ<=c sqrt y once y >=(10/c)^10. These are elementary comparisons; this file does not prove C9 itself.','largeYRootIllustrations':res,'sourceConditionLogXThreshold':{str(c):str((mp.mpf(10)/mp.mpf(c))**10) for c in ['1','.5','.1']},'caveat':'Uniform count in varying imaginary quadratic ray class fields including possible exceptional real zero is the source theorem not sourced in the human manuscript. We found no directly source-matching peer-reviewed statement in this pass. A dyadic-only theorem plus Siegel/zero-free/density estimates could be a substantially smaller proof target. The numerical roots are illustrative, not universal bound without actual constants.'}
Path('/mnt/data/riemann_20261123_1554/c9_weaker_dyadic_reduction.json').write_text(json.dumps(R,indent=2,default=bool))
print(json.dumps({'examples':res[:4],'sourceConditionLogXThreshold':R['sourceConditionLogXThreshold']},indent=2,default=str))
