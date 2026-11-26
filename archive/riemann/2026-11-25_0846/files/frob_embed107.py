from embed107 import *
# fixed slot has B-completion Q7, rational 7 valuation3 in F_v.
ex,vs,coefs=json.load(open('frob_element.json'));cv=[s.Rational(a) for a in coefs];p0=s.Poly.from_list(r['poly'],x);a0=sum(a*x**i for i,a in enumerate(cv));assert abs(s.resultant(p0.as_expr(),a0,x))==7**ex
vv=s.zeros(21,1)
for i,v in enumerate(cv):vv[3*i]=v
values=[evalrat(vv,a) for a in rr];assert valatleast(values[0],3) and not valatleast(values[0],4) and all(not valatleast(a,1) for a in values[1:]);assert all(v%7==0 for v in values[0]);values[0]=tuple(v//7 for v in values[0]);Frob=-s.Matrix.vstack(*[classvec(log(a)) for a in values]);Frob=mod(Frob)
assert rank(U.row_join(mod(GG*Frob-Frob)))==20
# full weight1 directions are y1,D^6 y1,D^3 yeta,D ybeta
vecs=[eig(1),mod(D**6*eig(1)),mod(D**3*eig(6)),mod(D*eig(5))];r0=rank(U);assert rank(U.row_join(s.Matrix.hstack(*vecs)))==24
# brute force four coefficients, only one solution
dual=nullmod(U.T,7).T; target=mod(dual*Frob); small=mod(dual*s.Matrix.hstack(*vecs));out=[]
for cc in itertools.product(range(7),repeat=4):
 z=mod(target-small*s.Matrix(cc))
 if not any(z):out.append(cc)
assert len(out)==1;print('Frob norm',s.resultant(p0.as_expr(),a0,x),'coefficients in y1,D6y1,D3yeta,Dybeta',out,'values',list(Frob));json.dump({'coefficients':out,'vector':list(map(int,Frob))},open('frob_certificate.json','w'))

