from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import hashlib,json
import sympy as sp
import mpmath as mp
mp.mp.dps=80
out=Path('/mnt/data/riemann_20261123_0936')

def chi(a,p):
  x=a%p
  if x==0:return 0
  return 1 if pow(x,(p-1)//2,p)==1 else -1

def rational_polynomial(k,p):
  return F(p**(k-1))*sum((F(chi(a,p))*F(sp.bernoulli(k,sp.Rational(a,p))) for a in range(1,p+1)),F(0))

def rational_generating(k,p):
  # Coefficients of sum chi(a)exp(a*t), and (exp(p*t)-1)/t.
  numer=[sum(F(chi(a,p)*a**j,factorial(j)) for a in range(1,p+1)) for j in range(k+1)]
  den=[F(p**(j+1),factorial(j+1)) for j in range(k+1)]
  v=[]
  for j in range(k+1):
    v.append((numer[j]-sum(den[r]*v[j-r] for r in range(1,j+1)))/den[0])
  return v[k]*factorial(k)

def legendre_lvalue(k,p):
  # L(1-k,chi) from Hurwitz zeta independent of Bernoulli-polynomial arithmetic.
  s=1-k
  return mp.mpf(p)**(-s)*sum(chi(a,p)*mp.zeta(s,mp.mpf(a)/p) for a in range(1,p+1))

rows=[]; lcross=[]; denfail=[]; parfail=[]
for p in [3,5,7,11,13,17,19,23,29]:
  parity=chi(-1,p)
  for k in range(1,11):
    b1=rational_polynomial(k,p)
    b2=rational_generating(k,p)
    assert b1==b2,(p,k,b1,b2)
    if parity!=(-1)**k and b1!=0:parfail.append((p,k,str(b1)))
    primes_k=list(sp.primerange(1,k+2))
    clear=p
    for z in primes_k:clear*=int(z)
    cleared=b1*clear
    if cleared.denominator!=1:denfail.append((p,k,str(b1),clear))
    if k in [1,2,3,4,6,8,10]:
      Lv=legendre_lvalue(k,p)
      val=-mp.mpf(b1.numerator)/(mp.mpf(b1.denominator)*k)
      err=abs(Lv-val)
      assert err<mp.mpf('1e-65'),(p,k,mp.nstr(err,20))
      lcross.append({'p':p,'k':k,'max_absolute_error':mp.nstr(err,4)})
    rows.append({'p':p,'k':k,'chi_of_minus_one':parity,'value':str(b1),'cleared_integer':str(cleared)})
assert not parfail and not denfail
result={'p_cases':[3,5,7,11,13,17,19,23,29],'k_range':[1,10],'exact_cases':len(rows),
        'independent_Hurwitz_checks':len(lcross),'parity_violations':len(parfail),'denominator_clear_violations':len(denfail),
        'sample_nonzero': [r for r in rows if r['value']!='0'][:17],
        'formula':'B_{k,chi}=N^{k-1} sum_{a=1}^N chi(a) B_k(a/N) = k! [t^k] sum chi(a)exp(a*t) / ((exp(Nt)-1)/t).',
        'source_context':'Rubinstein III.9 quoted PsiBound (III.261) bounds a COHOMOLOGY LENGTH by v_O(N * product_{p<=k+1}p * B_{k,psi}), with k=e+1 and a primitive character. These tests verify only special-function normalization, parity, denominator clearing and L(1-k,chi)=-B_{k,chi}/k for quadratic primitive chars of prime conductor.',
        'excluded':'No exact source proof of PsiBound, no class-group cohomology computation, no uniform bound for growing p or k, no RH implication.'}
f=out/'generalized_bernoulli_audit.json';f.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('BERNOULLI PASS exact',len(rows),'Hurwitz',len(lcross),'parity',len(parfail),'denomclear',len(denfail))
print('sample',result['sample_nonzero'][:5])
for x in [Path(__file__),f]:print(str(x),hashlib.sha256(x.read_bytes()).hexdigest())
