from fractions import Fraction as F
import json,random
from pathlib import Path
root=Path('/mnt/data/riemann_20261123_0751')
rng=random.Random(20261123)
counts=0
ex=[]
for T in (8,16,31,65,127):
    vals={n:F(rng.randint(-8,8),rng.randint(1,9)) for n in range(2,T+1)}
    ell=F(11,19)
    C=sum((v/F(n) for n,v in vals.items()),F(0))
    R=-ell-C
    ys=[F(1),F(2),F(7,2),F(T,2),F(T)]
    ys+=[F(rng.randint(1,10*T),10) for _ in range(45)]
    for y in ys:
        if y<1 or y>T:continue
        A=sum((v*(y/F(n)-1) for n,v in vals.items() if n<=y),F(0))
        S=sum((v*min(F(1),y/F(n)) for n,v in vals.items()),F(0))
        G=A+y*ell
        predicted=-S-y*R
        assert G==predicted, (T,y,G,predicted)
        # Deliberate wrong sign test should fail for most parameters
        if counts<5:ex.append({'T':T,'y':str(y),'G':str(G),'neg_S_minus_yR':str(predicted),'wrong_plus_S_plus_yR_is_valid':G==(S+y*R)})
        counts+=1
assert counts>200
out={'identity':'For T>=y>=1 and arbitrary coefficients a_n, A(y)=sum_{n<=y}a_n(y/n-1), S(y)=sum_{n<=T}a_n min(1,y/n), C=sum_{n<=T}a_n/n, R=-ell-C, G=A+y ell, exact G=-S-y R. All sums finite, no conditional convergence needed.','rational_random_trials':counts,'examples':ex,'wrong_sign_examples':sum(1 for x in ex if not x['wrong_plus_S_plus_yR_is_valid']),'status':'finite algebra identity only; no uniform analytic estimate for actual Dirichlet characters'}
(root/'prime_twist_truncation_identity.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
