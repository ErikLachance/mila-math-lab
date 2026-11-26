import sympy as sp,json
E=sp.symbols('epsilon',positive=True)
n=2+8*E
m=sp.Rational(1,2)-E/16
k=sp.Rational(9,2)+10*E
expr={
 'x_over_m':sp.expand(1-m),
 'x_times_m_over_k':sp.expand(1+m-k),
 'm':m,
 'k_over_n_squared':sp.expand(k-2*n),
 'word_count_required_m5_f_xepsilon':sp.expand(5*m+n+E),
 'word_count_slack_k_minus_m5_f_xepsilon':sp.expand(k-(5*m+n+E)),
 'k_upper_constraint_slack_n2_xhalfminepsilon_over_k':sp.expand(2*n+sp.Rational(1,2)-E-k),
 'k_lower_constraint_slack_k_over_xm':sp.expand(k-(1+m)),
 'm_lower_constraint_slack_m_over_xhalfminepsilon':sp.expand(m-(sp.Rational(1,2)-E)),
}
checks={
 'x_over_m':sp.Rational(1,2)+E/16,
 'x_times_m_over_k':-3-sp.Rational(161,16)*E,
 'k_over_n_squared':sp.Rational(1,2)-6*E,
 'word_count_slack_k_minus_m5_f_xepsilon':sp.Rational(21,16)*E,
 'k_upper_constraint_slack_n2_xhalfminepsilon_over_k':5*E,
 'k_lower_constraint_slack_k_over_xm':3+sp.Rational(161,16)*E,
 'm_lower_constraint_slack_m_over_xhalfminepsilon':sp.Rational(15,16)*E,
}
for q,val in checks.items():
 assert sp.simplify(expr[q]-val)==0,(q,expr[q],val)
# Auxiliary prime/scale constraint from previous work: for fixed eps>0, J>=1, and Y huge,
# exp((1/2)*Y^(eps/5)) > Y^J; equivalently (1/2)Y^(eps/5)>J log Y.
# This follows from exp growth; test a concrete theoretical log Y sequence where it holds.
E0=sp.Rational(1,100);J=sp.Integer(10)
test=[50,100,1000,6000,10000,30000]
from mpmath import mp
mp.dps=50
primeranges=[{'logY':z,'half_Y_eps_over5':mp.nstr(mp.exp(mp.mpf(z)*mp.mpf('0.002'))/2,20),'J_logY':str(J*z),'condition':bool(mp.exp(mp.mpf(z)*mp.mpf('0.002'))/2 > J*z)} for z in test]
assert all(sp.simplify(expr[x].subs(E,sp.Rational(1,100)))>0 for x in ['word_count_slack_k_minus_m5_f_xepsilon','k_upper_constraint_slack_n2_xhalfminepsilon_over_k','k_lower_constraint_slack_k_over_xm','m_lower_constraint_slack_m_over_xhalfminepsilon'])
with open('/mnt/data/riemann_20261123_power_budget.json','w') as f:json.dump({'source':'Rubinstein working draft v2 §III.10-III.11, parameter powers and four errors; this is merely independent exact symbolic bookkeeping, not proof of the 13 H inputs', 'formulas':{key:str(sp.factor(val)) for key,val in expr.items()},'assertions':{key:str(val) for key,val in checks.items()},'checked':True,'auxiliary_growth_numerics':primeranges,'warning':'Constant factors, arithmetic existence, and uniformity across x and characters remain unproved here; asymptotic exponent slack cannot establish H12.'},f,indent=2)
for name,val in expr.items():print(name,'=',val)
print('PASS exact symbolic rational exponent identities and positive epsilon slacks')
print('scale condition at logY=6000:',primeranges[3])
