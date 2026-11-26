from itertools import permutations,product
from math import prod
import json,time
start=time.monotonic()
def mul(a,b):return tuple(a[i] for i in b)
def cycles(g):
 seen=set(); out=[]
 for i in range(len(g)):
  if i in seen:continue
  s=[];j=i
  while j not in seen:seen.add(j);s.append(j);j=g[j]
  out.append(tuple(s))
 return out
checks=0;normchecks=0;noncop=0;obstructions=0; examples={}
for n in range(1,6):
 ident=tuple(range(n)); perms=list(permutations(range(n))); inv=[c for c in perms if mul(c,c)==ident]
 for g in perms:
  H={ident};h=g
  while h not in H:H.add(h);h=mul(g,h)
  O=cycles(g); idx={i:j for j,o in enumerate(O) for i in o}
  for c in inv:
   if mul(c,mul(g,c)) not in H:continue
   k=tuple(idx[c[o[0]]] for o in O)
   assert all(idx[c[i]]==k[j] for j,o in enumerate(O) for i in o)
   for w in product(range(3),repeat=len(O)):
    if any(w[j]!=w[k[j]] for j in range(len(O))):continue
    # direct independent valuation enumeration on points with invariance tests
    d=[w[idx[i]] for i in range(n)]
    brute=0; cop=0
    for bO in product(*(range(x+1) for x in w)):
     b=[bO[idx[i]] for i in range(n)]
     if all(b[i]+b[c[i]]==d[i] for i in range(n)):
      brute+=1
      cop+=all(not(b[i] and b[c[i]]) for i in range(n))
    fixed=[j for j in range(len(O)) if k[j]==j]
    pairs=[j for j in range(len(O)) if j<k[j]]
    expected=0 if any(w[j]%2 for j in fixed) else prod(w[j]+1 for j in pairs)
    expcop=0 if any(w[j]>0 for j in fixed) else 2**sum(w[j]>0 for j in pairs)
    assert brute==expected and cop==expcop,(n,g,c,w,brute,cop,expected,expcop)
    checks+=1; normchecks+=1
    if brute and not cop:noncop+=1;examples.setdefault('even_fixed_orbit_non_coprime',[g,c,w])
    if not brute:obstructions+=1;examples.setdefault('odd_fixed_orbit_no_factor',[g,c,w])
print(json.dumps(dict(checks=checks,normalization_count_checks=normchecks,noncoprime_only=noncop,impossible_even_without_coprimality=obstructions,examples=examples,seconds=time.monotonic()-start),indent=2))
