import sympy as sp,json
s,u=sp.symbols('s u',real=True)
beta=sp.Rational(3,4);theta=sp.Rational(3,5)
Fneg=-1/(s-beta)
Fpos=1/(s-beta)
assert sp.residue(Fneg,s,beta)==-1
assert sp.residue(Fpos,s,beta)==1
# signed Taylor coefficients A_j(sigma)=(-1)^j F^(j)(sigma)/j!
sigma=sp.Integer(3)
rows=[]
for j in [0,1,2,5,10,20]:
    an=sp.simplify((-1)**j*sp.diff(Fneg,s,j).subs(s,sigma)/sp.factorial(j))
    ap=sp.simplify((-1)**j*sp.diff(Fpos,s,j).subs(s,sigma)/sp.factorial(j))
    assert sp.simplify(an+(sigma-beta)**(-j-1))==0
    assert sp.simplify(ap-(sigma-beta)**(-j-1))==0
    rows.append({'j':j,'neg_pole_Aj':str(an),'pos_pole_Aj':str(ap),'neg_pair_absA_plus_A':str(abs(an)+an),'pos_pair_absA_plus_A':str(abs(ap)+ap)})
out={'assumptions':'Generic abstract Mellin F(s); x>=1, G_minus(x)=-x^(3/4) <= x^(3/5) for every x, yet F_minus(s)=-1/(s-3/4) has real pole at 3/4. It disproves an overgeneralized one-sided-criterion-for-arbitrary-meromorphic-F formulation; it does not apply to zeta F, whose zeros are nonreal in (0,1).','positive_real_pole':'G_plus=x^(3/4) has residue +1 at beta; its positive part violates the x^(3/5) bound for large x. For Dirichlet L a real zero beta in (0,1) contributes -nu/[beta(beta-1)] = nu/[beta(1-beta)]>0, so the relevant pole has favorable sign.','beta':str(beta),'theta':str(theta),'rows':rows,'status':'Exact symbolic SymPy rational assertions PASS; no Riemann proof/disproof.'}
with open('/mnt/data/riemann_20261123_real_pole_sign_guard.json','w') as f:json.dump(out,f,indent=2)
print('Exact real-pole sign guard PASS; sample A_20(-) =',rows[-1]['neg_pole_Aj'],'A_20(+) =',rows[-1]['pos_pole_Aj'])
