import json, sympy as s, numpy as np, time,math
from pathlib import Path
exec(Path('audit_units.py').read_text().split('for q in (683,907):')[0])
start=time.monotonic();out={}
for q in (683,907):
 d=json.loads(Path(f'units_rel{q}.json').read_text());M=[s.Matrix(a) for a in d['matrices']];one=s.Matrix(d['one']);assert sum((v*m for v,m in zip(one,M)),s.zeros(21))==s.eye(21)
 assert all(m*one==s.eye(21)[:,j] for j,m in enumerate(M))
 for v,norm,_ in d['units']:
  N=sum((int(a)*m for a,m in zip(v,M) if a),s.zeros(21));assert N.det(method='domain-ge')==norm and abs(norm)==1
 a=json.loads(Path(f'rel_cert{q}_6.json').read_text());b=json.loads(Path(f'rel_cert{q}_7.json').read_text());assert a==b
 V=np.array(a['V'],dtype=np.int64).T;g=np.array(a['G'],dtype=np.int64);G=np.zeros_like(I)
 for j in range(7):G[(3*j%7)*6:(3*j%7+1)*6,j*6:(j+1)*6]=g
 assert np.array_equal(G@S%7,powm(S,3)@G%7) and np.array_equal(powm(G,6),I)
 U=np.zeros((42,0),dtype=np.int64);sel=[]
 # select low height exact units that give full orbit span; none of the large search pools needed for certificate
 for i in sorted(range(V.shape[1]),key=lambda i:max(map(abs,d['units'][i][0]))):
  Y=np.hstack([powm(S,k)@V[:,i:i+1]%7 for k in range(7)]);B=base(np.hstack([U,Y]));
  if B.shape[1]>U.shape[1]:U=B;sel.append(i)
  if U.shape[1]==20:break
 assert rank(U)==20 and rank(np.hstack([U,G@U]))==20
 ranks=[rank(powm(D,k)@U) for k in range(8)];weights=[rank(sum((pow(w,-k,7)*powm(G,k) for k in range(6)),np.zeros_like(I))@U) for w in range(1,7)];assert sum(weights)==20
 print(q,'exact norms',len(d['units']),'selected',len(sel),'indices',sel,'heights',[max(map(abs,d['units'][i][0])) for i in sel], 'D ranks',ranks,'weights',weights,flush=True)
 out[q]={'units':[d['units'][i] for i in sel],'V':[a['V'][i] for i in sel],'G':a['G'],'indices':sel,'ranks':ranks,'weights':weights}
Path('minimal_certificate.json').write_text(json.dumps(out,indent=2));print('seconds',time.monotonic()-start)
