import sympy as s,json
h=s.symbols('h');K,K1,g,g1=s.symbols('K K1 g g1')
# s=1+h; K(s)=K+K1h; -L'/L(s)= -K(s) for nonprincipal
F_non=(-K-K1*h)/(h*(1+h))+K/h
F_non_wrong=(-K-K1*h)/(h*(1+h))-K/h
# zeta: -zeta'/zeta=1/h-g+(2 g1+g^2)h+...
F_z=(1/h-g+(2*g1+g**2)*h)/(h*(1+h))-(1/h**2-(1+g)/h)
F_z_wrong=(1/h-g+(2*g1+g**2)*h)/(h*(1+h))-(1/h**2-g/h)
R=lambda ex:s.limit(h*ex,h,0)
L=lambda ex:s.limit(ex,h,0)
out={'nonprincipal_correct_pole_residue':str(s.simplify(R(F_non))),'nonprincipal_wrong_sign_residue':str(s.simplify(R(F_non_wrong))),'nonprincipal_finite_limit':str(s.simplify(L(F_non))),'zeta_correct_pole_residue':str(s.simplify(R(F_z))),'zeta_wrong_center_residue':str(s.simplify(R(F_z_wrong))),'zeta_finite_limit':str(s.simplify(L(F_z))),'real_zero_beta_3over4_residue':str(-1/(s.Rational(3,4)*(s.Rational(3,4)-1))),'negative_toy_real_residue': '-1'}
open('/mnt/data/riemann_20261123_1728/analytic_pole_symbolic.json','w').write(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
assert out['nonprincipal_correct_pole_residue']=='0' and out['zeta_correct_pole_residue']=='0'
