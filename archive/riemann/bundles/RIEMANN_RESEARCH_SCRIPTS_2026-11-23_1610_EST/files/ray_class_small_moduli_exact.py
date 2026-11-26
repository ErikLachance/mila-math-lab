"""Exact finite residue-ring unit computation for O_{Q(sqrt(-23))}/m.
K has discriminant -23, O=Z[w], w^2=w-6, global units +/-1.
"""
import math,json
from pathlib import Path

def mul(u,v,m):
 a,b=u;c,d=v
 # (a+bw)(c+dw) = ac-6bd+(ad+bc+bd)w
 return ((a*c-6*b*d)%m,(a*d+b*c+b*d)%m)

def units(m):
 one=(1%m,0)
 els=[(a,b) for a in range(m) for b in range(m)]
 return [u for u in els if any(mul(u,v,m)==one for v in els)]

sizes={}
for m in [2,3,4,5,7]:
 U=units(m)
 distinct_global_units={((1%m),0),((-1)%m,0)}
 assert distinct_global_units.issubset(set(U))
 ratio=len(U)//len(distinct_global_units)
 assert len(U)%len(distinct_global_units)==0
 sizes[str(m)]={'unitGroupSize':len(U),'globalUnitsImageSize':len(distinct_global_units),'rayClassNumberIfClassNumber3':3*ratio,'predictedRationalPrimeDensity':f'1/{2*3*ratio}'}
assert sizes['2']['unitGroupSize']==1
assert sizes['3']['unitGroupSize']==4
assert sizes['2']['rayClassNumberIfClassNumber3']==3
assert sizes['3']['rayClassNumberIfClassNumber3']==6
R={'field':'Q(sqrt(-23))','ring':'Z[w], w=(1+sqrt(-23))/2, w^2=w-6','reducedFormClassNumber':3,'rayClassExactSequence':'Cl_(m)(K) -> Cl(K) quotient by residue unit group (O/m)^* / image(O^*) ; thus size=h_K * #((O/m)^*)/#image(O^*) for integral modulus m, when m is an ordinary integer ideal.','mods':sizes,'limitation':'The predicted rational-prime densities are consequences of Chebotarev/prime ideal theorem, NOT proved by finite enumeration. The residue group cardinalities and ray class sizes are exact given the class number 3. C9 requires uniform short-interval lower bounds for all admissible varying d,M,X,h, not shown.'}
Path('/mnt/data/riemann_20261123_1554/ray_class_small_moduli_exact.json').write_text(json.dumps(R,indent=2));print(json.dumps(sizes,indent=2))
