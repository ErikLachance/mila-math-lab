import json,math
# Three exact logical nonimplications needed for the supply-on-windows hypothesis H12.
xs=list(range(1,1001)); pairs=('alpha','beta')
B=lambda x,p: p=='alpha'
M=lambda x,p: p=='beta'
C=lambda x,p: True
assert all(any(B(x,p) for p in pairs) and any(M(x,p) for p in pairs) and any(C(x,p) for p in pairs) for x in xs)
assert all(not any(B(x,p) and M(x,p) and C(x,p) for p in pairs) for x in xs)
# For any positive integer x, a point-dependent constant K(x)=x exists;
# no fixed K can bound all x. Finite truncations document growth, analytic proof is unboundedness of integers.
finite_min_K=[max(range(1,N+1)) for N in [10,100,1000,10000]]
assert finite_min_K==[10,100,1000,10000]
# For x>=e^(4*pi), any [log x,1.5 log x] has length>=2*pi,
# hence contains a multiple of 2*pi, where G_toy(e^u)=(e^u)^beta>(e^u)^theta.
# A bounded-ratio window does exist for each n by cos(pi+t)<0 on [0,pi/3].
U_values=[20,50,100,400,1000]
window_tests=[]
for U in U_values:
    k=math.ceil(U/(2*math.pi))
    u=2*math.pi*k
    assert U<=u<=1.5*U
    window_tests.append({'U':U,'x_log_point':u,'interval_end':1.5*U,'cos_at_witness':1.0,'failure_analytic':'G_toy(e^u)=e^(3u/4)>e^(3u/5) at this point'})
out={'source':'Rubinstein v2 §III.11 Hypothesis H12 exact quantifiers, printed pp212-214','nonimplication_1':'(forall x exists pair B(x,p)) AND (forall x exists pair M(x,p)) does not imply forall x exists same pair B and M; two-element pair set gives exact witness','model1_pairs':list(pairs),'model1_values':{'B_valid':['alpha'],'M_valid':['beta'],'C_valid':['alpha','beta']},'model1_checked_points':len(xs),'nonimplication_2':'forall x exists K_x finite does not imply exists uniform K forall x; use required K_x>=x over positive integers','model2_min_K_for_prefixes':finite_min_K,'nonimplication_3':'arbitrarily large isolated x or bounded multiplicative intervals do not imply arbitrarily large power-width [Z,Z^(3/2)] intervals of success','model3_toy':'G_toy(x)=x^(3/4) cos(log x), theta=3/5; G<=0 on [Y_n,e^(pi/3)Y_n] but every sufficiently large [Z,Z^(3/2)] contains x=e^(2*pi*k) where G>x^theta','model3_witnesses':window_tests,'scope':'Simple logical sanity tests, not tests of actual Lean assumptions, not RH disproof.'}
with open('/mnt/data/riemann_20261123_H12_quantifier_models.json','w') as f:json.dump(out,f,indent=2)
print('PASS: disjoint pair witnesses 1000, point-dependent constant prefixes 4, power-window counterwitnesses 5')
