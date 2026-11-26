"""Independent symbolic cancellation check of the pole at s=1 of the
Mellin transform F(s) = -zeta'(s)/[s(s-1)zeta(s)] -1/(s-1)^2
+ (1+gamma)/(s-1), for zeta(s)=1/(s-1)+gamma+c1*(s-1)+...
from Rubinstein's 22-Nov-2026 zeta paper, Part II eq. (II.1).
This local algebra does not prove the meromorphic continuation or RH.
"""
import sympy as S
import json
t,g,c1,c2=S.symbols('t gamma c1 c2')
zeta=1/t+g+c1*t+c2*t**2
A=-S.diff(zeta,t)/zeta
F=A/(t*(1+t))-1/t**2+(1+g)/t
pole_2=S.simplify(S.limit(t**2*F,t,0))
pole_1=S.simplify(S.limit(t*F,t,0))
finite=S.simplify(S.limit(F,t,0))
assert pole_2==0 and pole_1==0
assert finite.is_finite or finite.free_symbols.issubset({g,c1,c2})
print(json.dumps({'double_pole_coefficient':str(pole_2),'simple_pole_coefficient':str(pole_1),'finite_part':str(finite),'proved_scope':'Formal Laurent-series cancellation only, assuming local Laurent expansion of zeta near s=1; no global RH result'},indent=2))
