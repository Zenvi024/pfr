// Renders <dir>/frames.json ([{id, html}]) to <dir>/frames/<id>.png at 1920x1080 with the given stylesheet.
// Each .fit box shrinks its font size until its content fits, and frames that share a box's text get the same size.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [dir, cssFile, only] = process.argv.slice(2);
const frames = JSON.parse(fs.readFileSync(path.join(dir, 'frames.json'), 'utf8'));
const css = fs.readFileSync(cssFile, 'utf8');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  fs.mkdirSync(path.join(dir, 'frames'), { recursive: true });
  const sizes = {}; let n = 0;
  for (const f of frames) {
    if (only && !new RegExp(only).test(f.id)) continue;
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${f.html}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    const key = f.id.replace(/_(r|s\d|c\d?|t\d|a)$/, '_q');           // the question frames of one item share a size
    const got = await p.evaluate(([start, big]) => {
      const el = document.querySelector('.fit'); if (!el) return null;
      let fs = start || (big ? 46 : 40); el.style.fontSize = fs + 'px';
      while (fs > 16 && el.scrollHeight > el.clientHeight + 1) { fs -= 1; el.style.fontSize = fs + 'px'; }
      return { fs, over: el.scrollHeight - el.clientHeight };
    }, [sizes[key], f.id.endsWith('_x')]);
    if (got) { if (!sizes[key]) sizes[key] = got.fs; if (got.over > 1) console.log('OVERFLOW', f.id, got.over); if (got.fs < 22) console.log('SMALL', f.id, got.fs); }
    await p.screenshot({ path: path.join(dir, 'frames', f.id + '.png') });
    if (++n % 50 === 0) console.log(n, '/', frames.length);
  }
  await b.close();
})();
