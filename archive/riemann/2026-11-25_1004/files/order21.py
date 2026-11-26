import sys, json,time
from pathlib import Path
import sympy as s
exec(Path('/mnt/data/riemann_1004/order7.py').read_text().split('for q in map(int,sys.argv[1:]):')[0])
for q in map(int,sys.argv[1:]):
 t=time.monotonic();a=json.loads(Path(f'/mnt/data/riemann_1004/fullorder{q}.json').read_text());M=[s.Matrix(x) for x in a['M']];one=s.Matrix([s.Rational(x) for x in a['one']]);M3=structure(C);MM=[s.kronecker_product(a,b) for a in M for b in M3];oo=s.kronecker_product(one,s.eye(3)[:,0]);dd=disc(MM);assert dd==int(a['disc'])**3*49**7
 B,MM,oo,dd=saturate(MM,[7],oo);expected=-7**14*q**9;assert dd==expected,(dd,expected);print('q',q,'degree21 order disc',dd,'index',1/abs(B.det()),'elapsed',time.monotonic()-t,flush=True)
 data={'q':q,'B':[[str(x) for x in row] for row in B.tolist()],'one':[str(x) for x in oo],'M':[[[int(x) for x in row] for row in m.tolist()] for m in MM],'disc':dd};Path(f'/mnt/data/riemann_1004/fullorder21_{q}.json').write_text(json.dumps(data))
