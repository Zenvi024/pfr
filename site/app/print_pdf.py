#!/usr/bin/env python3
"""Make a printable PDF of the reviewer sections (cover + contents + sections).
Usage: python3 app/print_pdf.py --data example_data --out build/reviewer.pdf [--size 8.5in,13in]
Needs Playwright + Chromium (node). Writes build/print.html, then renders with headless Chromium."""
import glob, os, re, argparse, subprocess, json
ap = argparse.ArgumentParser(); ap.add_argument('--data', default='example_data'); ap.add_argument('--out', default='build/reviewer.pdf'); ap.add_argument('--size', default='8.5in,13in')
A = ap.parse_args(); W, H = A.size.split(',')
cfg = json.load(open(os.path.join(A.data, 'course.config.json')))
secs = [open(f).read() for f in sorted(glob.glob(os.path.join(A.data, 'reviewer', '*.html')))]
toc = []
for s in secs:
    title = re.search(r'data-title="([^"]*)"', s).group(1); sid = re.search(r'id="([^"]*)"', s).group(1)
    hs = re.findall(r'<h3 id="([^"]+)">(.*?)</h3>', s, re.S)
    toc.append(f'<li><a href="#{sid}">{title}</a><ol>' + ''.join(f'<li><a href="#{i}">{h}</a></li>' for i, h in hs) + '</ol></li>')
css = '''
:root{--ink:#1f1a1c;--muted:#5d5357;--line:#d9d2d4;--accent:#7b1e2b;--accent-soft:#f6e9eb;--good:#1f6b45;--good-soft:#e6f3ea;--warn:#7a4f00;--warn-soft:#fbf2df;--codal:#f1eeef;
--display:"Libre Caslon Text",Georgia,"Times New Roman",serif;--body:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif;--mono:"IBM Plex Mono",Menlo,Consolas,monospace}
@page{size:%s %s;margin:0.75in 0.7in 0.8in}
*{box-sizing:border-box} body{margin:0;background:#fff;color:var(--ink);font:10.5pt/1.5 var(--body)}
.cover{min-height:9in;display:flex;flex-direction:column;justify-content:center;gap:14px;page-break-after:always}
.cover .ey{font:500 9pt var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent)} .cover h1{font:700 34pt/1.1 var(--display);margin:0}
.toc{page-break-after:always} .toc h2{font:700 20pt var(--display)} .toc>ol>li{margin:10px 0 2px;font:700 11pt var(--display)}
.toc ol ol{font:400 8.5pt/1.4 var(--body);color:var(--muted);columns:2} .toc a{color:inherit;text-decoration:none}
section.rv{page-break-before:always} .rv h2{font:700 21pt/1.15 var(--display);margin:0 0 6px} .rv .lede{color:var(--muted);font:9pt/1.45 var(--mono)}
.rv h3{font:700 14pt/1.25 var(--display);margin:22px 0 8px;padding-top:8px;border-top:1px solid var(--line);break-after:avoid}
.rv h4{font:600 11pt var(--body);margin:14px 0 4px;color:var(--accent);break-after:avoid} .rv p{margin:0 0 8px} .rv li{margin-bottom:3px}
.rv .codal{background:var(--codal);border-left:3px solid var(--ink);padding:8px 12px;margin:8px 0 12px;font-family:var(--display);font-size:10pt}
.rv .codal .art{font:700 8pt var(--mono);display:block;color:var(--accent)}
.rv .case{border:1px solid var(--line);border-radius:5px;padding:8px 12px;margin:8px 0 12px;break-inside:avoid} .rv .case .cn{font:700 10.5pt var(--display);font-style:italic}
.rv .note{display:block;border-radius:4px;padding:7px 11px;margin:8px 0 12px;font-size:10pt;break-inside:avoid}
.note.uribe{background:var(--accent-soft);border-left:3px solid var(--accent)} .note.trap{background:var(--warn-soft);border-left:3px solid var(--warn)}
.note.tol{background:var(--good-soft);border-left:3px solid var(--good)} .note.warn{border:1px dashed var(--muted)}
.rv .ex{border:1px solid var(--line);border-radius:5px;margin:8px 0 12px;break-inside:avoid} .rv .ex .q{margin:0;padding:7px 11px;background:#f6f4f4} .rv .ex .a{margin:0;padding:7px 11px}
.rv table{border-collapse:collapse;width:100%%;font-size:8.5pt} .rv th,.rv td{padding:4px 6px;border:1px solid var(--line);vertical-align:top;text-align:left} .rv th{background:#f3f0f1}
''' % (W, H)
html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{cfg['title']} Reviewer</title><style>{css}</style></head><body>
<div class="cover"><div class="ey">{cfg['eyebrow']}</div><h1>{cfg['title']}: Reviewer</h1></div>
<div class="toc"><h2>Contents</h2><ol>{''.join(toc)}</ol></div>{''.join(secs)}</body></html>'''
os.makedirs(os.path.dirname(os.path.abspath(A.out)), exist_ok=True)
ph = os.path.join(os.path.dirname(os.path.abspath(A.out)), 'print.html'); open(ph, 'w').write(html)
js = f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch(process.env.CHROMIUM?{{executablePath:process.env.CHROMIUM}}:{{}});
const p=await b.newPage();await p.goto('file://{ph}',{{waitUntil:'load'}});
await p.pdf({{path:'{os.path.abspath(A.out)}',width:'{W}',height:'{H}',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<div></div>',
footerTemplate:'<div style="width:100%;font:8px Arial;color:#888;padding:0 0.7in;text-align:right"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
margin:{{top:'0.75in',bottom:'0.8in',left:'0.7in',right:'0.7in'}}}});await b.close();}})();'''
jp = ph.replace('.html', '.js'); open(jp, 'w').write(js)
subprocess.run(['node', jp], check=True); print('wrote', A.out)
