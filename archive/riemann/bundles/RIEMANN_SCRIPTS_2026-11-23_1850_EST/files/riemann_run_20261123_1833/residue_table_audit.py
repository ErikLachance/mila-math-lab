"""Independent exact modular arithmetic verification of the worked q=11,
d=1319, N=16 residue-class table in Rubinstein's 22 Nov 2026
zeta guide Part II sec. 4.1. It also tests a textual sign error.
All are exact finite calculations, not a proof of RH.
"""
import json

def prime(n):
  if n<2: return False
  return all(n%d for d in range(2,int(n**.5)+1))
def leg(a,p):
  a%=p
  if a==0: return 0
  t=pow(a,(p-1)//2,p)
  assert t in (1,p-1)
  return 1 if t==1 else -1
q,d,N=11,1319,16
assert prime(q) and prime(d)
assert q%8==3 and d%16==7 and (d+1)%q==0
squares_q={k*k%q for k in range(1,q)}
assert squares_q=={1,3,4,5,9}
rows={(row,col):[] for row in (0,1) for col in (1,3,5,7)}
for p in range(3,62,2):
  if not prime(p) or p in (q,d): continue
  if leg(p,d)==1: continue
  row=(1+leg(p,q))//2
  col=min(p%N,(-p)%N)
  assert col in (1,3,5,7)
  rows[(row,col)].append(p)
expected={(0,1):[17],(0,3):[13,29,61],(0,5):[],(0,7):[41],(1,1):[47],(1,3):[],(1,5):[37,59],(1,7):[23]}
assert rows==expected,(rows,expected)
# Prose sentence says (1+chi)/2 is 1 for nonsquare, but the formula
# and computed table imply the opposite. q=11, p=13: chi=-1 and row=0.
assert leg(13,11)==-1 and (1+leg(13,11))//2==0
assert leg(23,11)==1 and (1+leg(23,11))//2==1
print(json.dumps({'primes_verified':[q,d],'worked_table_exactly_matches':True,'prime_cells':{f'{r},{c}':ls for (r,c),ls in sorted(rows.items())},'exposition_error':'Formula v=(1+chi_q)/2 gives row 1 for quadratic residues, not nonresidues; first sentence after formula says the reverse. Table remains correct.','not_RH_proof':True},indent=2))
