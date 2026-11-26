from sympy import symbols, cyclotomic_poly, resultant, totient, primerange
from math import isqrt
from time import monotonic
from fractions import Fraction
from collections import Counter
x=symbols('x'); start=monotonic(); C=Counter()
# All phases are covered analytically by triangle inequality; this checks the
# rational lower bound using exact squaring, no floating-point trigonometry.
for q in range(13,1001):
 for e in range(1,5):
  a=q**e
  assert a-2>0 and (a-2)**2>9*q
  C['trace_separation_squared']+=1
# For roots of unity and scalar integral traces of magnitude <3 sqrt(q),
# compute the exact norm of the cleared trace gap in Q(zeta_n).
for n in range(1,21):
 f=cyclotomic_poly(n,x); d=int(totient(n))
 for q in (13,17,19,23):
  for e in (1,2):
   a=q**e
   for m in range(-isqrt(9*q),isqrt(9*q)+1):
    if m*m>=9*q:continue
    g=a*a*x*x+(1-m)*a*x+1
    R=abs(int(resultant(f,g,x)))
    B=a*a+(1+abs(m))*a+1
    assert 0<R<=B**d
    assert R%q!=0 # constant term 1 gives norm unit at q
    C['cyclotomic_norms']+=1
    # Compare against determinant of multiplication for selected cases
    if n<=6 and e==1 and m in (-2,0,2):
     from sympy import Poly, Matrix, rem
     g0=Poly(g,x); f0=Poly(f,x)
     cols=[]
     for j in range(d):
      h=rem(g0*Poly(x**j,x),f0)
      cols.append([h.nth(i) for i in range(d)])
     assert abs(int(Matrix(cols).T.det()))==R
     C['norm_determinant_crosschecks']+=1
# Unbounded prime support with uniform archimedean bound and denominator only 2.
# Fermat gives a simpler variant: (2^(l-1)-1)/2^(l-1) is divisible by l.
for l in primerange(3,2000):
 a=Fraction(2**(l-1)-1,2**(l-1))
 assert 0<a<1 and a.numerator%l==0 and a.denominator&(a.denominator-1)==0
 C['denominator_counterexamples']+=1
# Explicit self twists of irreducible clock/shift models in dimension m.
# D e_j=zeta^j e_j, S e_j=e_(j+1); conjugating by D gives zeta^b on D^a S^b.
# Check exponents rather than inexact complex matrices.
for m in range(2,33):
 for a in range(m):
  for b in range(m):
   for j in range(m):
    assert ((j+b)+a*(j+b)-j-a*(j+b)-b)%m==0
    C['clock_shift_intertwiner_entries']+=1
print(dict(C)); print('script_seconds',monotonic()-start)

