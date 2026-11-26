from fractions import Fraction as Q
from itertools import product
import json,hashlib
from pathlib import Path
out=Path('/mnt/data/riemann_20261123_0936')

# Derived from Rubinstein III.9 equations III.258 and III.259.
# L=log x, y=x^eps>=L^2, b=exp(y), B0=f*m*b*y.
# To test algebra without transcendental rounding, treat y,L,b as positive
# rational parameters satisfying the SAME inequalities required in G2.
passed=0; tight=0; failures=[]; examples=[]
for L,y,b,C,f,m,Nc,D0 in product([Q(1),Q(2),Q(3),Q(5)], [Q(1),Q(4),Q(9),Q(25),Q(100)],
  [Q(1),Q(2),Q(11)], [Q(0),Q(1),Q(2),Q(5)], [Q(1),Q(3)], [Q(1),Q(4)], [Q(0),Q(5)], [Q(1),Q(3)]):
    if L*L>y:continue
    B0=f*m*b*y
    source_budget=y*(B0+Nc)+C*(y-L*L)*Nc
    assert source_budget>=b
    link_base=C*(f*m*b*y*y+L*L*Nc)
    target=(C+1)*y*(B0+Nc)
    assert link_base+source_budget==target
    assert link_base+source_budget+b/Q(100000)>target
    # If V<=b this is source's coarser sufficient input.
    assert link_base+b<=target
    passed+=1
    if source_budget==b:tight+=1
    if len(examples)<8 and L==Q(2) and y==Q(9) and C==Q(2):
       examples.append({'L':str(L),'y':str(y),'b':str(b),'f':str(f),'m':str(m),'Nc':str(Nc),
            'original_G_requirement_V_le':str(b),'relaxed_exact_budget':str(source_budget),'slack_factor':str(source_budget/b)})
# Even for fixed theta<1 V<=b^theta far below V~b*y² on x-scale.
res={'pass_count':passed,'all_exact':True,'tight_source_budget_equals_b':tight,'examples':examples,
 'derived_maximal_cohomology_budget':'For C>=0, V <= y(B0+Nc)+C(y-(log x)^2)Nc is the SHARP sufficient V-budget given saturation of LinkN and target bound, with B0=f*m*b*y and y>=(log x)^2.',
 'source_G_assumption':'Theorem G gives V<=sqrt(b); source Proposition G2 only needs V<=b. The exact algebraic allowance can be as large as f*m*b*y^2 when Nc=0. No assertion that a weaker global Galois theorem has been established.',
 'limitation':'This only tests implication LinkN+V bound=>III.259; obtaining LinkN and any uniform V bound for actual fields remains a difficult theorem.'}
file=out/'denominator_budget_exact.json';file.write_text(json.dumps(res,indent=2)+'\n')
print('PASS',passed,'budget equal b cases',tight)
print('EXAMPLE',examples[0])
for f in [Path(__file__),file]:print(str(f),hashlib.sha256(f.read_bytes()).hexdigest())
