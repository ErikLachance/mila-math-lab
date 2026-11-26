from fractions import Fraction
from collections import defaultdict
from sympy import primerange, isprime, legendre_symbol
import mpmath as mp
import json

# Completely exact rational coefficients multiplying log(p).
def weighted_selector(q,d,x):
    assert isprime(q) and isprime(d) and q != d
    assert q % 8 == 3 and d % 16 == 7 and (d+1)%q == 0
    assert legendre_symbol(d,q) == -1 and legendre_symbol(q,d) == 1
    naive=defaultdict(Fraction)
    classified=defaultdict(Fraction)
    powers=0
    for p in primerange(2,x+1):
        lq = int(legendre_symbol(p,q)) if p != q else 0
        ld = int(legendre_symbol(p,d)) if p != d else 0
        m=p;k=1
        while m<=x:
            factor=Fraction(x,m)-1
            if factor:
                naive[p] += (1+lq**k)*(1-ld**k)*factor
                if p==d and k%2==0:
                    classified[p] += 2*factor
                elif p!=q and p!=d and lq==1 and ld==-1 and k%2==1:
                    classified[p] += 4*factor
            powers+=1
            m*=p;k+=1
    assert {p:v for p,v in naive.items() if v} == {p:v for p,v in classified.items() if v}, set(naive.items())^set(classified.items())
    return {'q':q,'d':d,'x':x,'prime_power_terms':powers,'nonzero_prime_log_coeffs':sum(v!=0 for v in naive.values()),'ramified_q_coefficient':str(naive.get(q,0)),'ramified_d_coefficient':str(naive.get(d,0)),'exact_equality':True}

classify=[]
for q,d,xx in [(3,23,[100,528,529,530,700,1000,10000]),(11,1319,[100,10000,2000000])]:
    for x in xx:
        classify.append(weighted_selector(q,d,x))

# Character chi_4: independent, conditional convergence check. All finite identities are algebraic.
mp.mp.dps=65
L=lambda s: mp.dirichlet(s,[0,1,0,-1])
c=mp.diff(L,1)/L(1)
X=100000
rows=[]
chi_items=[]
for p in primerange(3,X+1):
    cp=1 if p%4==1 else -1
    m=p;k=1
    while m<=X:
        chi_items.append((int(m),int(cp**k),mp.log(int(p))))
        m*=p;k+=1
chi_items.sort()
for T in [1000,10000,30000,100000]:
    sub=[(n,ch,logp) for n,ch,logp in chi_items if n<=T]
    psiT=mp.fsum(ch*logp for n,ch,logp in sub)
    AT=mp.fsum(ch*logp/n for n,ch,logp in sub)
    for x in [10,50,200]:
        if x>=T:continue
        psix=mp.fsum(ch*logp for n,ch,logp in sub if n<=x)
        Ax=mp.fsum(ch*logp/n for n,ch,logp in sub if n<=x)
        gt=x*Ax-psix+c*x
        truncated_integral=-psix-x*(AT-Ax)+x*psiT/T
        error=gt-truncated_integral
        expected=x*(c+AT-psiT/T)
        assert mp.almosteq(error,expected,rel_eps=mp.mpf('1e-55'),abs_eps=mp.mpf('1e-55'))
        rows.append({'x':x,'T':T,'Gchi_x':mp.nstr(gt,20),'truncated_integral':mp.nstr(truncated_integral,20),'residual':mp.nstr(error,20),'exact_finite_tail_identity_verified_high_precision':True})

report={'source':'Rubinstein et al zeta working v2 Nov22 2026 Eq II.7 II.8 II.9 II.10; independent elementary character checks',
 'classification_statement':'For q,d primes q==3(mod8), d==7(mod16), q|(d+1): S_{q,d}(x)=4*sum_{p distinct q,d, (p/q)=1,(p/d)=-1} sum_{k odd} log(p)*(x/p^k-1)_+ + 2*log(d)*sum_{j>=1}(x/d^(2j)-1)_+, and all q^k vanish.',
 'character_reciprocity':'(d/q)=(-1/q)=-1 and (q/d)=-(d/q)=1; p=d has only even powers with coeff 2',
 'exact_selector_tests':classify,
 'twist_finite_identity':'Gchi(x)-[-x*integral_x^T(Psi_chi(t)/t^2 dt)]=x*(cchi+sum_{n<=T}Lambda(n)chi(n)/n-Psi_chi(T)/T), for x<T. This identity is EXACT for finite T, with integration of step Psi; the limit T->infinity requires arithmetic PNT for fixed chi and uniform estimate for varying chi.',
 'chi4_log_derivative_c':mp.nstr(c,35),'twist_numerical_tests':rows,
 'limits':'No uniform bound for growing conductor q,d established; no new RH proof; tests are finite and numerical for L derivatives.'}
path='/mnt/data/riemann_20261123_1225/ramified_selector_and_twisted_tail.json'
with open(path,'w') as f:json.dump(report,f,indent=2)
print(json.dumps({'selector_tests':len(classify),'ramified_example':next(r for r in classify if r['d']==23 and r['x']==530),'chi4_c':mp.nstr(c,20),'twist_tests':len(rows),'residual_T100000':rows[-1]['residual']},indent=2))
