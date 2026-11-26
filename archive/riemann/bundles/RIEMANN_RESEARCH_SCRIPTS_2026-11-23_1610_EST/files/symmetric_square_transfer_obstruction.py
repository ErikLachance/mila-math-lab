"""Exact local-algebra counterexample: residual Sym^2 shape does NOT force an
arbitrary 3x3 characteristic-zero lift to lie in Sym^2(GL_2).
This does not construct a global polarized Galois representation.
"""
from fractions import Fraction
import json
from pathlib import Path
ell=7;e=2;a=2 # mod 7 cyclotomic generator value
res=[pow(a,e,ell),1,pow(a,-e,ell)]
# rational, 7-adically integral diagonal matrix lifting residual [4,1,2]
eigs=[Fraction(4,1), Fraction(8,1), Fraction(1,32)]
assert eigs[0]*eigs[1]*eigs[2] == 1

def modl(x):
 assert x.denominator%ell!=0
 return (x.numerator*pow(x.denominator,-1,ell))%ell
assert [modl(z) for z in eigs]==res
# For A=Sym^2 B, eigenvalues include det(B). If det(A)=1 then det(B)^3=1.
# Thus one eigenvalue of A must be a cube root of unity.
assert all(z**3!=1 for z in eigs)
# Also no geometric progression since a candidate middle would satisfy mid^2=other1*other2.
assert all(eigs[i]**2!=eigs[(i+1)%3]*eigs[(i+2)%3] for i in range(3))
R={'prime':ell,'e':e,'chiValueModPrime':a,'residualExponents':[e,0,-e],'residualDiagonal':res,'liftDiagonal':[str(z) for z in eigs],'determinant':'1','eachEigenvalueCubeNot1':True,'noEigenvalueGeometricMiddle':True,'proof':'If a semisimple 3x3 matrix A is Sym^2 B over a field of characteristic 0, its eigenvalues with multiplicity are alpha^2, alpha*beta, beta^2. Hence det A=(det B)^3 and one eigenvalue alpha*beta=det B has cube equal det A. Our A has det1 and none of 4,8,1/32 has cube1, so it is not Sym^2 B even over an algebraic closure. Yet reduction mod7 is exactly chi^2,1,chi^-2 for chi(g)=2 mod7. Thus the residual triple does NOT alone imply arbitrary characteristic-0 deformations are symmetric squares of GL2.','limitation':'This is only a single matrix over Q_7 with the right residue, not a full global Galois representation or polarized deformation. It rules out a naive functorial inference, not a sophisticated compatible-family argument.'}
Path('/mnt/data/riemann_20261123_1554/symmetric_square_transfer_obstruction.json').write_text(json.dumps(R,indent=2));print(json.dumps(R,indent=2))
