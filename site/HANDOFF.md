# Study-site kit: handoff for a new AI agent

This kit lets you rebuild, for a new law subject, the study website that was built for a UP Law student's Persons and Family Relations (PFR) course. Read this whole file before touching the user's new materials.

The first build (PFR, Atty. Uribe) is included as a **worked example**, not as a template to copy blindly. The next subject is **Constitutional Law** with a **different professor who tests differently**. Your first real job is to work out how *that* professor tests, then decide which parts of this system fit.

---

## 0. Contents of the kit

```
HANDOFF.md                 this file (context, decisions, pipeline, lessons)
README.md                  60-second quick start
app/
  template.html            the single-page app shell (quiz, reviewer, drill tabs); placeholders filled by build.py
  build.py                 assembles one self-contained HTML file from a data folder
  print_pdf.py             renders the reviewer sections to a printable PDF (cover, contents, page numbers)
  drill/drill.html|css|js  the Drill tab (spaced review, fill-in-the-blank, spot-the-change, grids)
  drill/grids.py           how the PFR grids were authored (example of a grid data file)
specs/                     the exact prompts given to sub-agents at each pipeline stage (PFR-specific wording; adapt)
example_data/              the complete PFR data set, in the formats build.py expects
  course.config.json       title, topics, presets, source labels
  quiz_bank/*.json         467 verified questions
  reviewer/*.html          9 reviewer sections (~200,000 words)
  drill/cloze.json, alter.json, grids.json
reference_build/pfr-quiz-bank.html   the finished PFR site, for looking at behaviour
tests/                     Playwright smoke tests (quiz flow, drill flow)
```

Build the example to see it work:

```bash
python3 app/build.py --data example_data --out build/site.html
CHROMIUM=/path/to/chromium node tests/smoke_quiz.js build/site.html   # needs playwright installed
python3 app/print_pdf.py --data example_data --out build/reviewer.pdf --size 8.5in,13in
```

---

## 1. The user

- **Vinzen "Zen" Borja**, first-year JD student, University of the Philippines College of Law (2026–27). Call him **Zen**. Use "Vinzen Borja" only in formal/student-identity contexts.
- Preferences: grammatically correct writing; APA 7 citations unless told otherwise; 12-hour time; Philippine pesos; SI units; concise replies.
- He works under time pressure (quizzes "today", midterms "in two days"). He wants **depth and accuracy**, explicitly asked to "double check for accuracy", and wants to know **where each question came from**.
- He prints on **8.5 × 13 in (folio)** paper.
- He reviews on phone and laptop. Progress lives in the browser's localStorage, so tell him to stick to one device during a crunch.

## 2. What happened in the PFR build (chronological)

1. **Quiz bank.** He uploaded the syllabus, a treatise (Tolentino, scanned with no text layer), two block reviewers, and a 1,237-page merged PDF of samplexes (past quizzes/exams with answer keys), class transcripts, recitation logs and bar Q&A compilations. He asked for an HTML quiz site with explanations and retakes, all samplex questions included **verbatim**, new questions written in the professor's style, every item **marked samplex or new**, topic dividers, and **coverage presets** (quiz 1, quiz 2, midterms). Result: 467 questions, each with an origin tag, source label, explanation, and a "key note" wherever a circulated answer key was wrong or the point was debatable.
2. **Reviewer tab.** He asked for an encyclopedic, rule-book-style reviewer: provisions, exceptions, exceptions to exceptions, treatise commentary, cases, doctrines, and everything the professor said in class, cross-checked against the quiz bank. Result: 9 sections, a searchable sidebar table of contents, and labelled callouts.
3. **Printable PDF** of the whole reviewer (323 pages, folio).
4. **Retention features.** He asked for suggestions first ("suggest only, don't implement"), then chose four: spaced repetition, codal fill-in-the-blank, spot-the-alteration, and fill-in grids. The full suggestion list, including the unbuilt ones, is in §9.
5. **This kit.**

Working pattern that worked: he states the goal and the deadline. The agent does the work in parallel (sub-agents per page range or per topic), verifies independently, publishes, and replies in a few lines covering what changed and what he should double-check.

## 3. Pipeline (how the content was produced)

Every stage used parallel sub-agents with a written spec file (see `specs/`). A **separate verification pass by a fresh agent** after each authoring pass caught real errors every time, including wrong case holdings, a wrong answer index, outdated law, and invented citations. Don't skip it.

