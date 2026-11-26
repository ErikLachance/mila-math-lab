/* Independent reconstructions and targeted extensions. Node.js, standard library only. */
function check(c,m){if(!c)throw Error(m)}

function rationalMatrixTest(){
 const abs=n=>n<0n?-n:n, gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a},lcm=(a,b)=>a/gcd(a,b)*b;
 const zero=(n,m)=>Array.from({length:n},()=>Array(m).fill(0n));
 function strassen(){return {dims:[2,2,2],U:[[1,0,0,1],[0,0,1,1],[1,0,0,0],[0,0,0,1],[1,1,0,0],[-1,0,1,0],[0,1,0,-1]],V:[[1,0,0,1],[1,0,0,0],[0,1,0,-1],[-1,0,1,0],[0,0,0,1],[1,1,0,0],[0,0,1,1]],W:[[1,0,0,1,-1,0,1],[0,0,1,0,1,0,0],[0,1,0,1,0,0,0],[1,-1,1,0,0,1,0]]}}
 function classical(a,b,c){const U=[],V=[],W=Array.from({length:a*c},()=>[]);for(let i=0;i<a;i++)for(let j=0;j<c;j++)for(let k=0;k<b;k++){const r=U.length;U.push(Array.from({length:a*b},(_,t)=>Number(t===i*b+k)));V.push(Array.from({length:b*c},(_,t)=>Number(t===k*c+j)));for(let t=0;t<a*c;t++)W[t][r]=Number(t===i*c+j)}return {dims:[a,b,c],U,V,W}}
 function scale(menu){
  const r=menu.U.length,s=Array.from({length:r},(_,i)=>[BigInt((i%2?-1:1)*(i%5+1)),BigInt(i%3+2)]),t=Array.from({length:r},(_,i)=>[BigInt(i%7+1),BigInt(i%4+2)]);
  function fraction(n,d){if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]}
  const Ur=menu.U.map((row,i)=>row.map(x=>fraction(BigInt(x)*s[i][0],s[i][1]))),Vr=menu.V.map((row,i)=>row.map(x=>fraction(BigInt(x)*t[i][0],t[i][1]))),Wr=menu.W.map(row=>row.map((x,i)=>fraction(BigInt(x)*s[i][1]*t[i][1],s[i][0]*t[i][0])));
  function clear(rows){const d=rows.flat().reduce((z,x)=>lcm(z,x[1]),1n);return [rows.map(row=>row.map(([n,q])=>n*(d/q))),d]}
  const [U,du]=clear(Ur),[V,dv]=clear(Vr),[W,dw]=clear(Wr),D=du*dv*dw;
  const [a,b,c]=menu.dims;
  for(let u=0;u<a*b;u++)for(let v=0;v<b*c;v++)for(let w=0;w<a*c;w++){
   let x=0n;for(let k=0;k<r;k++)x+=W[w][k]*U[k][u]*V[k][v];
   const i=Math.floor(u/b),k=u%b,k2=Math.floor(v/c),j=v%c;check(x===(k===k2&&w===i*c+j?D:0n),"base tensor identity");
  }
  const maxrow=M=>M.reduce((z,row)=>{const s=row.reduce((a,b)=>a+abs(b),0n);return s>z?s:z},1n);
  return {dims:menu.dims,U,V,W,du,dv,dw,D,A:maxrow(U),B:maxrow(V),C:maxrow(W),rank:r};
 }
 let state=20261126;function rand(){state=(Math.imul(state,1664525)+1013904223)>>>0;return BigInt(state)}
 function sample(i,j,M,mode){if(mode===0)return ((rand()<<32n)|rand())%(2n*M+1n)-M;if(mode===1)return 0n;if(mode===2)return (i+j)%2?-M:M;return (i*5+j*7)%11===0?M:0n}
 function naive(X,Y){const Z=zero(X.length,Y[0].length);for(let i=0;i<X.length;i++)for(let k=0;k<Y.length;k++)for(let j=0;j<Y[0].length;j++)Z[i][j]+=X[i][k]*Y[k][j];return Z}
 const details=[];let total=0,totalDiv=0,totalLeaf=0,maximumBits=0;
 for(const raw of [strassen(),classical(2,3,2),classical(2,2,3),classical(3,2,2)]){
  const menu=scale(raw),[a,b,c]=menu.dims,{U,V,W,A,B,C,D,rank}=menu;let tests=0,divisions=0,leaves=0,maxBits=0;
  for(let h=1;h<=3;h++)for(const bits of [8,40])for(let mode=0;mode<4;mode++){
   const M=(1n<<BigInt(bits))-1n,H=M*M*C*(A*B*BigInt(b))**BigInt(h);let peak=0n;
   function track(v){const n=abs(v);if(n>peak)peak=n;check(n<=H,"magnitude guard");return v}
   function mix(blocks,weights,rows,cols){const Z=zero(rows,cols);for(let k=0;k<blocks.length;k++){const w=weights[k];if(!w)continue;for(let i=0;i<rows;i++)for(let j=0;j<cols;j++)Z[i][j]=track(Z[i][j]+track(w*blocks[k][i][j]));}return Z}
   function split(X,n,m,rr,cc){return Array.from({length:n*m},(_,k)=>Array.from({length:rr},(_,i)=>X[Math.floor(k/m)*rr+i].slice(k%m*cc,k%m*cc+cc)))}
   function rec(X,Y,d){if(!d){leaves++;return [[track(X[0][0]*Y[0][0])]]}
    const ar=a**(d-1),br=b**(d-1),cr=c**(d-1),xs=split(X,a,b,ar,br),ys=split(Y,b,c,br,cr);
    const ps=Array.from({length:rank},(_,r)=>rec(mix(xs,U[r],ar,br),mix(ys,V[r],br,cr),d-1));
    const out=zero(a*ar,c*cr);
    for(let k=0;k<a*c;k++){const z=mix(ps,W[k],ar,cr);for(let i=0;i<ar;i++)for(let j=0;j<cr;j++){check(z[i][j]%D===0n,"inexact normalization");divisions++;out[Math.floor(k/c)*ar+i][k%c*cr+j]=track(z[i][j]/D)}}
    return out;
   }
   const X=Array.from({length:a**h},(_,i)=>Array.from({length:b**h},(_,j)=>sample(i,j,M,mode))),Y=Array.from({length:b**h},(_,i)=>Array.from({length:c**h},(_,j)=>sample(i,j,M,mode)));
   const Z=rec(X,Y,h),E=naive(X,Y);check(Z.every((row,i)=>row.every((v,j)=>v===E[i][j])),"matrix mismatch");
   maxBits=Math.max(maxBits,peak===0n?0:peak.toString(2).length);tests++;
  }
  details.push({dimensions:menu.dims,rank,integer_denominators:[menu.du,menu.dv,menu.dw].map(String),row_norms:[A,B,C].map(String),tests,divisions,leaf_multiplications:leaves,max_intermediate_bits:maxBits});
  total+=tests;totalDiv+=divisions;totalLeaf+=leaves;maximumBits=Math.max(maximumBits,maxBits);
 }
 return {tests:total,exact_divisions:totalDiv,leaf_multiplications:totalLeaf,maximum_intermediate_bits:maximumBits,all_pass:true,details,scope:"fixed tested identities only; general lemma proved in note, no PIT transfer claimed"};
}

