from fractions import Fraction
import random, json, math
from pathlib import Path

root=Path('/mnt/data/riemann_20261123_0751')
rng=random.Random(20261123)

def gauss_mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def gauss_minus(a,b):
    return (a[0]-b[0],a[1]-b[1])

def sq(a): return a[0]*a[0]+a[1]*a[1]

rows=[]
for j in range(600):
    M=[(rng.randint(-4,4),rng.randint(-4,4)) for _ in range(4)]
    delta=gauss_minus(gauss_mul(M[0],M[3]),gauss_mul(M[1],M[2]))
    D=sq(delta)
    if D==0: continue
    T=sum(map(sq,M))
    disc=T*T-4*D
    assert disc>=0,(M,T,D,disc)
    lammax=(T+math.sqrt(disc))/2
    ratio=lammax/math.sqrt(D)
    assert ratio>=1-1e-12
    rows.append((M,T,D,ratio,disc))
assert len(rows)>=570
# Simple scalar maps: equality, and anisotropic maps strict.
examples=[]
for a,b in ((1,1),(2,2),(1,3),(2,9),(3,7),(10,100)):
    T=a*a+b*b;D=(a*b)**2
    lammax=(T+math.sqrt(T*T-4*D))/2
    ratio=lammax/math.sqrt(D)
    assert abs(ratio - max(a,b)/min(a,b))<1e-10
    examples.append({'a':a,'b':b,'slope_shift':-math.log(a*b),'height':math.log(max(a*a,b*b)),'slack':math.log(ratio),'ratio':ratio})
# Bad 'all images' inference: 1d images of e_1 don't span target lattice Z e_1 + N Z e_2.
# Target slope mu=-0.5*log(N) in ordinary Z Euclidean norm normalization.
# Mean slope cannot be bounded from many short rank-one maps unless their images span.
nonspan=[]
for N in (2,10,1000,10**9):
    target_mu=-math.log(N)/2
    image_spans_target=False
    hypothetical_bad_claim=0<=target_mu
    assert not hypothetical_bad_claim
    nonspan.append({'N':N,'target_mu':target_mu,'maps':'all 1 -> (1,0)','image_rank':1,'target_rank':2,'hypothetical_mean_slope_bound_valid':False})

report={'Q_i_normalization':'rank r=2, n0=2, base Z[i]^2 covolume 1, mu=-ln |det_complex phi|; ht=ln ||phi||_op^2','exact_identity':'T=sum(|a_ij|^2), D=|det(phi)|^2, discriminant T^2-4D>=0; lambda_max=(T+sqrt(discriminant))/2; mu(phi Lambda)+ht(phi)-mu(Lambda)=ln(lambda_max/sqrt(D)) >= 0', 'nonzero_random_gaussian_matrices':len(rows),'minimum_ratio':min(x[3] for x in rows),'maximum_ratio':max(x[3] for x in rows),'scalar_and_anisotropic_examples':examples,'nonspanning_rank_one_warning':nonspan,'status':'simple 2x2 number field toy check; no audit of high rank Arakelov theorem or RH proof'}
with (root/'gaussian_lattice_slope_audit.json').open('w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
