import numpy as np, sympy as s, itertools as it,json,time,sys
from pathlib import Path
from sympy.matrices.normalforms import hermite_normal_form as hnf
q=int(sys.argv[1]);t=time.monotonic();f=Path(f'units{q}.json');data=json.loads(f.read_text());M=np.array(data['matrices'],dtype=np.int64);oo=s.Matrix(data['one']);n=21; units=data['units'];known={tuple(u[0]) for u in units};primes=(1009,1013,1019);inv={p:np.array([0]+[pow(i,-1,p) for i in range(1,p)],dtype=np.int64) for p in primes};mod=int(np.prod(primes));coeff=[(mod//p)*pow(mod//p,-1,p) for p in primes]
# Batch exact determinants over finite fields, including singular matrices.
def det_batch(A,p):
 A=A.copy()%p;N=len(A);ix=np.arange(N);d=np.ones(N,dtype=np.int64)
 for i in range(n):
  z=A[:,i:,i]!=0;j=np.argmax(z,axis=1)+i;d=d*np.where(np.any(z,axis=1),np.where(j==i,1,-1),0)%p
  tmp=A[ix,i].copy();A[ix,i]=A[ix,j];A[ix,j]=tmp
  v=A[:,i,i];d=d*v%p
  if i+1<n:
   factors=A[:,i+1:,i]*inv[p][v,None]%p
   A[:,i+1:,i+1:]=(A[:,i+1:,i+1:]-factors[:,:,None]*A[:,i:i+1,i+1:])%p
 return d

def candidates():
 for k in range(2,6):
  for ids in it.combinations(range(21),k):
   for sg in it.product((-1,1),repeat=k-1):
    v=np.zeros(n,dtype=np.int64);v[list(ids)]=(1,)+sg;yield v

def save():
 data['units']=units;Path(f'units_coll{q}.json').write_text(json.dumps(data))

def unit(v,why):
 v=tuple(map(int,v));v=min(v,tuple(-x for x in v))
 if v in known or tuple(-x for x in v) in known or list(v)==list(oo) or list(-s.Matrix(v))==list(oo):return
 A=s.Matrix(np.tensordot(v,M,axes=1).tolist());d=int(A.det(method='domain-ge'));assert abs(d)==1
 units.append((list(v),d,[]));known.add(v);print('new unit',len(units),why,'maxcoef',max(map(abs,v)),flush=True);save()

cache={};cnt=0;small=0;coll=0;gen=candidates();limit=int(sys.argv[2]);maxnorm=10000
while time.monotonic()-t<limit:
 vs=np.array(list(it.islice(gen,256)))
 if len(vs)==0:break
 A=np.tensordot(vs,M,axes=1);d=sum(det_batch(A,p)*c for p,c in zip(primes,coeff))%mod;d=np.minimum(d,mod-d);cnt+=len(vs)
 for i in np.flatnonzero((d>0)&(d<=maxnorm)):
  B=s.Matrix(A[i].tolist());norm=abs(int(B.det(method='domain-ge')))
  if norm>maxnorm or not norm:continue
  assert norm==d[i];small+=1
  if norm==1:unit(vs[i],'direct');continue
  H=hnf(B);key=tuple(H)
  if key in cache:
   old,oldv=cache[key];v=old.inv()*s.Matrix(vs[i].tolist());assert all(x.q==1 for x in v);coll+=1;unit(v,f'ideal norm {norm}')
  else:cache[key]=(B,vs[i].tolist())
 print('candidates',cnt,'small exact norms',small,'collisions',coll,'units',len(units),'elapsed',round(time.monotonic()-t,2),flush=True) if cnt%4096==0 else None
save();print('FINAL',cnt,small,coll,len(units),'time',time.monotonic()-t,flush=True)
