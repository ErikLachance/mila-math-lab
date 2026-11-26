import math,json
from pathlib import Path

def primes_upto(n):
 a=bytearray(b'\x01')*(n+1);a[:2]=b'\x00\x00'
 for p in range(2,math.isqrt(n)+1):
  if a[p]:a[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
 return [i for i in range(n+1) if a[i]]
terms=[];N=1000000
for p in primes_upto(N):
 v=p;k=1
 while v<=N:
  terms.append((v,p,k,math.log(p)))
  if v>N//p:break
  v*=p;k+=1
terms.sort()
def char(p,q):return 0 if p%q==0 else (1 if p%q==1 else -1) if q==3 else (0 if p%2==0 else (1 if p%4==1 else -1))
def S(y,q,include_powers=True):return sum((1-(char(p,q)**k if q else 0))*lp*(1/v-1/y) for v,p,k,lp in terms if v<y and (k==1 or include_powers))

def independent_integral(X,Y,q):
  # piecewise constant step psi - psi_chi, accurate by telescoping integral of 1/u^2
  total=0.0;psigap=0.0;last=X
  for v,p,k,lp in terms:
    if v>X:break
    psigap+=(1-(char(p,q)**k if q else 0))*lp
  for v,p,k,lp in terms:
    if v<=X:continue
    if v>=Y:break
    total+=psigap*(1/last-1/v)
    last=v
    psigap+=(1-(char(p,q)**k if q else 0))*lp
  total+=psigap*(1/last-1/Y)
  return total-math.log(Y/X)

results=[]
for q in [0,3,4]:
 for X,Y in [(100,1000),(1000,10000),(10000,100000),(100000,1000000)]:
  lhs=(S(Y,q)-math.log(Y))-(S(X,q)-math.log(X))
  rhs=independent_integral(X,Y,q)
  assert abs(lhs-rhs)<1e-9,(q,X,Y,lhs,rhs)
  results.append({"q":q,"X":X,"Y":Y,"diff_error_terms":lhs,"integrated_error":rhs,"abs_difference":abs(lhs-rhs),"prime_only_omission_at_Y":S(Y,q)-S(Y,q,False)})
print(json.dumps(results,indent=2))
Path('/mnt/data/riemann_20261123_1431_error_transport.json').write_text(json.dumps(results,indent=2))
