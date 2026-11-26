from fractions import Fraction as F
import json,time
s=time.monotonic(); n=0; worst=F(0)
for i in range(1,101):
 sig=F(i,2000)
 for j in range(251):
  a=F(j,1000)
  numerator=(1+sig/2)*(1+sig/2+sig*(1+sig/2)**2)
  denom=(1-a-sig/2)**2
  assert numerator<=1+F(21,10)*sig
  assert 1/denom<=1+F(10,3)*(a+sig/2)
  assert numerator/denom<=1+4*sig+4*a
  assert 4*a*a<=F(9,4)*a # not needed; also 4a <=3sqrt(a) follows 16a^2<=9a
  assert 16*a*a<=9*a
  worst=max(worst,(numerator/denom-1)/(4*sig+4*a))
  n+=1
print(json.dumps(dict(rational_grid_pairs=n,inequalities_per_pair=5,max_fraction_of_new_budget=float(worst),seconds=time.monotonic()-s),indent=2))

