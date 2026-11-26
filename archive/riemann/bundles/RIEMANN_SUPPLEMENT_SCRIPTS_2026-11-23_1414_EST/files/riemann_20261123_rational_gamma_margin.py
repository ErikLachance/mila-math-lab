from fractions import Fraction as F
import json
# Entirely rational lower bounds for two large-deviation rates,
# and upper bound for source's sigma=252, theta=3/5, rough growth B=2.
a=F(4,5);b=F(6,5)
left_rate_lower=F(1,50)       # -1/5 - log(1-1/5) >= (1/5)^2/2
right_rate_lower=F(13,750)  # 1/5 - log(1+1/5) >= (1/5)^2/2 -(1/5)^3/3
lower=min(left_rate_lower,right_rate_lower)
q=F(252)-F(3,5)
lam=F(252)-F(2)
ratio=q/lam
logratio_upper=ratio-1 # log(1+x)<x
assert (a,b)==(F(4,5),F(6,5))
assert ratio==F(1257,1250)
assert logratio_upper==F(7,1250)
assert lower>logratio_upper
margin=lower-logratio_upper
# The optimization requires only continuity as U->infinity; no rounded gamma probabilities used.
out={'purpose':'Independent rigorous rational inequality certifying positive Chernoff exponent gap in source Part II §1, for h=5/4, alpha=3/2, sigma=252, theta=3/5, rough-growth B=2.','definitions':{'a':str(a),'b':str(b),'q':str(q),'lambda':str(lam),'q/lambda':str(ratio)},'inequalities':['I(4/5)=-1/5-log(1-1/5)>=(1/5)^2/2=1/50 by positive -log series','I(6/5)=1/5-log(1+1/5)>=(1/5)^2/2-(1/5)^3/3=13/750 by alternating log series','log(q/lambda)=log(1+7/1250)<7/1250'], 'rate_lower':str(lower),'logratio_upper':str(logratio_upper),'strict_gap_lower':str(margin),'numerical_gap_lower':float(margin),'exact_fraction_checks':'PASS', 'caution':'This verifies an elementary numerical margin of the published one-sided sparse-window analytical criterion, not its global RH premise. Source already proves criterion. No hypothesis of Riemann proved here.'}
with open('/mnt/data/riemann_20261123_rational_gamma_margin.json','w') as f:json.dump(out,f,indent=2)
print('RATIONAL PASS: kappa >=',lower,'> log ratio <=',logratio_upper,'with gap >',margin,'(~',float(margin),')')
