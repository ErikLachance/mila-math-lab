import json

def deriv(A,B,f,mod):
    C={};E={}
    for k,v in B.items():
        for j,c in f.items():
            idx=j+k-1
            z=((2*k+j)*c*v)%mod
            if idx>=0:C[idx]=(C.get(idx,0)+z)%mod
    for k,v in A.items():
        if k:E[k-1]=(E.get(k-1,0)+2*k*v)%mod
    return ({k:v for k,v in C.items() if v},{k:v for k,v in E.items() if v})

cases=[(7,{3:1,0:-1},'CM j=0 split p=7'),(13,{3:1,0:-1},'CM j=0 split p=13'),(5,{3:1,1:-1},'CM j=1728 split p=5'),(13,{3:1,1:-1},'CM j=1728 split p=13'),(5,{3:1,0:-1},'CM j=0 inert p=5'),(7,{3:1,1:-1},'CM j=1728 inert p=7')]
out=[]
for p,f,name in cases:
    A,B={1:1},{}
    for _ in range(p): A,B=deriv(A,B,f,p)
    result={'prime':p,'case':name,'Dpowp_x_modp':{'A':A,'B':B},'vanishes':not bool(A or B)}
    out.append(result)
    print(result)
open('/mnt/data/riemann_20261123_1728/split_controls.json','w').write(json.dumps(out,indent=2))
