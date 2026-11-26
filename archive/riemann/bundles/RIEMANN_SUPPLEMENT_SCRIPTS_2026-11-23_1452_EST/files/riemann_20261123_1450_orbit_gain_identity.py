#!/usr/bin/env python3
"""Exact rational audit of sec12_loss.tex formulas (r2:g0,r2:g1).
For positive al(s), cap(s,e), and any finite Excl set, show
 g1-g0 = sum_oddTop sum_Excl max(al/p^e-cap,0)
       + sum_evenTop [gamma_p*al-sum_nonExcl max(al/p^e-cap,0)] >=0.
If cap varies with e, take any finite prescribed cap list plus a positive
constant tail; this script uses cap independent of e as one test model.
No theorem about g1-price or positive gain is implied.
"""
from fractions import Fraction as F
import json, random
R=random.Random(271828)

def gamma(p):return F(p,p*p-1)

def max_odd(a,cap,p,excluded):
    acc=F(0)
    e=1
    while True:
        term=a/F(p**e)
        if term<=cap:break
        if e not in excluded:acc+=term-cap
        e+=2
        assert e<90
    return acc

def sec12_difference(items,p):
    gam=gamma(p)
    g0=F(0);g1=F(0)
    correct=F(0)
    for is_odd,a,cap,exc in items:
        all_max=max_odd(a,cap,p,set())
        except_max=max_odd(a,cap,p,exc)
        g0+=except_max
        if is_odd:
            g1+=all_max
            correct+=all_max-except_max
        else:
            g1+=gam*a
            correct+=gam*a-except_max
    assert g1>=g0
    assert g1-g0==correct
    return g1-g0

count=0; best=None
for p in [3,5,7,11,17]:
    for rep in range(1000):
        items=[]
        for _ in range(R.randint(1,6)):
            is_odd=bool(R.randrange(2))
            a=F(R.randrange(1,2000),R.randrange(1,8))
            cap=F(R.randrange(1,500),R.randrange(1,15))
            exc=set(R.sample([1,3,5,7,9],R.randrange(0,3)))
            items.append((is_odd,a,cap,exc))
        delta=sec12_difference(items,p)
        count+=1
        if best is None or delta<best:best=delta
print('PASS',count,'exact rational orbit-model cases; minimum g1-g0:',best)
# Necessary caveat: price is independent, so g1-price can be BELOW g0.
price=F(1); example_g1=F(0);example_g0=F(0)
assert example_g1-price<example_g0
with open('/mnt/data/riemann_20261123_1450_orbit_gain_identity.json','w') as f:
    json.dump({'status':'PASS','exact_fraction_cases':count,'least_difference':str(best),'scope':'source algebra g1>=g0 at positive adjusted al and nonnegative caps, before price; not proof of source lower bound'},f,indent=2)
