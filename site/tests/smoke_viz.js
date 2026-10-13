// Smoke test for reviewer visuals: every figure renders, trees walk, sorters score, calculators compute,
// no horizontal page overflow at phone width, no console errors.
// Run: NODE_PATH=$(npm root -g) CHROMIUM=/opt/pw-browsers/chromium node tests/smoke_viz.js [build/site.html]
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const src = path.resolve(process.argv[2] || 'build/site.html');
  const tmp = src.replace(/\.html$/, '.u8.html');
  fs.writeFileSync(tmp, '<meta charset="utf-8">' + fs.readFileSync(src, 'utf8'));
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM });
  let fail = 0;
  for (const [w, scheme] of [[400, 'light'], [1280, 'dark']]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, colorScheme: scheme });
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' && !/fonts\.g/.test(m.text())) errs.push(m.text()) });
    await p.goto('file://' + tmp); await p.evaluate(() => localStorage.clear()); await p.reload();
    await p.click('#tabRev');
    const r = await p.evaluate(() => {
      const out = { secs: {}, trees: 0, walked: 0, sorters: 0, sorted: 0, calcs: 0, calcOk: 0, overflow: [] };
      const secs = [...document.querySelectorAll('#rcontent section.rv')];
      secs.forEach((s, i) => {
        openSec(i, false);
        out.secs[s.id] = s.querySelectorAll('figure.viz').length;
        s.querySelectorAll('.tree[data-walk]').forEach(t => {
          out.trees++;
          t.querySelector('[data-m=walk]').click();
          let guard = 0;
          while (t.querySelector('.wopts button') && guard++ < 12) t.querySelector('.wopts button').click();
          if (t.querySelector('.wout')) out.walked++;
          t.querySelector('[data-m=map]').click();
        });
        s.querySelectorAll('.sorter').forEach(so => {
          out.sorters++;
          const it = so.querySelector('.sit'); it.querySelector('.sbtn button').click();
          if (it.classList.contains('done') && /answered/.test(so.querySelector('.sscore').textContent)) out.sorted++;
          so.querySelector('[data-reset]')?.click();
        });
        s.querySelectorAll('.calc').forEach(c => { out.calcs++; if (/₱/.test(c.querySelector('.cout')?.textContent || '')) out.calcOk++; });
        s.querySelectorAll('figure.viz').forEach(f => { if (f.scrollWidth > f.clientWidth + 2 && !f.querySelector('.vscroll')) out.overflow.push(s.id + ':' + (f.querySelector('figcaption')?.textContent || '').slice(0, 40)) });
      });
      out.pageW = document.documentElement.scrollWidth;
      return out;
    });
    const total = Object.values(r.secs).reduce((a, x) => a + x, 0);
    console.log(JSON.stringify({ w, scheme, total, ...r, errs }));
    if (r.walked !== r.trees || r.sorted !== r.sorters || r.calcOk !== r.calcs || r.pageW > w || r.overflow.length || errs.length) fail = 1;
    await p.close();
  }
  await b.close(); fs.unlinkSync(tmp);
  if (fail) { console.error('FAIL'); process.exit(1) } else console.log('OK');
})();
