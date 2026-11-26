/* Exact finite certificates and rational bounds; Node.js, no dependencies.
   See notes/pnp-tseitin.md, notes/beal-local-points.md, notes/riemann-intervals.md. */
function check(c,m){if(!c)throw Error(m)}

function tseitin(){
 const edges=[];for(let a=0;a<4;a++)for(let b=a+1;b<4;b++)edges.push([a,b]);
 function generators(charges){
  const rows=[];
  for(let v=0;v<4;v++){
   const inc=edges.flatMap((e,i)=>e.includes(v)?[i]:[]),local=inc.flatMap(i=>[2*i,2*i+1]),outside=Array.from({length:12},(_,i)=>i).filter(i=>!local.includes(i));
   for(let a=0;a<64;a++){
    let flux=0,positive=0,negative=0;
    for(let j=0;j<3;j++)flux+=(edges[inc[j]][0]===v?1:-1)*((a>>(2*j))&3);
    if(((flux-charges[v])%4+4)%4===0)continue;
    for(let j=0;j<6;j++)if(a&(1<<j))positive|=1<<local[j];else negative|=1<<local[j];
    const monomials=[];let sub=negative;while(true){monomials.push(positive|sub);if(!sub)break;sub=(sub-1)&negative;}
    rows.push({v,local_assignment:a,monomials,outside});
   }
  }
  return rows;
 }
 function span(rows,degree){
  const basis=new Map(),labels=[],vectors=[];
  function insert(vec,i){let combination=1n<<BigInt(i);while(vec){const p=vec.toString(2).length-1,r=basis.get(p);if(r){vec^=r.vec;combination^=r.combination}else{basis.set(p,{vec,combination});return}}}
  for(let i=0;i<rows.length;i++)for(const bit of degree===6?[-1]:[-1,...rows[i].outside]){
   let vec=0n;for(const m of rows[i].monomials)vec^=1n<<BigInt(bit<0?m:m|(1<<bit));
   const j=labels.length;labels.push({generator:i,multiplier_bit:bit});vectors.push(vec);insert(vec,j);
  }
  let target=1n,combination=0n;while(target){const p=target.toString(2).length-1,r=basis.get(p);if(!r)break;target^=r.vec;combination^=r.combination;}
  const cert=[];let v=0n;if(!target){for(let i=0;i<labels.length;i++)if((combination>>BigInt(i))&1n){cert.push(labels[i]);v^=vectors[i];}check(v===1n,"certificate mismatch")}
  return {degree,row_count:labels.length,rank:basis.size,contains_constant:target===0n,certificate:cert};
 }
 const results=[];
 for(let c=1;c<=3;c++){const charges=[c,0,0,0],rows=generators(charges),d6=span(rows,6),d7=c===2?span(rows,7):null;check(rows.length===192,"generator count");check(d6.contains_constant===(c!==2),"degree6 expected");if(d7)check(d7.contains_constant,"degree7 expected");results.push({charges,generators:rows.length,degree6:d6,degree7:d7,minimum_static_degree:c===2?7:6})}
 return {edges,bit_encoding:"edge i: low bit 2i; high bit 2i+1; flow outgoing minus incoming",results,scope:"static degree-truncated monomial-multiple span in Boolean quotient, not a general polynomial calculus lower bound"};
}

