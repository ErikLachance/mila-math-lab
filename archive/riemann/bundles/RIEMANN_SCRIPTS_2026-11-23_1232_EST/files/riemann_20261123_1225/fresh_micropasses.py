#!/usr/bin/env python3
"""Exact finite tests and analytic countermodels, November 23 2026.
Not a proof of RH or of the external formal source.
"""
import math,json,random
from fractions import Fraction
from pathlib import Path
from sympy import Matrix,Rational,factorint
import mpmath as mp

out={}
# Test (1): logical nonimplication of unbounded scale supply to curvature-budget net.
# For any theta<=1, a>=4 and gap a(a-1), gap^2>=9a^2>8a^(1+theta).
scales=[]
for j in range(1,9):
    a=2**(2**j)
    b=a*a
    gap=b-a
    # theta=3/5; exact integer inequality needed for gap <= sqrt(8)*a^((1+theta)/2)
    violates=(gap**10 > 8**5 * a**8)
    assert violates
    assert gap**2 > 8*a**2
    scales.append({'j':j,'a_digits':len(str(a)),'gap_digits':len(str(gap)),'theta_3over5_budget_violated':violates})
out['unbounded_scales_not_dense']={'proof':'For theta<=1 and a>=4: gap=a(a-1), gap^2>=9a^2>8*a^(1+theta). This fails the sufficient interpolation mesh bound. Unboundedness is not enough for H12_grid.','scales':scales}

# Test (2): H1 common one-sided upper bound cannot imply two-sided H3 spread.
for bound in [1,5,100,10**5]:
    vals=[Fraction(0),Fraction(-bound)]
    assert all(v <= 0 for v in vals)
    assert abs(vals[0]-vals[1]) == bound
out['one_sided_height_not_spread']={'proof':'Even for common upper bound 0, y1=0 and y2=-R yield arbitrary spread R. H3 does not follow from the one-sided upper part of H1 alone.','examples_R':[1,5,100,100000]}

# Test (3): elementary slope and covolume sign conventions from Part III.11.
A=Matrix.diag(Rational(1,2),Rational(1,3),Rational(1,5))
B=Matrix.diag(1,2,3)*A
C=A/7
vA=abs(A.det());vB=abs(B.det());vC=abs(C.det())
assert vA==Rational(1,30) and vB==Rational(1,5) and vC==Rational(1,10290)
assert vB/vA==6 and vC/vA==Rational(1,343)
# mu = -log covol / rank; mu(B)-mu(A) = -log(6)/3 <0; mu(C)-mu(A)=log7 >0
out['slope_covolume_sign_test']={'covol_base':str(vA),'covol_sublattice':str(vB),'covol_dilated':str(vC),'index_sublattice':str(vB/vA),'uniform_scale':str(Fraction(1,7)),'symbolic_differences':{'mu_sub_minus_base':'-log(6)/3','mu_dilated_minus_base':'log(7)'},'status':'exact determinant identities; no claim about theta-lift lattices'}

# Test (4): independent arithmetic consequence regression for Robin and Lagarias,
# as a cross-check of implications of verified RH but NOT an RH certificate.
N=100000
sig=[0]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d):sig[n]+=d
# Independent divisor formula from prime factorization for seeded/checkpoint samples
samples={1,2,3,10,5040,5041,10080,45360,65520,99999,100000}
rng=random.Random(20261123)
samples.update(rng.sample(range(2,N+1),120))
for n in sorted(samples):
    p=factorint(n)
    product=1
    for prime,k in p.items():product*= (prime**(k+1)-1)//(prime-1)
    assert product==sig[n]
gamma=float(mp.euler)
H=0.0
minimum_robin=(float('inf'),None)
minimum_lagarias=(float('inf'),None)
fail_robin=[];fail_lag=[]
for n in range(1,N+1):
    H += 1/n
    lag_rhs=H+math.exp(H)*math.log(H)
    diff=lag_rhs-sig[n]
    if diff<minimum_lagarias[0]:minimum_lagarias=(diff,n)
    if diff<-1e-9:fail_lag.append(n)
    if n>5040:
        rhs=math.exp(gamma)*n*math.log(math.log(n))
        rmargin=rhs-sig[n]
        if rmargin<minimum_robin[0]:minimum_robin=(rmargin,n)
        if rmargin<=0:fail_robin.append(n)
assert not fail_lag and not fail_robin
# High-precision audit of absolute minimum slacks for safety
mp.mp.dps=70
nR=minimum_robin[1];nL=minimum_lagarias[1]
hr=sum(mp.mpf(1)/k for k in range(1,nL+1))
rhp=mp.e**mp.euler*nR*mp.log(mp.log(nR))-sig[nR]
lhp=hr+mp.e**hr*mp.log(hr)-sig[nL]
assert rhp>0 and lhp>=0
assert nL==1 and lhp==0
out['robin_lagarias_regression']={'N':N,'no_robin_failures_after_5040':len(fail_robin)==0,'no_lagarias_failures':len(fail_lag)==0,'sieve_sigma_and_factorint_crosschecks':len(samples),'smallest_float_margin_robin':{'n':nR,'margin':str(rhp)},'smallest_float_margin_lagarias':{'n':nL,'margin':str(lhp)},'caveat':'Finite numerical checks of RH-equivalent consequences are not proof of RH; these inequalities were reportedly separately formalized and deduced from submitted Lean RH proof.'}

path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False))
print(json.dumps(out,indent=2,ensure_ascii=False))