| Stage | What | Spec |
|---|---|---|
| A. Text extraction | `pdftotext -layout` and a non-layout version with `=== PAGE n ===` markers. Scanned PDFs (no text layer) must be read as page images with the Read tool, 20 pages per call. Map the big compilation by page: grep keyword density per page to find where the samplexes, transcripts and bar Q&As sit. | — |
| B. Raw extraction | One agent per page range pulls every in-coverage question **verbatim**, with the source's answer and reasoning, and flags answers it believes are wrong. Agents never silently fix a key: they put the fix in `corrected_answer` with a `flag`. | `01_extract_raw_questions.md` |
| C. Dedupe hints | Cluster near-duplicates (SequenceMatcher > 0.85 on normalized text) and pass the clusters to the next stage as **hints only**. The professor reuses statements with one word changed, so automatic merging would destroy distinct items. | — |
| D. Finalize per topic | One agent per topic group: dedupe, decide the correct answer under current law, convert essays into MCQs, write explanations, fill coverage gaps with new items, and validate the JSON. | `02_finalize_question_bank.md` |
| E. Verify bank | A fresh agent per topic file checks every answer index against its explanation, checks legal accuracy, and edits in place with a changelog. | `03_verify_question_bank.md` |
| F. Reviewer sections | One agent per syllabus section, writing restricted-HTML fragments. Every case on the syllabus must appear. The section is cross-checked against the bank, and conflicts are written to a file. | `04_write_reviewer_section.md` |
| G. Verify reviewer | A fresh agent per section checks quotations against the source text, removes fabricated or uncertain details (deleting a year rather than guessing it), and adds any missing syllabus cases. | `05_verify_reviewer_section.md` |
| H. Drill cards | Fill-in-the-blank and spot-the-change cards from verbatim provision text, validated by script (exactly one blank; a word-diff yields exactly one changed region). The grids were hand-written by the main agent because they are high-stakes summary tables. | `06_author_drill_cards.md` |
| I. Build, test, publish | `build.py` → Playwright smoke tests at 400px and 1280px in light and dark → publish as an Artifact (same URL on every update). | — |

Scale reference: about 8 extraction agents, 5 finalize agents, 5 verify agents, 9 reviewer agents, 9 reviewer verifiers and 2 drill-card agents. Sub-agents can hit rate limits mid-run. When that happens, check which output files are complete (closing tag present, parses) and relaunch only the missing ones with a tighter word budget.

## 4. The app

### 4.1 Architecture

- **One self-contained HTML file** (about 2 MB) with all data inlined as JSON. There are no external requests apart from Google Fonts. This is required by the Artifact host (strict content security policy). See §7.
- Tabs: **Quiz bank** | **Reviewer** | **Drill**.
- State lives in localStorage, with every access wrapped in try/catch. Keys: `pfr_hist` (last result per question), `pfr_srs` (spaced-repetition schedule), `pfr_topics`, `pfr_orig`, `pfr_tab`, `pfr_sec`, `pfr_dtopics`, `pfr_dtypes`. Each Artifact has its own origin, so prefixes don't collide; renaming them is optional.
- `build.py` fills these placeholders: `__CONFIG__ __DATA__ __REVIEWER__ __DRILLHTML__ __DRILLCSS__ __DRILLJS__ __CLOZE__ __ALTER__ __GRIDS__ __TITLE__ __EYEBROW__ __INTRO__ __FOOTER__ __PROF_LABEL__`.

### 4.2 `course.config.json`

```json
{
 "title": "…", "eyebrow": "Course · Subject · Professor", "intro": "one paragraph (HTML allowed)",
 "footer": "legend explaining the source tags (HTML allowed)",
 "profLabel": "label for the professor-remark callout in the reviewer legend",
 "pairInstruction": "default stem for two-statement items (only if the professor uses them)",
 "topics": [{"key":"…","name":"…","range":"Arts. … / Sections …"}],
 "origins": [{"key":"samplex","label":"Samplex"}, …],
 "presets": [{"id":"q1","name":"Quiz 1","sub":"…","topics":["…"]}, {"id":"mid","name":"Midterms","sub":"…","topics":"all"}]
}
```

The `origin` keys `samplex`, `recit`, `bar` and `new` have tag colours in CSS (`.tag.samplex` etc.). If you add a new origin key, add a `.tag.<key>` rule.

### 4.3 Question item schema (`quiz_bank/*.json`)

```json
{
 "id": "R-12", "topic": "<topic key>", "origin": "samplex|recit|bar|new",
 "src": "human-readable source label(s)",
 "type": "tf|mcq|pair",
 "stem": "question text (pair: instruction or facts, may be empty)",
 "statements": ["1. …", "2. …"],
 "choices": ["…"],
 "answer": 0,
 "explanation": "plain text, cites the provision or case and explains why each option is right or wrong",
 "key_note": null
}
```

