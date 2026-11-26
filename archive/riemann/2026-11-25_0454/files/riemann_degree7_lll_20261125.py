import math, sympy as s, mpmath as m, itertools,time
start=time.monotonic();m.mp.dps=100; N=553;g=5
H=[a for a in range(1,N) if math.gcd(a,N)==1 and (a%7,int(s.legendre_symbol(a%79,79))) in [(1,1),(6,-1)]]
C=[[(pow(g,j,N)*a)%N for a in H] for j in range(6)]
e=[1,-2,-3,-1,2,3];r=[pow(3,j,7) for j in range(6)]
logs=[sum(m.log(2*abs(m.sin(m.pi*a/N))) for a in c) for c in C]
print('u logs',[float(v) for v in logs]); print('b logs',[float(sum(e[l]*logs[(l+j)%6] for l in range(6))/7) for j in range(6)])
# Try short integer combinations of trace vectors; heuristic basis selection.
E=[[e[(l-j)%6] for l in range(6)] for j in range(6)]
d=[[ (E[j][l]-r[j]*e[l])//7 for l in range(6)] for j in range(6)]
zeta=m.exp(2j*m.pi/7)
def values(k):
 bs=[m.exp(sum(e[l]*logs[(l+j)%6] for l in range(6))/7+k*logs[j]) for j in range(6)]
 return [sum(bs[j]*zeta**(i*r[j]) for j in range(6)) for i in range(4)]
def vec(v):return [m.re(v[0])]+[a for x in v[1:] for a in (m.sqrt(2)*m.re(x),m.sqrt(2)*m.im(x))]
# search unit exponent vector k_j with small max archimedean bound
cands=[]
for k in itertools.product(range(-1,2),repeat=5):
 k=k+(0,)
 bs=[m.exp(sum(e[l]*logs[(l+j)%6] for l in range(6))/7+sum(k[l]*logs[(l+j)%6] for l in range(6))) for j in range(6)]
 cands.append((max(bs),k,vec([sum(bs[j]*zeta**(i*r[j]) for j in range(6)) for i in range(4)])))
cands.sort(key=lambda a:a[0]); scale=10**35
# select independent Minkowski vectors by exact rational rank of rounded lattice (numeric rank used separately)
rows=[[1]*1+[m.sqrt(2),0]*3]; ks=[None]
for _,k,v in cands[:100]:
 test=m.matrix(rows+[v]); G=test*test.T
 if abs(m.det(G))<m.mpf('1e-40'):continue
 rows.append(v);ks.append(k)
 if len(rows)==7:break
assert len(rows)==7
A=s.Matrix([[int(m.nint(t*scale)) for t in row] for row in rows]); L,U=A.lll_transform(delta=s.Rational(3,4)); print('basis exponents',ks);print('transform',U.tolist());print('norms',[float(m.sqrt(sum(m.mpf(int(x))**2 for x in L.row(i)))/scale) for i in range(7)])
# certify exact polynomial for first nonconstant small vector
candidate=next(list(map(int,U.row(i))) for i in range(7) if any(U.row(i)[1:]))
print('candidate',candidate)
# exact upper bound u_j <=2^78, u_j^-1<=2^390, all b_j<279.
# sharpen individual unit monomial bounds via exact trace of its 7th power,
# using nonnegative exponent shift (product u_j=1). Since all conjugates positive,
# max b'_j^7 <= trace(alpha * unit^7).
ram=[(6 if a%7==0 else -1)*(78 if a%79==0 else -1) for a in range(N)]
def trace_bound(k):
 exp=[e[j]+7*k[j] for j in range(6)];exp=[x-min(exp) for x in exp];v=[1]+[0]*(N-1)
 for j in range(6):
  for a in C[j]*exp[j]:v=[x-y for x,y in zip(v,v[-a:]+v[:-a])]
 tr=sum(x*y for x,y in zip(v,ram));assert tr%78==0 and tr>0;tr//=78
 B=int(s.integer_nthroot(tr,7)[0])+1
 return 6*B
boundroot=abs(candidate[0])+sum(abs(c)*trace_bound(k) for c,k in zip(candidate[1:],ks[1:]) if c)
bound=max(math.comb(7,k)*boundroot**k for k in range(8));print('rootbound',boundroot,'coeffbound',bound)
M=1; coeff=[0]*8;pr=[]
for k in range(2,100000):
 q=N*k+1
 if not s.isprime(q):continue
 q=int(q);z=pow(int(s.primitive_root(q)),k,q);zz=pow(z,79,q)
 us=[math.prod((1-pow(z,a,q))%q for a in c)%q for c in C];al=math.prod(pow(u,v,q) for u,v in zip(us,e))%q
 if pow(al,(q-1)//7,q)!=1:continue
 b=int(s.nthroot_mod(al,7,q));bs=[pow(b,r[j],q)*math.prod(pow(u,v,q) for u,v in zip(us,d[j]))%q for j in range(6)]
 cs=[sum(c*math.prod(pow(us[(l+j)%6],v,q) for l,v in enumerate(k)) for c,k in zip(candidate[1:],ks[1:]))%q for j in range(6)]
 zs=[(candidate[0]+sum(pow(zz,i*r[j],q)*bs[j]*cs[j] for j in range(6)))%q for i in range(7)]
 c=[1]
 for v in zs:
  cc=[0]*(len(c)+1)
  for j,a in enumerate(c):cc[j]=(cc[j]-v*a)%q;cc[j+1]=(cc[j+1]+a)%q
  c=cc
 if M>2*bound:
  assert all((a if 2*a<=M else a-M)%q==b for a,b in zip(coeff,c));print('extra prime',q);break
 coeff=[a+M*((b-a)*pow(M,-1,q)%q) for a,b in zip(coeff,c)];M*=q;pr.append(q)
assert M>2*bound
coeff=[a if 2*a<=M else a-M for a in coeff];x=s.symbols('x');P=s.Poly(sum(a*x**i for i,a in enumerate(coeff)),x)
print('certified poly',P.as_expr());assert P.is_irreducible;print('disc',s.factorint(abs(int(P.discriminant()))));print('CRT primes',pr,'elapsed',time.monotonic()-start)

