"""Exact reduced quadratic-form class-number enumeration for small fundamental
imaginary quadratic discriminants; illustrates why Dirichlet GRH is not Hecke GRH.
Not a proof that Hecke GRH is false or of C9.
"""
from math import gcd,isqrt
import json
from pathlib import Path

def reduced_forms(D):
 assert D<0 and D%4 in (0,1)
 forms=[]
 for a in range(1,isqrt(abs(D)//3)+3):
  for b in range(-a,a+1):
   if (b*b-D)%(4*a):continue
   c=(b*b-D)//(4*a)
   if a>c:continue
   if gcd(gcd(a,abs(b)),c)>1:continue
   if (abs(b)==a or a==c) and b<0:continue
   forms.append((a,b,c))
 return sorted(forms)

cases={-7:1,-11:1,-19:1,-23:3,-31:3,-47:5,-59:3,-71:7}
R={}
for D,expected in cases.items():
 f=reduced_forms(D)
 assert len(f)==expected,(D,f,expected)
 assert all(b*b-4*a*c==D for a,b,c in f)
 R[str(D)]={'classNumber':len(f),'primitiveReducedForms':f}
# K=Q(sqrt(-23)); the class group has exactly 3 elements, so it has nontrivial
# characters of order 3, whose L-functions are Hecke class characters of K.
# Such characters are not rational Dirichlet characters on Gal(Q_ab/Q):
# inversion of a nontrivial class under complex conjugation acts nontrivially,
# whereas every character of G_Q factoring through an abelian group is fixed by
# all inner conjugations. Thus a proof for ALL Dirichlet L over Q cannot just be
# substituted into the prime ideal theorem for ray classes of varying K.
R['scope']='K=Q(sqrt(-23)) has class number 3, hence nontrivial order-3 unramified Hecke class group characters. These characters are inverted by complex conjugation and therefore cannot be restrictions of rational Dirichlet characters: the latter are invariant under inner conjugation. A Dirichlet-only GRH statement does not directly control those Hecke L-functions. This only obstructs an invalid shortcut; does not prove logical independence or falsity of C9.'
Path('/mnt/data/riemann_20261123_1554/ray_class_dirichlet_scope.json').write_text(json.dumps(R,indent=2))
print(json.dumps({'casesTested':len(cases),'formsDMinus23':R['-23'],'formsDMinus47':R['-47']},indent=2))