- `statements` is for the `pair` type only. `choices` has no letter prefixes; tf is exactly `["True","False"]`. `answer` is a 0-based index.
- `key_note` is set only where the circulated key differs from the bank's answer or the point is debatable.
- `pair` is the "two statements → Both true / Both false / 1 true 2 false / 1 false 2 true" format. Use it only if the new professor uses it.

### 4.4 Reviewer fragment format (`reviewer/NN_slug.html`)

```html
<section class="rv" id="slug" data-title="Full title" data-short="Short label"> … </section>
```

Allowed inside the section: `h2` (once), `p.lede`, `h3` with a unique `id` prefixed by the slug (these build the table of contents), `h4`, `p`, `ul/ol/li`, `strong/em/br`.

| Element | Use |
|---|---|
| `div.codal > span.art` | verbatim provision text |
| `div.case > span.cn + span.cy + p` | case block |
| `aside.note.uribe` | **professor's remarks** (class name kept for CSS; label comes from `profLabel`) |
| `aside.note.trap` | quiz traps |
| `aside.note.tol` | treatise commentary |
| `aside.note.warn` | updates and conflicting views |
| `div.ex > p.q + p.a` | worked application examples |
| `div.tw > table` | tables |

No inline styles or scripts. Validate tag balance with `html.parser`.

### 4.5 Drill data

- **cloze.json:** `{"id","topic","art","text":"… [[answer]] …","accept":["alt forms"],"why"}`. Exactly one `[[…]]`. The matcher strips case and punctuation and treats number words and numerals ("five" = "5") as equal. It also ignores unit words (days, years, months, hours, consecutive).
- **alter.json:** `{"id","topic","art","original","altered","why"}`. The altered text must differ from the original in **exactly one contiguous word span**; the rest must match character for character. The app computes the span. The user sees only the altered text and taps the changed word (for a deletion, the word next to the gap counts). The original is revealed afterwards. Showing both at once turns it into a comparison exercise instead of a recall drill.
- **grids.json:** `{"id","topic","title","src","cols":[{"h","t":"pick|num"}],"rows":[{"h","topic"?,"c":[cell…]}]}`. For `pick` columns, the cell value is a string and the options are drawn from the same column. For `num` columns, the cell is a list of accepted answers. Blank cells on "Check" are revealed but not scheduled.
- **Spaced-repetition engine** (drill.js): steps of 1 min, 10 min, 1 h, 6 h, 1 day, 2 days, 4 days. Again resets to the first step; Hard keeps the step at half its interval (minimum 5 minutes); Good moves up one step; Easy moves up two (minimum 6 hours). A card answered wrong is re-inserted about three cards later in the same round. Answers in the Quiz tab also feed the schedule. The intervals suit a crunch of days, not months; stretch them for a longer horizon.

## 5. Adapting to a new professor and subject (start here)

**Do not assume the PFR professor's habits carry over.** Before writing a single question, build a **testing profile** from the new samplexes, syllabus and transcripts, and confirm it with the user in a few lines:

1. **Formats used**, with rough proportions: true/false, two-statement pairs, MCQ, "all/none of the above", essay or bar-type problems, case digests, identification, recitation-only.
2. **What is tested:** verbatim provisions; doctrines and case holdings (ponente, facts, ratio, vote); tests and elements (multi-part tests); comparisons; policy or reasoning; current events.
3. **How tricks are built:** one-word alterations, swapped case names, wrong elements, outdated doctrine, facts that trigger a different test.
4. **Answer conventions:** does he want ALAC (Answer, Legal basis, Application, Conclusion)? Does he penalize wrong reasons? Does he follow his own view over jurisprudence?
5. **Grading and schedule:** quiz frequency, coverage per quiz, exam dates → these become the coverage presets.

Then map the profile to features:

