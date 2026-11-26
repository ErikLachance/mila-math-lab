#!/usr/bin/env python3
"""A full exact rational monotone-quadrature bathtub certificate for Weil Q on two width-1/24 endpoint collars.
No floats in decisions. Source dependencies: classical digamma series, Zhu lemma 3.1 not needed here.
"""
from fractions import Fraction as F
import json,time,sys
sys.path.insert(0,'/mnt/data/riemann_research_20261123')
from w25_exact_bathtub import (pi_lb,pi_ub,H0_lb,c5_ub,sinh_ub)
start=time.monotonic()
w=F(1,24);L=F(81,100); T0=F(3769,100); S=10**12; M=1024; N=1200
assert 2*w*T0/pi_lb < 1
assert H0_lb > -F(269,50)
h0=-F(269,50)
# t_i=T0*i/M=p/q. Exact series H(t)-H(0) = sum t^2/(a*(4a^2+t^2)), a=n+1/4.
# Every term is positive, so truncation gives certified LOWER bound.
q=T0.denominator*M
u=T0.numerator
scaled_sum=0
for i in range(M):
  p=u*i; pp=p*p
  for n in range(N):
    aa=4*n+1
    scaled_sum+=(S*16*pp)//(aa*(q*q*aa*aa+4*pp))
I_lower=T0*(h0+F(scaled_sum,M*S))
# H(T0) >= h0 + finite rational sum
p=T0.numerator; q0=T0.denominator
hp=0
for n in range(N):
  aa=4*n+1
  hp+=(S*16*p*p)//(aa*(q0*q0*aa*aa+4*p*p))
hT0_lower=h0+F(hp,S)
assert hT0_lower>0
assert I_lower>0
# Generalized bathtub inequality with T0 slightly smaller than pi/(2w):
# integral H*rho >= (2w/pi)*integral_0^T0 H(t)dt +(1-2w*T0/pi)*H(T0).
arch_lb=(2*w/pi_ub)*I_lower+(1-2*w*T0/pi_lb)*hT0_lower
q_lb=arch_lb-c5_ub-4*w*sinh_ub*sinh_ub
for candidate in [F(1,100),F(1,150),F(1,200),F(1,250),F(1,300)]:print('Q>',candidate,q_lb>candidate)
assert q_lb>F(1,100)
output={'L':'81/100','w':'1/24','T0':str(T0),'M':M,'N':N,'S':S,
  'I_lower':str(float(I_lower)),'H_T0_lower':str(float(hT0_lower)),
  'arch_lower':str(float(arch_lb)),'c5_upper':str(float(c5_ub)),
  'pole_lower':str(float(-4*w*sinh_ub*sinh_ub)),'Q_lower':str(float(q_lb)),
  'Q_bigger_1_over_100':q_lb>F(1,100),'elapsed_sec':time.monotonic()-start}
with open('/mnt/data/riemann_research_20261123/w24_exact_bathtub_report.json','w') as o:json.dump(output,o,indent=2)
print(json.dumps(output,indent=2))
