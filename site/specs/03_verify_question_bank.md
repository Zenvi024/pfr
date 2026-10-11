# Verification pass (independent second check) — Uribe PFR quiz bank

You are an independent checker. A law student (UP Law, Atty. Uribe's Persons & Family Relations) will use these items to review for a quiz today. Accuracy is paramount.
Read /home/claude/final/SPEC.md for the item schema and answer policy. Then check EVERY item in your assigned file:
1. Answer index: does choices[answer] actually match the explanation's conclusion? (Off-by-one or letter/index mismatch is the most likely bug — e.g. explanation says "(c)" but answer index is not 2.) For pair items: choices order is ["Both are true","Both are false","No. 1 is true, No. 2 is false","No. 1 is false, No. 2 is true"] unless the item shows otherwise — verify the index matches the explanation's T/F verdicts for statements 1 and 2.
2. Legal correctness under current Philippine law (verify the codal wording; e.g., FC 55(9) is only "against the life of the petitioner"; FC 45/47 periods; FC 41 4 yrs/2 yrs; FC 20 120 days; FC 15 3 months; FC 17 10 consecutive days; FC 57 five years from occurrence; FC 58 six months; RA 10572 Art 73; RA 11596; Manalo; Tan-Andal etc.). If the item follows Uribe's own key on a debatable point, that is allowed only if key_note explains it.
3. Ambiguity: if two choices are defensible and no key_note addresses it, fix the item (tweak a choice/fact minimally for new items; for verbatim samplex items, keep text and add key_note).
4. Explanation quality: correct article numbers, no contradictions, plain text.
5. origin label sanity (samplex/recit/bar/new).
Fix problems by editing the JSON file IN PLACE (load with python, modify, dump with ensure_ascii=False, indent=1). Do not drop items unless hopelessly wrong; do not change verbatim samplex wording except OCR typos.
Write a changelog to /home/claude/final/verify_<yourfile>.txt listing each change (id: what & why). Reply with the number of items checked and changed, and the most important corrections.