| If the professor tests… | Emphasize | De-emphasize |
|---|---|---|
| Verbatim provisions, one-word changes | Codal fill-in-the-blank, spot-the-change, pair items | — |
| Case doctrines (likely for Constitutional Law) | Case → doctrine and doctrine → case cards; "which test applies" MCQs; grids of tests and elements (e.g. standards of review, requisites of judicial review) | Fill-in-the-blank for long constitutional text, except for frequently tested sections |
| Essay or bar problems | Issue-spotting MCQs from fact patterns; an ALAC answer builder (§9 #12); a model-answer reveal | Pure true/false |
| Constitutional text | Fill-in-the-blank on the exact numbers and terms in the Constitution (terms of office, vote thresholds, periods), and grids of them | — |
| Recitation-heavy | Short Q→A cards from the transcripts, using spaced review | — |

For Constitutional Law specifically, expect (but **verify from his materials**) that the questions turn on doctrines, tests and their elements, landmark cases and their evolution (overruled vs. current), and exact constitutional numbers. Good card families include: case ↔ doctrine; "state the test and its elements"; "overruled or still good law?"; and constitutional numbers (age, residency, term, vote thresholds, periods) in fill-in-the-blank cards and grids.

Keep these general conventions; they are not professor-specific:

- Mark each item's **origin** and keep verbatim items verbatim.
- When a circulated key looks wrong, keep the item, give the correct answer, and add a `key_note` explaining both.
- Where the professor's stated view differs from jurisprudence, **teach both** and say which to write on his exam.
- Show source labels on every item.

## 6. Accuracy rules that mattered

- **Never invent** case names, G.R. numbers, years or holdings. If unsure, delete the detail. Verification agents repeatedly found fabricated or misremembered specifics (a holding stated backwards, a wrong year, a citation to a case that doesn't exist).
- Check the **answer index against the explanation** for every item. Off-by-one and letter/index mismatches are the most likely mechanical bug.
- Apply **current law** and flag outdated sources. Treatises and old samplex keys predate amendments and newer cases. Every update needs a note that names the newer law or case.
- **Scanned PDFs:** OCR of handwritten keys is unreliable. Read the page images. Two-column layouts interleave in text extraction, so verify against the images.
- **Circulated answer keys are often wrong.** Copies of the same quiz carry conflicting keys. Prefer the professor's own in-class answer when the transcript has it.
- **Debatable points:** follow the professor's stated teaching for his exam, and note the other view.
- **Keep the bank and the reviewer consistent.** Every reviewer agent cross-checks the bank and logs conflicts. You then fix the bank (`bankfix_*.txt` → patch the JSON → rebuild).

## 7. Publishing and UI constraints (Artifact host)

- Load the design guidance before writing a page. The page must be self-contained: inline CSS and JS, only Google Fonts as an external host, no `alert`/`confirm`, no downloads from the page, no `window.print()`.
- Colours are defined as tokens on `:root`, with dark-mode overrides in both `@media (prefers-color-scheme: dark)` (guarded by `:root:not([data-theme="light"])`) and `:root[data-theme="dark"]`. `body` gets an explicit background.
- Add `[hidden]{display:none!important}` yourself, so toggling works in local testing too.
- The layout must work at 400px wide with no horizontal scroll. Tables scroll inside `.tw`.
- Republish to the **same URL** for updates. On a first publish, pass a one-word generic `icon` and a one-sentence `description`.
- Visual identity used: a maroon accent on a cool off-white; Libre Caslon Text for display, IBM Plex Sans for body, IBM Plex Mono for labels. A new subject can get its own palette.

## 8. Testing checklist before every publish

1. `node --check` on the extracted `<script>`.
2. Playwright run at 400px: start a quiz, answer 20 items, see the results; open the reviewer, search, jump to a hit; start a drill round, answer each card type, check a grid. Assert no `pageerror` and `scrollWidth == viewport`.
3. Screenshot one view at desktop and one at phone width and look at them.
4. Re-validate the JSON (answer in range, unique ids) and the fragment HTML (balanced tags, unique h3 ids).

## 9. Feature backlog

Built: spaced review (#1), codal fill-in-the-blank (#2), spot-the-change (#3) and grids (#4).

Not built yet, in priority order:

- **#5 Mock exam:** draws items in the professor's topic proportions, timed, with answers hidden until the end. The report shows weak spots **by provision or doctrine**, with links into the reviewer.
- **#6 Heat map** of accuracy per article or doctrine.
- **#7 Confidence rating** before the answer is revealed; confidently wrong answers are reviewed first.
- **#8 Mixed drills of confusable pairs:** confusable concepts shuffled together on purpose.
- **#9 Professor-only filter:** samplex and recitation items only.
- **#10 Case ↔ doctrine flashcards in both directions.** This is probably the top priority for Constitutional Law.
- **#11 One-page "last 30 minutes" sheet:** all section checklists merged into one dense printable page.
- **#12 ALAC answer builder:** the student writes Answer, Legal basis, Application and Conclusion, then compares with a model answer.

## 10. What is PFR-specific (do not carry over as rules)

- The "consider the statement true only when absolutely true" pair format, and his habit of one-word codal alterations.
- His positions where they differ from jurisprudence (e.g. the Art. 34 five-year cohabitation reading, the Art. 13 day-count, civil interdiction in Art. 39).
- The labels "Samplex / Recitation / Bar / New" and the reviewer callout labelled with his name.
- The grids' content, the coverage presets, and the topic keys.

All of these live in `course.config.json` and the data files, so a new course swaps them out without touching the code.
