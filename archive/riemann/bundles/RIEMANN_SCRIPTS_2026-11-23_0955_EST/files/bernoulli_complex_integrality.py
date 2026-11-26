import sympy as sp
from math import prod
from pathlib import Path
from hashlib import sha256
import json
out=Path('/mnt/data/riemann_20261123_0936')
z=sp.symbols('z')
res=[]
for p in [5,7,11,13,17,19]:
  gen=sp.primitive_root(p)
  for t in [1,2,3]:
    order=(p-1)//sp.igcd(t,p-1)
    ph=sp.Poly(sp.cyclotomic_poly(order,z),z,domain='QQ')
    # a(j) primitive-root powers; character maps a(j) -> z^(tj mod order)
    aa=[int(pow(gen,j,p)) for j in range(p-1)]
    parity=(-1)**t  # chi(-1)=exp(2pi i t/2)=(-1)^t
    for k in range(1,9):
      # p*B_{k,chi} = sum_j chi(a_j) sum_{r=0}^k binom(k,r)B_r*a_j^(k-r)*p^r
      poly=0
      for j,a in enumerate(aa):
        local=sum(sp.binomial(k,r)*sp.bernoulli(r,0)*a**(k-r)*p**r for r in range(k+1))
        poly+=local*z**((j*t)%order)
      P=prod(int(q) for q in sp.primerange(2,k+2))
      reduced=sp.rem(sp.Poly(P*poly,z,domain='QQ'),ph,domain='QQ')
      is_integer=all(c.q==1 for c in reduced.all_coeffs())
      assert is_integer,(p,t,k,reduced)
      parity_zero=(parity!=(-1)**k)
      if parity_zero: assert reduced.is_zero,(p,t,k,reduced)
      res.append({'modulus':p,'character_order':int(order),'t':t,'k':k,'parity_forces_zero':parity_zero,
                  'integral_after_clearing':True,'polynomial_degree_reduced':reduced.degree() if not reduced.is_zero else -1})
file=out/'bernoulli_complex_integrality.json'
file.write_text(json.dumps({'tests':len(res),'all_pass':True,'cases':res,'theorem':'For any Dirichlet character chi mod N with root-of-unity values and integer k>=1, N*P_k*B_{k,chi} is an algebraic integer, where P_k is the product of all rational primes <=k+1. Proof: expand B_k(a/N), then N*B_{k,chi}=sum_a chi(a) sum_{j=0}^k binom(k,j)B_j*a^(k-j)*N^j; von Staudt-Clausen implies P_k B_j integer for j<=k, chi(a) algebraic integer. This is denominator integrality, not a Selmer-length bound.',
 'limitation':'Finite tests use primitive nontrivial characters of prime modulus only; proof applies more broadly provided chi values are roots of unity.'},indent=2)+'\n')
print('PASS complex characters',len(res),'parity zero',sum(t['parity_forces_zero'] for t in res))
for f in [Path(__file__),file]:print(str(f),sha256(f.read_bytes()).hexdigest())
