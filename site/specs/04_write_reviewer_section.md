# Writing task: Midterms Reviewer section — Atty. Crisostomo Uribe, Persons & Family Relations (UP Law, Law 100)

The student (UP Law 1L) needs a FOOLPROOF, encyclopedic midterms reviewer: a complete rule book with every provision, its elements, rules, exceptions, exceptions to exceptions, commentary (Tolentino), cases and doctrines, and EVERYTHING Uribe has said (class transcripts, recitation situationers, samplex answer keys, doctrines outline). Uribe tests provisions and application of provisions, often by changing one word in the codal ("void" vs "voidable", "either" vs "both", periods). So exact codal wording, periods, who-may-file, and distinctions matter most.

## Sources (read all that bear on your section; cross-check everything)
- Uribe's syllabus/outline: /home/claude/txt/7b489bb1-00_PFR_Syllabus_-_Uribe.txt  → EVERY case listed under your section must appear with its doctrine.
- Uribe's doctrines outline (case doctrines per syllabus heading): /home/claude/txt/20b6a4eb-00_0.6-Online-Uribe-Doctrines_3.txt
- Uribe recitation situationers (Q&A Sir asked): /home/claude/txt/7c92cc9d-00_2_Online_-_Uribae-Situationers.txt
- Uribe class transcripts + quiz discussions + samplexes: /home/claude/txt/merged_pages.txt (page markers "=== PAGE n ==="). Most relevant: pages 1-60 (Uribe Civil Law Review 2025 transcripts covering Arts 1-51 and marriage → legal separation, with "SIR:" remarks), 750-822 (old Uribe quizzes and class discussion), 1056-1160 (samplex answer sets with reasons, Uribe notes). Grep by article number / keywords to find what is relevant to your section.
- Block 2029B reviewers (codal text + jurisprudence + commentary): /home/claude/txt/16b4cd0f-00_Law_100_B29_Midterms_Reviewer_-_Provisions.txt, /home/claude/txt/c567aa59-00_Law_100_B29_Midterms_Reviewer_-_Case_Repository.txt, /home/claude/txt/33dd17bf-00_Law_100_B29_Finals_Reviewer_-_Provisions.txt, /home/claude/txt/d5f5ff69-00_Law_100_B29_Finals_Reviewer_-_Case_Repository.txt
- The finished quiz bank (already verified answers + explanations + key notes): /home/claude/final/out_prelim.json, out_req.json, out_void.json, out_voidable.json, out_lsrights.json. CROSS-CHECK: every legal point tested by the quiz items in your topic must be covered in your reviewer, and your reviewer must not contradict the bank's answers (if you believe a bank answer is wrong, write it to /home/claude/rev/conflicts_<slug>.txt with the item id and reason, and state the correct rule in the reviewer).
- Tolentino, Civil Code Vol. I (scanned, no text layer): /root/.claude/uploads/a7d9fc60-23ef-5395-a27e-5295698352d9/f800a92e-00_Tolentino_PFR.pdf — use the Read tool with the pages parameter (max 20 pages per call). Mapping: PDF page ≈ book page/2 + 31. Preliminary title (Arts 1-18) is early in the PDF; Family Code marriage material ≈ PDF pages 148-215. Read the pages for your section and include Tolentino's commentary (paraphrased, cite "Tolentino").

## Current law to apply (flag outdated views)
RA 6809 (age of majority 18); RA 10655 (2015) repealed RPC 351 premature marriages; RA 11596 (2021) child marriage void & criminal; RA 8533 (Art 39 no prescription); Art 26(2) per Republic v. Orbecido (2005) & Republic v. Manalo (2018) and later cases; Art 36 per Tan-Andal v. Andal (2021); Art 40 (Domingo, Mercado, Pulido v. People 2021); Art 34 (Niñal, Manzano v. Sanchez); Art 41 (Republic v. Cantor strict well-founded belief); A.M. 02-11-10-SC and 02-11-11-SC; RA 10572 (2013) amended Arts 73 and 111; CIR v. Primetown on "year"; Local Government Code 1991 (mayors solemnize). Where Uribe's own stated view differs from jurisprudence/commentators, present BOTH, label Uribe's view, and tell the student what to answer in his quiz (follow Uribe's key when it is his stated teaching).

## Accuracy rules
- Codal text must be verbatim (check against the B29 provisions reviewer text). Never invent case names, G.R. numbers, or holdings. If unsure of a date/GR, omit it.
- Distinguish clearly: rule → exceptions → exceptions to exceptions; who may file; prescriptive periods; effects; ratification.
- Include worked application examples (short facts → answer) in Uribe's style.

## Output format: ONE HTML fragment file at the path in your prompt
Wrap everything in: <section class="rv" id="SLUG" data-title="FULL TITLE" data-short="SHORT TAB LABEL"> ... </section>
Inside use ONLY these elements/classes (no inline styles, no scripts, no markdown):
- <h2>Section title</h2> once at top, then a short <p class="lede"> scope line (articles covered).
- <h3 id="SLUG-xxx">Subtopic</h3> (each h3 MUST have a unique id prefixed by your slug; these build the table of contents), <h4> for sub-subtopics.
- <p>, <ul>/<ol>/<li>, <strong>, <em>, <br>.
- Verbatim provisions: <div class="codal"><span class="art">Art. 45, FC.</span> text ... </div> (numbered paragraphs inside as <ol> or line breaks ok)
- Cases: <div class="case"><span class="cn">Case Name</span> <span class="cy">(year or citation if sure)</span><p>Facts in 1-2 lines (optional). <strong>Doctrine:</strong> ...</p></div>
- Uribe remarks: <aside class="note uribe"><strong>Uribe:</strong> ...</aside>
- Quiz traps / one-word alterations he uses: <aside class="note trap"><strong>Quiz trap:</strong> ...</aside>
- Tolentino commentary: <aside class="note tol"><strong>Tolentino:</strong> ...</aside>
- Conflicting views / updates: <aside class="note warn"><strong>Note:</strong> ...</aside>
- Application examples: <div class="ex"><p class="q">Facts...</p><p class="a"><strong>Answer:</strong> ...</p></div>
- Tables (comparisons, periods, who-may-file): <div class="tw"><table><thead>...</thead><tbody>...</tbody></table></div>
End with <h3 id="SLUG-checklist">Last-minute checklist</h3> — a dense bullet list of the must-memorize points (numbers, periods, one-word distinctions).
Escape & as &amp; and < as &lt; in text. Validate the fragment parses (e.g. python html.parser, check tags balance). Aim for depth: this should be the most complete reviewer the student has ever read for these articles (typically 6,000-14,000 words for your section). Reply with: word count, list of h3 headings, list of syllabus cases covered, and any conflicts found with the quiz bank.
