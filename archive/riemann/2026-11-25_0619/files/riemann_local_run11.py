from riemann_order_run11 import *
import json,itertools
r=json.load(open('/mnt/data/riemann_units_run11.json'));M=[s.Matrix(m) for m in r['matrices']];one=s.Matrix(r['one']);n=len(M);p=7
# Frobenius 49 is identity on reduced quotient iff residue fields degrees divide 2.
F7=s.Matrix.hstack(*[power(M,s.eye(n)[:,i],7,7,one) for i in range(n)]);F49=F7*F7;F49=F49.applyfunc(lambda v:int(v)%7)
K=nullmod(F49,7);I=hnf((7*s.eye(n)).row_join(K));Ii=I.inv();print('radical dim',K.cols,'residue dim',n-K.cols)
assert all(int(z)%7==0 for z in F49*F49-F49)
# I^4=7 I, checking via ideals (all local ramification indices 3)
J=I
for k in range(2,5):
 J=hnf(s.Matrix.hstack(*[lin(M,I[:,i])*J for i in range(n)]));print('I^',k,'index',J.det())
assert J==hnf(7*I)
# Verify norms independently, compute log(u^48) mod 7I
vs=[];ind=[]
for i,(v,norm,logs) in enumerate(r['units']):
 v=s.Matrix(v);assert int(lin(M,v).det(method='domain-ge'))==norm
 a=power(M,v,48,49,one)-one;assert all(z.q==1 for z in Ii*a)
 a2=mulmod(M,a,a,49);a3=mulmod(M,a2,a,49)
 l=(a-pow(2,-1,49)*a2+pow(3,-1,49)*a3).applyfunc(lambda v:int(v)%49)
 w=Ii*l;assert all(z.q==1 for z in w);w=w.applyfunc(lambda z:int(z)%7)
 prev=len(vs)-nullmod(s.Matrix.hstack(*vs),7).cols if vs else 0
 vs.append(w);rank=len(vs)-nullmod(s.Matrix.hstack(*vs),7).cols
 if rank>prev:ind.append(i+1)
 print('unit',i+1,'local rank',rank,'vector',list(w))
print('final rank',rank,'independent indices',ind)
# pairwise test log multiplicativity for all 19*19 pairs, using products mod49
for i,j in itertools.product(range(len(vs)),repeat=2):
 a=mulmod(M,s.Matrix(r['units'][i][0]),s.Matrix(r['units'][j][0]),49);a=power(M,a,48,49,one)-one;a2=mulmod(M,a,a,49);a3=mulmod(M,a2,a,49)
 l=(a-pow(2,-1,49)*a2+pow(3,-1,49)*a3).applyfunc(lambda v:int(v)%49);w=Ii*l;assert all(z.q==1 for z in w);assert all(int(z)%7==0 for z in w-vs[i]-vs[j])
print('pairwise additive checks',len(vs)**2)

