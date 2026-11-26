/* Historical checkpoint rechecks, 2026-11-26. Node.js, no dependencies. */
function assert(c,m){if(!c)throw Error(m)}

function envelopeCheck(){
 const cmp=(x,y)=>x[0]*y[1]-y[0]*x[1];
 const max=(...xs)=>xs.reduce((x,y)=>cmp(x,y)>=0?x:y);
 const min=(x,y)=>cmp(x,y)<=0?x:y;
 const U=(...args)=>{const [x,y,z]=args.sort((a,b)=>b-a);if(z*(x+y)<=x*y)return [x+y,1];return [(x*y+y*z+z*x)**2,4*x*y*z]};
 let tested=0,equalities=[];
 for(let d=2;d<=72;d++)for(let a=0;a<=d;a++)for(let b=0;b<=d-a;b++)for(let bp=0;bp<=d-a-b;bp++){
  const c=d-a-b-bp;
  if(3*(a+b)<=d||3*(a+b)>2*d||3*(a+bp)<=d||3*(a+bp)>2*d)continue;
  const E=min(max(U(a,b,c),U(a,bp,c),[a+c,1]),max(U(b,a,bp),U(b,c,bp),[b+bp,1]));
  const A=Math.max(a,c),B=Math.max(b,bp),t=Math.min(a,c,b,bp);
  assert(cmp(E,U(A,B,t))===0,"reduction mismatch");
  const r=72*E[0]-49*d*E[1];
  assert(r<=0,"formal bound violated");
  if(r===0){assert(2*a===d&&6*b===d&&6*bp===d&&6*c===d,"unexpected equality profile");equalities.push([a,b,bp,c]);}
  tested++;
 }
 return {d_min:2,d_max:72,admissible_quadruples:tested,equality_profiles:equalities,all_pass:true,scope:"formal envelope, not bit complexity"};
}

function ncCheck(){
 const n=8192,perm=[5,3,1,4,6,7,0,2],pairs=[[2,0],[3,1],[2,3],[5,3],[6,5],[6,0],[8,6],[9,8],[10,9],[11,4]];
 const inverse=new Int32Array(n).fill(-1);
 for(let x=0;x<n;x++){let y=perm[x&7];for(let i=3;i<13;i++){const [a,b]=pairs[i-3];y|=(((x>>i)^((x>>a)&(x>>b)))&1)<<i}assert(inverse[y]===-1,"not bijective");inverse[y]=x}
 const vec=fn=>BigInt("0b"+Array.from({length:n},(_,i)=>fn(n-1-i)?"1":"0").join(""));
 const ys=Array.from({length:13},(_,i)=>vec(y=>(y>>i)&1));
 function rank(h,k){const vs=[...ys,vec(y=>h[y])],basis=new Map();function insert(v){while(v){const p=v.toString(2).length;if(basis.has(p))v^=basis.get(p);else{basis.set(p,v);return}}}
 const all=(1n<<BigInt(n))-1n;function visit(start,rem,v){insert(v);if(rem)for(let i=start;i<14;i++)visit(i+1,rem-1,v&vs[i]);}visit(0,k,all);return basis.size;}
 const hFor=(g,triple)=>Array.from(inverse,x=>(g>>triple.reduce((s,j,i)=>s+(((x>>j)&1)<<i),0))&1);
 const masks=[0,2,4,8,16,5,10,18,12,20,21,14];
 const B=Array.from({length:n},(_,y)=>masks.reduce((v,m)=>v^Number((y&m)===m),0));
 const cases=[];
 for(const [g,expected] of [[60,24],[105,32],[150,44],[195,36]]){
  const h=hFor(g,[2,8,12]),a=h.map((v,y)=>v&B[y]);
  for(let i=0;i<13;i++)for(let y=0;y<n;y++)if(y&(1<<i))a[y]^=a[y^(1<<i)];
  const terms=a.flatMap((v,m)=>v?[m]:[]);
  assert(terms.length===expected&&terms.every(m=>m.toString(2).replace(/0/g,"").length<=4),"degree-four witness mismatch");
  for(let y=0;y<n;y++)assert(terms.reduce((v,m)=>v^Number((y&m)===m),0)===(h[y]&B[y]),"witness fails");
  const r=rank(h,3);assert(r===470,"degree-three rank mismatch");cases.push({g,degree_le_3_rank:r,witness_terms:terms.length,minimum_degree:4});
 }
 const h=hFor(23,[10,11,12]);for(let y=0;y<n;y++)assert(!(h[y]&&((y>>9)&1)&&((y>>10)&1)&&((y>>12)&1)&&!((y>>8)&1)),"degree-five witness fails");
 const r=rank(h,4);assert(r===1471,"degree-four rank mismatch");
 return {outputs:n,cases,extra:{g:23,tail:[10,11,12],degree_le_4_rank:r,minimum_degree:5},scope:"one fixed triangular generator, no general lower bound"};
}

