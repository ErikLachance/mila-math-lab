import sympy as s
from itertools import product
a,b,v=s.symbols('a b v'); X=s.Matrix([[0,b,0],[0,0,b],[a,0,0]]);V=s.zeros(3);V[0,2]=1
br=lambda A,B:A*B-B*A
U=br(X,V);W=br(X,U);q=a*b*b
assert X**3==q*s.eye(3)
assert br(V,U)==2*a*V
assert br(V,W)==2*a*U
assert br(X**7,V)==q*q*U
print('brackets symbolic exact',br(V,U),br(V,W),br(X**7,V))
# Need class-2 lift information at order12: in the specific truncated exponential model
# [B_i,B_j] has coefficients v²(j-i)[V,U] at11, v²(j²-i²)/2[V,W] at12.
# Matrix pair (B_0,B_1) and (B_0,B_2) gives independent leading central directions.
for a0,b0,v0 in product(range(1,7),repeat=3):
 a1=2*a0*v0*v0%7; a2=a0*a0*v0*v0%7
 assert (a1*(4*a2)-2*a1*a2)%7 !=0
print('all 216 nonzero triples: rank 2 in leading coefficient pair')

