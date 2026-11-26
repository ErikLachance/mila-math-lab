from pathlib import Path
exec(Path('prime_prepare.py').read_text().split('# Persist idempotent')[0]);import pickle
primecache.update(pickle.loads(Path(f'primeparts{q}.pkl').read_bytes()));old=valuation
src=Path('process_fast.py').read_text();exec(src[src.index('ecache={}'):src.index('# Reconstruct prior state')]);new=valuation
checks=0
for v,N in sorted(json.loads(Path(f'pool{q}.json').read_text()),key=lambda a:a[1]):
 if N==1:continue
 for p,e in s.factorint(N).items():
  p,e=int(p),int(e)
  if p not in primecache:continue
  for i,(deg,B,H) in enumerate(primecache[p]):
   if deg>e:continue
   a=old(s.Matrix(v),p,i,e//deg,B,H);b=new(s.Matrix(v),p,i,e//deg,B,H);assert a==b;checks+=1
 if checks>=50:break
print(q,'independent HNF vs Hensel membership checks',checks,'seconds',time.monotonic()-start)