function kummerCheck(){
 const one=[1n,0n,0n],p3=[-2n,2n,1n],p5d=[-2n,-1n,0n],p5s=[-5n,-1n,-1n],p11=[1n,3n,1n],eps=[26n,15n,2n];
 const mul=(a,b)=>{const [x,y,z]=a,[v,w,k]=b,T=y*k+z*w,U=z*k;return [x*v-15n*T+60n*U,x*w+y*v-9n*T+21n*U,x*k+y*w+z*v-4n*T+7n*U]};
 function pow(a,k){let v=one;for(let i=0;i<k;i++)v=mul(v,a);return v}
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
 const G0=[1,0,0,0,-90,180,-15,180,-315,105].map(BigInt),G1=[0,3,0,0,-54,63,-9,63,-9,-42].map(BigInt),G2=[0,0,3,3,-24,21,-4,21,-21,25].map(BigInt);
 const points=[];for(let y=0;y<27;y++)for(let z=0;z<27;z++)points.push([1,y,z]);for(let x=0;x<27;x+=3)for(let z=0;z<27;z++)points.push([x,1,z]);for(let x=0;x<27;x+=3)for(let y=0;y<27;y+=3)points.push([x,y,1]);assert(points.length===1053,"projective enumeration");
 const rows=[];
 for(const u of [1,5])for(const d of (u===1?[1,3,5,11,15,33,55,165]:[1,3,11,33]))for(let k=0;k<3;k++){
  let H=one;for(const [p,a] of [[3,p3],[5,p5d],[11,p11]])if(d%p===0)H=mul(H,a);if(u===5)H=mul(H,pow(p5s,11));H=mul(H,pow(eps,k));const [a,b,c]=H;
  const raw=G0.map((v,i)=>c*v+(b-4n*c)*G1[i]+(a-4n*b+7n*c)*G2[i]);const g=raw.reduce(gcd,0n);assert(g>0n,"zero cubic");const coeff=raw.map(v=>v/g);const m=coeff.map(v=>Number((v%27n+27n)%27n));let count=0;
  for(const [x,y,z] of points){const mon=[x*x*x,x*x*y,x*x*z,x*y*y,x*y*z,x*z*z,y*y*y,y*y*z,y*z*z,z*z*z];if(mon.reduce((s,v,i)=>s+v*m[i],0)%27===0)count++}
  rows.push({u,delta:d,k,N27:count,coefficients:coeff.map(String)});
 }
 const eliminated=rows.filter(r=>!r.N27);assert(rows.length===36&&eliminated.length===9,"obstruction count");assert(eliminated.every(r=>(r.u===1&&r.delta===33)||(r.u===5&&[3,33].includes(r.delta))),"branch mismatch");
 return {cubics:rows.length,residue_classes_per_cubic:points.length,excluded:eliminated.length,not_excluded_mod27:27,rows,scope:"specified auxiliary cubics only; rational-root and descent premises unproved here"};
}

function riemannCheck(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
 const F=(n,d=1)=>{n=BigInt(n);d=BigInt(d);const g=gcd(n,d);return [n/g,d/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const sub=(a,b)=>add(a,[-b[0],b[1]]);
 const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
 const repr=a=>a.map(String).join("/");
 const eta=F(17,1000),oneMinus=sub(F(1),eta),beta=F(16918,100000),M=F(975369,100000),trace=F(30734,100),variance=F(928,1000),leak=F(186,1000000);
 const index=add(trace,div(variance,eta)),margin=sub(sub(mul(oneMinus,beta),mul(eta,M)),div(mul(F(2),leak),oneMinus));
 assert(cmp(index,F(362))<0n,"index arithmetic");
 assert(cmp(margin,F(1,10000))>0n,"margin arithmetic");
 return {index_upper_bound:repr(index),index_decimal:Number(index[0])/Number(index[1]),net_margin_lower_bound:repr(margin),margin_decimal:Number(margin[0])/Number(margin[1]),scope:"exact final inequalities conditional on recorded spectral premises; full analytic certificate not independently reproduced"};
}

const result={formal_envelope:envelopeCheck(),finite_generator:ncCheck(),beal_auxiliary_cubics:kummerCheck(),riemann_rational_arithmetic:riemannCheck()};
console.log(JSON.stringify(result,null,2));
