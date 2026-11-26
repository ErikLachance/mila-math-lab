from pathlib import Path
import sympy as s,math,time
x=s.symbols('x')
for q in (683,907):
 start=time.monotonic();P=s.Poly(Path(f'/mnt/data/riemann_1004/poly{q}.txt').read_text(),x);d=int(P.discriminant());d0=-7**4*q**3;idx=math.isqrt(d//d0);assert idx**2*d0==d
 f=s.factorint(idx,limit=10000);assert math.prod(p**e for p,e in f.items())==idx
 print(q,'factorization partial',[(p,e,s.isprime(p)) for p,e in f.items()],'elapsed',time.monotonic()-start,flush=True)
