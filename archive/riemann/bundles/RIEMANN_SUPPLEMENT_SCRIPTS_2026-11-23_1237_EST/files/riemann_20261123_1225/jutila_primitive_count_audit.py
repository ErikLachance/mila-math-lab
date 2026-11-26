import sympy as s,json
Qmax=500
Pstar={n:int(sum(s.mobius(n//d)*s.totient(d) for d in s.divisors(n))) for n in range(1,Qmax+1)}
assert min(Pstar.values())>=0
bad=[]
for q in range(1,Qmax+1):
    lhs=int(sum(Pstar[d] for d in s.divisors(q)))
    if lhs!=int(s.totient(q)):bad.append((q,lhs,int(s.totient(q))))
assert not bad
weights={n:{'primitive_characters_at_conductor':Pstar[n], 'all_characters_induced_from_conductor_n_up_to_Q':Pstar[n]*(Qmax//n),'repetition_factor':Qmax//n} for n in [1,2,3,4,5,8,12,20,25,100]}
assert Pstar[4]==1 and weights[4]['repetition_factor']==125
# For alpha>=4/5, Euler factors in imprimitive L-functions do not add any zeros in Re(s)>0;
# hence all-character density sum = sum_d floor(Q/d) * primitive character zero counts at conductor d.
res={'source_matched':'Matti Jutila, On Linnik\'s constant, Math. Scand. 41 (1977), p.46, Theorem 1 eqs(1.7),(1.8): N*(alpha,T,Q) ≪_eps (Q^2*T)^((2+eps)*(1-alpha)), 4/5<=alpha<=1, T>=1; N* sums only primitive characters.', 'exact_character_primitive_decomposition_check':{'moduli_checked':Qmax,'failures':bad},'example_Q':Qmax,'examples':weights,'critical_strip_identity':'For 0<alpha<=1 and nontrivial Dirichlet L zeros only, sum over ALL chars mod q <=Q equals sum over conductors d<=Q of floor(Q/d) times sum over PRIMITIVE chars conductor d. No new zeros in Re(s)>0 from finite missing Euler factors.', 'caution':'Replacing the asterisk primitive sum by all characters while keeping the same zero-density exponent is NOT justified without addressing induction multiplicity; this does NOT challenge Jutila or the formal Lean proof. Exact Lean theorem declaration/signature not inspected.'}
with open('/mnt/data/riemann_20261123_1225/jutila_primitive_count_audit.json','w') as f:json.dump(res,f,indent=2)
print(json.dumps(res,indent=2)[:3800])
