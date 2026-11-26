from pathlib import Path
exec(Path('prime_prepare.py').read_text().split('# Persist idempotent')[0])
import pickle
primecache.update(pickle.loads(Path(f'primeparts{q}.pkl').read_bytes()))
targets=[I]+[H for p,ls in primecache.items() for deg,B,H in ls if deg<=2 and p**deg<=1000]
primes=(1009,1013,1019,1021); inv={p:np.array([0]+[pow(i,-1,p) for i in range(1,p)],dtype=np.int64) for p in primes};mod=math.prod(primes);coeff=[(mod//p)*pow(mod//p,-1,p) for p in primes]
code=Path('norm_collisions.py').read_text();exec(code[code.index('def det_batch'):code.index('def candidates')])
file=Path(f'pool{q}.json');pool=json.loads(file.read_text()) if file.exists() else [];seen={tuple(v) for v,N in pool};rnd=int(sys.argv[2]);rng=random.Random(q+10001+rnd);count=0;exact=0
for i in range(100):
 if time.monotonic()-start>18:break
 H=targets[(rnd*13+i)%len(targets)];w=[rng.uniform(-2,2) for _ in range(12)]; a=w[:3]+[z for z in w[3:] for _ in range(2)];weights=[mp.exp(z) for z in a];EH=E*mp.matrix(H.tolist());A=s.Matrix([[int(mp.nint(EH[j,jj]*weights[j]*10**22)) for j in range(n)] for jj in range(n)])
 try:L,U=A.lll_transform(delta=s.Rational(3,4));assert abs(U.det())==1 and L==U*A
 except (AssertionError,ValueError):continue
 V=H*U.T;vs=[]
 for k in range(1,4):
  for ids in it.combinations(range(8),k):
   for sg in it.product((-1,1),repeat=k-1):
    v=tuple(map(int,sum((z*V[:,j] for j,z in zip(ids,(1,)+sg)),s.zeros(n,1))));v=min(v,tuple(-z for z in v))
    if v not in seen:vs.append(v);seen.add(v)
 if not vs:continue
 aa=np.array(vs,dtype=np.int64);As=np.tensordot(aa,mats,axes=1);dd=sum(det_batch(As,p)*c for p,c in zip(primes,coeff))%mod;dd=np.minimum(dd,mod-dd);count+=len(vs)
 for j in np.flatnonzero((dd>0)&(dd<=10**8)):
  N=int(dd[j]);r=N
  for p in [7]+list(primecache):
   while r%p==0:r//=p
  if r!=1:continue
  norm=abs(int(mat(vs[j]).det(method='domain-ge')));exact+=1
  if norm==N:pool.append((vs[j],N))
 file.write_text(json.dumps(pool));print('batch',rnd,'round',i,'candidates',count,'exact',exact,'pool',len(pool),'secs',round(time.monotonic()-start,2),flush=True)
