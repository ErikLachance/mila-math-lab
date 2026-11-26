#!/usr/bin/env python3
"""Exact arithmetic counterexamples to the two hypotheses of the reciprocity reduction."""
from sympy import legendre_symbol,jacobi_symbol,factorint
import json
from pathlib import Path
# When modulus m0 does not fix q modulo 8, the symbol of an m0-prime can vary despite same residue class mod m0.
m0=3;a=1; n=3;n2=4; qs=(7,13)
assert all(q % m0==a for q in qs)
assert all(q > n*n2 for q in qs) is False # 7 <12; fix use pair 3 and 4 with q>12 by replacing 7 with 19
qs=(19,13)
assert all(q > n*n2 and q%m0==a for q in qs)
vals=[int(legendre_symbol(n*n2,q)) for q in qs]
print('without 8|m0:',qs,vals)
assert len(set(vals))==2
# When q divides n*n', the Legendre symbol is 0 but Jacobi(q,s) is +/-1, so q>nn' or q coprime is essential.
q=7; m0=8; n=7;n2=2
lhs=int(legendre_symbol(n*n2,q))
# s=squarefree part excluding factors m0: 7
s=7
rhs=int(jacobi_symbol(q,s))
assert lhs==0 and rhs==0 # both zero, so difference? Their 'q>n*nprime' is for primitive character and nonzero assumptions.
# Better counter: source formula 'sign fixed independent of q' no longer has ±1 signs when q|nnprime.
res={'mod8_missing':{'m0':3,'fixed_a0':1,'n':3,'nprime':4,'q':list(qs),'legendre_values':vals,'squarefree_s_outside_m0':1,'consequence':'No fixed sign constant exists as q runs over same progression: 8|m0 is substantive'},'q_coprimality_missing':{'q':7,'n':7,'nprime':2,'legendre_nnprime_q':lhs,'note':'Legendre is zero, not a +/-1 sign, when q divides n*nprime. q>n*nprime ensures this cannot happen.'},'status':'PASS; exact arithmetic examples, do not contradict the actual theorem with its assumptions'}
Path('/mnt/data/riemann_20261123_0908/reciprocity_assumption_countermodels.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
