/* ---------- Videos tab: explainer videos with chapters, captions and transcript ---------- */
(function(){
const VIDEOS = __VIDEOS__;
const tabBtn = $("tabVid");
if (!VIDEOS.length) { if (tabBtn) tabBtn.hidden = true; return; }
const V = $("vvid"), P = $("vplayer");
const fmt = s => { s = Math.max(0, Math.floor(s || 0)); const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = String(s % 60).padStart(2, "0"); return h ? `${h}:${String(m).padStart(2, "0")}:${x}` : `${m}:${x}`; };
const prefs = Object.assign({ cc: true, rate: 1, vol: 1, muted: false, vid: VIDEOS[0].id, panel: "chap" }, store.get("pfr_vprefs", {}));
const pos = store.get("pfr_vpos", {});
const savePrefs = () => store.set("pfr_vprefs", prefs);
let cur = Math.max(0, VIDEOS.findIndex(v => v.id === prefs.vid)), track = null, cues = [], seeking = false, lastSave = 0;

/* picker */
function renderPick(){
  $("vpick").innerHTML = VIDEOS.map((v, i) => {
    const r = pos[v.id] > 5 ? ` · resume at ${fmt(pos[v.id])}` : "";
    return `<button role="tab" data-v="${i}" aria-selected="${i === cur}"><img src="${esc(v.poster)}" alt="" loading="lazy"><span><b>${esc(v.title)}</b><small>${esc(v.range)} · ${fmt(v.duration)} · ${v.chapters.length} chapters${r}</small></span></button>`;
  }).join("");
}
$("vpick").addEventListener("click", e => { const b = e.target.closest("[data-v]"); if (b && +b.dataset.v !== cur) { savePos(true); load(+b.dataset.v, true); } });

/* chapters */
function chapters(){ return VIDEOS[cur].chapters; }
function chapAt(t){ const c = chapters(); let k = 0; for (let i = 0; i < c.length; i++) if (c[i].t <= t + 0.25) k = i; return k; }
function renderChapters(){
  let html = "", last = null;
  chapters().forEach((c, i) => {
    if (c.part !== last) { if (c.part) html += `<li class="vpart">${esc(c.part)}</li>`; last = c.part; }
    html += `<li><button data-c="${i}"><span>${fmt(c.t)}</span>${esc(c.title)}</button></li>`;
  });
  $("vchap").innerHTML = html;
  const d = VIDEOS[cur].duration;
  $("vticks").innerHTML = chapters().slice(1).map(c => `<i style="left:${(100 * c.t / d).toFixed(2)}%"></i>`).join("");
}
$("vchap").addEventListener("click", e => { const b = e.target.closest("[data-c]"); if (b) { go(chapters()[+b.dataset.c].t + 0.05); play(); } });

/* transcript */
function buildTranscript(){
  cues = VIDEOS[cur].cues.map(([s, , t]) => ({ s, t: t.replace(/\n/g, " ") }));
  renderTranscript();
}
function renderTranscript(){
  const q = $("vtxq").value.trim().toLowerCase();
  const rx = q ? new RegExp(q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi") : null;
  const list = cues.map((c, i) => [c, i]).filter(([c]) => !q || c.t.toLowerCase().includes(q));
  $("vtxlist").innerHTML = list.length ? list.map(([c, i]) => `<button data-q="${i}"><span>${fmt(c.s)}</span><span>${rx ? esc(c.t).replace(rx, m => `<mark>${m}</mark>`) : esc(c.t)}</span></button>`).join("")
    : `<p class="tiny" style="color:var(--muted)">${cues.length ? "No match." : "Transcript loads with the video."}</p>`;
  markCue();
}
$("vtxq").addEventListener("input", renderTranscript);
$("vtxlist").addEventListener("click", e => { const b = e.target.closest("[data-q]"); if (b) { go(cues[+b.dataset.q].s + 0.02); play(); } });
function markCue(){
  const t = V.currentTime; let k = -1;
  for (let i = 0; i < cues.length; i++) { if (cues[i].s <= t + 0.05) k = i; else break; }
  const box = $("vtxlist"); let on = null;
  box.querySelectorAll("button.on").forEach(b => b.classList.remove("on"));
  if (k >= 0) { on = box.querySelector(`[data-q="${k}"]`); if (on) on.classList.add("on"); }
  if (on && $("vfollow").checked && !V.paused && !$("vtx").hidden) {
    const top = on.offsetTop - box.offsetTop - box.clientHeight / 3;
    if (Math.abs(box.scrollTop - top) > 4) box.scrollTop = top;
  }
}

/* side panel tabs */
function setPanel(p){
  prefs.panel = p; savePrefs();
  $("vchap").hidden = p !== "chap"; $("vtx").hidden = p !== "tx";
  $("vsidetabs").querySelectorAll("button").forEach(b => b.setAttribute("aria-pressed", b.dataset.p === p));
  if (p === "tx") markCue();
}
$("vsidetabs").addEventListener("click", e => { const b = e.target.closest("[data-p]"); if (b) setPanel(b.dataset.p); });

/* load a video; captions are added as cues (artifact hosting serves no .vtt), one track per video */
const tracks = {};
function makeTrack(v){
  const tt = V.addTextTrack("captions", "English", "en");
  if (window.VTTCue) for (const [a, b, x] of v.cues) tt.addCue(new VTTCue(a, b, x));
  return tt;
}
function load(i, autoplay){
  cur = i; prefs.vid = VIDEOS[i].id; savePrefs();
  const v = VIDEOS[i];
  V.poster = v.poster; V.src = v.src; $("verr").hidden = true;
  if (track) track.mode = "disabled";
  track = tracks[v.id] || (tracks[v.id] = makeTrack(v));
  applyCC(); buildTranscript();
  V.playbackRate = prefs.rate; V.defaultPlaybackRate = prefs.rate;
  renderPick(); renderChapters(); update();
  V.addEventListener("loadedmetadata", () => {
    const p = pos[v.id]; if (p > 5 && p < (V.duration || v.duration) - 10) V.currentTime = p;
    V.playbackRate = prefs.rate; update(); if (autoplay) play();
  }, { once: true });
  V.load();
}
V.addEventListener("error", () => { if (V.error) $("verr").hidden = false; });

/* controls */
function play(){ const p = V.play(); if (p && p.catch) p.catch(() => {}); }
function toggle(){ V.paused ? play() : V.pause(); }
function go(t){ const d = V.duration || VIDEOS[cur].duration; V.currentTime = Math.max(0, Math.min(d - 0.1, t)); update(); }
let flashT = 0;
function flash(msg){ const f = $("vflash"); f.textContent = msg; f.classList.add("on"); clearTimeout(flashT); flashT = setTimeout(() => f.classList.remove("on"), 900); }
function skip(s){ go(V.currentTime + s); flash(s < 0 ? `↺ ${-s} s` : `${s} s ↻`); }
function chapJump(dir){
  const c = chapters(), k = chapAt(V.currentTime);
  let to = dir < 0 ? (V.currentTime - c[k].t > 3 ? k : Math.max(0, k - 1)) : Math.min(c.length - 1, k + 1);
  go(c[to].t + 0.05); flash(c[to].title);
}
function applyCC(){
  if (track) track.mode = prefs.cc ? "showing" : "hidden";
  $("vcc").setAttribute("aria-pressed", prefs.cc); $("vcc").title = `Captions ${prefs.cc ? "on" : "off"} (C)`;
}
function setRate(r){ r = Math.min(2, Math.max(0.75, Math.round(r * 4) / 4)); prefs.rate = r; savePrefs(); V.playbackRate = r; $("vrate").value = String(r); flash(`${r}×`); }
function applyVol(){ V.volume = prefs.vol; V.muted = prefs.muted; $("vvol").value = prefs.vol; $("vmute").textContent = prefs.muted || prefs.vol === 0 ? "🔇" : "🔊"; $("vmute").setAttribute("aria-label", prefs.muted ? "Unmute" : "Mute"); }
function fullscreen(){
  if (document.fullscreenElement) document.exitFullscreen();
  else if (P.requestFullscreen) P.requestFullscreen().catch(() => {});
  else if (V.webkitEnterFullscreen) V.webkitEnterFullscreen();
}
$("vplay").onclick = toggle; $("vbig").onclick = play;
V.addEventListener("click", toggle);
$("vback").onclick = () => skip(-10); $("vfwd").onclick = () => skip(10);
$("vprev").onclick = () => chapJump(-1); $("vnext").onclick = () => chapJump(1);
$("vcc").onclick = () => { prefs.cc = !prefs.cc; savePrefs(); applyCC(); flash(prefs.cc ? "Captions on" : "Captions off"); };
$("vrate").onchange = e => setRate(+e.target.value);
$("vmute").onclick = () => { prefs.muted = !prefs.muted; savePrefs(); applyVol(); };
$("vvol").oninput = e => { prefs.vol = +e.target.value; prefs.muted = prefs.vol === 0; savePrefs(); applyVol(); };
$("vfs").onclick = fullscreen;
$("vseek").addEventListener("input", e => { seeking = true; const d = V.duration || VIDEOS[cur].duration; $("vtime").textContent = `${fmt(e.target.value / 1000 * d)} / ${fmt(d)}`; });
$("vseek").addEventListener("change", e => { const d = V.duration || VIDEOS[cur].duration; seeking = false; go(e.target.value / 1000 * d); });

/* state → UI */
function update(){
  const d = V.duration || VIDEOS[cur].duration, t = V.currentTime || 0;
  if (!seeking) $("vseek").value = d ? Math.round(1000 * t / d) : 0;
  $("vtime").textContent = `${fmt(t)} / ${fmt(d)}`;
  const k = chapAt(t), c = chapters()[k];
  $("vchap").querySelectorAll("button").forEach(b => b.classList.toggle("on", +b.dataset.c === k));
  $("vnow").innerHTML = `<small>${esc(VIDEOS[cur].title)} · chapter ${k + 1} of ${chapters().length}</small>${esc(c.part ? c.part + " — " : "")}${esc(c.title)}`;
}
function savePos(force){
  const now = Date.now(); if (!force && now - lastSave < 4000) return; lastSave = now;
  const d = V.duration || VIDEOS[cur].duration;
  pos[VIDEOS[cur].id] = V.currentTime > d - 15 ? 0 : Math.floor(V.currentTime); store.set("pfr_vpos", pos);
}
let lastChap = -1;
V.addEventListener("timeupdate", () => {
  update(); markCue(); savePos(false);
  const k = chapAt(V.currentTime);
  if (k !== lastChap) { lastChap = k; const b = $("vchap").querySelector(`[data-c="${k}"]`), box = $("vchap"); if (b && !V.paused) box.scrollTop = Math.max(0, b.offsetTop - box.offsetTop - 40); }
});
V.addEventListener("play", () => { $("vbig").hidden = true; $("vplay").textContent = "❚❚"; $("vplay").setAttribute("aria-label", "Pause"); });
V.addEventListener("pause", () => { $("vbig").hidden = false; $("vplay").textContent = "▶"; $("vplay").setAttribute("aria-label", "Play"); savePos(true); renderPick(); });
V.addEventListener("ended", () => { pos[VIDEOS[cur].id] = 0; store.set("pfr_vpos", pos); renderPick(); });
V.addEventListener("seeked", () => { update(); markCue(); });

/* keyboard (only while the Videos tab is open) */
document.addEventListener("keydown", e => {
  if ($("vidTab").hidden || e.ctrlKey || e.metaKey || e.altKey) return;
  const tg = e.target, tag = tg.tagName;
  if (tag === "TEXTAREA" || tag === "SELECT" || (tag === "INPUT" && !["range", "checkbox"].includes(tg.type))) return;
  const k = e.key;
  if ((k === " " || k === "Enter") && tag === "BUTTON") return;
  const map = {
    " ": toggle, k: toggle, K: toggle, ArrowLeft: () => skip(-10), j: () => skip(-10), J: () => skip(-10),
    ArrowRight: () => skip(10), l: () => skip(10), L: () => skip(10), "[": () => chapJump(-1), "]": () => chapJump(1),
    c: () => $("vcc").click(), C: () => $("vcc").click(), m: () => $("vmute").click(), M: () => $("vmute").click(),
    f: fullscreen, F: fullscreen, "<": () => setRate(prefs.rate - 0.25), ">": () => setRate(prefs.rate + 0.25), ",": () => setRate(prefs.rate - 0.25), ".": () => setRate(prefs.rate + 0.25)
  };
  if (map[k]) { e.preventDefault(); map[k](); }
});

/* tab wiring */
let inited = false;
function onTab(tab){
  if (tab === "vid") { if (!inited) { inited = true; applyVol(); $("vrate").value = String(prefs.rate); setPanel(prefs.panel); load(cur, false); } }
  else if (!V.paused) V.pause();
}
document.addEventListener("pfr:tab", e => onTab(e.detail));
if (!$("vidTab").hidden) onTab("vid");
window.addEventListener("pagehide", () => { if (inited) savePos(true); });
})();
