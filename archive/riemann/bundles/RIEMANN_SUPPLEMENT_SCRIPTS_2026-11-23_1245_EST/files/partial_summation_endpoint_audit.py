from fractions import Fraction
from sympy import primerange
import mpmath as mp
import json
# Log variable v=log t; U=e^4, a=e^2.
# Fake weighted atoms t=e and t=e^3, each contributes c_j to the unweighted count and c_j*log(t) to theta.
c1,c2=Fraction(5),Fraction(7)
theta_a=c1
# theta(U)=5*1+7*3=26
theta_U=c1+3*c2
# theta(v) =5 for v in [2,3), 26 for v in [3,4]
integral=theta_a*(Fraction(1,2)-Fraction(1,3))+theta_U*(Fraction(1,3)-Fraction(1,4))
correct=theta_U/Fraction(4)-theta_a/Fraction(2)+integral
printed=theta_U/Fraction(4)-theta_a/Fraction(4)+integral
assert correct==c2
assert printed-correct==theta_a/Fraction(4)==Fraction(5,4)
# Actual prime count test, actual theta over residue class mod 5, U=1e6.
mp.mp.dps=55
U=1000000;a=1000;m=5;b=1
P=[int(p) for p in primerange(2,U+1) if p%m==b]
Psmall=[p for p in P if p<=a]
Pwin=[p for p in P if a<p<=U]
thU=mp.fsum(mp.log(p) for p in P)
tha=mp.fsum(mp.log(p) for p in Psmall)
lgU=mp.log(U);lga=mp.log(a)
# analytical integration using exact event jump antiderivative
integral_num=tha*(1/lga-1/lgU)+mp.fsum(mp.log(p)*(1/mp.log(p)-1/lgU) for p in Pwin)
correct_num=thU/lgU-tha/lga+integral_num
printed_num=thU/lgU-tha/lgU+integral_num
assert mp.almosteq(correct_num,len(Pwin),abs_eps=mp.mpf('1e-40'),rel_eps=mp.mpf('1e-40'))
assert mp.almosteq(printed_num-len(Pwin),tha/lgU,abs_eps=mp.mpf('1e-40'),rel_eps=mp.mpf('1e-40'))
rep={'source':'Rubinstein working v2 Nov22 2026 printed page63, §III.1 proof (III.6), text states pi*=theta(U)/logU-theta(sqrtU)/logU+integral; source Thorner & Zaman Cor1.4 fully checked elsewhere',
 'printed_identity':'pi*=theta(U)/logU - theta(sqrt(U))/logU + integral_a^U theta(t)/(t(logt)^2) dt',
 'correct_identity':'pi*=theta(U)/logU - theta(sqrt(U))/log(sqrt(U)) + same integral',
 'missing_term':'printed_right_side minus correct = theta(sqrt(U))/logU, when a=sqrt(U). This is nonzero for any residue class containing a prime <=sqrt(U).',
 'exact_rational_counterexample_v_logdomain':{'theta_a':str(theta_a),'theta_U':str(theta_U),'integral':str(integral),'correct':str(correct),'printed':str(printed),'true_count':str(c2),'difference':str(printed-correct)},
 'actual_prime_test':{'m':m,'b':b,'U':U,'sqrtU':a,'primes_in_window':len(Pwin),'theta_at_sqrtU':mp.nstr(tha,25),'correct_rhs':mp.nstr(correct_num,25),'printed_rhs':mp.nstr(printed_num,25),'positive_discrepancy':mp.nstr(printed_num-correct_num,25)},
 'impact':'Likely isolated typesetting error in human working guide, NOT in formally checked Lean source. Subsequent proof prose uses factors 1+2+2, consistent with correct denominator 2/logU. Replacement of theta by Lambda_b yields exactly M_b only with correct endpoint denominator. A rigorous author-side erratum would change /logU to /log(sqrtU) in first boundary subtraction. No question about theorem statement, RH Lean validity, or full article proved here.'}
with open('/mnt/data/riemann_20261123_1225/partial_summation_endpoint_audit.json','w') as f:json.dump(rep,f,indent=2)
print(json.dumps(rep,indent=2))
