import sympy as s, math, itertools, time
from functools import reduce
start=time.monotonic();N=553;g=5
H=[a for a in range(1,N) if math.gcd(a,N)==1 and (a%7,int(s.legendre_symbol(a%79,79))) in [(1,1),(6,-1)]]
C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]
e=[1,-2,-3,-1,2,3]; r=[pow(3,j,7) for j in range(6)]
E=[[e[(l-j)%6] for l in range(6)] for j in range(6)]
assert all((E[j][l]-r[j]*e[l])%7==0 for j in range(6) for l in range(6))
d=[[ (E[j][l]-r[j]*e[l])//7 for l in range(6)] for j in range(6)]
# polynomial trace of b, over full real-unit orbit; CRT with proven bound
A=130713168770152422
B=1
while B**7<=A:B+=1
bound=max(math.comb(7,k)*(6*B)**k for k in range(8))
print('b bound',B,'coefficient bound',bound)
M=1; coeff=[0]*8; primes=[]
for k in range(2,20000):
 q=N*k+1
 if not s.isprime(q):continue
 q=int(q); z=pow(int(s.primitive_root(q)),k,q); zz=pow(z,79,q)
 us=[math.prod((1-pow(z,a,q))%q for a in c)%q for c in C]
 al=math.prod(pow(u,v,q) for u,v in zip(us,e))%q
 if pow(al,(q-1)//7,q)!=1:continue
 # b is any root, changes z_i by permutation
 rr=s.nthroot_mod(al,7,q,all_roots=True); assert len(rr)==7
 b=int(rr[0]); bs=[pow(b,r[j],q)*math.prod(pow(u,v,q) for u,v in zip(us,d[j]))%q for j in range(6)]
 assert all(pow(bs[j],7,q)==math.prod(pow(u,v,q) for u,v in zip(us,E[j]))%q for j in range(6))
 zs=[sum(pow(zz,i*r[j],q)*bs[j] for j in range(6))%q for i in range(7)]
 c=[1]
 for v in zs:
  cc=[0]*(len(c)+1)
  for j,a in enumerate(c):cc[j]=(cc[j]-v*a)%q;cc[j+1]=(cc[j+1]+a)%q
  c=cc
 coeff=[a+M*((b-a)*pow(M,-1,q)%q) for a,b in zip(coeff,c)];M*=q;primes.append(q)
 print('prime',q,'CRT modulus digits',len(str(M)))
 if M>2*bound:break
assert M>2*bound
coeff=[a if 2*a<=M else a-M for a in coeff]
x=s.symbols('x');P=s.Poly(sum(a*x**i for i,a in enumerate(coeff)),x)
print('POLYNOMIAL',P.as_expr());print('irreducible',P.is_irreducible);assert P.is_irreducible
print('disc factor',s.factorint(abs(int(P.discriminant()))))
print('primes',primes,'elapsed',time.monotonic()-start)

