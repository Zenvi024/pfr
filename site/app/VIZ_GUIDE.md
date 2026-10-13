# Reviewer visuals: component guide

Every visual is a `<figure class="viz">` placed inside a reviewer section fragment
(`data/reviewer/NN_*.html`), right where the concept is discussed (usually after the
codal box or after the breakdown list it summarizes). Each figure has:

- a kicker `<span class="vk">Map</span>` (one or two words: Map, Decision tree, Timeline,
  Compare, Steps, Numbers, Sort it, Calculator, Diagram),
- the visual body (one of the components below),
- a `<figcaption>` with one sentence stating what the picture shows.

Colour roles: `data-c="1"` accent (maroon), `2` good (green), `3` warn (amber),
`4` bad (red), `5` muted. Use them for meaning (green = valid / exclusive / included,
red = void / excluded / forfeited, amber = voidable / conditional), not decoration.

Visuals are excluded from blur mode and from reviewer search, so they must not be the
only place a rule is stated; they restate the prose as a picture.

Keep labels short. No `<script>` or `<style>` in fragments. No external images.
Everything must read at 400px wide (mobile) and in dark mode (use only the classes
below, never hard-coded colours).

## 1. Mind map (`.mm`)
```html
<figure class="viz"><span class="vk">Map</span>
<div class="mm">
  <div class="mm-root">Marriage settlements <small>Arts. 74–81</small></div>
  <div class="mm-brs">
    <div class="mm-br" data-c="1"><div class="mm-h">Form <small>Art. 77</small></div><ul><li>In writing</li><li>Signed</li></ul></div>
    <div class="mm-br" data-c="2"><div class="mm-h">Parties</div><p>Short text</p></div>
  </div>
</div>
<figcaption>…</figcaption></figure>
```

## 2. Decision tree (`.tree`, optionally `data-walk` for the interactive walk-through)
Nested lists. Each `li` has an optional edge label `<i>Yes</i>`, then exactly one
`<span class="q">Question?</span>` (with children) or `<span class="o">Outcome</span>`
(a leaf). Outcome variants: `.o` green, `.o.no` red, `.o.mid` amber. Add
`<small>` inside q/o for a short note. With `data-walk`, the page adds "Full map /
Walk me through it" buttons that turn the tree into a stepper.
```html
<figure class="viz"><span class="vk">Decision tree</span>
<div class="tree" data-walk><ul><li><span class="q">Valid marriage settlement?</span><ul>
  <li><i>Yes</i><span class="o">Follow the settlement <small>Art. 74(1)</small></span></li>
  <li><i>No</i><span class="q">Married on or after Aug. 3, 1988?</span><ul>
    <li><i>Yes</i><span class="o">ACP</span></li>
    <li><i>No</i><span class="o mid">CPG <small>NCC 119</small></span></li>
  </ul></li>
</ul></li></ul></div>
<figcaption>…</figcaption></figure>
```

## 3. Timeline (`ol.tl`)
```html
<ol class="tl">
  <li data-c="5"><span class="d">Aug. 30, 1950</span><b>Civil Code takes effect</b><span>short note</span></li>
  <li data-c="1"><span class="d">Aug. 3, 1988</span><b>Family Code takes effect</b></li>
</ol>
```

## 4. Compare, Venn-style (`.venn`): left only / both / right only
```html
<div class="venn">
  <div class="vl"><h5>ACP only</h5><ul><li>…</li></ul></div>
  <div class="vm"><h5>Both</h5><ul><li>…</li></ul></div>
  <div class="vr"><h5>CPG only</h5><ul><li>…</li></ul></div>
</div>
```

## 5. Steps / process (`ol.steps`, add class `v` for a vertical list)
```html
<ol class="steps">
  <li><b>Inventory</b><span>separate lists</span></li>
  <li data-c="4"><b>Pay debts</b><span>community first</span></li>
</ol>
```

## 6. Bars for numbers and periods (`.bars`)
`--v` is the bar length in percent of the longest (compute it yourself; use a
sensible scale, e.g. months, and say so in the caption). Add class `in` to the `b`
label when the bar is long (above ~70) so the label sits inside.
```html
<div class="bars">
  <div class="bar" data-c="3"><span>Cooling-off period</span><div style="--v:10"><i></i><b>6 months</b></div></div>
  <div class="bar" data-c="1"><span>Prescription (Art. 57)</span><div style="--v:100"><i></i><b class="in">5 years</b></div></div>
</div>
```

## 7. Tiles / infographic cards (`.tiles`)
```html
<div class="tiles">
  <div class="tile" data-c="2"><span class="big">⅕</span><b>Cap on donations</b><span>regime other than ACP</span></div>
</div>
```

## 8. Sort it: interactive classifier (`.sorter`)
`data-b` lists the buckets separated by `|`. Each item: `data-a` is the 0-based
index of the right bucket; `<p>` is the item; `.why` is the explanation shown after
answering.
```html
<div class="sorter" data-b="Community|Excluded">
  <div class="sit" data-a="1"><p>Land A inherited during the marriage</p><div class="why">Art. 92(1): gratuitous title during the marriage.</div></div>
</div>
```

## 9. Calculator (`.calc` with `data-calc`)
Available: `fifth` (Art. 84), `art120` (reverse accession), `netprofit` (Art. 102(4)
vs. Tolentino), `doubleprop` (Art. 131). Markup is just
`<div class="calc" data-calc="fifth"></div>` inside the figure.

## 10. Inline SVG diagram (for mechanisms that need arrows: flows between
patrimonies, overlaps, before/after)
`<svg viewBox="0 0 W H" role="img" aria-label="same claim as the caption">`.
Text uses `currentColor` automatically. Classes: strokes `s-ink s-m s-a s-g s-w s-b`
(add `f-n` for no fill), fills `f-a f-g f-w f-b f-s f-c` (soft tints) and
`fa fg fw fm` (solid), text `t-m t-a t-g t-w t-b`, bold `b`, dashed `dash`.
Arrowheads: a `<marker>` in `<defs>` with an id unique on the whole page
(prefix it with the section id) whose path has class `fm` or `fa`.
Font size 12px at the drawn scale; keep W around 640 and text short. If the drawing
needs to stay wide, wrap the svg in `<div class="vscroll">` (min 560px, scrolls on
phones).
