from pathlib import Path
exec(Path('prime_prepare.py').read_text().split('# Persist idempotent')[0])
import pickle
primecache.update(pickle.loads(Path(f'primeparts{q}.pkl').read_bytes()))
# Idempotent Hensel lift avoids rational HNF inverses in membership tests.
ecache={}
def valuation(v,p,i,kmax,B,H):
 mod=p**kmax;key=(p,i,kmax)
 dtype=object if mod>10**6 else np.int64
 def m(a,b):
  A=np.tensordot(a,np.asarray(mats,dtype=dtype),axes=1)%mod
  return A@b%mod
 if key not in ecache:
  e=np.array([(int(a)-int(b))%p for a,b in zip(one,B*one)],dtype=dtype)
  prec=1
  while prec<kmax:
   z=m(e,e);e=(3*z-2*m(z,e))%mod;prec*=2
  assert np.array_equal(m(e,e),e)
  ecache[key]=e
 e=ecache[key];z=m(e,np.array([int(a)%mod for a in v],dtype=dtype));k=0
 while k<kmax and all(int(a)%p**(k+1)==0 for a in z):k+=1
 return k
# Reconstruct prior state only from trusted local data created during this run.
state=Path(f'state{q}.pkl')
if state.exists():
 pivot,history,seen,cert,units,rels,skipped,powercache=pickle.loads(state.read_bytes());known={tuple(u[0]) for u in units}
# The order-three automorphism of the cubic factor c -> c^2-2.
Cmat=s.Matrix([[1,-2,3],[0,0,-1],[0,1,-1]])
# c^4-4c^2+4 = 3-c-c^2 using c^3=-c^2+2c+1? c^4=3c^2-c-1, yes.
Sig=T.inv()*s.kronecker_product(s.eye(7),Cmat)*T
assert all(z.q==1 for z in Sig) and Sig**3==I and Sig*one==one
for j in range(n):assert Sig*M[j]==mat(Sig[:,j])*Sig
pool=json.loads(Path(f'pool{q}.json').read_text());pool.sort(key=lambda v:v[1]);cnt=0
for v,N in pool:
 v=s.Matrix(v)
 for i in range(3):
  vv=tuple(map(int,v));vv=min(vv,tuple(-z for z in vv));v=Sig*v
  if vv in seen:continue
  seen.add(vv);cnt+=1;A=mat(vv)
  if N==1:add(vv,'direct or cubic conjugate');continue
  relation(s.Matrix(vv),A,N,factors(s.Matrix(vv),A,N))
 if cnt and (cnt%30<=2 or time.monotonic()-start>18):
  save();state.write_bytes(pickle.dumps((pivot,history,seen,cert,units,rels,skipped,powercache)))
 if time.monotonic()-start>18:break
save();state.write_bytes(pickle.dumps((pivot,history,seen,cert,units,rels,skipped,powercache)));print('FINAL pool',len(pool),'new processed',cnt,'processed',len(seen),'rels',rels,'skipped',skipped,'units',len(units),'secs',time.monotonic()-start,flush=True)
