#!/usr/bin/env python3
"""Exact rational audit of elementary prime-log sum bound in sec16_local.tex.
No certified numerical floats used in the inequality.
"""
from fractions import Fraction as F
import json

def log_bracket(a,K=64):
    u=F(a-1,a+1)
    assert F(0)<u<F(1)
    low=2*sum((u**(2*j+1))/F(2*j+1) for j in range(K))
    # geometric tail: atanh(u) upper <= u^(2K+1)/((2K+1)*(1-u^2))
    error=2*u**(2*K+1)/F((2*K+1)) /(1-u*u)
    return low,low+error

P=[2,3,5,7,11,13]
first_lower=F(0);first_upper=F(0)
for p in P:
    a,b=log_bracket(p)
    first_lower+=a/F(p*p-1)
    first_upper+=b/F(p*p-1)
ln16_lo,ln16_hi=log_bracket(16)
tail_upper=F(256,255)*(ln16_hi+1)/16
left_upper=first_upper+tail_upper
assert left_upper < F(3,4), 'ERROR, claim unsupported'
# using denominator exact integer rather than floats as validation
assert (F(3,4)-left_upper).numerator>0
result={'inequality':'sum over all primes p of log(p)/(p^2-1) < 3/4',
    'source':'https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/main/manuscript/sec16_local.tex lemma r5:lem:logsum',
    'prime_partition':'p<=13 exact rational log upper bounds + integer integral upper on p>=17',
    'atanh_series_terms':64,
    'first6_lower_decimal':format(float(first_lower),'.15f'),
    'first6_upper_decimal':format(float(first_upper),'.15f'),
    'tail_integral_upper_decimal':format(float(tail_upper),'.15f'),
    'total_upper_decimal':format(float(left_upper),'.15f'),
    'strict_margin_lower_decimal':format(float(F(3,4)-left_upper),'.15f'),
    'exact_fraction_comparison_pass':True,
    'proof':'ln(x)=2 sum_{j>=0}u^(2j+1)/(2j+1), u=(x-1)/(x+1), tail <= 2u^(2K+1)/((2K+1)(1-u^2)); t>=16: ln(t)/t^2 decreases, n^2-1 >= (255/256)n^2 for n>=17, integral from16 to infinity =(ln16+1)/16.'}
print(json.dumps(result,indent=2))
with open('/mnt/data/riemann_run_20261123_1524/logsum_rational_certificate.json','w') as f:json.dump(result,f,indent=2)
