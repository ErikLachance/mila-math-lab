from fractions import Fraction
from itertools import product
import mpmath as mp, json
from pathlib import Path
mp.mp.dps=65
root=Path('/mnt/data/riemann_20261123_0751')

def add(x,y,mods): return tuple((a+b)%m for a,b,m in zip(x,y,mods))
def neg(x,mods): return tuple(-a %m for a,m in zip(x,mods))
def multiple(x,k,mods): return tuple((k*a)%m for a,m in zip(x,mods))
def phase(q,x,mods):
    s=sum((Fraction(a*b,m) for a,b,m in zip(q,x,mods)),Fraction(0))
    return mp.exp(2j*mp.pi*mp.mpf(s.numerator)/s.denominator)
def group(mods):return list(product(*(range(m) for m in mods)))
def subgrp(gens,mods):
    elems={(0,)*len(mods)}
    stack=list(elems)
    while stack:
        x=stack.pop()
        for y in gens:
            z=add(x,y,mods)
            if z not in elems:elems.add(z);stack.append(z)
    return sorted(elems)

cases=[]
max_err=mp.mpf(0)
for mods in ((2,2,3),(2,2,5),(2,2,7),(2,2,9)):
    G=group(mods);F=(1,0,1); gs=[(0,0,0),(1,1,1),(0,1,2),(1,0,4),(1,1,mods[2]-1)]
    Is=[subgrp([(0,0,0)],mods),subgrp([(0,0,1)],mods),subgrp([(1,1,0)],mods),subgrp([(0,1,1)],mods)]
    checked=0
    for I in Is:
        for j in (1,2,3):
            jf=multiple(F,j,mods)
            for g in gs:
                total=mp.mpc(0)
                wrong=mp.mpc(0)
                for q in G:
                    v=sum((phase(q,add(jf,h,mods),mods) for h in I),mp.mpc(0))/len(I)
                    total+=mp.conj(phase(q,g,mods))*v
                    wrong+=phase(q,g,mods)*v
                total/=len(G);wrong/=len(G)
                expected=mp.mpf(1)/len(I) if add(g,neg(jf,mods),mods) in I else mp.mpf(0)
                error=abs(total-expected)
                assert error<mp.mpf('1e-60'),(mods,I,g,j,error)
                max_err=max(max_err,error)
                checked+=1
    cases.append({'group':str(mods),'order':len(G),'checked':checked})
# Counterexample to omitting conjugation: G=(Z/2)^2 x Z/5, inertia trivial, F=(1,0,1), j=1, g=F
mods=(2,2,5);G=group(mods);F=(1,0,1);g=F
right=sum((mp.conj(phase(q,g,mods))*phase(q,F,mods) for q in G),mp.mpc(0))/len(G)
wrong=sum((phase(q,g,mods)*phase(q,F,mods) for q in G),mp.mpc(0))/len(G)
assert abs(right-1)<mp.mpf('1e-60') and abs(wrong)<mp.mpf('1e-60')
report={'identity':'(1/|G|) sum_character conjugate(chi(g))*(1/|I|)sum_h_in_I chi(j F+h) = (1/|I|)1[g-jF in I]','cases':cases,'tests':sum(c['checked'] for c in cases),'max_numerical_error_high_precision':mp.nstr(max_err,12),'without_conjugation_counterexample':{'G':str(mods),'I':'trivial','j':1,'g':str(g),'correct_value':mp.nstr(right,6),'wrong_value':mp.nstr(wrong,6)},'proof':'For each h, the character sum is |G| if jf+h-g=0 and 0 otherwise by finite Fourier orthogonality. Exactly one h in I may solve this, giving the stated formula.','status':'independent finite character algebra sanity check, not a proof of analytic/geometric inputs or RH'}
(root/'finite_abelian_inertia_fourier.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
