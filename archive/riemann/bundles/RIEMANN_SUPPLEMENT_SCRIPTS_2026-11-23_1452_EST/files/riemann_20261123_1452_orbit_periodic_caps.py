#!/usr/bin/env python3
"""Exact source-like g0/g1 algebra for PERIODIC varying cap(s,e), e odd.
Two independent paths:
  min sum: finite evaluated terms then exact geometric tail.
  max sum: finite terms until a/p^e below min cap.
Compare g1-g0 against decomposition into excluded and even-top gains.
"""
from fractions import Fraction as F
import random,json
R=random.Random(1729)

def test(p,items):
    gp=F(p,p*p-1)
    g0=g1=rhs=F(0)
    for is_odd,a,caps,exclude in items:
        cap_min=min(caps)
        e=1; maxima_all=maxima_allowed=mins=F(0)
        while a/F(p**e)>cap_min:
            cap=caps[((e-1)//2)%len(caps)]
            term=a/F(p**e)
            mins+=min(term,cap)
            gain=max(term-cap,F(0))
            maxima_all+=gain
            if e not in exclude:maxima_allowed+=gain
            e+=2
            assert e<=95
        # Exact infinite tail of min terms beginning odd e, because caps>0.
        mins+= a*F(p*p,(p**e)*(p*p-1))
        assert mins+maxima_all==gp*a
        g0+=maxima_allowed
        if is_odd:
            g1+=gp*a-mins
            rhs+=maxima_all-maxima_allowed
        else:
            g1+=gp*a
            rhs+=gp*a-maxima_allowed
    assert g1-g0==rhs and rhs>=0
    return rhs

N=0; small=large=None
for p in [3,5,7,11,19]:
    for _ in range(1000):
        items=[]
        for j in range(R.randrange(1,6)):
            caps=[F(R.randrange(1,300),R.randrange(1,15)) for _ in range(R.randrange(1,7))]
            a=F(R.randrange(1,3000),R.randrange(1,12))
            exc=set(R.sample([1,3,5,7,9,11],R.randrange(0,3)))
            items.append((bool(R.randrange(2)),a,caps,exc))
        delta=test(p,items)
        small=delta if small is None else min(small,delta)
        large=delta if large is None else max(large,delta)
        N+=1
print('PASS',N,'periodic-cap exact Fraction tests, min',small,'max',large)
with open('/mnt/data/riemann_20261123_1452_orbit_periodic_caps.json','w') as f:
    json.dump({'passed':True,'tests':N,'min_difference':str(small),'max_difference':str(large),'exclusions':'arbitrary finite odd exponents','analytic_identity':'g1>=g0 before price for al>=0, cap>=0, all odd e'},f,indent=2)
