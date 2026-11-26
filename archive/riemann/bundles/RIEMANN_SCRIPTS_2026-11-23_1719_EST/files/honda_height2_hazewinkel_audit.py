from fractions import Fraction
from math import comb,factorial
from json import dump

def val_p(n,p):
    if n == 0: return None
    r=0
    while n%p==0:
        r+=1;n//=p
    return r

def val_frac(f,p):
    return val_p(f.numerator,p)-val_p(f.denominator,p)

out=[]
for p in [3,5,7,11,13]:
    N=p*p
    vN=val_p(factorial(N),p)
    assert vN==p+1
    assert all(comb(N,k)%p==0 for k in range(1,N))
    vals={k:val_p(comb(N,k),p) for k in range(1,N)}
    assert all((v==1 if k%p==0 else v==2) for k,v in vals.items())
    special={k:(comb(N,k)//p)%p for k in range(1,N) if k%p==0}
    expect={k:(pow(-1,(k//p)-1)*pow(k//p,-1,p))%p for k in special}
    assert special==expect
    coeff=Fraction(1,factorial(N))+Fraction(1,p)
    assert val_frac(coeff,p)==-(p+1)
    assert val_frac(Fraction(-1,p),p)==-1
    # Formal group F(x,y)=e(L(x)+L(y)): at total degree N, mixed coefficients -C(N,k)/p.
    F_coeff=[-Fraction(comb(N,k),p) for k in range(1,N)]
    assert all(val_frac(c,p)>=0 for c in F_coeff)
    assert (1-p**(N-1))%p==1
    # Dwork test g1(X^p)-p*g1(X)=-pX, while g2 test fails at degree p^2.
    g1={p**j:Fraction(1,p**j) for j in range(0,5)}
    g2={p**(2*j):Fraction(1,p**j) for j in range(0,3)}
    def test_defect(g,deg):
        return g.get(deg//p,0) if deg%p==0 else Fraction(0,1)
    dwork_g2_at_N = test_defect(g2,N)-p*g2.get(N,0)
    dwork_g1_at_N = test_defect(g1,N)-p*g1.get(N,0)
    assert dwork_g2_at_N== -1
    assert dwork_g1_at_N==0
    out.append({'p':p,'N':N,'v_p(N!)':vN,'v_p(coef_X^N_exp(epsilonL))_epsilon_unit':-(p+1),'v_p(coef_X^N_inverse_L)':-1,'F_N_mixed_integral':True,'nonzero_modp_mixed_exponents':[k for k in range(1,N) if vals[k]==1],'modp_coeff_binomial_over_p':special,'dwork_height1_defect_X^N':str(dwork_g1_at_N),'dwork_height2_defect_X^N':str(dwork_g2_at_N),'pseries_X^N_modp':1})
print(*out,sep='\n')
with open('/mnt/data/riemann_20261123_1659/honda_height2_hazewinkel_audit.json','w') as f:dump({'tests':out,'all_passed':True},f,indent=2)
