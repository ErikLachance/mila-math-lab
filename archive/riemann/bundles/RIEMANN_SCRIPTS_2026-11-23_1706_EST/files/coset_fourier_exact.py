import sympy as sp,json
rs=[]
for o in range(2,64):
 q=next(q for k in range(1,10000) if (q:=k*o+1)>10*o and sp.isprime(q) and q%(3*o+1)!=0)
 g=sp.primitive_root(q)
 z=pow(int(g),(q-1)//o,q)
 c=pow(3*o+1,-1,q)
 vals=[]
 for j in range(o):
  hsum=sum((4 if h==0 else 3)*c*pow(z,j*h,q) for h in range(o))%q
  expected=1 if j==0 else c
  assert hsum==expected,(o,j,q,hsum,expected)
  vals.append(hsum)
 rs.append({'o':o,'q':q,'nontrivial_coeff':c,'all_characters_pass':True})
print('PASS exact finite field Fourier coefficients for',len(rs),'orders,',sum(r['o'] for r in rs),'character cases')
print(json.dumps(rs[:7],indent=2))
with open('/mnt/data/riemann_20261123_1659/coset_fourier_exact.json','w') as f:json.dump(rs,f,indent=2)
