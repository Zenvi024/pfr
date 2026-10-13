#!/usr/bin/env python3
"""Assemble the single-file study site.

Usage:
  python3 app/build.py --data example_data --out build/site.html

<data> must contain:
  course.config.json        title, topics, origins, presets, labels (see HANDOFF.md §4.2)
  quiz_bank/*.json          question items (schema in HANDOFF.md §4.3), concatenated in filename order
  reviewer/*.html           reviewer section fragments, concatenated in filename order (optional)
  drill/cloze.json          codal/rule fill-in cards (optional, [] if absent)
  drill/alter.json          spot-the-change cards (optional)
  drill/grids.json          fill-in grids (optional)
"""
import json, glob, os, argparse
here = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('--data', default='example_data'); ap.add_argument('--out', default='build/site.html')
A = ap.parse_args()
J = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
def load(p, default):
    return json.load(open(p)) if os.path.exists(p) else default

cfg = json.load(open(os.path.join(A.data, 'course.config.json')))
items = []
for f in sorted(glob.glob(os.path.join(A.data, 'quiz_bank', '*.json'))): items += json.load(open(f))
data = []
for x in items:
    o = {'i': x['id'], 't': x['topic'], 'o': x['origin'], 's': x.get('src', ''), 'y': x['type'], 'q': x.get('stem', ''),
         'c': x['choices'], 'a': x['answer'], 'e': x.get('explanation', '')}
    assert 0 <= o['a'] < len(o['c']), x['id']
    if x.get('statements'): o['st'] = x['statements']
    if x.get('key_note'): o['k'] = x['key_note']
    data.append(o)
rev = '\n'.join(open(f).read() for f in sorted(glob.glob(os.path.join(A.data, 'reviewer', '*.html'))))
cl = [{k: x[k] for k in ('id', 'topic', 'art', 'text', 'accept', 'why') if k in x} for x in load(os.path.join(A.data, 'drill', 'cloze.json'), [])]
al = [{k: x[k] for k in ('id', 'topic', 'art', 'original', 'altered', 'why')} for x in load(os.path.join(A.data, 'drill', 'alter.json'), [])]
gr = load(os.path.join(A.data, 'drill', 'grids.json'), [])

t = open(os.path.join(here, 'template.html')).read()
d = os.path.join(here, 'drill')
js = open(os.path.join(d, 'drill.js')).read().replace('__CLOZE__', J(cl)).replace('__ALTER__', J(al)).replace('__GRIDS__', J(gr))
t = t.replace('__DRILLHTML__', open(os.path.join(d, 'drill.html')).read()).replace('__DRILLCSS__', open(os.path.join(d, 'drill.css')).read()).replace('__DRILLJS__', js)
for k, v in {'__TITLE__': cfg['title'], '__EYEBROW__': cfg['eyebrow'], '__INTRO__': cfg['intro'], '__FOOTER__': cfg['footer'], '__PROF_LABEL__': cfg.get('profLabel', 'Professor')}.items():
    t = t.replace(k, v)
t = t.replace('__VIZCSS__', open(os.path.join(here, 'viz.css')).read()).replace('__VIZJS__', open(os.path.join(here, 'viz.js')).read())
t = t.replace('__CONFIG__', J(cfg)).replace('__DATA__', J(data)).replace('__REVIEWER__', rev)
assert '__' not in ''.join(s for s in ['__CONFIG__', '__DATA__', '__REVIEWER__'] if s in t) , 'unfilled placeholder'
os.makedirs(os.path.dirname(os.path.abspath(A.out)), exist_ok=True)
open(A.out, 'w').write(t)
print(f'wrote {A.out}: {len(t):,} bytes · {len(data)} questions · {len(cl)} cloze · {len(al)} alter · {len(gr)} grids')
