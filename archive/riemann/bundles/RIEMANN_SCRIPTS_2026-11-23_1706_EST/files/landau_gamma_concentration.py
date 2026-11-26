from fractions import Fraction
from math import floor
import mpmath as mp
import json
mp.mp.dps=80
q=1000
sig=1002
rows=[]
for U in [Fraction(1),Fraction(7,5),Fraction(2),Fraction(9,2),Fraction(10)]:
 m=(1250*U.numerator)//U.denominator
 k=m-1
 # Gamma(m, rate 1000), tail outside [U,3U/2]
 a=mp.mpf(U.numerator)/U.denominator
 low=mp.gammainc(m,0,q*a,regularized=True)
 high=mp.gammainc(m,q*mp.mpf(3)*a/2,mp.inf,regularized=True)
 relative=(low+high)*mp.power(mp.mpf(sig)/q,k)/q
 rows.append({'U':str(U),'m':m,'k':k,'tail_upper_log10':mp.nstr(mp.log10(low+high),16),'ratio_actual_to_goal_log10':mp.nstr(mp.log10(relative),16),'pass':relative<=1})
assert all(z['pass'] for z in rows)
# universal rational checks used in proof
assert Fraction(1000,1249)<Fraction(801,1000)
assert Fraction(199,1000)**2/2>Fraction(13,750)
assert Fraction(1249)*Fraction(13,750)>21
assert Fraction(1000)>Fraction(2)
print(json.dumps(rows,indent=2))
with open('/mnt/data/riemann_20261123_1659/landau_gamma_concentration.json','w') as o:json.dump(rows,o,indent=2)