function localCubics(){
 const O=[1n,0n,0n],B=[0n,1n,0n],B2=[0n,0n,1n],p3=[-2n,2n,1n],p5d=[-2n,-1n,0n],p5s=[-5n,-1n,-1n],p11=[1n,3n,1n],eps=[26n,15n,2n];
 function mul(a,b){const v=Array(5).fill(0n);for(let i=0;i<3;i++)for(let j=0;j<3;j++)v[i+j]+=a[i]*b[j];for(let i=4;i>=3;i--){v[i-1]-=4n*v[i];v[i-2]-=9n*v[i];v[i-3]-=15n*v[i]}return v.slice(0,3)}
 function pow(a,k){let b=O;for(let i=0;i<k;i++)b=mul(b,a);return b}
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a}
 const exps=[[3,0,0],[2,1,0],[2,0,1],[1,2,0],[1,1,1],[1,0,2],[0,3,0],[0,2,1],[0,1,2],[0,0,3]],basis=[O,B,B2];
 function coeffs(H){const c=Array(10).fill(0n);for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let k=0;k<3;k++){const e=[0,0,0];e[i]++;e[j]++;e[k]++;c[exps.findIndex(f=>f.every((v,i)=>v===e[i]))]+=mul(H,mul(basis[i],mul(basis[j],basis[k])))[2]}const d=c.reduce(gcd,0n);return c.map(v=>v/d)}
 function* pts(q,p){for(let y=0;y<q;y++)for(let z=0;z<q;z++)yield [0,[1,y,z]];for(let x=0;x<q;x+=p)for(let z=0;z<q;z++)yield [1,[x,1,z]];for(let x=0;x<q;x+=p)for(let y=0;y<q;y+=p)yield [2,[x,y,1]]}
 function value(c,x,der=-1){let r=0n;for(let i=0;i<10;i++){let e=exps[i].slice(),v=c[i];if(der>=0){if(!e[der])continue;v*=BigInt(e[der]);e[der]--}for(let j=0;j<3;j++)v*=BigInt(x[j])**BigInt(e[j]);r+=v}return r}
 function vp(n,p){if(!n)return 999;let k=0;while(n%p===0n){n/=p;k++}return k}
 const primes=[2,5,7,11,13,17,19,23,29,31,37,41,43],rows=[];
 for(const u of [1,5])for(const delta of u===1?[1,3,5,11,15,33,55,165]:[1,3,11,33])for(let k=0;k<3;k++){
  let H=O;for(const [p,a] of [[3,p3],[5,p5d],[11,p11]])if(delta%p===0)H=mul(H,a);if(u===5)H=mul(H,pow(p5s,11));H=mul(H,pow(eps,k));const c=coeffs(H);
  let count=0,witness=null;
  function hensel(fixed,x,v){for(let j=0;j<3;j++)if(j!==fixed){const w=value(c,x,j);if(w!==0n&&vp(v,3n)>2*vp(w,3n))return {point:x,fixed_coordinate:fixed,derivative_coordinate:j,F:v.toString(),derivative:w.toString(),v3_F:vp(v,3n)===999?"infinity":vp(v,3n),v3_derivative:vp(w,3n)}}return null}
  for(const [fixed,x] of pts(27,3)){const v=value(c,x);if(v%27n!==0n)continue;count++;if(!witness)witness=hensel(fixed,x,v)}
  if(count&&!witness)for(const [fixed,x] of pts(81,3)){const v=value(c,x);if(v%81n)continue;witness=hensel(fixed,x,v);if(witness)break}
  const other=[];for(const p of primes){const m=BigInt(p);let found=null;for(const [fixed,x] of pts(p,p)){if(value(c,x)%m)continue;for(let j=0;j<3;j++)if(j!==fixed&&value(c,x,j)%m!==0n){found={prime:p,point:x,fixed_coordinate:fixed,derivative_coordinate:j};break}if(found)break}check(found,"smooth witness absent "+[u,delta,k,p]);other.push(found)}
  rows.push({u,delta,k,coefficients:c.map(String),N27:count,hensel3:witness,other_prime_witnesses:other});
 }
 check(rows.length===36,"36");check(rows.filter(r=>!r.N27).length===9,"9 exclusions");check(rows.filter(r=>r.hensel3).length===27,"27 Q3 points");
 return {curves:36,excluded_over_Q3:9,certified_Q3_points:27,other_primes:primes,rows,scope:"local points on explicit cubics, not global rational points or proof of Beal"};
}

