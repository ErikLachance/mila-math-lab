from fractions import Fraction as Q
import json,time
s=time.monotonic(); n=0
for b in range(2,121):
 for a in range(1,b):
  q=Q(a,b); v=q-q/(1-q**4); assert v==-q**5/(1-q**4)
  assert sum(q**(4*k+1) for k in range(1,9)) <= -v
  assert -v-sum(q**(4*k+1) for k in range(1,9)) == q**37/(1-q**4)
  n+=1
report={'exact_fraction_checks':n,'elapsed_code_seconds':time.monotonic()-s,'identity':'q - q/(1-q^4) = -q^5/(1-q^4); tail after 8 terms = q^37/(1-q^4)'}
print(report)
open('/mnt/data/riemann_20261123_1927/arithmetic_tail_result.json','w').write(json.dumps(report))

