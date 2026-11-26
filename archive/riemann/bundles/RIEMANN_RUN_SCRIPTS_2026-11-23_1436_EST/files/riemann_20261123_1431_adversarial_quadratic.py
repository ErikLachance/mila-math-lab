from sympy import primerange,isprime,primerange
from math import prod
import json,math
out=[]
for Y in [10,30,100]:
 primes=list(primerange(1,Y+1))
 modulus=8*prod(p for p in primes if p!=2)
 k=1
 while not isprime(1+k*modulus):k+=1
 ell=1+k*modulus
 assert ell%8==1
 symbols={p:pow(p,(ell-1)//2,ell) for p in primes}
 assert all(v==1 for v in symbols.values())
 # by unique factorization, every n<=Y is split +1
 for n in range(1,Y+1):
  assert pow(n,(ell-1)//2,ell)==1
 out.append({"Y":Y,"prime_count":len(primes),"progression_modulus":str(modulus),"k":k,"ell":str(ell),"ell_digits":len(str(ell)),"all_small_prime_legendre_plus":True,"all_n_le_Y_character_plus":True,"signed_prime_power_sum":0})
print(json.dumps(out,indent=2))
open('/mnt/data/riemann_20261123_1431_adversarial_quadratic.json','w').write(json.dumps(out,indent=2))
