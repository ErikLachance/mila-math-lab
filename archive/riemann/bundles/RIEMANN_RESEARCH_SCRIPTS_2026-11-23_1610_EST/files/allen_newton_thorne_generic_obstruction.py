"""Exact character-exponent audit for applying ANT Thm 1.1(iv) to the
normalized residual triple of the independent human RH reconstruction.
The argument uses K=Q(sqrt(-3)), ell>=5, psi=1 and chi full order ell-1.
NOT an audit of the formal Lean proof.
"""
from math import isqrt
from pathlib import Path
import json

def prime(n):
 return n>1 and all(n%p for p in range(2,isqrt(n)+1))

samples=[]; eligible=0;fail_iv=0;counter=0
for ell in range(5,500):
 if not prime(ell):continue
 d=ell-1
 for e in range(2,251,2):
  if (2*e)%d==0:continue
  eligible+=1
  triple=[(e-1)%d,(-1)%d,(-e-1)%d]
  # For n=3, CSD individual condition on each chi^a: chi^a = (chi^a)^(-1) chi^-2.
  individual=[(2*a+2)%d==0 for a in triple]
  assert individual==[False, True, False],(ell,e,individual)
  # But full triple is CSD as a multiset: a -> -a-2 mod d.
  mapped=sorted([(-a-2)%d for a in triple]);assert sorted(triple)==mapped
  fail_iv+=1
  if len(samples)<10:samples.append({'ell':ell,'e':e,'order':d,'triple':triple,'individualCSD':individual,'wholeCSD':True})
  counter+=1
r={'setting':'K=Q(sqrt(-3)), psi=1, ell>=5, even twist e>=2, generic position (ell-1) does not divide 2e; normalized residual triple after chi^-1 is chi^(e-1) direct sum chi^-1 direct sum chi^(-e-1).','algebra':'Individual conjugate self-duality for each one-dimensional character chi^a in n=3 requires chi^a = chi^(-a-2) (since chi^c=chi), equivalently ell-1 divides 2(a+1). For extreme a=e-1 or a=-e-1 this is equivalent to ell-1 dividing 2e, CONTRARY to generic-position hypothesis. Middle a=-1 does satisfy. However the entire multiset is CSD because extremes are swapped. Thus 2020 Allen-Newton-Thorne Theorem 1.1(iv) cannot apply as stated on this generic input, independently of its Steinberg requirements (v),(vi)(c).','numberOfEligibleChecked':eligible,'numberFailingIndividualCSD':fail_iv,'sample':samples,'limitation':'Assumes K cyclotomic disjointness for ell>=5 and the normalization of the residual triple given in incomplete human reconstruction. This algebra does not prove or disprove RH or the Lean development, and does not exclude a different automorphy theorem or a new argument.'}
Path('/mnt/data/riemann_20261123_1554/allen_newton_thorne_generic_obstruction.json').write_text(json.dumps(r,indent=2));print(json.dumps({'checked':eligible,'eachFails':fail_iv,'sample':samples[:4]},indent=2))
