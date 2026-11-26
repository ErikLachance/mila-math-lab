#!/usr/bin/env python3
"""Rational 3-interval certificate for the Weil quadratic form on two width-1/15 collars.

Geometric interpretation: L=81/100, E=(-L,-L+w) union (L-w,L), w=1/15.
For f in C_c^infty(E;C), this *conditional on the standard Weil explicit formula*
computes a universal lower bound Q_W(f)/||f||^2>1/60, using three
closed-form minimizations in the endpoint-pair energy p, no p-bin grid.
This does NOT prove all-window nonnegativity or RH.
"""
from fractions import Fraction as F
from math import isqrt, factorial
from time import monotonic
from pathlib import Path
import json
start=monotonic()
L=F(81,100);w=F(1,15)
delta_lo=F(1056,100000);delta_hi=F(1057,100000)
pi_lo=F(314159,100000);pi_hi=F(314160,100000)
h0=-F(269,50);prime5=F(18,25);sinh_hi=F(5,12)

# Certify all coarse transcendental constants by outward exact rational series.
def atan_bracket(z,n):
    p=sum(((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    r=z**(2*n+1)/F(2*n+1)
    return (p,p+r) if n%2==0 else (p-r,p)
lo1,hi1=atan_bracket(F(1,5),10)
lo2,hi2=atan_bracket(F(1,239),4)
assert pi_lo < 16*lo1-4*hi2 <= 16*hi1-4*lo2 < pi_hi

def log_bracket(x,n):
    t=(x-1)/(x+1)
    s=F(0);z=t
    for k in range(n):
        s+=2*z/F(2*k+1);z*=t*t
    return s,s+2*z/(F(2*n+1)*(1-t*t))
ln5_lo,ln5_hi=log_bracket(F(5),100)
assert delta_lo < 2*L-ln5_hi < 2*L-ln5_lo < delta_hi
ln2_lo,ln2_hi=log_bracket(F(2),40)
lnpi_lo,lnpi_hi=log_bracket(pi_hi,100)
gamma_hi=sum((F(1,k) for k in range(1,65)),F(0))-6*ln2_lo-F(1,128)+F(1,12*64**2)
assert -gamma_hi -pi_hi/2 -3*ln2_hi -lnpi_hi > h0
sqrt5_lo=F(2236,1000)
assert sqrt5_lo**2<5 and ln5_hi/sqrt5_lo<prime5
x=L/2
sinh_partial=sum((x**(2*k+1)/factorial(2*k+1) for k in range(6)), F(0))
sinh_bound=sinh_partial+(x**13/F(factorial(13)))/(1-x*x/F(14*15))
assert sinh_bound<sinh_hi

# Bounds for sqrt(rational), all decisions use F (no floating point).
radix=10**12
def sqlo(q):
    assert q>=0
    if q==0:return F(0)
    k=isqrt(q.numerator*radix**2//q.denominator)
    o=F(k,radix)
    assert o*o<=q
    return o

def squp(q):
    assert q>=0
    if q==0:return F(0)
    k=isqrt(q.numerator*radix**2//q.denominator)+1
    o=F(k,radix)
    assert o*o>q
    return o

a=delta_hi;b=w-delta_lo
assert a>0 and b>0
pi=pi_lo

def Mupper(p):
    return (squp(a*p)+squp(b*(1-p)))**2/pi

def maxM(left,right):
    # Cauchy-Schwarz gives concave pointwise cap, peaking at a/(a+b).
    p0=a/(a+b)
    if left<=p0<=right:return (a+b)/pi
    return max(Mupper(left),Mupper(right))

def digamma_lower(T):
    # H(t)=Re psi(1/4+it/2)-ln pi >= h0 + sum_{n=0}^{N-1}
    #         16*t^2/[(4n+1)((4n+1)^2+4*t^2)].
    # Positive increasing summands justify left rectangle quadrature for I(T).
    N=400;cells=768;scale=10**10
    total=0
    for i in range(cells):
        p=T.numerator*i;q=T.denominator*cells;v=p*p
        for n in range(N):
            u=4*n+1
            total+=(scale*16*v)//(u*(q*q*u*u+4*v))
    I=T*(h0+F(total,cells*scale))
    v=T.numerator*T.numerator;q=T.denominator
    h=h0+F(sum((scale*16*v)//(u*(q*q*u*u+4*v)) for u in (4*n+1 for n in range(N))),scale)
    assert h>0 and I>0 and I-T*h<0
    return I,h


def interval_certificate(left,right,T):
    assert 0<=left<=right<=1
    max_density=maxM(left,right)
    assert 2*T*max_density<1, 'T too high for this p interval'
    I,h=digamma_lower(T)
    C=2*(T*h-I)   # positive: lower arch envelope h-C*M
    assert C>0
    A=C/pi
    X=A*(a-b)+prime5
    radius_squared=(A*(a+b))**2+2*A*(a-b)*prime5+prime5**2
    assert radius_squared>0
    rlo=sqlo(radius_squared);rhi=squp(radius_squared)
    # p_*=(1+X/sqrt(radius_squared))/2 (MAXIMIZER), enclosed exactly.
    plo=min((1+X/rlo)/2,(1+X/rhi)/2)
    phi=max((1+X/rlo)/2,(1+X/rhi)/2)
    pole=4*w*sinh_hi*sinh_hi
    if plo>right:
        method='increasing_endpoint';p=right
        bound=h-pole-C*Mupper(p)-prime5*p
    elif phi<left:
        method='decreasing_endpoint';p=left
        bound=h-pole-C*Mupper(p)-prime5*p
    else:
        method='global_closed_form'
        bound=h-pole-(A*(a+b)+prime5+rhi)/2
    assert bound>F(1,60), 'strict Q>1/60 failed'
    return {'p_range':[str(left),str(right)],'T':str(T),'method':method,
            'conservative_lower_float_display':float(bound),
            'uniform_density_mass_check':bool(2*T*max_density<1),
            'exact_comparison_gt_1_over_60':True,
            'p_star_bracket_display':[float(plo),float(phi)],
            'h_T_lower_display':float(h),'I_T_lower_display':float(I),
            'max_density_display':float(max_density)}

certificates=[interval_certificate(F(0),F(2,5),F(4711,200)),
              interval_certificate(F(2,5),F(11,25),F(25)),
              interval_certificate(F(11,25),F(1),F(26))]
assert [(a['p_range']) for a in certificates]==[['0','2/5'],['2/5','11/25'],['11/25','1']]
rep={'date':'2026-11-23','L':'81/100','w':'1/15','collar_support':'(-81/100,-81/100+1/15) union (81/100-1/15,81/100)',
     'mathematical_result':'Weil Q_W(f)>||f||_2^2/60 on this support for complex smooth compact support, conditional on source-to-formula interpretation, not global RH',
     'checks':'all inequalities and comparisons performed with exact Fraction and isqrt outward bounds',
     'n_p_bin_checks':0,'n_closed_form_intervals':3,'passes':certificates,
     'minimum_reported_lower_display':min(c['conservative_lower_float_display'] for c in certificates),
     'all_pass':True,'runtime_seconds':monotonic()-start,
     'critical_caveat':'Only a restricted-support result, nested inside previously certified w=1/12 support; 1/60 margin is a stronger quantitative lower bound on this narrower subset, not an extension of RH proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(rep,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(rep,ensure_ascii=False,indent=2))