function spectralConstants(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const f=(n,d=1)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]};
 const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
 const sq=a=>mul(a,a),one=f(1),two=f(2);
 function atanInv(q,n){let s=f(0),p=f(1,q),r=sq(p);for(let k=0;k<n;k++){let t=div(p,f(2*k+1));s=add(s,k%2?neg(t):t);p=mul(p,r)}let t=div(p,f(2*n+1));return n%2?[sub(s,t),s]:[s,add(s,t)]}
 const a5=atanInv(5,28),a239=atanInv(239,12),pi=[sub(mul(f(16),a5[0]),mul(f(4),a239[1])),sub(mul(f(16),a5[1]),mul(f(4),a239[0]))];
 function logUnit(x){let z=div(sub(x,one),add(x,one)),r=sq(z),p=z,s=f(0);for(let k=0;k<28;k++){s=add(s,div(p,f(2*k+1)));p=mul(p,r)}s=mul(two,s);return [s,add(s,div(mul(two,p),mul(f(57),sub(one,r))))]}
 const l2=logUnit(two);
 function log(x){check(cmp(x,one)>=0n,"log domain");let k=0;while(cmp(x,two)>0n){x=div(x,two);k++}let l=logUnit(x);return [add(l[0],mul(f(k),l2[0])),add(l[1],mul(f(k),l2[1]))]}
 function isqrt(n){let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));while(true){let y=(x+n/x)/2n;if(y>=x)return x;x=y}}
 function sqrt(n){const S=10n**20n,r=isqrt(BigInt(n)*S*S);return [f(r,S),f(r+1n,S)]}
 const l3=log(f(3)),l5=log(f(5)),r2=sqrt(2),r3=sqrt(3),r5=sqrt(5);
 const A=add(add(mul(r2[1],l2[1]),div(mul(two,l3[1]),r3[0])),add(l2[1],div(mul(two,l5[1]),r5[0])));
 const L=f(81,100),T=f(596),eta=f(17,1000),X=mul(mul(two,L),T);
 check(cmp(l5[1],mul(two,L))<0n&&cmp(log(f(6))[0],mul(two,L))>0n,"prime cutoff");
 let H=f(0);for(let i=1;i<=512;i++)H=add(H,f(1,i));
 // Euler-Maclaurin bounds: H_n-log n-1/(2n) < gamma < same+1/(12n^2).
 const gamma=sub(add(sub(H,f(1,1024)),f(1,12*512*512)),log(f(512))[0]);
 const beta=sub(sub(log(div(T,mul(two,pi[1])))[0],div(one,T)),A);
 const M=add(A,add(gamma,add(div(pi[1],two),add(mul(f(3),l2[1]),log(pi[1])[1]))));
 const trace=div(X,pi[0]),variance=div(add(add(gamma,log(mul(two,X))[1]),add(one,div(two,X))),sq(pi[0]));
 function hyperbolic(x,odd){let s=f(0),p=odd?x:one,r=sq(x),k=odd?1:0;for(let i=0;i<16;i++){s=add(s,p);p=div(mul(p,r),f((k+1)*(k+2)));k+=2}let ratio=div(r,f((k+1)*(k+2)));return add(s,div(p,sub(one,ratio)))}
 const sh=hyperbolic(div(L,two),true),ch=div(hyperbolic(div(L,two),false),two);
 const pole=mul(div(f(4),pi[0]),add(add(mul(sq(sh),add(div(one,mul(two,T)),div(one,mul(mul(two,L),sq(T))))),div(mul(sh,ch),mul(two,sq(T)))),div(sq(ch),mul(f(3),mul(T,sq(T))))));
 check(cmp(beta,f(16918,100000))>0n,"beta");check(cmp(M,f(975369,100000))<0n,"M");check(cmp(trace,f(30734,100))<0n,"trace");check(cmp(variance,f(928,1000))<0n,"variance");check(cmp(pole,f(186,1000000))<0n,"pole");
 const om=sub(one,eta),idx=add(f(30734,100),div(f(928,1000),eta)),margin=sub(sub(mul(om,f(16918,100000)),mul(eta,f(975369,100000))),div(mul(two,f(186,1000000)),om));
 check(cmp(idx,f(362))<0n&&cmp(margin,f(1,10000))>0n,"final bounds");
 function out(x,up){const S=10n**12n,n=x[0]*S;let v=n/x[1];if(up&&n%x[1])v++;return v.toString()+"/1000000000000"}
 return {prime_powers:[2,3,4,5],beta_lower:out(beta,false),M_upper:out(M,true),trace_upper:out(trace,true),variance_upper:out(variance,true),pole_tail_upper:out(pole,true),index_upper:idx.map(String).join("/"),margin_lower:margin.map(String).join("/"),scope:"rational enclosures for fixed-window spectral argument, using stated analytic inequalities"};
}

const result={tseitin:tseitin(),beal_local:localCubics(),riemann_constants:spectralConstants()};
console.log(JSON.stringify(result,null,2));
