from fractions import Fraction as F
from itertools import product
for a,b,c in product(range(1,31),repeat=3):
 if 3*c+b>=4*a:
  k=F(b-a,3);x,y,z=a+k,b-2*k,c+2*k;assert x==y<=z and x>0
 else:
  k=F(b-c,4);x,y,z=a+k,b-2*k,c+2*k;assert y==z<x and y>0
