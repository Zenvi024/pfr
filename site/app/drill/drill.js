
/* ================= DRILL: spaced review, codal blanks, spot the change, grids ================= */
const CLOZE = __CLOZE__;
const ALTER = __ALTER__;
const GRIDS = __GRIDS__;
const MIN = 60000;
const STEPS = [1, 10, 60, 360, 1440, 2880, 5760]; // minutes
const STEP_LBL = ["1 min","10 min","1 hr","6 hr","1 day","2 days","4 days"];
let SRS = store.get("pfr_srs", {});
function saveSRS(){ store.set("pfr_srs", SRS); updateDueBadge(); }

/* ---- card registry ---- */
const CARDS = {};
DATA.forEach(q => CARDS["q:"+q.i] = {k:"q:"+q.i, ty:"q", t:q.t, q});
CLOZE.forEach(c => CARDS["c:"+c.id] = {k:"c:"+c.id, ty:"c", t:c.topic, c});
ALTER.forEach(a => CARDS["a:"+a.id] = {k:"a:"+a.id, ty:"a", t:a.topic, a});
GRIDS.forEach(g => g.rows.forEach((r, ri) => g.cols.forEach((col, ci) => {
  const k = `g:${g.id}:${ri}:${ci}`;
  CARDS[k] = {k, ty:"g", t: r.topic || g.topic, g, ri, ci};
})));
const TYPE_NAME = {q:"Quiz items", c:"Codal blanks", a:"Spot the change", g:"Grid cells"};

/* ---- scheduling ---- */
function rate(k, grade){ // 0 again, 1 hard, 2 good, 3 easy
  const now = Date.now(), st = SRS[k] || {s:-1, n:0, l:0};
  if (grade === 0){ st.s = 0; st.l++; }
  else if (grade === 1){ st.s = Math.max(st.s, 0); }
  else if (grade === 2){ st.s = Math.min(Math.max(st.s + 1, 1), STEPS.length - 1); }
  else { st.s = Math.min(Math.max(st.s + 2, 3), STEPS.length - 1); }
  const mins = grade === 1 ? Math.max(5, STEPS[st.s] / 2) : STEPS[st.s];
  st.d = now + mins * MIN; st.n++;
  SRS[k] = st; saveSRS();
}
function preview(k, grade){ // label of interval each button would give
  const st = SRS[k] || {s:-1};
  let s = st.s;
  if (grade === 0) s = 0; else if (grade === 1) s = Math.max(s, 0); else if (grade === 2) s = Math.min(Math.max(s + 1, 1), STEPS.length-1); else s = Math.min(Math.max(s + 2, 3), STEPS.length-1);
  if (grade === 1) return (Math.max(5, STEPS[s] / 2) >= 60 ? Math.round(STEPS[s]/120)+" hr" : Math.max(5, STEPS[s]/2)+" min");
  return STEP_LBL[s];
}
function isDue(k){ const s = SRS[k]; return s && s.d <= Date.now(); }
function dueCount(filter){ return Object.keys(SRS).filter(k => CARDS[k] && isDue(k) && (!filter || filter(CARDS[k]))).length; }
function updateDueBadge(){
  const n = dueCount();
  let b = $("tabDrill") && $("tabDrill").querySelector(".dueBadge");
  if (b){ b.textContent = n; b.hidden = n === 0; }
  const s = $("srsHint"); if (s) s.textContent = n ? `${n} card${n===1?"":"s"} due in Drill` : "";
}
setInterval(updateDueBadge, 30000);

/* quiz answers feed the scheduler */
const _record = record;
record = function(q, i){ _record(q, i); rate("q:"+q.i, i === q.a ? 2 : 0); };

