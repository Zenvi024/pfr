// Renders one PNG per (scene, step) at 1920x1080.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const D = __dirname;
const scenes = JSON.parse(fs.readFileSync(path.join(D, 'scenes.json'), 'utf8'));
const css = fs.readFileSync(path.join(D, 'slide.css'), 'utf8');
const PARTS = ['Part 1', 'Part 2', 'Part 3', 'Part 4'];
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  fs.mkdirSync(path.join(D, 'frames'), { recursive: true });
  const only = process.argv[2] ? +process.argv[2] : null;
  for (let si = 0; si < scenes.length; si++) {
    if (only !== null && si !== only) continue;
    const sc = scenes[si];
    const part = PARTS.findIndex(x => sc.kicker.startsWith(x));
    const prog = PARTS.map((x, i) => `<i class="${i <= part || sc.kicker === 'Recap' ? 'on' : ''}"></i>`).join('');
    const inner = sc.title
      ? `<div class="frame"><div class="top"><div class="kicker">${sc.kicker}</div><div class="title">${sc.title}</div></div><div class="content">${sc.body}</div><div class="foot"><span>The Family · The Family Home · Paternity &amp; Filiation (FC 149–182)</span><div class="prog">${prog}</div></div></div>`
      : sc.body;
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${inner}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    for (let st = 0; st < sc.steps.length; st++) {
      await p.evaluate(n => document.querySelectorAll('[data-s]').forEach(e => { e.style.opacity = (+e.dataset.s <= n) ? 1 : 0 }), st);
      await p.screenshot({ path: path.join(D, 'frames', `s${String(si).padStart(2, '0')}_${st}.png`) });
    }
    // overflow check
    const of = await p.evaluate(() => { const c = document.querySelector('.content'); return c ? c.scrollHeight - c.clientHeight : 0 });
    if (of > 2) console.log('OVERFLOW scene', si, of);
  }
  await b.close();
})();
