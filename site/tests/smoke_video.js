// Smoke test for the Videos tab: picker, chapters, play/pause, ±10 s, chapter jumps, captions,
// transcript, speed, keyboard, switching videos, phone width, no console errors.
// Serves build/ over HTTP (tracks and media need an origin, as in the published artifact).
// The test browser has no H.264, so pass a folder of WebM stand-ins with the same base names:
// Run: NODE_PATH=$(npm root -g) CHROMIUM=/opt/pw-browsers/chromium VIDEO_TEST_WEBM_DIR=/path node tests/smoke_video.js
const { chromium } = require('playwright');
const http = require('http'), path = require('path'), fs = require('fs');
const ROOT = path.resolve(__dirname, '..', 'build');
const WEBM = process.env.VIDEO_TEST_WEBM_DIR;
const TYPES = { '.html': 'text/html; charset=utf-8', '.mp4': 'video/mp4', '.webm': 'video/webm', '.vtt': 'text/vtt', '.jpg': 'image/jpeg' };
const server = http.createServer((req, res) => {
  if (req.url === '/favicon.ico') { res.writeHead(204); return res.end(); }
  let f = path.join(ROOT, decodeURIComponent(req.url.split('?')[0]));
  if (WEBM && f.endsWith('.mp4')) f = path.join(WEBM, path.basename(f, '.mp4') + '.webm');
  if (!f.startsWith(ROOT) && !(WEBM && f.startsWith(path.resolve(WEBM)))) { res.writeHead(403); return res.end(); }
  fs.stat(f, (err, st) => {
    if (err) { res.writeHead(404); return res.end(); }
    const type = TYPES[path.extname(f)] || 'application/octet-stream', m = /bytes=(\d*)-(\d*)/.exec(req.headers.range || '');
    if (m) {
      const a = +m[1] || 0, b = m[2] ? +m[2] : st.size - 1;
      res.writeHead(206, { 'Content-Type': type, 'Content-Range': `bytes ${a}-${b}/${st.size}`, 'Accept-Ranges': 'bytes', 'Content-Length': b - a + 1 });
      fs.createReadStream(f, { start: a, end: b }).pipe(res);
    } else { res.writeHead(200, { 'Content-Type': type, 'Content-Length': st.size, 'Accept-Ranges': 'bytes' }); fs.createReadStream(f).pipe(res); }
  });
});
const ok = (c, m) => { if (!c) { console.error('FAIL:', m); process.exitCode = 1; } else console.log('ok -', m); };
(async () => {
  await new Promise(r => server.listen(0, r));
  const url = `http://127.0.0.1:${server.address().port}/site.html`;
  const vids = JSON.parse(fs.readFileSync(path.resolve(__dirname, '..', 'data', 'videos.json'), 'utf8'));
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM, args: ['--autoplay-policy=no-user-gesture-required'] });
  for (const [w, scheme] of [[1280, 'light'], [400, 'dark']]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, colorScheme: scheme });
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('response', r => { if (r.status() >= 400) errs.push(`${r.status()} ${r.url()}`); }); p.on('console', m => { if (m.type() === 'error' && !/fonts\.g/.test(m.text())) errs.push(m.text()); });
    await p.goto(url); await p.evaluate(() => localStorage.clear()); await p.reload();
    await p.click('#tabVid');
    ok(await p.isVisible('#vidTab') && !(await p.isVisible('#quizTab')), `${w}: Videos tab opens`);
    ok(await p.locator('#vpick [data-v]').count() === vids.length, `${w}: picker lists ${vids.length} videos`);
    ok(await p.locator('#vchap [data-c]').count() === vids[0].chapters.length, `${w}: chapters of video 1`);
    await p.waitForFunction(() => document.getElementById('vvid').readyState >= 1, null, { timeout: 20000 });
    const dur = await p.evaluate(() => document.getElementById('vvid').duration);
    ok(Math.abs(dur - vids[0].duration) < 2, `${w}: metadata loaded (${dur.toFixed(1)} s)`);
    await p.evaluate(() => { const v = document.getElementById('vvid'); v.muted = true; });
    await p.click('#vbig');
    await p.waitForFunction(() => document.getElementById('vvid').currentTime > 0.5, null, { timeout: 15000 });
    ok(await p.evaluate(() => !document.getElementById('vvid').paused), `${w}: plays`);
    await p.click('#vplay'); ok(await p.evaluate(() => document.getElementById('vvid').paused), `${w}: pauses`);
    const t0 = await p.evaluate(() => document.getElementById('vvid').currentTime);
    await p.click('#vfwd'); await p.waitForTimeout(300);
    const t1 = await p.evaluate(() => document.getElementById('vvid').currentTime);
    ok(Math.abs(t1 - t0 - 10) < 1, `${w}: +10 s`);
    await p.click('#vback'); await p.waitForTimeout(300);
    ok(Math.abs(await p.evaluate(() => document.getElementById('vvid').currentTime) - t0) < 1, `${w}: −10 s`);
    await p.click('#vnext'); await p.waitForTimeout(300);
    const tc = await p.evaluate(() => document.getElementById('vvid').currentTime);
    ok(Math.abs(tc - vids[0].chapters[1].t) < 1, `${w}: next chapter → ${vids[0].chapters[1].title}`);
    await p.click('#vchap [data-c="5"]'); await p.waitForTimeout(400); await p.click('#vplay');
    ok(Math.abs(await p.evaluate(() => document.getElementById('vvid').currentTime) - vids[0].chapters[5].t) < 1.5, `${w}: chapter list click seeks`);
    ok(await p.evaluate(() => document.querySelector('#vchap button.on')?.dataset.c) === '5', `${w}: current chapter highlighted`);
    await p.waitForFunction(() => document.getElementById('vvid').textTracks[0]?.cues?.length > 50, null, { timeout: 10000 });
    ok(await p.evaluate(() => document.getElementById('vvid').textTracks[0].mode) === 'showing', `${w}: captions on by default`);
    await p.click('#vcc');
    ok(await p.evaluate(() => document.getElementById('vvid').textTracks[0].mode) === 'hidden' && await p.getAttribute('#vcc', 'aria-pressed') === 'false', `${w}: captions off`);
    await p.keyboard.press('c');
    ok(await p.evaluate(() => document.getElementById('vvid').textTracks[0].mode) === 'showing', `${w}: C key turns captions back on`);
    await p.click('#vsidetabs [data-p="tx"]');
    const ncue = await p.locator('#vtxlist [data-q]').count();
    ok(ncue > 100, `${w}: transcript (${ncue} lines)`);
    await p.fill('#vtxq', 'earnest efforts'); const hits = await p.locator('#vtxlist mark').count();
    ok(hits > 0, `${w}: transcript search (${hits} hits)`);
    await p.locator('#vtxlist [data-q]').nth(1).click(); await p.waitForTimeout(400); await p.click('#vplay');
    const tq = await p.evaluate(() => document.getElementById('vvid').currentTime);
    ok(tq > 110 && tq < 116, `${w}: transcript line seeks (${tq.toFixed(1)} s)`);
    await p.fill('#vtxq', '');
    await p.selectOption('#vrate', '1.5');
    ok(await p.evaluate(() => document.getElementById('vvid').playbackRate) === 1.5, `${w}: speed 1.5×`);
    await p.click('#vtime'); const tk = await p.evaluate(() => document.getElementById('vvid').currentTime);
    await p.keyboard.press('ArrowRight'); await p.waitForTimeout(300);
    ok(Math.abs(await p.evaluate(() => document.getElementById('vvid').currentTime) - tk - 10) < 1, `${w}: → key skips 10 s`);
    await p.click('#vpick [data-v="1"]');
    await p.waitForFunction(d => Math.abs(document.getElementById('vvid').duration - d) < 2, vids[1].duration, { timeout: 20000 });
    ok(await p.locator('#vchap [data-c]').count() === vids[1].chapters.length, `${w}: switched to video 2 (${vids[1].chapters.length} chapters)`);
    ok(await p.evaluate(() => { const t = [...document.getElementById('vvid').textTracks]; return t.filter(x => x.mode === 'showing').length === 1 && t[1].mode === 'showing' && t[1].cues.length > 300; }), `${w}: video 2 captions replace video 1's`);
    await p.waitForTimeout(500);
    await p.click('#tabQuiz');
    ok(await p.evaluate(() => document.getElementById('vvid').paused), `${w}: leaving the tab pauses`);
    await p.click('#tabVid');
    ok(await p.evaluate(() => Object.keys(JSON.parse(localStorage.getItem('pfr_vpos') || '{}')).length) >= 1, `${w}: position remembered`);
    ok(await p.evaluate(() => document.documentElement.scrollWidth) <= w, `${w}: no horizontal overflow`);
    await p.screenshot({ path: path.join(ROOT, `video_${w}_${scheme}.png`), fullPage: false });
    ok(!errs.length, `${w}: no console errors ${errs.join(' | ')}`);
    await p.close();
  }
  await b.close(); server.close();
  console.log(process.exitCode ? 'FAIL' : 'OK');
})();
