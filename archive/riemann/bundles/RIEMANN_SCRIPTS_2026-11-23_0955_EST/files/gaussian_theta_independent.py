#!/usr/bin/env python3
"""Independent Gaussian lattice summation vs period-normalized rational theta moments."""
import json
import mpmath as mp
from fractions import Fraction
mp.mp.dps=110
R=12
omega=mp.beta(mp.mpf(1)/4,mp.mpf(1)/2)/2
T={}
for n in [0,4,8,12,16,20]:
    acc=mp.mpc(0)
    for x in range(-R,R+1):
        for y in range(-R,R+1):
            z=mp.mpc(x,y)
            acc+=mp.exp(-mp.pi*(x*x+y*y))*z**n
    T[n]=acc
assert all(abs(v.imag)<mp.mpf('1e-100') for v in T.values())
vals=[Fraction(1,4),Fraction(17,16),Fraction(-111,64),Fraction(12513,256),Fraction(-146079,1024)]
checks=[]
for k,f in enumerate(vals,1):
    r=T[4*k]/(T[0]*(omega/mp.pi)**(4*k))
    target=mp.mpf(f.numerator)/f.denominator
    diff=abs(r-target)
    checks.append({'k':k,'r':mp.nstr(r,55),'expected':str(f),'absolute_error':mp.nstr(diff,8)})
    assert diff<mp.mpf('1e-65'),(k,diff)
print('T0',mp.nstr(T[0],35),'omega',mp.nstr(omega,35))
for a in checks:print(a)
# exact symmetry argument: lattice invariant under multiplication by i; moment M_n=i^n M_n -> 0 unless 4|n.
res={'source':'Rubinstein 2026 guide section I.4.1 and III.12 Prop Le7, Cor Le8','precision_digits':mp.mp.dps,'lattice_cutoff_axis':R,'T0':mp.nstr(T[0],90),'omega':mp.nstr(omega,90),'checks':checks,'proven_finite_symmetry':'exact finite centered square invariant under multiplication by i, so non-4-divisible moments vanish; all infinite moments converge absolutely by Gaussian factor','note':'finite cutoff comparisons are high precision numerical checks, not proof of infinite Gaussian theta evaluations'}
with open('/mnt/data/riemann_20261123_0936/gaussian_theta_independent.json','w') as f:json.dump(res,f,indent=2)
print('PASS all 5 rational moments up to n20')
