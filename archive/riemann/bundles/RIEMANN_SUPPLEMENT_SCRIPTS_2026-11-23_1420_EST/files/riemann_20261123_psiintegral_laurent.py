"""Independent consistency check of the unconditional classical identity
 Integral_1^infinity (psi(u)-u)/u^2 du = -1-EulerGamma.
The proof is via Re(s)>1 Dirichlet series, PNT zero-free error integrability,
then Laurent series -zeta'/zeta(s)=1/(s-1)-EulerGamma+O(s-1).
Finite-X identity and tests here; do NOT claim numerical finite X proves infinite identity.
"""
import mpmath as mp,json
from pathlib import Path
N=1000000
mp.mp.dps=50
isprime=bytearray(b'\x01')*(N+1);isprime[:2]=b'\x00\x00'
for i in range(2,int(N**.5)+1):
 if isprime[i]:isprime[i*i:N+1:i]=b'\x00'*((N-i*i)//i+1)
# efficient summations with 25 significant digits for speed
with mp.workdps(30):
 events={}
 for p in range(2,N+1):
  if isprime[p]:
   lp=mp.log(p);m=p
   while m<=N:events[m]=lp;m*=p
 checkpoints=(10,100,1000,10000,100000,1000000)
 P=mp.mpf(0);Q=mp.mpf(0);checkpoint=[]
 for n in range(2,N+1):
  if n in events:
   P+=events[n]/n
   Q+=events[n]
  if n in checkpoints:
   integral=P-Q/n-mp.log(n)
   err=integral+(1+mp.euler)
   checkpoint.append({'x':n,'integral':mp.nstr(integral,18),'difference_from_limit':mp.nstr(err,14),
                      'primepower_mass_psi':mp.nstr(Q,16)})
 # independently evaluate a numerical *stepwise* integral of psi on [1,1000]
 # psi(u) step level and integrate psi/u^2 exactly on each step, subtract log(1000)
 upto=1000
 level=mp.mpf(0);J=mp.mpf(0)
 for i in range(1,upto):
  if i in events:level+=events[i]
  J+=level*(mp.mpf(1)/i-mp.mpf(1)/(i+1))
 # endpoint n=1000 contributes measure-zero; partial summation includes 1000 with weight zero
 F_ind=J-mp.log(upto)
 F_direct=mp.fsum((v*(mp.mpf(1)/n-mp.mpf(1)/upto) for n,v in events.items() if n<=upto))-mp.log(upto)
 assert abs(F_ind-F_direct)<mp.mpf('1e-23')
 # numerical near s=1 confirm residue constant only, not proof
 eps=mp.mpf('0.00000001')
 approx=-(mp.diff(mp.zeta,1+eps)/mp.zeta(1+eps))/(1+eps)-1/eps
 target=-1-mp.euler
 assert abs(approx-target)<mp.mpf('1e-6')
 r={'source':'https://mathworld.wolfram.com/MangoldtSummatoryFunction.html','finite_exact_formula':'Integral_1^X (psi(u)-u)/u^2 du = sum_{n<=X}Lambda(n)/n-psi(X)/X-log(X)',
 'infinite_result':'-1-EulerGamma', 'finite_checkpoints':checkpoint,
 'independent_step_integral_1000':mp.nstr(F_ind,25),
 'vs_primepower_formula_1000':mp.nstr(F_direct,25),
 'mellin_laurent_epsilon':str(eps), 'mellin_residue_numeric':mp.nstr(approx,25),
 'claimed_infinite_proof':'Dirichlet series analytic at Re(s)>1; PNT strong error for dominated limit as s down to1; Laurent expansion at1. Requires unconditional zero-free region/PNT input, not RH.',
 'conclusion':'source identity confirmed; no new Riemann proof'}
 out=Path('/mnt/data/riemann_20261123_psiintegral_laurent.json');out.write_text(json.dumps(r,indent=2))
 print(json.dumps(r,indent=2))
