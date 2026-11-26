import sympy as s, time, json
from collections import Counter
start=time.monotonic()
p=7
logs={pow(3,j,7):j for j in range(6)}
def rank(rows):
 a=[list(r) for r in rows]; i=0
 for j in range(len(a[0])):
  k=next((k for k in range(i,len(a)) if a[k][j]%7),None)
  if k is None: continue
  a[i],a[k]=a[k],a[i];a[i]=[v*pow(a[i][j],-1,7)%7 for v in a[i]]
  for k in range(len(a)):
   if k!=i:a[k]=[(x-a[k][j]*y)%7 for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i
def val(n):
 if not n:return 99
 v=0
 while n%7==0:v+=1;n//=7
 return v
def test(q):
 m=7*q;res={a*a%q for a in range(1,q)};eta=lambda a:0 if a%q==0 else (1 if a%q in res else -1)
 h=-sum(a*eta(a) for a in range(1,q))//q
 assert h>0
 if h%7==0:return None
 def bs(k):
  M=7**k;w={a:pow(a,7**(k-1),M) for a in range(1,7)}
  vals=[sum(a*eta(a)*pow(w[a%7],j,M) for a in range(1,m) if a%7 and a%q)%M for j in (2,4)]
  return [val(n)-1 for n in vals]
 v=bs(5);assert v==bs(6)
 if v!=[0,1]:return {'q':q,'hK':h,'vB2B4':v}
 # All six relative factors: cyclotomic odd part has v=-1, cancelled by mu7.
 # Stickelberger integral element kills the wrong character with nonzero scalar.
 def chi(a,j):return eta(a)*pow(a%7,j,7)%7
 b=next(b for b in range(2,m) if b%7 and b%q and chi(b,4)!=b%7)
 sc={j:sum((b*a//m)*(-pow(chi(a,j),-1,7)) for a in range(1,m) if a%7 and a%q)%7 for j in (2,4)}
 # using coefficients -floor(b*a/m) at sigma_a^-1
 assert sc[4]!=0 and sc[2]==0, (q,b,sc)
 groups=[[] for _ in range(6)]
 for a in range(1,m):
  if a%7 and a%q:groups[(logs[a%7]+(3 if eta(a)==-1 else 0))%6].append(a)
 assert all(len(g)==q-1 for g in groups)
 rows=[]; witnesses=[]
 for k in range(1,100):
  ell=k*m+1
  if not s.isprime(ell):continue
  g=int(s.primitive_root(ell));z=pow(g,k,ell);r=pow(g,(ell-1)//7,ell);d={pow(r,j,ell):j for j in range(7)}
  U=[]
  for group in groups:
   v0=1
   for a in group:v0=v0*(1-pow(z,a,ell))%ell
   U.append(v0)
  logs7=[d[pow(u,(ell-1)//7,ell)] for u in U]
  assert sum(logs7)%7==0
  rows.extend([[logs7[(i+j)%6] for j in range(5)] for i in range(6)])
  witnesses.append([ell,g,logs7,rank(rows)])
  if rank(rows)==5:break
 return {'q':q,'hK':h,'vB2B4':v,'stickelberger':[b,sc],'rank':rank(rows) if rows else 0,'witnesses':witnesses}
results=[]
for q in map(int,s.primerange(5,1000)):
 if q%4!=3 or q%7 not in (2,4):continue
 a=test(q)
 if a:results.append(a)
print('scan',len(results),'distribution',Counter(tuple(r['vB2B4']) for r in results))
for r in results:
 if r['vB2B4']==[0,1]:print(r)
print('elapsed',time.monotonic()-start)
open('/mnt/data/riemann_0815/scan.json','w').write(json.dumps(results,indent=2))

