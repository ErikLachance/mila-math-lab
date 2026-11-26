#!/usr/bin/env python3
"""Exact Fraction positivity certificate for a restricted support Weil form at L=81/100, w=1/25.
  No reliance on external interval arithmetic, floating point for any decision.
  Dependencies only on standard identity ψ(a+ib) and Zhu high-t bound.
"""
from fractions import Fraction as F
from math import factorial
import json, time
T0=time.monotonic()

def atan_interval(x: F, N=35):
    assert 0<=x<1
    s=F(0)
    for k in range(N):
        s+=((-1)**k)*x**(2*k+1)/(2*k+1)
    r=x**(2*N+1)/(2*N+1)
    return (s,s+r) if N%2==0 else (s-r,s)

def pi_interval():
    a,b=atan_interval(F(1,5),33)
    c,d=atan_interval(F(1,239),12)
    return 16*a-4*d,16*b-4*c

def log_interval(x:F,N=240):
    assert x>=1
    y=(x-1)/(x+1)
    s=F(0)
    term=y
    for k in range(N):
        s+=2*term/(2*k+1)
        term*=y*y
    r=2*term/((2*N+1)*(1-y*y))
    return s,s+r

pi_lb,pi_ub=pi_interval()
assert F(314159,100000)<pi_lb<pi_ub<F(314160,100000)
log2_lb,log2_ub=log_interval(F(2),40)
log5_lb,log5_ub=log_interval(F(5),90)
H64=sum((F(1,n) for n in range(1,65)),F(0))
gamma_ub=H64-6*log2_lb-F(1,128)+F(1,12*64*64)
logpi_lb,logpi_ub=log_interval(pi_ub,140)
H0_lb=-(gamma_ub+pi_ub/2+3*log2_ub+logpi_ub)
assert H0_lb > -F(269,50)

# Upper bound of sinh(81/200) via Taylor series + geometric remainder.
x=F(81,200)
s=F(0)
for k in range(6):s+=x**(2*k+1)/factorial(2*k+1)
next_term=x**13/factorial(13)
ratio=x*x/F(14*15)
sinh_ub=s+next_term/(1-ratio)
assert sinh_ub<F(5,12)

# Rational upper bound for c5=log(5)/sqrt(5), using squared-integer lower sqrt.
sqrt5_lb=F(2236067,1000000)
assert sqrt5_lb*sqrt5_lb<5
c5_ub=log5_ub/sqrt5_lb
assert c5_ub<F(18,25)

L=F(81,100); w=F(1,25);A=F(15,4)
M=768;N=320;S=10**15
# Lower Riemann sum over [0,A] of H(t).
# H(t) >= H(0) + sum_{n>=0} t^2 / (a*(4a^2+t^2)) .
# For t_i = 15i/(4M), a=(4n+1)/4, term = 900 i^2 / [(4n+1)*(4M^2(4n+1)^2+225 i^2)].
min_h0=-F(269,50)
scaled_sum=0
for i in range(M):
    ii=i*i
    for n in range(N):
        a=4*n+1
        scaled_sum+=(S*900*ii)//(a*(4*M*M*a*a+225*ii))
low_lb=A*(min_h0+F(scaled_sum,M*S))

# Analytic high integral from A to T=pi/(2w):
# I = T*(ln(1/(4w))-1) + A*(ln(2pi/A)+1) - ln(T/A).
# Use rational lower/upper values with exact monotonicity.
T_lb=pi_lb/(2*w)
logA_lb=log_interval(F(1,4)/w,230)[0] # ln(25/4)
log2piA_lb=log_interval(2*pi_lb/A,130)[0] # ln(8pi/15)
logTA_ub=log_interval(pi_ub/(2*w*A),290)[1] # ln(10pi/3)
assert logA_lb>1
hi_lb=T_lb*(logA_lb-1)+A*(log2piA_lb+1)-logTA_ub
assert hi_lb+low_lb>0
arch_lb=(2*w/pi_ub)*(hi_lb+low_lb)

# Exact rational dominance (use even safer human-readable constants on last line)
q_lb=arch_lb-c5_ub-4*w*sinh_ub**2
assert q_lb>F(1,500), ('requested margin insufficient',float(q_lb))
# claimed simpler bound with constants if possible
for target in [F(1,200),F(1,300),F(1,400),F(1,500),F(1,1000)]:
  print('check Q >',target,'?',q_lb>target)

output={
  'L':'81/100','w':'1/25','t_low':'15/4','T':'25 pi / 2',
  'M_Riemann_bins':M,'N_digamma_terms':N,'scaled_floor':str(S),
  'H0_lb_decimal':str(float(H0_lb)),'H0_fixed_bound':'-269/50',
  'gamma_upper_decimal':str(float(gamma_ub)),
  'pi_lb':str(float(pi_lb)),'pi_ub':str(float(pi_ub)),
  'sinh_upper_decimal':str(float(sinh_ub)),
  'c5_upper_decimal':str(float(c5_ub)),
  'I_low_lower_decimal':str(float(low_lb)),'I_hi_lower_decimal':str(float(hi_lb)),
  'arch_lower_decimal':str(float(arch_lb)),
  'Q_lower_decimal':str(float(q_lb)),
  'Q_exceeds_1_over_500':q_lb>F(1,500),
  'Q_exceeds_1_over_400':q_lb>F(1,400),
  'Q_exceeds_1_over_300':q_lb>F(1,300),
  'max_rational_bitlength':max(z.numerator.bit_length() for z in [pi_lb,pi_ub,hi_lb,logA_lb,logTA_ub]),
  'elapsed_sec':time.monotonic()-T0,
}
with open('/mnt/data/riemann_research_20261123/w25_exact_bathtub_report.json','w') as f:
  json.dump(output,f,indent=2)
print(json.dumps(output,indent=2))
