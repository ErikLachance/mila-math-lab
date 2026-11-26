import math,json
from sympy import primerange
# Four abstract cells c0..3, two allocated to chi=+/- and one to chi=0;
# not claiming these are reachable from the paper's automorphic construction.
q=7; d=3; Y=10000
terms=[]
for p in primerange(2,Y+1):
 v=p;k=1
 while v<=Y:
  if p!=2 and p!=q:
   c=(1 if p%3==1 else -1 if p%3==2 else 0)**k
   terms.append((v,p,k,c,math.log(p)))
  if v>Y//p:break
  k+=1;v*=p
weights=[(1e-4,1e-2,1e-2,1e-2),(1e-2,1e-4,1e-2,1e-2),(1e-2,1e-2,1e-4,1e-2),(1e-2,1e-2,1e-2,1e-4)]
cell={1:0,-1:1,0:2}
results=[]
for ww in weights:
 P=sum((1-z)*lp*max(1/v-ww[cell[z]],0) for v,p,k,z,lp in terms)
 g=math.exp(sum(math.log(w) for w in ww)/4)
 # naive uniform-cell main constant uses all cells despite no reason for equal density
 M=-1-0.5772156649015329+0.36828161597014784-math.log(g)
 results.append({'weights':ww,'log_geometric_mean':math.log(g),'P_odd_p_not_q':P,'formal_uniform_cell_main_M':M,'difference':P-M})
assert max(abs(x['log_geometric_mean']-results[0]['log_geometric_mean']) for x in results)<1e-12
print(json.dumps(results,indent=2))
open('/mnt/data/riemann_20261123_1431_fourcell_source_scope.json','w').write(json.dumps(results,indent=2))