function rationalRootTest(){
 const abs=a=>a<0n?-a:a,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a};
 function vp(a,p){if(!a)return Infinity;let v=0;while(a%p===0n){a/=p;v++}return v}
 function P(n,m){return 165n*n*n*n-440n*n*n*m+396n*n*m*m-120n*m*m*m}
 function Q(n,m){const q=[1n,4n,10n,20n,35n,56n,84n,120n];return q.reduce((s,x,i)=>s+x*n**BigInt(7-i)*m**BigInt(i),0n)}
 let coprime=0,c2=0,c3=0,identity=0;
 for(let n=1n;n<=128n;n++)for(let m=-128n;m<=128n;m++){if(gcd(n,m)!==1n)continue;coprime++;const p=P(n,m);check(n**11n===m**8n*p+(n-m)**4n*Q(n,m),"polynomial identity");identity++;
 if(n%2n===0n){check(vp(p,2n)===3,"2 valuation");check(vp(m**8n*p,2n)-11*vp(n,2n)===3-11*vp(n,2n),"2 rational valuation");c2++}
 if(n%3n===0n){check(vp(p,3n)===1,"3 valuation");c3++}
 }
 const fractionHalf={numerator:"1",denominator:"2",reason:"v2=-1, not 3 mod 11"};
 return {coprime_pairs:coprime,polynomial_identity_checks:identity,even_denominator_checks:c2,three_divides_denominator_checks:c3,excluded_target:fractionHalf,all_pass:true,scope:"necessary restrictions on the rational-root method, not on all solutions of the original equation"};
}

function carlemanIllustration(){
 function simpson(fn,a,b,n){let sum=fn(a)+fn(b),h=(b-a)/n;for(let i=1;i<n;i++)sum+=(i%2?4:2)*fn(a+i*h);return sum*h/3}
 const witnesses=[2,5,10,20,40,80].map(T=>({T,quotient:simpson(s=>(1-s/(2*T))/Math.cosh(s/2),0,2*T,Math.ceil(2*T*100)*2)}));
 check(witnesses.every((w,i)=>w.quotient<Math.PI&&(!i||w.quotient>witnesses[i-1].quotient)),"illustration trend");
 const kernel=[1e-2,1e-3,1e-4,1e-5,1e-6].map(s=>({s,remainder:-Math.exp(-s/2)/(-Math.expm1(-2*s))+1/(2*s)}));
 return {witnesses,kernel,limit:Math.PI,half_limit:Math.PI/2,scope:"floating quadrature illustration only; proof in analytic note"};
}

console.log(JSON.stringify({matrix:rationalMatrixTest(),rational_root:rationalRootTest(),carleman:carlemanIllustration()},null,2));
