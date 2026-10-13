/* ---------- reviewer visuals: tree walk-through, sorters, calculators ---------- */
(function(){
const P=n=>"₱"+Math.round(n).toLocaleString("en-PH");
const num=v=>{const x=parseFloat(String(v).replace(/[^\d.]/g,""));return isFinite(x)?x:0};

/* decision trees: "Full map" / "Walk me through it" */
document.querySelectorAll("#rcontent .tree[data-walk]").forEach(T=>{
  const root=T.querySelector(":scope>ul>li"); if(!root)return;
  const lab=li=>li.querySelector(":scope>.q,:scope>.o"), kids=li=>[...li.querySelectorAll(":scope>ul>li")];
  const edge=li=>{const i=li.querySelector(":scope>i");return i?i.textContent:lab(li).textContent};
  const bar=document.createElement("div");bar.className="vbtns";
  bar.innerHTML='<button type="button" data-m="map" aria-pressed="true">Full map</button><button type="button" data-m="walk" aria-pressed="false">Walk me through it</button>';
  const W=document.createElement("div");W.className="walk";
  T.prepend(bar);T.append(W);
  let hist=[root];
  function render(){
    const li=hist[hist.length-1],L=lab(li),isQ=L.classList.contains("q");
    const crumbs=hist.slice(1).map(x=>`<span>${esc(edge(x))}</span>`).join("");
    let h=crumbs?`<div class="wpath">${crumbs}</div>`:"";
    if(isQ){h+=`<div class="wq">${L.innerHTML}</div><div class="wopts">`+kids(li).map((k,j)=>`<button type="button" data-j="${j}">${esc(edge(k))}</button>`).join("")+"</div>"}
    else h+=`<div class="wout ${L.classList.contains("no")?"no":L.classList.contains("mid")?"mid":""}">${L.innerHTML}</div>`;
    h+=`<div class="wnav">${hist.length>1?'<button type="button" class="ghost" data-nav="back">Back</button><button type="button" class="ghost" data-nav="restart">Start over</button>':""}</div>`;
    W.innerHTML=h;
  }
  W.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;
    if(b.dataset.j!=null){hist.push(kids(hist[hist.length-1])[+b.dataset.j]);render()}
    else if(b.dataset.nav==="back"){hist.pop();render()} else if(b.dataset.nav==="restart"){hist=[root];render()}});
  bar.addEventListener("click",e=>{const b=e.target.closest("[data-m]");if(!b)return;const walk=b.dataset.m==="walk";
    T.classList.toggle("walking",walk);bar.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",x===b));if(walk){hist=[root];render()}});
});

/* sorters: tap a bucket for each item, then see why */
document.querySelectorAll("#rcontent .sorter").forEach(S=>{
  const B=S.dataset.b.split("|"),items=[...S.querySelectorAll(".sit")];
  const sc=document.createElement("div");sc.className="sscore";S.prepend(sc);
  const upd=()=>{const d=items.filter(x=>x.classList.contains("done")),r=d.filter(x=>x.classList.contains("right"));
    sc.innerHTML=`<span>${r.length} right · ${d.length} of ${items.length} answered</span>${d.length?'<button type="button" class="ghost" data-reset>Reset</button>':""}`};
  items.forEach(it=>{const bx=document.createElement("div");bx.className="sbtn";
    bx.innerHTML=B.map((b,j)=>`<button type="button" data-j="${j}">${esc(b)}</button>`).join("");
    it.querySelector("p").after(bx);
    bx.addEventListener("click",e=>{const b=e.target.closest("[data-j]");if(!b||it.classList.contains("done"))return;
      const ok=+b.dataset.j===+it.dataset.a;it.classList.add("done",ok?"right":"wrong");b.classList.add(ok?"ok":"bad");
      if(!ok)bx.querySelector(`[data-j="${it.dataset.a}"]`).classList.add("ok");upd()})});
  sc.addEventListener("click",e=>{if(!e.target.closest("[data-reset]"))return;
    items.forEach(it=>{it.classList.remove("done","right","wrong");it.querySelectorAll(".ok,.bad").forEach(b=>b.classList.remove("ok","bad"))});upd()});
  upd();
});

/* calculators */
const field=(id,label,val,type)=>`<label>${label}<input inputmode="decimal" data-k="${id}" value="${val}"${type?` type="${type}"`:""}></label>`;
const sel=(id,label,opts)=>`<label>${label}<select data-k="${id}">${opts.map(([v,t])=>`<option value="${v}">${t}</option>`).join("")}</select></label>`;
const seg=(parts)=>`<div class="cbar">${parts.filter(p=>p[1]>0).map(([lab,w,c])=>`<i style="width:${w}%;background:${c}" title="${esc(lab)}">${w>=12?esc(lab):""}</i>`).join("")}</div><div class="ckey">${parts.filter(p=>p[1]>0).map(([lab,,c])=>`<span style="--k:${c}">${esc(lab)}</span>`).join("")}</div>`;
const hb=rows=>{const mx=Math.max(1,...rows.map(r=>r[1]));return `<div class="bars" style="margin:10px 0 6px">${rows.map(([lab,v,c,txt])=>{const w=Math.max(0,100*v/mx);return `<div class="bar" style="--vc:${c}"><span>${esc(lab)}</span><div style="--v:${w.toFixed(1)}"><i></i><b${w>70?' class="in"':""}>${txt}</b></div></div>`}).join("")}</div>`};
const CALC={
  fifth:{
    html:`<div class="crow">${field("prop","Donor's present property (₱)","5,000,000")}${field("don","Donation to the future spouse (₱)","2,000,000")}</div>
      <div class="crow">${sel("reg","Regime in the settlement",[["cpg","Conjugal partnership of gains"],["sep","Complete separation"],["oth","Other regime"],["acp","Absolute community"]])}${sel("ms","Where is the donation made?",[["in","In the marriage settlement"],["out","Separate deed, in view of the marriage"]])}</div><div class="cout"></div>`,
    run(v){const cap=v.prop/5,d=v.don;
      if(v.reg==="acp")return `<b>No ⅕ cap</b> (Art. 84 applies only to a regime <em>other than</em> ACP). The donation still cannot exceed what the donor may give by will, and cannot impair legitimes (NCC 752, 771).`+seg([["Donation",Math.min(100,100*d/v.prop),"var(--good)"],["Rest of property",Math.max(0,100-100*d/v.prop),"var(--line)"]]);
      const ok=Math.min(d,cap),ex=Math.max(0,d-cap);
      let s=`Cap = ⅕ × ${P(v.prop)} = <b>${P(cap)}</b>.<br>Valid: <b>${P(ok)}</b> · Void excess: <b>${P(ex)}</b>`+(ex?" (only the excess is void; the donation stands up to ⅕).":" (within the cap).")+
        seg([["Valid part",100*ok/v.prop,"var(--good)"],["Void excess",100*ex/v.prop,"var(--bad)"],["Untouched",Math.max(0,100-100*d/v.prop),"var(--line)"]]);
      if(v.ms==="out")s+=`<br><small><strong>Text vs. Tolentino:</strong> Art. 84 caps donations "in their marriage settlements", so a separate deed is literally outside the cap. Tolentino would still apply ⅕ to any donation made in view of the marriage. On Sir's quizzes, follow the codal.</small>`;
      return s}},
  art120:{
    html:`<div class="crow">${field("val","Value of the separate property when improved (₱)","5,000,000")}${field("cost","Cost of the improvement (₱)","3,000,000")}${field("inc","Resulting increase in value (₱)","1,000,000")}</div><div class="cout"></div>`,
    run(v){const L=v.cost+v.inc,R=v.val,tot=L+R||1,conj=L>R;
      return `Cost + increase = <b>${P(L)}</b> vs. value of the property = <b>${P(R)}</b>.<br>`+
      (conj?`The improvement side is bigger, so the <strong>entire property becomes conjugal</strong>, and the owner-spouse is reimbursed <b>${P(R)}</b> (the property's value at the time of the improvement).`
           :`The property side is ${L===R?"not smaller":"bigger"}, so the <strong>owner-spouse keeps the entire property</strong>, and the partnership is reimbursed the cost of the improvement, <b>${P(v.cost)}</b>.`)+
      seg([["Improvement + increase",100*L/tot,"var(--good)"],["Separate property",100*R/tot,"var(--accent)"]])+
      `<small>Either way, ownership vests only upon reimbursement at liquidation (Art. 120, 2nd par.).${L===R?" On a tie the text keeps the property with the owner-spouse (\"more than\" is required).":""}</small>`}},
  netprofit:{
    html:`<div class="crow">${field("m0","Market value of the community at the wedding (₱)","75,000")}${field("m1","Market value at dissolution (₱)","225,000")}${field("debts","Community debts paid at liquidation (₱)","125,000")}</div><div class="cout"></div>`,
    run(v){const codal=Math.max(0,v.m1-v.m0),net=v.m1-v.debts,tol=net-v.m0,mx=Math.max(codal,Math.abs(tol),1);
      return `<strong>Codal formula (Art. 102(4)):</strong> ${P(v.m1)} − ${P(v.m0)} = <b>${P(codal)}</b> forfeitable net profits.<br>`+
      `<strong>Tolentino's formula:</strong> net assets ${P(net)} − ${P(v.m0)} = <b>${tol>0?P(tol):"no net profits ("+P(tol)+" loss)"}</b>.`+
      hb([["Codal formula",codal,"var(--accent)",P(codal)],["Tolentino",Math.max(tol,0),"var(--good)",tol>0?P(tol):"none"]])+
      `<small>On Sir's quizzes use the codal formula (increase in market value). Tolentino's version deducts the debts first.</small>`}},
  doubleprop:{
    html:`<div class="crow">${field("c1","First wife's capital (₱)","5,000")}${field("y1","First marriage (years)","4")}</div>
      <div class="crow">${field("c2","Second wife's capital (₱)","3,000")}${field("y2","Second marriage (years)","7")}</div>
      <div class="crow">${field("mass","Total mass at the husband's death (₱)","10,000")}</div><div class="cout"></div>`,
    run(v){const conj=v.mass-v.c1-v.c2;if(conj<=0)return "The capitals exceed the total mass; there is no conjugal property to divide.";
      const w1=v.c1*v.y1,w2=v.c2*v.y2,s1=conj*w1/(w1+w2||1),s2=conj-s1;
      return `Conjugal remainder = ${P(v.mass)} − ${P(v.c1+v.c2)} capital = <b>${P(conj)}</b>.<br>Weights: ${P(v.c1)} × ${v.y1} = ${w1.toLocaleString("en-PH")} and ${P(v.c2)} × ${v.y2} = ${w2.toLocaleString("en-PH")}.<br>`+
      `First partnership: <b>${P(s1)}</b> · Second partnership: <b>${P(s2)}</b>. Each is then halved between the husband's estate and the wife (or her heirs), and each wife gets her capital back.`+
      seg([["1st partnership",100*s1/conj,"var(--accent)"],["2nd partnership",100*s2/conj,"var(--good)"]])+
      `<small>Tolentino's "double proportion" for Art. 131 when there is no proof which partnership owns what. With equal years it reduces to the ratio of the capitals.</small>`}},
};
document.querySelectorAll("#rcontent .calc[data-calc]").forEach(C=>{
  const def=CALC[C.dataset.calc];if(!def)return;
  const box=document.createElement("div");box.innerHTML=def.html;C.append(box);
  const go=()=>{const v={};box.querySelectorAll("[data-k]").forEach(x=>v[x.dataset.k]=x.tagName==="SELECT"?x.value:num(x.value));box.querySelector(".cout").innerHTML=def.run(v)};
  box.addEventListener("input",go);go();
});
})();
