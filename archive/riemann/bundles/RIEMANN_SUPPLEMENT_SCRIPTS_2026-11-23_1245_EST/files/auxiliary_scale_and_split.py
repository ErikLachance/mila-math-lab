from fractions import Fraction
from math import factorial
import json
# Theorem III.1.1: log(q)> 1/2 Y^(eps/5), with Y=e^u.
# For a fixed A, q>Y^A when e^((eps/5)u)>2Au.
# Exact rational lower bound for a concrete large u; no numerical sign issue.
epsilon=Fraction(1,100); A=10; u=6000
z=Fraction(u)*epsilon/5   # z=12 exactly
partial=Fraction(0)
first_sufficient=None
for n in range(1,101):
    partial += z**(n-1)/factorial(n-1)
    if first_sufficient is None and partial>2*A*u:
        first_sufficient=n-1
assert first_sufficient is not None
assert partial>2*A*u
# More generally exp(c*u)/(u) tends infinity for c>0: only fixed A may be quantified before Y.
# q | d+1 and q==3 mod4,d==3 mod4 gives (q/d)=+1; so chi_d(q)=+1.
results={'reference':'Rubinstein et al v2 Theorem III.1.1(a)(b)(c), page61',
'general_assertion':'For each fixed eps>0 and fixed A>=1, eventually 0.5*Y^(eps/5) > A*logY; the theorem then forces q>Y^A and d>Y^A (the latter with additional (logY)^2). Therefore q,d>x for all x in [Y,Y^A], and the special p=d^2 ramified term vanishes in the actual large-Y regime.',
'not_uniform_in_A':'If A=A(Y) grows arbitrarily fast, the argument does NOT apply. The theorem only fixes A before Y.',
'rational_example':{'epsilon':str(epsilon),'A':A,'logY':u,'z':str(z),'first_taylor_degree_to_prove_exp_z_gt_2Au':first_sufficient,'strict_rational_lower_bound_asserted':True},
'edge_case':'At toy q=3,d=23,x=530, ramified d^2=529 term coefficient 2*(530/529-1)=2/529 is nonzero; this does not violate the eventual q,d>x assertion because toy q,d do NOT satisfy the giant size hypotheses.',
'no_RH_proof':True}
with open('/mnt/data/riemann_20261123_1225/auxiliary_scale_and_split.json','w') as f:json.dump(results,f,indent=2)
print(json.dumps(results,indent=2))