/* ---- answer normalization for typed cards ---- */
const NUMW = {zero:0,one:1,two:2,three:3,four:4,five:5,six:6,seven:7,eight:8,nine:9,ten:10,eleven:11,twelve:12,thirteen:13,fourteen:14,fifteen:15,sixteen:16,seventeen:17,eighteen:18,nineteen:19,twenty:20,"twenty-one":21,"twenty-four":24,"twenty-five":25,thirty:30,first:"1st",second:"2nd",third:"3rd",fourth:"4th",fifth:"5th"};
function norm(s){
  s = String(s).toLowerCase().replace(/[‘’]/g,"'").replace(/[“”]/g,'"').replace(/\(\s*\d+\s*\)/g," ").replace(/[.,;:!?"()]/g," ");
  s = s.split(/\s+/).filter(Boolean).map(w => NUMW[w] !== undefined ? String(NUMW[w]) : w).join(" ");
  s = s.replace(/\b(\d+)(st|nd|rd|th)\b/g, "$1");
  return s.split(" ").filter(w => !/^(days?|years?|months?|hours?|consecutive)$/.test(w)).join(" ").trim();
}
function typedOK(input, answers){ const v = norm(input); return v.length > 0 && answers.some(a => norm(a) === v); }

/* ---- diff for alteration cards ---- */
function diffRange(o, t){ // returns [ostart,oend,tstart,tend) for the single changed region
  let i = 0; while (i < o.length && i < t.length && o[i] === t[i]) i++;
  let j = 0; while (j < o.length - i && j < t.length - i && o[o.length-1-j] === t[t.length-1-j]) j++;
  return [i, o.length - j, i, t.length - j];
}
ALTER.forEach(a => { a.ot = a.original.split(/\s+/); a.tt = a.altered.split(/\s+/); a.r = diffRange(a.ot, a.tt); });

/* ---- drill state ---- */
let dmode = "review";
let dsel = new Set(store.get("pfr_dtopics", [...sel]));
let dtypes = new Set(store.get("pfr_dtypes", ["q","c","a","g"]));
const MODE = {
  review:{title:"Spaced review", blurb:"Mixed cards from every drill: quiz items, codal blanks, altered provisions and grid cells. Cards you miss come back in a minute; cards you know move out to hours, then days. Do a round whenever the due count is above zero.", types:null},
  cloze:{title:"Codal blanks", blurb:"Type the missing word of the provision. These are the words that change the legal result: periods, ages, who may act, which effect follows.", types:["c"]},
  spot:{title:"Spot the change", blurb:"One word or phrase of the provision has been altered so the statement becomes false. Tap the word that was changed. If words were removed, tap the word next to the gap.", types:["a"]}
};
function activeTypes(){ return MODE[dmode].types || [...dtypes]; }
function inFilter(c){ return dsel.has(c.t) && activeTypes().includes(c.ty); }

function renderDSetup(){
  ["dsetup","dcard","ddone","dgrids"].forEach(id => $(id).hidden = true);
  document.querySelectorAll("#dmodes button").forEach(b => b.setAttribute("aria-pressed", b.dataset.m === dmode));
  if (dmode === "grids"){ $("dgrids").hidden = false; renderGridList(); return; }
  $("dsetup").hidden = false;
  $("dTitle").textContent = MODE[dmode].title; $("dBlurb").textContent = MODE[dmode].blurb;
  $("dtypesWrap").hidden = dmode !== "review";
  const all = Object.values(CARDS).filter(inFilter);
  const due = all.filter(c => isDue(c.k)).length;
  const learning = all.filter(c => SRS[c.k] && !isDue(c.k)).length;
  const fresh = all.filter(c => !SRS[c.k]).length;
  $("dstats").innerHTML = `<div class="dstat due"><b>${due}</b><span>Due now</span></div><div class="dstat"><b>${learning}</b><span>Scheduled later</span></div><div class="dstat"><b>${fresh}</b><span>Not yet seen</span></div>`;
  $("dtopics").innerHTML = TOPICS.map(([k,n,a]) => {
    const cnt = Object.values(CARDS).filter(c => c.t === k && activeTypes().includes(c.ty)).length;
    return `<label class="chip${dsel.has(k)?" on":""}" for="dt_${k}"><input type="checkbox" id="dt_${k}" data-t="${k}" ${dsel.has(k)?"checked":""}><span><b>${esc(n)}</b><br><em>${a} · ${cnt} cards</em></span></label>`;
  }).join("");
  $("dtypes").innerHTML = Object.entries(TYPE_NAME).map(([k,n]) => `<label class="chip${dtypes.has(k)?" on":""}" for="dy_${k}"><input type="checkbox" id="dy_${k}" data-y="${k}" ${dtypes.has(k)?"checked":""}><span>${n} <em>${Object.values(CARDS).filter(c=>c.ty===k).length}</em></span></label>`).join("");
  $("dstart").textContent = due ? `Start: ${due} due + up to ${$("dnew").value} new` : `Start with ${Math.min(fresh, +$("dnew").value)} new cards`;
  $("dstart").disabled = !due && !fresh;
  store.set("pfr_dtopics", [...dsel]); store.set("pfr_dtypes", [...dtypes]);
}
$("dmodes").addEventListener("click", e => { const b = e.target.closest("[data-m]"); if (!b) return; dmode = b.dataset.m; renderDSetup(); });
$("dtopics").addEventListener("change", e => { const t = e.target.dataset.t; if (!t) return; e.target.checked ? dsel.add(t) : dsel.delete(t); renderDSetup(); });
$("dtypes").addEventListener("change", e => { const y = e.target.dataset.y; if (!y) return; e.target.checked ? dtypes.add(y) : dtypes.delete(y); renderDSetup(); });
$("dpresets").innerHTML = PRESETS.map(p => `<button class="ghost dpre" data-p="${p.id}">${esc(p.name)}</button>`).join("");
$("dpresets").onclick = e => { const b = e.target.closest("[data-p]"); if (!b) return; dsel = new Set(PRESETS.find(p => p.id === b.dataset.p).topics); renderDSetup(); };
$("dnew").onchange = renderDSetup;

/* ---- session ---- */
let DQ = [], dcur = null, dstats = {seen:0, right:0, again:0}, answered = false, lastGrade = null;
function startRound(){
  const all = Object.values(CARDS).filter(inFilter);
  const due = all.filter(c => isDue(c.k)).sort((a,b) => SRS[a.k].d - SRS[b.k].d);
  const fresh = shuffle(all.filter(c => !SRS[c.k])).slice(0, +$("dnew").value);
  DQ = interleave(due, fresh);
  if (!DQ.length){ renderDSetup(); return; }
  dstats = {seen:0, right:0, again:0, total:DQ.length};
  ["dsetup","ddone","dgrids"].forEach(id => $(id).hidden = true); $("dcard").hidden = false;
  nextCard();
}
function interleave(a, b){ const out = []; let i = 0, j = 0; while (i < a.length || j < b.length){ if (i < a.length) out.push(a[i++]); if (i < a.length) out.push(a[i++]); if (j < b.length) out.push(b[j++]); } return out; }
$("dstart").onclick = startRound;
$("dagain").onclick = startRound;
$("dback").onclick = renderDSetup;
$("dend").onclick = endRound;
function endRound(){
  $("dcard").hidden = true; $("ddone").hidden = false;
  const left = Object.values(CARDS).filter(c => inFilter(c) && isDue(c.k)).length;
  const soon = Object.values(CARDS).filter(c => inFilter(c) && SRS[c.k] && !isDue(c.k) && SRS[c.k].d - Date.now() <= 15*MIN).length;
  $("ddoneTxt").textContent = `${dstats.seen} cards answered, ${dstats.right} right the first time you saw them this round, ${dstats.again} sent back for another look. ${left ? left + " cards are due again now." : soon ? soon + " cards come back within 15 minutes; start another round then." : "Nothing is due right now; come back when the Drill tab shows a count."}`;
}
function nextCard(){
  if (!DQ.length){ endRound(); return; }
  dcur = DQ.shift(); answered = false; lastGrade = null;
  $("dreveal").hidden = true; $("drate").hidden = true; $("dreveal").innerHTML = ""; $("drate").innerHTML = "";
  const c = dcur, isNew = !SRS[c.k];
  $("dprog").textContent = `${dstats.seen + 1} · ${DQ.length} left in round`;
  $("dtags").innerHTML = `<span class="tag">${TYPE_NAME[c.ty]}</span><span class="tag">${esc(TNAME[c.t] || "")}</span>${isNew ? '<span class="tag new">New</span>' : ""}${c.ty==="q" ? `<span class="tag ${c.q.o}">${ONAME[c.q.o]}</span>` : ""}`;
  ({q:renderQCard, c:renderCCard, a:renderACard, g:renderGCard})[c.ty](c);
  const f = $("dbody").querySelector("input,button"); if (f && c.ty === "c") f.focus();
}
function showRate(correct){
  answered = true;
  const k = dcur.k;
  if (!correct){
    $("drate").className = "rate one"; $("drate").hidden = false;
    $("drate").innerHTML = `<button class="primary" data-g="0">Continue <small style="color:inherit">back in ${preview(k,0)}</small></button>` + (dcur.ty === "c" ? `<button class="override" data-g="2">My answer was right. Count it.</button>` : "");
  } else {
    $("drate").className = "rate"; $("drate").hidden = false;
    $("drate").innerHTML = [["Again",0,"again"],["Hard",1,""],["Good",2,"good"],["Easy",3,""]].map(([n,g,cl]) => `<button class="${cl}" data-g="${g}">${n}<small>${preview(k,g)}</small></button>`).join("");
  }
  $("drate").scrollIntoView({block:"nearest", behavior:"smooth"});
}
$("drate").addEventListener("click", e => {
  const b = e.target.closest("[data-g]"); if (!b) return;
  const g = +b.dataset.g; rate(dcur.k, g);
  dstats.seen++; if (g >= 1 && !dcur._missed) dstats.right++;
  if (g === 0){ dstats.again++; dcur._missed = true; DQ.splice(Math.min(3, DQ.length), 0, dcur); }
  nextCard();
});
document.addEventListener("keydown", e => {
  if ($("drillTab").hidden || $("dcard").hidden) return;
  if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;
  if (answered && /^[1-4]$/.test(e.key)){ const b = $("drate").querySelectorAll("[data-g]")[+e.key - 1]; if (b) b.click(); }
  else if (answered && (e.key === "Enter" || e.key === " ")){ e.preventDefault(); const b = $("drate").querySelector(".good,.primary"); if (b) b.click(); }
  else if (!answered && dcur && (dcur.ty === "q" || (dcur.ty === "g" && dcur.g.cols[dcur.ci].t === "pick"))){ const i = "abcdefgh".indexOf(e.key.toLowerCase()); const b = $("dbody").querySelectorAll(".choice")[i]; if (b) b.click(); }
});

/* quiz item card */
function renderQCard(c){
  const q = c.q, stem = q.q || (q.y === "pair" ? CONFIG.pairInstruction : "");
  $("dbody").innerHTML = `${stem ? `<p class="stem">${esc(stem)}</p>` : ""}${q.st ? `<div class="stmts">${q.st.map(s => `<p>${esc(s)}</p>`).join("")}</div>` : ""}<div class="choices" style="margin-top:12px">${q.c.map((ch,i) => `<button class="choice" data-i="${i}"><span class="L">${q.y==="tf"?"":LETTERS[i]+"."}</span><span>${esc(ch)}</span></button>`).join("")}</div>`;
  $("dbody").querySelector(".choices").onclick = e => {
    const b = e.target.closest("[data-i]"); if (!b || answered) return;
    const i = +b.dataset.i, ok = i === q.a;
    $("dbody").querySelectorAll(".choice").forEach((x,j) => { x.disabled = true; if (j === q.a) x.classList.add("right"); else if (j === i) x.classList.add("wrong"); });
    const h = history[q.i] || {n:0}; h.n++; h.r = ok ? 1 : 0; history[q.i] = h; store.set("pfr_hist", history);
    $("dreveal").hidden = false; $("dreveal").innerHTML = feedbackHTML(q, i);
    showRate(ok);
  };
}
/* codal blank card */
function renderCCard(c){
  const x = c.c, m = x.text.match(/^([\s\S]*)\[\[([\s\S]+?)\]\]([\s\S]*)$/);
  const ans = m[2], w = Math.max(6, Math.min(28, ans.length + 2));
  $("dbody").innerHTML = `<div class="artlbl">${esc(x.art)}</div><p class="cz">${esc(m[1])}<input id="czIn" size="${w}" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Missing word">${esc(m[3])}</p><div class="row" style="margin-top:10px"><button class="primary" id="czCheck">Check</button><button class="ghost" id="czShow">Show answer</button></div>`;
  const check = give => {
    if (answered) return;
    const v = $("czIn").value, ok = !give && typedOK(v, [ans, ...(x.accept || [])]);
    const p = $("dbody").querySelector(".cz");
    p.innerHTML = `${esc(m[1])}<span class="ans ${ok?"ok":"no"}">${esc(ans)}</span>${esc(m[3])}`;
    $("dbody").querySelector(".row").remove();
    $("dreveal").hidden = false;
    $("dreveal").innerHTML = `<div class="expl"><div class="verdict ${ok?"ok":"no"}">${ok ? "Correct." : give ? "Answer shown." : `Not quite. You wrote “${esc(v)}”.`}</div>${x.why ? `<p>${esc(x.why)}</p>` : ""}</div>`;
    showRate(ok);
  };
  $("czCheck").onclick = () => check(false); $("czShow").onclick = () => check(true);
  $("czIn").addEventListener("keydown", e => { if (e.key === "Enter"){ e.preventDefault(); check(false); } });
}
/* spot the change card */
function renderACard(c){
  const a = c.a, [o1,o2,t1,t2] = a.r;
  $("dbody").innerHTML = `<div class="artlbl">${esc(a.art)}</div><p class="prompt">One word or phrase was changed. Tap it.</p><div class="toks" id="tk">${a.tt.map((w,i) => `<button data-i="${i}">${esc(w)}</button>`).join("")}</div><button class="ghost" id="tkGive" style="justify-self:start">I can't find it</button>`;
  const finish = i => {
    if (answered) return;
    const ok = i !== null && (t1 < t2 ? (i >= t1 && i < t2) : (i === t1 - 1 || i === t1));
    const marked = a.tt.map((w,j) => `<button disabled class="${j>=t1&&j<t2?"chg":""}${j===i?" pick":""}">${esc(w)}</button>`).join("");
    const orig = a.ot.map((w,j) => `<button disabled class="${j>=o1&&j<o2?"ins":""}">${esc(w)}</button>`).join("");
    $("dbody").innerHTML = `<div class="artlbl">${esc(a.art)}</div><div class="cmp"><div><div class="lbl">Altered</div><div class="toks">${marked}</div></div><div><div class="lbl">Codal</div><div class="toks">${orig}</div></div></div>`;
    $("dreveal").hidden = false;
    $("dreveal").innerHTML = `<div class="expl"><div class="verdict ${ok?"ok":"no"}">${ok ? "Found it." : i === null ? "Here is the change." : "That word is unchanged."}</div><p>${esc(a.why || "")}</p></div>`;
    showRate(ok);
  };
  $("tk").onclick = e => { const b = e.target.closest("[data-i]"); if (b) finish(+b.dataset.i); };
  $("tkGive").onclick = () => finish(null);
}
/* grid cell card */
function colPool(g, ci){ const seen = new Set(); g.rows.forEach(r => { const v = r.c[ci]; if (typeof v === "string") seen.add(v); }); return [...seen]; }
function renderGCard(c){
  const g = c.g, r = g.rows[c.ri], col = g.cols[c.ci], v = r.c[c.ci];
  const head = `<div class="artlbl">${esc(g.src)}</div><p class="stem">${esc(r.h)}</p><p class="prompt">${esc(g.title)} · <strong>${esc(col.h)}</strong></p>`;
  if (col.t === "num"){
    $("dbody").innerHTML = head + `<div class="row"><input id="gIn" style="font:inherit;padding:8px 10px;border-radius:7px;border:1px solid var(--line);background:var(--surface);color:var(--ink);width:140px" autocomplete="off" aria-label="Answer"><button class="primary" id="gChk">Check</button></div>`;
    const chk = () => { if (answered) return; const ok = typedOK($("gIn").value, v); $("dreveal").hidden = false; $("dreveal").innerHTML = `<div class="expl"><div class="verdict ${ok?"ok":"no"}">${ok?"Correct.":"Not quite."} Answer: ${esc(v[0])}</div></div>`; $("gChk").disabled = true; $("gIn").disabled = true; showRate(ok); };
    $("gChk").onclick = chk; $("gIn").addEventListener("keydown", e => { if (e.key === "Enter"){ e.preventDefault(); chk(); } }); setTimeout(() => $("gIn").focus(), 0);
  } else {
    let opts = colPool(g, c.ci).filter(o => o !== v);
    // borrow distractors from the same column of other grids if the column is small
    opts = shuffle(opts).slice(0, 4); opts = shuffle([v, ...opts]);
    $("dbody").innerHTML = head + `<div class="choices">${opts.map((o,i) => `<button class="choice" data-i="${i}"><span class="L">${LETTERS[i]}.</span><span>${esc(o)}</span></button>`).join("")}</div>`;
    $("dbody").querySelector(".choices").onclick = e => {
      const b = e.target.closest("[data-i]"); if (!b || answered) return;
      const i = +b.dataset.i, ok = opts[i] === v;
      $("dbody").querySelectorAll(".choice").forEach((x,j) => { x.disabled = true; if (opts[j] === v) x.classList.add("right"); else if (j === i) x.classList.add("wrong"); });
      $("dreveal").hidden = false; $("dreveal").innerHTML = `<div class="expl"><div class="verdict ${ok?"ok":"no"}">${ok?"Correct.":"Not quite."}</div></div>`;
      showRate(ok);
    };
  }
}

/* ---- grids view ---- */
let curGrid = null;
function renderGridList(){
  if (!curGrid) curGrid = GRIDS[0].id;
  $("glist").innerHTML = GRIDS.map(g => {
    const keys = []; g.rows.forEach((r,ri) => g.cols.forEach((c,ci) => keys.push(`g:${g.id}:${ri}:${ci}`)));
    const due = keys.filter(isDue).length;
    return `<button class="ghost${curGrid===g.id?" on":""}" data-g="${g.id}" style="${curGrid===g.id?"border-color:var(--accent);background:var(--accent-soft)":""}">${esc(g.title)}${due?` <span class="dueBadge">${due}</span>`:""}</button>`;
  }).join("");
  if (!curGrid) curGrid = GRIDS[0].id;
  renderGrid();
}
$("glist").addEventListener("click", e => { const b = e.target.closest("[data-g]"); if (!b) return; curGrid = b.dataset.g; renderGridList(); });
function renderGrid(){
  const g = GRIDS.find(x => x.id === curGrid);
  const num = g.cols.length === 1 && g.cols[0].t === "num";
  let html = `<div class="artlbl">${esc(g.src)}</div>`;
  if (num){
    html += `<div class="grow"><div class="gnum">${g.rows.map((r,ri) => `<span class="q">${esc(r.h)}</span><div class="gcell" id="gc_${ri}_0"><input aria-label="${esc(r.h)}" autocomplete="off"></div>`).join("")}</div></div>`;
  } else {
    html += g.rows.map((r,ri) => `<div class="grow"><h4>${esc(r.h)}</h4>${g.cols.map((c,ci) => {
      const pool = shuffle(colPool(g, ci));
      return `<div class="gcell" id="gc_${ri}_${ci}"><label for="gs_${ri}_${ci}">${esc(c.h)}</label><select id="gs_${ri}_${ci}"><option value="">Choose…</option>${pool.map(p => `<option>${esc(p)}</option>`).join("")}</select></div>`;
    }).join("")}</div>`).join("");
  }
  html += `<div class="row"><button class="primary" id="gCheck">Check grid</button><button class="ghost" id="gReset">Clear and reshuffle</button><span class="gscore" id="gScore"></span></div>`;
  $("gbox").innerHTML = html;
  $("gReset").onclick = renderGrid;
  $("gCheck").onclick = () => {
    let right = 0, total = 0, blanks = 0;
    g.rows.forEach((r,ri) => g.cols.forEach((c,ci) => {
      const cell = $(`gc_${ri}_${ci}`), el = cell.querySelector("input,select"), v = r.c[ci];
      const ok = c.t === "num" ? typedOK(el.value, v) : el.value === v;
      const blank = !el.value.trim();
      total++; if (ok) right++; if (blank) blanks++;
      cell.classList.toggle("ok", ok); cell.classList.toggle("no", !ok);
      const old = cell.querySelector(".fix"); if (old) old.remove();
      if (!ok) cell.insertAdjacentHTML("beforeend", `<span class="fix">Answer: ${esc(c.t === "num" ? v[0] : v)}</span>`);
      if (!blank) rate(`g:${g.id}:${ri}:${ci}`, ok ? 2 : 0);
    }));
    $("gScore").textContent = `${right} / ${total}`;
    const miss = total - right - blanks;
    if (miss) $("gScore").textContent += ` · ${miss} wrong added to review`;
    if (blanks) $("gScore").textContent += ` · ${blanks} left blank (not counted in review)`;
  };
}

/* ---- tab wiring ---- */
setTab = function(tab){
  if (!["quiz","rev","drill"].includes(tab)) tab = "quiz";
  $("quizTab").hidden = tab !== "quiz"; $("revTab").hidden = tab !== "rev"; $("drillTab").hidden = tab !== "drill";
  document.body.classList.toggle("rev", tab === "rev");
  $("tabQuiz").setAttribute("aria-selected", tab === "quiz"); $("tabRev").setAttribute("aria-selected", tab === "rev"); $("tabDrill").setAttribute("aria-selected", tab === "drill");
  if (tab === "drill" && $("dcard").hidden) renderDSetup();
  if (tab === "quiz") updateDueBadge();
  store.set("pfr_tab", tab);
};
updateDueBadge();
setTab(store.get("pfr_tab", "quiz"));
