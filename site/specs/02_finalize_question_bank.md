# Finalization task: Uribe PFR quiz bank (UP Law, Atty. Crisostomo Uribe, Persons & Family Relations)

The student is reviewing for (1) a quiz today, (2) a quiz on voidable marriages/legal separation/rights & obligations of spouses, (3) midterms covering Civil Code Arts. 1-51 through FC Arts. 68-73. Uribe quizzes mostly test PROVISIONS and APPLICATION OF PROVISIONS, using "pair" items (two statements; consider a statement true only where it is ABSOLUTELY true; choices "Both are true / Both are false / No. 1 is true, No. 2 is false / No. 1 is false, No. 2 is true") and MCQ application problems (short facts, ages, dates; choices like valid/void/voidable, "None of the above", "All of the above").

Your input file holds raw extracted items (fields: id, src, page, topic, type, stem, statements, choices, answer, source_reason, corrected_answer, flag, dup_cluster). Items sharing the same dup_cluster number are LIKELY duplicates (same question copied from different samplex copies) — but CAREFUL: Uribe often reuses a statement with one word changed (void/voidable, one/five years, either/both). Only merge true duplicates (same legal point AND same correct answer). When merging, keep the best-transcribed version and list all source labels.

## Your job
1. Dedupe as above.
2. Decide the CORRECT answer for each item under CURRENT Philippine law (Family Code as amended: RA 6809 age of majority 18; RA 10655 (2015) decriminalized premature marriage; RA 11596 (2021) child marriages void; Art 26(2) per Republic v. Orbecido (2005) & Republic v. Manalo (2018); Art 36 per Tan-Andal v. Andal (2021); Art 40 per Domingo v. CA, Mercado; Art 34 per Niñal v. Bayadog & Manzano v. Sanchez; Art 41 strict standard per Republic v. Cantor; Civil Code Art 13 vs Admin Code 1987 Sec. 31 & CIR v. Primetown (2007) for "year" = 12 calendar months, while Uribe's own class teaching may count a month as 30 days — when Uribe's answer key is based on his own stated teaching and the issue is genuinely debatable, follow Uribe's key and note the alternative view). Where the source key is wrong, use the correct answer and say in the explanation: "Note: the samplex key marked X; this is incorrect because ...". If an item is irreparably garbled, or its answer genuinely cannot be determined, DROP it.
3. Convert any "essay" items into tf or mcq (fact pattern as stem; write 4-5 plausible choices), or drop if redundant.
4. Write a clear EXPLANATION for every item (2-5 sentences): the governing provision quoted or closely paraphrased with article number, how it applies, and for pair items say why EACH statement is true/false. Mention Tolentino's commentary or key cases where helpful. Be precise — this is for a law student; accuracy is paramount.
5. ADD NEW questions in Uribe's style to cover gaps, so every provision in your topic range is tested at least once and key application patterns are drilled. Prefer pair items built from near-verbatim provisions with one subtle alteration, and short-fact application MCQs. New items must be legally airtight and unambiguous.
6. Target final count for your group is stated in your prompt.

## Output: JSON array to the path in your prompt. Each item:
{
 "id": "<group>-<n>",
 "topic": "<topic key>",
 "origin": "samplex" | "recit" | "bar" | "new",
     // samplex = verbatim from an Uribe quiz/samplex/exam (src from Uribe quizzes, CivRev quizzes, scanned quizzes, samplex sets)
     // recit = from Uribe recitation questions/class hypotheticals
     // bar = from QuAMTO / UP BOC bar questions (verbatim bar MCQ, or bar fact pattern adapted)
     // new = written now (incl. the Tolentino-based new items)
 "src": "source label(s), e.g. 'Uribe Quiz #3 (scanned samplex); Uribe CivRev 2025 Quiz 3 #4'",
 "type": "tf" | "mcq" | "pair",
 "stem": "question text (for pair: the instruction/fact pattern if any, else empty string)",
 "statements": ["1. ...", "2. ..."]  // pair only
 "choices": ["Both are true", "Both are false", ...]  // NO letter prefixes; for tf use ["True","False"]
 "answer": <0-based index into choices>,
 "explanation": "text",
 "key_note": null or "short note when the samplex/bar key differed from our answer or the point is debatable"
}
Text must be plain text (no markdown/HTML). Keep verbatim items verbatim (only fix OCR typos). Validate your output with python (json loads; answer index within range; tf choices exactly ["True","False"]). Reply with counts by origin and topic, and list items where you overrode a source key.
