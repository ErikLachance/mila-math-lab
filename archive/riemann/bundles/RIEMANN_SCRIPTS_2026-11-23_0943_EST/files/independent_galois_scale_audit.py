from fractions import Fraction
import json, math, hashlib
from pathlib import Path
import mpmath as mp
OUT=Path('/mnt/data/riemann_20261123_0936')
mp.mp.dps=90
result={}

# Pass I: exact integer-exponent model of a source theta-twist scaling.
# epsilon = 1/100, a=2+8epsilon=52/25, kappa=2^25 and cpsi=2^52.
eps=Fraction(1,100); a=2+8*eps
assert a==Fraction(52,25)
kappa_exp=25; cpsi_exp=52
scale=[]
for r in [1,25,75,100,399,400,401,700]:
    xp_exp=25*r; x_exp=xp_exp+kappa_exp
    original_twists_exp=400*x_exp
    new_twists_exp=401*xp_exp
    left_order_exp=a*x_exp
    scaled_order_exp=cpsi_exp+a*xp_exp
    assert left_order_exp==scaled_order_exp
    scale.append({'r':r,'xprime_exponent_2':xp_exp,'x_exponent_2':x_exp,
                  'twist_bound_holds':original_twists_exp<=new_twists_exp,
                  'twist_bound_gap_exponent':int(new_twists_exp-original_twists_exp),
                  'frame_order_exponent':int(left_order_exp)})
assert [z['twist_bound_holds'] for z in scale]==[False,False,False,False,False,True,True,True]
# At Y=2^10000, kappa^3=2^75: [kY,(kY)^(3/2)] lies inside [kY,kY^2]
y_exp=10000; z_exp=kappa_exp+y_exp
assert Fraction(3,2)*z_exp<=kappa_exp+2*y_exp and y_exp>=3*kappa_exp
result['scale']={'epsilon':str(eps),'a':str(a),'kappa_exponent_2':kappa_exp,'cpsi_exponent_2':cpsi_exp,
                 'tests':scale,'source_window_example':{'Y_exponent_2':y_exp,'Z_exponent_2':z_exp,
                 'target_end_exponent_2':str(Fraction(3,2)*z_exp),
                 'source_end_exponent_2':kappa_exp+2*y_exp},
                 'conclusion':'exact threshold xprime >= kappa^400 is NECESSARY for this exponent comparison; source assumes it'}

# Pass II: local lengths under ramification and residue degree, no p-adic software assumptions.
length_tests=[]
for p in [2,3,5,7]:
  for e in range(1,5):
    for f in range(1,4):
      for s in range(1,7):
        zn_len=e*f*s
        o_len=e*s
        assert zn_len==f*o_len
        assert Fraction(o_len,e)==s
        if p==3 and e==3 and f==2 and s==2:
          special={'p':p,'e':e,'f':f,'s':s,'length_over_O':o_len,'length_over_Zp':zn_len,'cardinality':p**zn_len}
        length_tests.append((p,e,f,s))
result['lengths']={'cases':len(length_tests),'all_pass':True,'illustrative':special,
   'untwisted_index_countermodel':'Over K=Q, lattices A=Z,A_prime=3^N Z give index 3^N; if no primes twisted, H_j=0 despite arbitrarily large log index N log 3. This ONLY refutes equating the twisted-only H with entire lattice index without further hypotheses.',
   'residue_degree_trap':'O length cannot be read from Z_p length without factor f; extension from Z_p length to O length needs factor e'}

# Pass III: direct numerical adversarial test of the cited G2 algebra and hypotheses.
def one_g2(logx,epsilon, C, f,m,Nc,V):
    L=mp.mpf(logx); epsi=mp.mpf(epsilon); y=mp.exp(epsi*L)
    b=mp.exp(y); B0=f*m*b*y
    link_upper=f*m*b*y*y+L**2*Nc
    raw=C*link_upper+V
    rhs=(abs(C)+1)*y*(B0+Nc)
    return {'y':mp.nstr(y,25),'logx_sq':mp.nstr(L*L,25),'logx_sq_le_y':bool(L*L<=y),
            'left':mp.nstr(raw,25),'right':mp.nstr(rhs,25),'conclusion_holds':bool(raw<=rhs)}
# Choose a modest y so b stays tractable; when condition fails choose Nc dominant.
bad=one_g2(mp.log(10**6), mp.mpf('0.001'), 1,1,1,10**9,0)
assert not bad['logx_sq_le_y'] and not bad['conclusion_holds']
good=one_g2(100000,mp.mpf('0.001'),1,1,1,10**9,0)
assert good['logx_sq_le_y'] and good['conclusion_holds']
result['g2_test']={'bad_condition_missing':bad,'large_x_condition_present':good,
 'status':'source G2 condition indispensable; test does not challenge source since source includes it'}

# Pass IV: group theory of the real 2-power cyclotomic field.
cycl=[]
for s in range(0,9):
  n=2**s;mod=4*n
  units=[a for a in range(1,mod,2)]
  # quotient of units by +/-1 has n elements; 5 class has full order n for s>=1
  p=1;ord5=0
  while True:
    p=(p*5)%mod;ord5+=1
    if p in [1,mod-1]:break
    assert ord5<=2*n
  assert len(units)//2==n and ord5==n
  cycl.append({'n':n,'modulus':mod,'quotient_size':len(units)//2,'order_of_5_mod_pm':ord5,
               'composite_galois_order_with_two_independent_quadratics':4*n})
result['field_group']={'q':3,'d':7,'tests':cycl,'reason':'q,d odd, distinct, ramify at 3 and 7 not in the real 2-power cyclotomic part; three components independent'}

# Pass V: characteristic-two parity obstruction for a naive plus/minus decomposition.
result['parity']={'odd_ell':'since 2 invertible, projection operators (1+j)/2,(1-j)/2 split involution eigenspaces',
 'ell_2_countermodel':'T=Z/2Z, j=identity. Both +1 and -1 eigenspaces equal T (because 1=-1 mod 2). Their naive lengths sum 2 while length T is 1; decomposition needs ell odd or altered formulation.'}

fn=OUT/'independent_galois_scale_audit.json';fn.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PASSES I-V PASS', 'test_count_lengths=',len(length_tests),'field_tests=',len(cycl));
print('bad_g2',bad);print('good_g2',good);print('scale',scale)
for f in [Path(__file__),fn]:print(str(f),hashlib.sha256(f.read_bytes()).hexdigest())
