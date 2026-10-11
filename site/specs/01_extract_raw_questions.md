# Extraction task: Uribe PFR quiz bank (UP Law, Persons & Family Relations)

Goal: harvest quiz questions (verbatim) from a source range so they can be loaded into a self-quiz website.

## Coverage (only extract items within this coverage)
Topic keys:
- "laws": Civil Code Arts. 1-18 (effectivity, publication, ignorance of law, retroactivity, Art 5-6 waiver, repeal, custom, computation of periods Art 13, binding effect/conflicts Arts 14-18 incl. Art 15, 16, 17)
- "human": Civil Code Arts. 19-36 (abuse of rights, Arts 19-21, 26, 32-35 independent civil actions, prejudicial question Art 36, breach of promise to marry)
- "persons": Civil Code Arts. 37-51 (juridical capacity, capacity to act, restrictions, conceived child Art 40-41, death Art 42-43 survivorship, juridical persons 44-47, citizenship/domicile 48-51); also Family Code effectivity/retroactivity (FC 255-256, EO 209/227, RA 6809 age of majority)
- "req": Marriage — nature/definition, governing law (incl. FC Art 26 foreign marriages & foreign divorce), essential & formal requisites FC 1-34 (legal capacity, consent, authority of solemnizing officer, marriage license, ceremony, parental consent/advice, marriage counseling, exempt marriages Arts 27-34, certificate of legal capacity, place of solemnization, etc.)
- "void": Void marriages FC 35-44 (Art 35, 36 psychological incapacity, 37 incestuous, 38 public policy, 39 prescription, 40 judicial declaration, 41-44 subsequent marriage/presumptive death, effects of nullity incl. FC 50-54 as applied to void marriages, A.M. 02-11-10-SC), bigamy issues
- "voidable": Voidable marriages FC 45-47 (grounds, who may file, prescriptive periods, ratification/cohabitation), and FC 48-54 effects/procedure
- "ls": Legal separation FC 55-67 (grounds, defenses Art 56, period Art 57, cooling-off Art 58, reconciliation efforts Art 59, no stipulation/confession Art 60, pendency effects Art 61-62, decree effects Art 63-64, reconciliation Arts 65-67)
- "rights": Rights & obligations of spouses FC 68-73 (live together, fix family domicile, support, management of household, exercise of profession, Art 72 remedy)
EXCLUDE: property relations (FC 74+), family home, paternity/filiation, adoption, support (except FC 68/70), succession, property, obligations, etc. If a question mixes a covered and an excluded point, include it only if the covered point decides the answer.

## What to extract
Every quiz/exam question (True/False, "two statements" pair questions, MCQ, short problems) that falls in coverage, copied VERBATIM (fix only obvious OCR typos; do not rephrase). Include the answer as given in the source (answer key, "ANS:", "Class answer", "SIR:", "Final Answer", etc.) and the source's reasoning/legal basis.
Also extract essay/bar problems in coverage, but mark type "essay" (they will be converted to MCQ later).

Then CHECK the source's answer against the Family Code / Civil Code text you know. If you think the source answer is wrong, outdated (e.g., pre-RA 6809 age, pre-RA 10655, RA 11596 child marriage prohibition 2021, Art 26(2) Manalo 2018), or doubtful, set "flag" with a short explanation. Do NOT silently change the source answer — put your corrected answer in "corrected_answer".

## Output
Write a JSON array (valid JSON, UTF-8) to the output path given in your prompt. Each item:
{
 "id": "<prefix>-<n>",
 "src": "short label of where it came from, e.g. 'Uribe CivRev Quiz 3 (2025)' or 'Uribe samplex (old Quiz #3)' or 'QuAMTO 2015 Bar'",
 "page": <page number in the PDF>,
 "topic": "laws|human|persons|req|void|voidable|ls|rights",
 "type": "pair" | "mcq" | "tf" | "essay",
 "stem": "question text verbatim (for pair: any instruction/fact pattern preceding the two statements)",
 "statements": ["statement 1", "statement 2"],   // only for pair type
 "choices": ["a. ...", "b. ...", ...],           // for mcq and pair (pair usually: a. Both are true b. Both are false c. No.1 true, No.2 false d. No.1 false, No.2 true — copy the actual choice order used in that quiz if visible; if not visible use exactly that default order)
 "answer": "the letter (e.g. 'c') or 'True'/'False' as given in source; null if source gives none",
 "source_reason": "the explanation/basis given in the source, condensed but faithful (cite articles)",
 "corrected_answer": null or "letter/True/False",
 "flag": null or "why the source answer is wrong/doubtful"
}
For tf type, answer is "True" or "False". Keep the JSON compact but complete. Do not skip duplicates within your range (dedupe happens later) but do not create two entries for the identical text on the same page.
When done, reply with: count of items per topic, and a list of any flagged items (id + one line).
