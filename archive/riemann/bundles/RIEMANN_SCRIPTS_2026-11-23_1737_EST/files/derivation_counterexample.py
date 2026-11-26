import json
out=[]
for p in [3,5,7,11,13]:
    def on_gen(power,start=0):
        # Z_p[x_0,...,x_(p-1)], D x_i=x_(i+1) cyclic with multiplier p on wrap
        wraps=(start+power)//p
        return wraps,(start+power)%p
    tests=[]
    for a in [p,p*p,p**3,2*p**3,3*p**3]:
        v,idx=on_gen(a)
        flooronly=a//p
        newbound=a//p+a//(p**3)
        tests.append({'a':a,'monomial':'x_'+str(idx),'coefficient':str(p)+'^'+str(v),'vp':v,'baseline_floor_a_over_p':flooronly,'height_two_proposal':newbound,'height_two_holds':v>=newbound})
    out.append({'p':p,'derivation':f'D(x_i)=x_(i+1) for i< {p-1}; D(x_{p-1})={p}x_0','Dpowp_all_generators':'p times identical generator','Dpowp_modp_is_zero_on_entire_polynomial_ring':True,'tests':tests})
open('/mnt/data/riemann_20261123_1728/derivation_counterexample.json','w').write(json.dumps(out,indent=2))
for case in out:print(case['p'],case['tests'][2])
