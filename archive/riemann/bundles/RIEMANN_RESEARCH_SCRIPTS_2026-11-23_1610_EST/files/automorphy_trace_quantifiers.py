from fractions import Fraction
from math import isqrt
import json
from pathlib import Path
# Exact proof constants for the (Count) trace nonzero mechanism in incomplete HUMAN reconstruction.
# For any complex root of unity z, |z|=1, a=p**e, t=a*z+1+z.conjugate()/a,
# reverse triangle gives |t|>=a-1-1/a. Every pure normalized tempered triple with
# eigenvalues of modulus 1 has |trace|<=3. Therefore t cannot equal its trace
# if a-1-1/a>3, i.e. a^2-4a-1>0, already true for a>=5.
examples=[];checks=0
for p in [2,3,5,7,11,13,17,23]:
 for e in range(1,11):
  a=p**e
  low=Fraction(a-1,1)-Fraction(1,a)
  has_gap=(a*a-4*a-1)>0
  assert (low>3)==has_gap
  checks+=1
  if e<=2: examples.append({'p':p,'e':e,'a':a,'lowerBoundAsFraction':str(low),'strictGapFrom3':str(low-Fraction(3,1)),'provedDistinctUsingThisBound':has_gap})
# Quantifier audit for V: regardless of scale, a single fixed prime l with nonzero Sha only
# contributes >=log l; fixed-e limit l<=exp(C(e+1)^A) not uniform in e.
# For p=1 mod8, set e=(p-1)/4 (even): e~p/4, (p-1) not dividing 2e.
def isprime(n):
 if n<2: return False
 for d in range(2,isqrt(n)+1):
  if n%d==0:return False
 return True
varying=[]
for p in range(9,2000,8):
 if isprime(p):
  e=(p-1)//4
  assert e%2==0 and (2*e)%(p-1)!=0
  varying.append([p,e])
result={'claim':'Under normalized purity |tr rho(Frob_w)|<=3, |t(z)|>=p^e-1-p^-e>3 whenever p^e>=5. This PROVES the local nonvanishing inequality only, assuming the source normalized-purity and trace hypotheses; it does NOT prove Count, whose cardinality/integer-norm bound is the difficult ingredient.','arithmeticCondition':'a^2-4a-1>0, true for integers a>=5, false for a in {1,2,3,4}.','checksExactRational':checks,'selectedExamples':examples,'varyingEvenTwistCounterToUniformity':varying[:15],'varyingTwistTotalUnder2000':len(varying),'scope':'Exact rational identity and elementary triangle inequalities. Neither G3 automorphy lifting nor RH independently proved.'}
p=Path('/mnt/data/riemann_20261123_1554/automorphy_trace_quantifiers.json');p.write_text(json.dumps(result,indent=2));print(json.dumps({'checks':checks,'strictGapAt7':str(Fraction(7-1,1)-Fraction(1,7)-3),'varyingExamples':varying[:6]},indent=2))
