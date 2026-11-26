from fractions import Fraction
import json,math
# If A(u)=sum_{d<=u} primitive_zero_count(d), then S(Q)=sum_{q<=Q} all_char_zeros(q)=sum_d floor(Q/d) primitive_zero_count(d)=sum_{k<=Q} A(floor(Q/k)).
# This exact identity arises by conductor-induction, because removed Euler factors have no zero for Re(s)>0.
def both_counts(a,Q):
    direct=sum((Q//d)*a.get(d,0) for d in range(1,Q+1))
    layer=sum(sum(a.get(d,0) for d in range(1,Q//k+1)) for k in range(1,Q+1))
    return direct,layer
res=[]
for Q in [4,12,100,1000,10000]:
    # Fictitious single primitive character with ONE zero at conductor 4: valid as a counting countermodel, not a claim about chi4 actual zeros.
    a={4:1}
    s1,s2=both_counts(a,Q)
    assert s1==s2==Q//4
    res.append({'Q':Q,'A_primitive':1,'S_all_char':s1,'ratio_all_over_primitive':s1})
regimes=[]
for alpha in [Fraction(4,5),Fraction(9,10),Fraction(99,100)]:
    eps=Fraction(1,10);a=(2+eps)*(1-alpha);b=2*a
    regimes.append({'alpha':str(alpha),'eps':str(eps),'primitive_exponent_Q':str(b),'loss_exponent_Q_if_b_lt_1':str(max(Fraction(0),1-b)),'status':'b<1' if b<1 else 'b>=1'})
assert all(Fraction(item['primitive_exponent_Q'])<1 for item in regimes)
result={'source':'M. Jutila On Linnik\'s constant Math Scand 41 (1977) theorem 1 eq (1.8) is PRIMITIVE summed over q<=Q, not all characters','exact_induction_count_identity':'S_all(Q)=sum_d<=Q floor(Q/d)*a_d = sum_k<=Q A_prim(floor(Q/k)); a_d primitive zero-count at conductor d','single_nonzero_conductor_countermodel':res,'transfer_exponent_regimes':regimes,'upper_bound_deduction':'If A_prim(U) <= C*(U^2*T)^a with a=(2+eps)(1-alpha), then S_all(Q) <= C*(Q^2*T)^a*sum_{k<=Q}k^(-2a). For 2a<1 this is O(C*Q*T^a), not O(C*Q^(2a)*T^a) without other input. For 2a=1 add logQ; for 2a>1 no power loss.','qualification':'The single conductor toy assigns a fictitious zero; it is an exact combinatorial countermodel to an illegitimate inference, not a statement that real Dirichlet characters have zeros off critical line. Source eq(1.7) separately bounds all characters for ONE fixed modulus q; check whether the archive uses (1.7) or (1.8) before drawing any conclusion about source fidelity.'}
with open('/mnt/data/riemann_20261123_1225/jutila_induction_transfer.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
