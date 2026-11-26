import sympy as s
z=s.symbols('z');logs={pow(3,j,7):j for j in range(6)}
for q in (79,107,683,907):
 m=q*7;eta=lambda a:int(s.legendre_symbol(a%q,q)); num0=sum(a*eta(a) for a in range(1,q));num2=s.rem(sum(a*eta(a)*z**(logs[a%7]%3) for a in range(1,m) if a%7 and a%q),z*z+z+1,z);num4=s.rem(num2.subs(z,z*z),z*z+z+1,z);prod=s.rem(num2*num4,z*z+z+1,z);Bprod=s.Rational(num0,q)*prod/m**2
 assert Bprod.is_Rational and Bprod<0
 hh=[-Bprod*s.Rational(Q,4) for Q in (1,2)];print(q,'B',Bprod,'hminus candidates',hh,'7-parts',[s.factorint(int(h)).get(7,0) for h in hh]);assert all(h.q==1 for h in hh)
