import json
from math import prod
from sympy import primerange, isprime

def legendre(a,p):
    t=pow(a%p,(p-1)//2,p)
    return 0 if t==0 else (-1 if t==p-1 else 1)

out=[]
for bound,q in [(5,11),(7,11),(11,19),(13,19),(17,19)]:
    small=list(primerange(3,bound+1))
    assert q%8==3 and isprime(q)
    mods=list(dict.fromkeys([16,q]+small))
    # moduli coprime, with residues d == 7 mod 16, and == -1 mod odd primes
    residue=7; modulus=16
    for p in mods[1:]:
        shift=((-1-residue)*pow(modulus,-1,p))%p
        residue+=modulus*shift
        modulus*=p
        residue%=modulus
    found=None
    for k in range(0,100000):
        d=residue+modulus*k
        if d>max(small+[q]) and isprime(d):
            found=(d,k);break
    assert found is not None
    d,k=found
    checks={p:{'d_mod_p':d%p,'symbol_d_p':legendre(d,p),'symbol_p_d':legendre(p,d),'reciprocity_rhs':(-1 if p%4==3 else 1)*legendre(d,p)} for p in small}
    assert all(v['d_mod_p']==p-1 and v['symbol_p_d']==1 and v['symbol_d_p']==(-1 if p%4==3 else 1) for p,v in checks.items())
    assert d%16==7 and (d+1)%q==0 and legendre(2,d)==1
    out.append({'bound':bound,'q':q,'d':d,'k':k,'CRT_modulus':modulus,'CRT_residue':residue,'two_splits':legendre(2,d)==1,'primes':checks})
print(json.dumps(out,indent=2))
with open('/mnt/data/riemann_runs/20261123_1047/splitting_reciprocity.json','w') as f:json.dump(out,f,indent=2)
