#!/usr/bin/env python3
"""Independent exact rational audit of Rubinstein v2 (III.308–309)->(M) exponent 17/8."""
from fractions import Fraction as F
from pathlib import Path
import json
cases=0;max_ratio=F(0);maxcase=None
for t in [1,2,3,4,6]:
 X=t**8; n=2*t**9;T=t**8;T2=2*t;delta=F(T2,n)
 assert delta==F(1,X) and F(T,n)==F(1,2*t)
 for x in [1,7,101,10000]:
  for m in [1,5,19]:
   for k in [1,41,1000]:
    a=x; b=1;B0=2*n*m*b*X; Nc=F(T2*k*b*X**2,n*n)
    E=T*a*(1+F(m*m,k))+m*(B0+Nc)
    B=F(T*m*b,2)*delta
    errors=F(x,m)+F(x*m,k)+m+F(k,n*n)
    ratio=(E/B)/(8*(t**17)*errors)
    assert ratio<=1, (t,x,m,k,ratio)
    if ratio>max_ratio:max_ratio=ratio;maxcase={'t':t,'x':x,'m':m,'k':k,'ratio':str(ratio)}
    cases+=1
# Witness that dropping either lower bound can make the same inequality fail at fixed X=1.
# x=m=k=1, n=100, T=1, T2=1, b=1; both density bounds violated.
examples={}
for who,T,T2 in [('drop_T_density',1,100),('drop_delta_density',100,1)]:
 n=100;X=1; x=m=k=b=1; delta=F(T2,n)
 E=F(T*x*(1+F(m*m,k)),1)+m*(2*n*m*X+F(T2*k*X*X,n*n))
 B=F(T*m,2)*delta
 ratio=(E/B)/(8*(F(x,m)+F(x*m,k)+m+F(k,n*n)))
 examples[who]={'T':T,'T2':T2,'ratio':str(ratio),'fails':bool(ratio>1)}
 assert ratio>1
# symbolically exact coefficient bounds under density assumptions
# 2/δ<=2t^8, 4n X/(Tδ)<=8t^17, 2X²/(T*n)<=4t^17/n².
result={'exact_fraction_test_cases':cases,'largest_ratio_to_claimed_bound':str(max_ratio),'largest_ratio_float':float(max_ratio),'most_stressed_case':maxcase,'sharp_relative_coefficient':'4n*m*X/(T*δ) = 8*m*t^17 at the density endpoints; explains exponent 17/8','counterexamples_without_required_densities':examples,'status':'PASS; algebraic normalisation only','limitation':'Does not establish unnormalised estimate (III.309), density/existence conditions, or RH'}
Path('/mnt/data/riemann_20261123_0908/main_M_normalization_audit.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
