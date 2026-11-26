#!/usr/bin/env python3
"""Exact analytic countermodels to weakening H12's quantifiers. Not counterexamples to RH."""
import math, json, hashlib
from pathlib import Path
from fractions import Fraction

theta=Fraction(3,5); beta=Fraction(4,5)
# F(x)=x^beta sin^2(log x), x>=1.
# F(exp(k*pi))=0, but F(exp(k*pi+pi/2))=exp(beta*(k*pi+pi/2)).
# For k>=1, exp(k*pi+pi/2) <= exp(3*k*pi/2) = [exp(k*pi)]^(3/2).
# Derivative = x^(beta-1) [beta sin^2(log x) + sin(2 log x)]
# Thus |F'|<=beta+1 <2 on x>=1, even stronger than the G(x) elementary polylog Lipschitz cap.
ratios=[]
for k in [1,2,5,10,20,40]:
    logY=k*math.pi
    logx=(k+.5)*math.pi
    logratio=float(beta-theta)*logx
    ratios.append({'k':k,'logY':logY,'log(xbad)':logx,'F(xbad)/xbad^theta':math.exp(logratio),'F(Y)/Y^theta':0,'bad_point_inside_window':logx<=1.5*logY})
assert all(r['bad_point_inside_window'] for r in ratios)

# Uniform constants are needed. A pointwise bound C(x)=x^(beta-theta) for F(x)=x^beta is vacuous.
# With any fixed C, eventually x^(beta-theta)>C.
for c in [Fraction(1),Fraction(3),Fraction(1000),Fraction(1000000)]:
    x=math.exp((math.log(float(c))+3.0)/float(beta-theta))
    assert x**float(beta-theta)>float(c)

# The interval exponent 3/2 is irrelevant: for all c>0, x_k=Y_k*exp(pi/2)
# lies in [Y_k,Y_k^(1+c)] once k>=(1/(2*c)).
for width in [Fraction(1,100),Fraction(1,10),Fraction(1,2),Fraction(2)]:
    k=math.ceil(1/(2*float(width)))
    assert (k+.5)<= (1+float(width))*k + 1e-10

out={'theta':str(theta),'beta':str(beta),'countermodel':'F(x)=x^(4/5)*sin(log x)^2, x>=1. F is C^1, nonnegative, and |F\'(x)| <= 9/5 for all x>=1. Zeros Y_k=exp(k*pi) are unbounded, so F(Y_k)<=Y_k^theta for every k. But x_k=exp((k+1/2)*pi) lies inside [Y_k,Y_k^(3/2)] for all k>=1, and F(x_k)/x_k^theta=exp((1/5)*(k+1/2)*pi)->infinity. Thus single good scales, even under global bounded derivative, cannot replace full windows. This is a toy function, not the prime-power statistic G(x).','uniform_constant_countermodel':'F(x)=x^(4/5): for each x there is C_x=x^(1/5) with F(x)<=C_x*x^(3/5), but there is no x-independent C. Thus the fixed K in H12 is a substantive quantifier.','samples':ratios,'scope':'Quantifier logic of the human guide III.11, not an objection to Alpoge Lean theorem, which asserts full H12-type hypotheses within the formal proof.'}
p=Path('/mnt/data/riemann_current/riemann_h12_quantifier_countermodels.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('SHA256 CODE',hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print('SHA256 JSON',hashlib.sha256(p.read_bytes()).hexdigest())
