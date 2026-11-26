"""Finite local-cohomology obstruction to an omitted converse argument in a human draft,
NOT a global counterexample and NOT a criticism of Lean's checked theorem.
At l=3, N=7, E=Q(zeta7)^+ is real cyclic degree3, totally ramified at7.
Cyclotomic twist e=1 is unramified at7, Frobenius acts as 7^-1;
M^G_{E_w} = 3-primary subgroup killed by (7^-1-1), size3.
Gal(E_w/Q_7)=C3 acts trivially. H1(C3,Z/3) has three classes.
Inflation-restriction exhibits local kernel of H1(Q_7,M_e)->H1(E_w,M_e).
This does NOT establish failure of globally claimed Sha^Gal surjectivity.
"""
import json
from pathlib import Path
l=3;N=7;e=1
assert N%l!=0 and e%(l-1)!=0
assert (l-1)==2
p=7; n=p**e-1
v=0
while n%l==0:n//=l;v+=1
assert v==1
# 1-cocycles z_g determined by z(generator), any of three choices; trivial action.
classes=[]
for t in range(3):
 vals=tuple((t*k)%3 for k in range(3))
 assert all(vals[(i+j)%3]==(vals[i]+vals[j])%3 for i in range(3) for j in range(3))
 classes.append(vals)
assert len(set(classes))==3
# Coboundary delta b(g)=g.b-b is zero for all b in trivial action.
assert all((b-b)%3==0 for b in range(3))
r={'l':l,'N':N,'e':e,'local_prime':p,
 'field':'real cubic subfield E=Q(zeta_7)^+; E_w/Q_7 totally ramified cyclic degree3',
 'invariants':'M_e^{G_Ew} has order 3 (since v_3(7^e-1)=1) and C3 acts trivially',
 'H1_C3_Z3_classes':classes,
 'local_inflation_restriction_kernel_order':3,
 'source_file':'https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/manuscript/sec17_twisted.tex',
 'precise_warning':'The displayed proof establishes injection and invariant image, not the stated onto-all-invariants part for global Sha. Local restriction at a ramified 7-place has nonzero kernel; this alone does NOT disprove global surjectivity or affect the weaker injection/length claim actually used, and does NOT refute the Lean proof.',
 'global_counterexample':False,
 'riemann_status':'no RH implication'}
Path('/mnt/data/riemann_20261123_local_selmer_descent_guard.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
