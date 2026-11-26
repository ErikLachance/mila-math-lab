import math, itertools, sympy as s
N=553;g=5
H=[a for a in range(1,N) if math.gcd(a,N)==1 and (a%7,int(s.legendre_symbol(a%79,79))) in [(1,1),(6,-1)]]
C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]
logs=[sum(math.log(2*abs(math.sin(math.pi*a/N))) for a in c) for c in C]
print('logs units',logs)
ex=[1,5,4];cand=[]
for h in range(1,7):
 for b in itertools.product(range(-3,4),repeat=3):
  e=[(h*x)%7+7*y for x,y in zip(ex,b)];e=e+[-x for x in e]
  l=[sum(e[j]*logs[(j+k)%6] for j in range(6)) for k in range(6)]
  cand.append((max(map(abs,l)),sum(map(abs,e)),h,e,l))
for row in sorted(cand)[:6]:print(row)

