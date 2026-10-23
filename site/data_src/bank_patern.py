from qb import Bank, ABS

# ======================= PATERNITY AND FILIATION (FC 163–182) =======================
p = Bank("patern", "P")
Q5 = "Uribe CivRev 2025 Quiz 5 (Sep 27, 2025)"
Q2 = "Uribe CivRev 2025 Quiz 2 (Aug 28, 2025)"
QC1 = "Uribe Quiz Compilation, Set 1"
QC3 = "Uribe Quiz Compilation, Set 3 (= Quiz No. 4)"
MT = "Uribe Midterm Exam (Civ Rev samplex)"
Q1 = "Uribe 1st Quiz (Civ Rev samplex)"
SIT = "Uribe recitation situationer (2018)"
TSR = "Uribe CivRev 2025 recitation (Sep 27, 2025)"

# ---- Kinds; legitimate children
p.tf("samplex", f"{QC1} TF6", "Children conceived or born outside a valid marriage are illegitimate.", False,
     "Art. 165: children conceived AND born outside a valid marriage are illegitimate. A child conceived outside but born inside a valid marriage is legitimate (Art. 164: conceived OR born during the marriage).")
p.mcq("samplex", f"{QC1} MC14",
      "For a child to be legitimate, he must be:",
      ["Conceived during the marriage", "Born during the marriage", "Conceived and born during the marriage", "Conceived or born during the marriage", "All of the above", "None of the above"], "d",
      "Art. 164: 'Children conceived OR born during the marriage of the parents are legitimate.' Keyed (d) in Sir's older quizzes (also Midterm #44). Compare 2025 Quiz 5 item 1, where the T/F version ('must be conceived or born during the marriage') was FALSE because children of Art. 36 and 53 marriages (Art. 54), adopted children and legitimated children are also legitimate.")
p.tf("samplex", f"{Q5} #1", "To be a legitimate child, he/she must be conceived or born during the marriage of the parents.", False,
     "Not absolutely true. Children conceived or born before the judgment of nullity under Art. 36 becomes final, and children of a subsequent marriage void under Art. 53, are legitimate (Art. 54); adopted children are legitimate children of the adopter; legitimated children have the same rights. In the discussion Sir cautioned: on a status question never answer 'legitimated' ('legitimation happens AFTER … It presupposes na illegitimate ang bata').",
     key="The class notes record the basis as FALSE; Sir pushed back on using legitimation or artificial insemination as the reason.")
p.tf("samplex", f"{Q5} #2", "Children conceived as a result of artificial insemination of the wife with the sperm of the husband are legitimate children of the husband and his wife.", False,
     "Art. 164, 2nd par. adds the proviso: 'provided, that both of them authorized or ratified such insemination in a written instrument executed and signed by them before the birth of the child.' The statement omits it. A student who answered TRUE (presumption of legitimacy) was made to correct himself.",
     key="Tolentino and the 2006 UPLC bar answer treat the written instrument as evidence only; Sir treats it as a requirement.")
p.mcq("samplex", f"{QC1} MC19",
      "This is required for a child by artificial insemination to be a legitimate child of A and B, husband and wife, respectively:",
      ["The child was conceived as a result of artificial insemination of C", "The child was conceived with the sperm of A", "Both A and B authorize the artificial insemination in a written instrument",
       "The authority or ratification of such artificial insemination may be signed after the birth of the child", "None of the above"], "c",
      "Art. 164, 2nd par.: insemination OF THE WIFE (not C, which would be surrogacy) with the sperm of the husband OR a donor or both (so b is not required), authorized or ratified in a written instrument executed and signed BEFORE the birth (so d is wrong).")
p.mcq("samplex", f"{Q2} (2025 version)",
      "This is required for a child by artificial insemination to be a legitimate child of A and B, husband and wife, respectively:",
      ["the child was conceived as a result of artificial insemination of C.", "the child was conceived with the sperm of A.", "both A and B authorize the artificial insemination in a public instrument.",
       "the authority or ratification of such artificial insemination may be signed after the birth of the child.", "none of the above"], "e",
      "The 2025 trap: 'written instrument' became 'PUBLIC instrument'. Sir: 'Written lang, di naman kailangan published di ba? The correct answer is E.' On (a): 'IT IS STILL AI! Ang insemination ay nasa asawa hindi sa kapitbahay', i.e., insemination of someone other than the wife is not covered. On (b): donor sperm is allowed.")
p.tf("samplex", f"{Q1} TF7", "Children conceived or born before the promulgation of judgment of annulment or absolute nullity of the marriage under Article 36 shall be considered legitimate.", True,
     "Art. 54 speaks of the judgment having 'become final and executory'. A child conceived or born before promulgation is necessarily conceived or born before finality, so the statement is true.")
p.tf("samplex", f"{Q2} TF9 (= 1st Quiz TF4)", "Children born after the dissolution of the marriage of the parents may be legitimate.", True,
     "Art. 164: conceived during the marriage. Sir's example: a child conceived before the husband's death and born after it. Do not cite void marriages: 'There is nothing to dissolve if it is void.' (Annulment may be cited: Art. 54.) A student key marking this FALSE is wrong.")
p.tf("samplex", "Uribe Quiz No. 4 TF1", "Children conceived and born outside a valid marriage are illegitimate.", False,
     "Art. 165 ends with 'unless otherwise provided in this Code'. E.g., children of a marriage void under Art. 36 conceived or born before the judgment becomes final, and children of a subsequent marriage void under Art. 53, are legitimate (Art. 54).")
p.mcq("bar", "UP BOC – 2012 Bar MCQ",
      "Who are illegitimate children?",
      ["Children conceived or born outside a valid marriage.", "Children born under a valid marriage, which was later declared void because of the psychological incapacity of either or both of the spouses.",
       "Children conceived and born outside a valid marriage.", "Children born under a valid marriage, but the parents later obtained a legal separation."], "c",
      "Art. 165. B is legitimate under Art. 54; D is legitimate (legal separation does not affect the marriage bond).")
p.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Fidel, a Filipino with fair complexion, married Gloria. Before the marriage, Gloria confessed to Fidel that she was two-month pregnant with the child of a black African who had left the country for good. When the child was born, Fidel could not accept it being too black in complexion. What is the status of the child?",
      ["Illegitimate, because Gloria confessed that the child is not Fidel's.", "Illegitimate, because by the color of its skin, the child could not possibly be that of Fidel.",
       "Legitimate, because the child was born within a valid marriage.", "Legitimate, because Fidel agreed to treat the child as his own after Gloria told him who the father was."], "c",
      "Art. 164: born during the marriage. The mother's declaration does not matter (Art. 167), and until Fidel successfully impugns legitimacy (e.g., on biological grounds, Art. 166(2)) within the Art. 170 period, the child is legitimate.")
p.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Arthur and Helen, both Filipinos, got married and had 2 children. Arthur later worked in Rome where he acquired Italian citizenship. He got a divorce from Helen in Rome but, on returning to the Philippines, he realized his mistake, asked forgiveness of his wife, and resumed living with her. They had 2 more children. What is the status of their 4 children?",
      ["The children born before the divorce are legitimate but those born after it are not since Arthur got the divorce when he had ceased to be a Filipino.", "The divorce rendered illegitimate the children born before it since the marriage that begot them had been nullified.",
       "The children born before and after the divorce are all legitimate since Philippine law does not recognize divorce.", "All the children are legitimate since they were born of the same father and mother."], "a",
      "UPLC's suggested answer is (A): the foreign divorce obtained by Arthur as an Italian citizen dissolved the marriage (cf. Art. 26), so children born after it, out of wedlock, are illegitimate. The answer turns on the recognition of the divorce, so be ready to explain.",
      key="Bar key (A); the answer depends on Art. 26 and the recognition of the foreign divorce.")
p.mcq("recit", f"{TSR} (adapted to MCQ)",
      "X and Y's marriage was declared void for lack of a marriage license. Their child C was conceived and born before the judgment of nullity became final. What is C's status?",
      ["Legitimate, under Art. 54", "Legitimate, in the best interest of the child", "Illegitimate", "Legitimated"], "c",
      "Sir: the Art. 54 exception covers ONLY Art. 36 marriages and Art. 53 subsequent marriages. 'In all other grounds of nullity, dapat illegitimate child siya.' Do not argue 'best interest of the child': 'unfair yun sa ibang mga anak … mababawasan yung share nung iba.'")
p.tf("recit", f"{SIT} (adapted)", "If spouses A and B have their child through the implantation of an embryo (sperm of A, egg of B) in a third woman, C, who carries and delivers the baby, the child is the legitimate child of A and B under Article 164.", False,
     "Sir's 2018 answer: 'No. The FC does not recognize the concept of surrogacy.' Art. 164 covers artificial insemination OF THE WIFE.")
p.tf("recit", f"{SIT} (adapted)", "A and B are spouses. During A's lifetime, B cohabited with C. After A's death, B married C, and during that marriage X was born, conceived after A's death. X was legitimated by the marriage of B and C.", False,
     "Sir: 'No. X was already legitimate because he was born within a valid marriage. Legitimation presupposes that the child was born illegitimate.'")
p.tf("recit", f"{TSR} (2025 Bar problem)", "A husband who discovered through a secret DNA test that he was not the father of his wife's child, and who thereafter only filed for and obtained the annulment of their marriage, has thereby made the child illegitimate.", False,
     "The child, born during the marriage, is legitimate (Art. 164; children conceived or born before the annulment decree is final are legitimate). Sir: 'Legitimate. Kasi wala namang impugn.' To change the status, the husband must file an action to impugn on biological or scientific grounds (Art. 166(2)) within the Art. 170 period.")
p.tf("new", "New (Uribe format; FC 163)", "The filiation of children may be by nature or by adoption. Natural filiation may be legitimate or illegitimate.", True,
     "Verbatim Art. 163.")
p.mcq("samplex", f"{QC3} MC10",
      "The status of the child in relation to the father or the mother, and may be used to indicate paternity or maternity is known as:",
      ["Legitimacy", "Paternity", "Maternity", "Filiation"], "d",
      "Filiation is the child's relationship to the parent; paternity and maternity are the parent's side. In the 2025 version (Quiz 5 #11), 'Filiation' was removed from the choices and replaced by 'Natural', so the answer became 'None of the above'.")
p.mcq("samplex", f"{Q5} #11",
      "The status of the child in relation to the father or the mother, and may be used to indicate paternity or maternity is known as:",
      ["Legitimacy", "Paternity", "Maternity", "Natural", "None of the above"], "e",
      "The answer is 'filiation', which is not among the choices. Watch Sir's trick of removing the correct answer from an old item.")

# ---- Rights; illegitimate children
p.tf("samplex", f"{QC3} TF1 (= Quiz 5 #5)", "The legitime of the illegitimate children shall consist of one-half of the legitime of the legitimate children.", False,
     "Art. 176: 'The legitime of EACH illegitimate child shall consist of one-half of the legitime of A legitimate child.' With two or more legitimate children, take one legitimate child's legitime and halve it.")
p.mcq("bar", "UP BOC – 2012 Bar MCQ",
      "An illegitimate child may use the surname of his father when his filiation is established in any of the following instances, except:",
      ["Filiation has been recognized by the father through the record of birth appearing in the civil register", "Admission of filiation by the father in a public document.",
       "Private handwritten instrument is made by the father acknowledging his filiation.", "Affidavit by the mother stating the name of his true father."], "d",
      "Art. 176, as amended by R.A. 9255: the father's express recognition through the record of birth, or his admission in a public document or private handwritten instrument. The mother's affidavit is not the father's recognition.")
p.mcq("bar", "UP BOC – 2009 Bar (adapted to MCQ)",
      "Rodolfo, married to Sharon, begot Rona with his secretary Nanette. He later acknowledged Rona and gave her regular support. Can he compel Rona to use his surname?",
      ["Yes, because he acknowledged her", "Yes, because he supports her", "No; under R.A. 9255 the illegitimate child MAY use the father's surname, and the choice is the child's (through the mother, who has sole parental authority, while the child is a minor)", "No, because illegitimate children can never use the father's surname"], "c",
      "Art. 176 as amended: illegitimate children 'may' use the father's surname if he expressly recognized them. 'May' is permissive (Grande v. Antonio, 2014; Barcelote v. Republic, 2017). The mother has sole parental authority over an illegitimate child.")
p.tf("new", "New (Uribe format; FC 176)", "Illegitimate children shall use the surname of their father if their filiation has been expressly recognized by the father through the record of birth appearing in the civil register.", False,
     "Art. 176 (R.A. 9255): they 'MAY use the surname of their father' upon express recognition; otherwise they 'shall use the surname … of their mother'. 'May' is permissive (Grande v. Antonio; Barcelote v. Republic).")
p.tf("new", "New (Uribe format; FC 176)", "Illegitimate children shall be under the parental authority of their mother, and shall be entitled to support in conformity with this Code.", True,
     "Art. 176. The father, even if he recognized the child and gives support, has no parental authority; to obtain custody he must first deprive the mother of parental authority on a legal ground (bar answers).")
p.mcq("new", "New (Osmeña de Valencia v. Rodriguez)",
      "The legitimate children of X sued to stop X's illegitimate children from using the surname of X. Will the suit prosper?",
      ["Yes, because only legitimate children have the right to the father's surname", "Yes, because the use of the surname implies legitimacy",
       "No, because the right of legitimate children to their father's surname creates no monopoly over it", "No, because surnames are not property"], "c",
      "Osmeña de Valencia v. Rodriguez: the article 'has marked a right of which legitimate children may not be deprived, but it cannot be interpreted as a prohibition against the use by others of what may happen to be the surname of their father. If plaintiff's theory were correct, they can stop countless inhabitants from bearing the surname \"Valencia.\"'")
p.mcq("new", "New (Moore; Naldoza)",
      "A mother whose first marriage ended petitioned for her legitimate minor son to use the surname of her second husband. Rule.",
      ["Grant, in the best interest of the child", "Grant, since the stepfather supports the child", "Deny; a legitimate child may not use the surname of a person who is not his father", "Grant, if the father consents"], "c",
      "Moore v. Republic (1963): it may cause confusion as to the child's real paternity and prejudice him in the long run. Similarly, Naldoza v. Republic: minors may not, at the mother's behest alone, drop their father's surname for the mother's.")
p.tf("new", "New (Uribe format; Mangulabnan v. IAC)", "Before an illegitimate child whose father was married at the time of his conception may be granted support, he must first be recognized by the father.", False,
     "Mangulabnan v. IAC (1990): such a child is spurious, and recognition is not required before support; there must be a declaration of the child's status, which may be provisional, by affidavits.")

# ---- Impugning
p.mcq("samplex", f"{QC3} MC3",
      "Legitimacy of a child may be impugned on the ground that it was physically impossible for the husband to have sexual intercourse with the wife:",
      ["Right after the solemnization of the marriage", "Within the first 30 days of the 300 days which immediately preceded the birth of the child",
       "Within the first 180 days which immediately preceded the birth of the child", "Within the first 120 days of the 300 days which immediately preceded the birth of the child"], "d",
      "Art. 166(1). Why 120 of 300? If conception was impossible during the first 120 days, the child could have been conceived only within the last 180 days before the birth, which is shorter than the minimum gestation of a viable child (Sir's explanation).")
p.mcq("samplex", f"{Q5} #14",
      "Legitimacy of a child may be impugned on the ground that it was physically impossible for the husband to have sexual intercourse with the wife:",
      ["right after the solemnization of the marriage", "within the first 30 days of the 300 days which immediately preceded the birth of the child",
       "within the first 180 which immediately preceded the birth of the child", "within the first 180 days of the 300 days which immediately preceded the birth of the child", "none of the above"], "e",
      "The 2025 trap: '120' became '180'. Art. 166(1): within the first 120 days of the 300 days which immediately preceded the birth of the child. Answer: none of the above.")
p.mcq("samplex", f"{QC3} MC5",
      "If the husband resides in the municipality or city where the birth took place or was recorded, the action to impugn the legitimacy of the child shall be brought within:",
      ["1 year from knowledge of birth or its recording in the civil register", "2 years from knowledge of birth or its recording in the civil register",
       "3 years from knowledge of birth or its recording in the civil register", "4 years from knowledge of birth or its recording in the civil register"], "a",
      "Art. 170, 1st par. Two years if he (or all his heirs) resides elsewhere in the Philippines; three years if abroad. There is no 4-year period; concealment only changes the starting point (from discovery or knowledge, whichever is earlier).")
p.mcq("samplex", f"{Q5} #16",
      "If the husband resides in the country where the birth took place or was recorded, the action to impugn the legitimacy of the child shall be brought within:",
      ["1 year from knowledge of the birth or its recording in the civil register", "2 years from knowledge of the birth or recording in the civil register",
       "3 years from knowledge of the birth or recording in the civil register", "4 years from knowledge of the birth or recording in the civil register", "none of the above"], "e",
      "The 2025 trap: 'city or municipality' became 'COUNTRY'. Residence in the same country tells you only that it is not 3 years; it may be 1 year (same city or municipality) or 2 years (elsewhere in the Philippines). Correct answer: E.")
p.tf("samplex", f"{QC3} TF5", "The child shall be considered legitimate although the mother may have been sentenced as an adulteress.", True,
     "Art. 167 (codal): '… although the mother may have declared against its legitimacy or may have been sentenced as an adulteress.'")
p.mcq("samplex", f"{QC3} MC1 (= Quiz 5 #12)",
      "A child conceived before the death of the husband (A) of B but born one month after the marriage between B and C is:",
      ["Legitimate child of A and B", "Illegitimate child of A and B", "Legitimated child of B and C", "Illegitimate child of B and C", "Legitimate child of B and C"], "a",
      "Art. 168(1): born before 180 days after the subsequent marriage (and within 300 days of the termination), so considered conceived during the former marriage. Sir: 'Pag na-conceive na siya sa unang asawa, alangan naman na sa loob ng sinapupunan naging anak na siya ng pangalawang asawa.'")
p.mcq("samplex", f"{QC3} MC2",
      "A died on January 1, 2011. His widow, B, married C on May 1, 2011. D was born on October 15, 2011. In the absence of proof to the contrary, D will be considered as the:",
      ["Legitimate child of A and B", "Illegitimate child of A and B", "Legitimated child of B and C", "Illegitimate child of B and C", "none of the above"], "a",
      "October 15 is 287 days after A's death (within 300) and 167 days after the May 1 wedding (before 180), so Art. 168(1) applies: conceived during the former marriage.")
p.mcq("samplex", f"{Q5} #13",
      "\"A\" died on January 1, 2024. His widow, \"B\", married C on August 1, 2024. D was born on November 15, 2024. In the absence of proof to the contrary, D will be considered as the:",
      ["legitimate child of A and B", "illegitimate child of A and B", "legitimate child of B and C", "illegitimate child of B and C", "none of the above"], "c",
      "D was born 319 days after A's death, beyond 300 days, so Art. 168(1)'s proviso fails and A cannot be the father ('Alangan naman makabuntis pa ang patay'). Sir: the 180-day computation is irrelevant, and Art. 169 is not the point. D was born during the B–C marriage: legitimate child of B and C (Art. 164).")
p.tf("bar", "QuAMTO – 1999 Bar (adapted)", "Two months after the death of her husband, Rose married her childhood boyfriend, and seven months after that marriage she delivered a baby. In the absence of evidence as to who the father is, the child is the legitimate child of the second marriage.", True,
     "Art. 168(2): a child born after 180 days following the celebration of the subsequent marriage is considered conceived during it, even if born within 300 days after the termination of the former marriage. (Seven months ≈ 210 days.)")
p.mcq("bar", "UP BOC – 2012 Bar MCQ",
      "The husband may impugn the legitimacy of his child but not on the ground that:",
      ["the wife is suspected of infidelity.", "the husband had a serious illness that prevented him from engaging in sexual intercourse.", "they were living apart.", "he is physically incapable of sexual intercourse."], "a",
      "Art. 166 grounds are exclusive; the wife's infidelity is not one, and even her conviction for adultery does not affect legitimacy (Art. 167).")
p.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "A left B, his wife, in the Philippines to work in Egypt but died in that country after a year's continuous stay. Two months after A's death, B gave birth to a child, claiming it is A's child. Who can assail the legitimacy of the child?",
      ["A's other heirs apart from B.", "The State which has interest in the welfare of overseas contract workers.", "Any one who is outraged by B's claim.", "No one since A died."], "a",
      "Art. 171(1) and (3): the heirs may impugn if the husband died before the expiration of his period, or if the child was born after his death. The ground would be Art. 166(1)(b).")
p.tf("bar", "UP BOC – 2008 Bar (adapted)", "Laica, born during the marriage of Faye and Brad, may herself bring an action to impugn her status as Brad's legitimate child on the ground that DNA results show that Roderick is her biological father.", False,
     "UPLC answer: 'The law does not allow a child to impugn his or her own filiation.' Only the husband, or his heirs in the Art. 171 cases, may impugn (Liyao). Note: Sir reads Yap v. Yap (2022) as allowing the child to establish filiation with the biological father, so be ready to qualify.",
     key="Codal and bar answer: FALSE. Sir in 2025 endorsed Yap v. Yap; qualify in an essay.")
p.mcq("bar", "QuAMTO – 2024 Bar (adapted to MCQ)",
      "Monica was born in 1990 during the marriage of Anton and Steph. In 2024 she learned that Patrick, Steph's ex-boyfriend who had died a year earlier, signed her birth certificate as father. She sued for partition of Patrick's estate, claiming to be his non-marital child. May she impugn her own legitimacy in the partition case?",
      ["Yes, because the birth certificate signed by Patrick is primary evidence", "Yes, because the action to claim filiation does not prescribe",
       "No; legitimacy cannot be attacked collaterally, only the husband (or his heirs in proper cases) may impugn it, and the period has long lapsed", "No, because Patrick is dead"], "c",
      "The bar answer (Central Bar Q&A): Liyao; De Jesus v. Estate of Dizon; Arts. 170–171. This is the item Sir mentioned ('Eto ang naging tanong last year'). Sir prefers Yap v. Yap (truth over reputation), so in recitation add that view.")
p.tf("new", "New (Uribe format; FC 166)", "Legitimacy of a child may be impugned on the ground that the husband was sterile within the first 120 days of the 300 days which immediately preceded the birth of the child.", False,
     "Art. 166(1)(a) speaks of 'physical incapacity of the husband to have sexual intercourse' (impotence), not sterility (inability to procreate). Tolentino: short of absent testicles or a blocked vas deferens there is no absolute sterility. Proof that the child cannot be his for biological reasons falls under Art. 166(2).")
p.tf("new", "New (Uribe format; FC 166, Andal v. Macaraig)", "Legitimacy of a child may be impugned on the ground of serious illness of the husband during the first 120 days of the 300 days which immediately preceded the birth of the child.", False,
     "Art. 166(1)(c): serious illness 'which ABSOLUTELY prevented sexual intercourse'. In Andal v. Macaraig, advanced tuberculosis did not prevent intercourse.")
p.tf("new", "New (Uribe format; Macadangdang v. CA)", "Where the spouses were estranged and slept in separate rooms but continued to live in the same town during the period of conception, the husband may successfully impugn the legitimacy of the child on the ground of physical impossibility of access.", False,
     "Only physical, not moral, impossibility counts. In Macadangdang, the spouses lived in the same province, so access was possible, and the presumption stood.")
p.mcq("new", "New (Jao v. CA)",
      "A blood grouping test shows that the child and the alleged father have incompatible blood types. What is its evidentiary value?",
      ["It conclusively proves paternity", "It conclusively proves non-paternity", "It is inadmissible", "It is merely corroborative of paternity"], "b",
      "Jao v. CA (1987): 'Blood tests are conclusive as to non-paternity and inconclusive to paternity.' DNA testing can now establish paternity positively.")
p.mcq("new", "New (Lim v. IAC)",
      "The nephews of a childless decedent claim her estate, alleging that V, who claims to be her daughter, is not her child at all. V invokes the prescriptive periods for an action to impugn legitimacy. Rule.",
      ["The nephews' action has prescribed", "Only the decedent's husband could have questioned V's status",
       "The periods for impugning legitimacy do not apply, because the claim is that V is not the decedent's child at all", "V is presumed legitimate and cannot be questioned"], "c",
      "Lim v. IAC (1988): NCC 263 (now Art. 170) applies to an action to impugn legitimacy; it is inapplicable where the claim is that the person 'is not the decedent's child at all'. Same for a simulated birth (Benitez-Badua v. CA).")
p.tf("new", "New (Uribe format; FC 167, Chua Keng Giap)", "Under Article 167, a mother's denial that she gave birth to the claimant is to be disregarded.", False,
     "Art. 167 disregards a mother's declaration AGAINST THE LEGITIMACY of her child (i.e., that her husband is not the father). A denial of MATERNITY is different: in Chua Keng Giap v. IAC, the mother's long-standing denial was given decisive weight ('Who better than Sy Kao herself would know …').")
p.tf("new", "New (Uribe format; FC 169)", "The legitimacy or illegitimacy of a child born after three hundred days following the termination of the marriage shall be proved by whoever alleges such legitimacy or illegitimacy.", True,
     "Verbatim Art. 169. There is no presumption either way. (Tolentino would treat the child as the mother's illegitimate child absent proof; the codal is neutral.)")
p.pair("new", "New (Uribe format; FC 170–171)",
       "If the birth of the child has been concealed from or was unknown to the husband or his heirs, the period to impugn shall be counted from the discovery or knowledge of the birth of the child or of the fact of registration of said birth, whichever is later.",
       "The heirs of the husband may impugn the filiation of the child if the husband should die after the filing of the complaint without having desisted therefrom.",
       False, True,
       "No. 1 is FALSE: 'whichever is EARLIER' (Art. 170). No. 2 is TRUE: Art. 171(2). The other two cases: the husband died before his period expired (1), or the child was born after his death (3).")
p.mcq("new", "New (FC 171)",
      "The heirs of the husband may impugn the filiation of the child in any of the following cases, EXCEPT:",
      ["If the husband should die before the expiration of the period fixed for bringing his action", "If he should die after the filing of the complaint without having desisted therefrom",
       "If the child was born after the death of the husband", "If the husband, during his lifetime, let the period to impugn lapse without filing an action"], "d",
      "Art. 171. If the husband let the period lapse, the child's status became fixed, and the heirs cannot sue (Tolentino: the heirs act only in substitution of the husband).")
p.mcq("new", "New (Liyao; Yap)",
      "Under the codal provisions as applied in Liyao v. Tanhoti-Liyao, who may bring the action to impugn the legitimacy of a child born to a married woman?",
      ["The child", "The mother", "The alleged biological father", "The husband, or his heirs in the cases provided by law"], "d",
      "Arts. 170–171; Liyao (2002): 'The child himself cannot choose his own filiation.' Uribe in 2025: Yap v. Yap (2022) now allows the child to establish filiation with the biological father, and he agrees with that ruling.")
p.tf("new", "New (Uribe format; impugning)", "If the legitimacy of a child is successfully impugned by the husband, the child becomes an illegitimate child of the spouses.", False,
     "Sir called this a non sequitur. Successful impugning establishes that the child is not the husband's child at all; he is not 'an illegitimate child of the spouses' or of the husband. (He becomes the mother's illegitimate child; Tolentino.)")

# ---- Proof of filiation (FC 172–176)
p.tf("samplex", f"{QC3} TF6", "Illegitimate children may establish their illegitimate filiation in the same way and on the same evidence as legitimate children.", True,
     "Verbatim Art. 175, 1st par.", topic="filiat")
p.mcq("samplex", f"{QC3} MC4",
      "After the death of the alleged parent, the filiation of an illegitimate child may be established by any of the following EXCEPT:",
      ["The record of birth appearing in the civil register", "An admission of illegitimate filiation in a public document", "An admission of illegitimate filiation in a private handwritten instrument and signed by the parent concerned",
       "The open and continuous possession of the status of an illegitimate child", "none of the above"], "d",
      "Art. 175, 2nd par.: an action based on the second paragraph of Art. 172 (possession of status or other means) 'may be brought during the lifetime of the alleged parent.' Sir's note on this key: 'That's because the law says \"may.\" … Sir doesn't think this is good law because technology has already improved. Even if the person is already dead, you can still get his DNA to prove filiation. So it's like the law is regressing.'",
      topic="filiat")
p.mcq("samplex", f"{Q5} #15",
      "After the death of the alleged parent, the filiation of an illegitimate child may be established by any of the following, EXCEPT:",
      ["The record of birth appearing in the civil register", "An admission of illegitimate filiation in a public document", "An admission of illegitimate filiation in a private handwritten instrument and signed by the parent concerned",
       "Any other means allowed by the Rules of Court and special laws.", "none of the above"], "d",
      "Codal answer: (d), because Art. 175's last paragraph limits actions based on the 2nd paragraph of Art. 172 (which includes 'any other means') to the alleged parent's lifetime. Sir, however, reads 'may' as permissive and cites Aquino v. Aquino and Yap v. Yap for DNA proof after death, so (e) was also defended.",
      key="The class notes record 'D or E'. Answer D on the codal; explain E (Aquino; Yap) if there is room.", topic="filiat")
p.tf("samplex", f"{Q1} TF5 (annotated copy)", "The filiation of illegitimate children may be established by the open and continuous possession of the status of a child after the death of the alleged parent.", False,
     "Art. 175, 2nd par.: an action based on open and continuous possession (2nd par. of Art. 172) may be brought only during the lifetime of the alleged parent. (The annotated copy writes 'w/in the lifetime' over 'after the death'.)",
     key="In the 2025 Quiz 2 discussion of the same statement, the class answered TRUE and Sir mused that 'may' is not mandatory (DNA; Aquino; Yap). The older key is FALSE, which is the codal answer.", topic="filiat")
p.mcq("samplex", f"{MT} Part Two #45",
      "After the death of the alleged parent, the filiation of the child may NOT be established by:",
      ["Record of birth appearing in the civil register.", "Final judgment.", "An admission of legitimate filiation in a public document and signed by the parent concerned.",
       "The open and continuous possession of the status of a legitimate child.", "None of the above."], "e",
      "The stem says 'the child', not 'an illegitimate child'. For legitimate filiation, the action may be brought by the child during his or her lifetime (Art. 173), and the parent's death bars none of the Art. 172 proofs. Compare the illegitimate-child version (keyed d).", topic="filiat")
p.pair("samplex", f"{MT} Part One #8",
       "Illegitimate children may establish their illegitimate filiation in the same way and on the same evidence as legitimate children.",
       "Property acquired before the marriage by either spouse who has a child prior to the marriage shall be excluded from the community property.",
       True, False,
       "No. 1 is TRUE (Art. 175). No. 2 is FALSE: Art. 92(3) excludes property acquired before the marriage by either spouse 'who has LEGITIMATE DESCENDANTS BY A FORMER MARRIAGE'.", topic="filiat")
p.tf("samplex", "Uribe Quiz No. 4 TF2", "The action to claim legitimacy may be brought by the child during his or her lifetime and shall be transmitted to the heirs should the child die during minority or in a state of insanity.", True,
     "Verbatim Art. 173. The heirs then have five years to sue, and an action already commenced by the child survives the death of either or both parties.", topic="filiat")
p.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "While engaged to be married, Arnold and Josephine agreed in a public instrument to adopt out the economic regime of absolute community of property. Arnold acknowledged in the same instrument that Josephine's daughter Mary, is his illegitimate child. But Josephine died before the marriage could take place. Does the marriage settlement have any significance?",
      ["None, since the instrument containing the marriage settlement is essentially void for containing an unrelated matter.", "Yes, insofar as Arnold acknowledged Mary as his illegitimate child.",
       "None, since the marriage did not take place.", "Yes, if they acquired properties while living together as husband and wife."], "b",
      "The settlement lapsed (Art. 81), but the acknowledgment is an admission of filiation in a public document signed by the parent (Arts. 172(2), 175).", topic="filiat")
p.tf("bar", "UP BOC – 2015 Bar (adapted)", "A son born in 1981 to Julie and a married man, who supported him and regularly spent time with him but never recognized him in the birth certificate or in any writing, may, after the father's death in 2000 when the son was already 18, file an action to establish his illegitimate filiation based on open and continuous possession of status.", False,
     "UPLC answer: under Art. 175, an action based on open and continuous possession must be filed during the lifetime of the putative father; NCC 285's exception (father dies during the child's minority) does not apply because the child was no longer a minor. Sir disagrees with the lifetime limit (DNA; Aquino; Yap), so mention it in an essay.",
     key="Codal/bar answer: FALSE.", topic="filiat")
p.tf("bar", "UP BOC – 2015 Bar (adapted)", "In the same case, the court may approve a compromise in which the child abandons his petition for recognition in exchange for what he would have received as an illegitimate child.", False,
     "UPLC answer: filiation is a matter for the law; it is not for the parties to stipulate whether a person is a legitimate or illegitimate child (De Jesus v. Estate of Dizon; NCC 2035(1): no compromise on civil status). An alternative answer would allow it as not involving future inheritance.",
     key="Bar answers differ; the UPLC answer (no) rests on NCC 2035(1).", topic="filiat")
p.mcq("bar", "UP BOC – 2009 Bar (adapted to MCQ)",
      "Four children were born to the spouses Conrado and Clarita; their birth certificates were signed by Conrado as their father. Later, Edilberto executed a notarial document acknowledging two of them as his illegitimate children with Clarita, and died. May the two share in Edilberto's estate?",
      ["Yes, because a notarial acknowledgment is primary evidence of filiation", "Yes, because Edilberto is their biological father",
       "No; they are the legitimate children of Conrado and Clarita until Conrado successfully impugns their legitimacy, and a person cannot have two natural filiations", "No, because the acknowledgment was not in a will"], "c",
      "UPLC answer: their legitimate status was conferred by law at birth and can be changed only if the husband successfully impugns it. They cannot be the illegitimate children of Edilberto at the same time.", topic="filiat")
p.tf("recit", f"{SIT}", "If the only evidence presented as proof of filiation is a birth certificate with the name of the putative father, which he did not sign, that is a sufficient basis that the child is the child of that person.", False,
     "Sir: 'Nope … You can actually put Gokongwei's name.' A birth certificate not signed by the alleged father is incompetent evidence of paternity (Reyes v. CA; Vda. de Alberto v. CA; Baluyut v. Baluyut).", topic="filiat")
p.tf("new", "New (Uribe format; FC 172)", "The filiation of legitimate children is established by the record of birth appearing in the civil register or a final judgment, or by the open and continuous possession of the status of a legitimate child.", False,
     "Not absolutely true. Open and continuous possession of status is SECONDARY evidence, available only 'in the absence of' the record of birth, final judgment, or a signed admission in a public document or private handwritten instrument (Art. 172, 2nd par.).", topic="filiat")
p.mcq("new", "New (FC 172)",
      "Which of the following is PRIMARY evidence of filiation under Article 172?",
      ["The open and continuous possession of the status of a child", "A baptismal certificate naming the father",
       "An admission of filiation in a private handwritten instrument signed by the parent concerned", "Testimony of relatives on family reputation"], "c",
      "Art. 172, 1st par.: (1) the record of birth or a final judgment; (2) an admission in a public document or a private handwritten instrument signed by the parent. A and D are secondary; B is not proof of filiation (Mendoza v. IAC; Perla v. Baring).", topic="filiat")
p.tf("new", "New (Uribe format; Lim v. CA)", "A marriage contract of the child, in which the alleged father is named as her father, is a public document of recognition sufficient to prove filiation.", False,
     "Lim v. CA (1975): a marriage contract is a mere declaration by the contracting parties, not an instrument executed before and certified by a notary; it does not have the requisites of a public document of recognition.", topic="filiat")
p.mcq("new", "New (Mendoza v. CA)",
      "To establish open and continuous possession of the status of an illegitimate child, which must be shown?",
      ["That the father acknowledged the child in a public document", "That the father treated the child as his own, directly and not through others, spontaneously and without concealment, with a permanent intention shown by continuous and clear manifestations of paternal affection and care",
       "That the child always used the father's surname", "That the child lived with the father"], "b",
      "Mendoza v. CA (1991). 'Continuous' means not intermittent while it continues. Money given 'off-and-on' through relatives was not enough. Using the surname and living together are relevant but not decisive.", topic="filiat")
p.tf("new", "New (Uribe format; FC 173)", "The action to claim legitimacy may be brought by the child within five years from attaining the age of majority.", False,
     "Art. 173: during the child's LIFETIME (imprescriptible for the child). The five-year period applies to the HEIRS, when the action is transmitted because the child died during minority or in a state of insanity.", topic="filiat")
p.mcq("new", "New (RPC 345; People v. Rizo; People v. Barranco)",
      "A married man is convicted of rape, and a child is born of the crime. The court may order him to:",
      ["acknowledge the child as his legitimate child", "acknowledge the child as his illegitimate child", "support the child, but not acknowledge it", "neither acknowledge nor support the child"], "c",
      "RPC 345: acknowledge the offspring 'unless the law should prevent him from so doing', and 'in every case' support it. A married offender cannot be compelled to recognize the child (People v. Rizo; People v. Barranco).", topic="filiat")
p.tf("new", "New (Uribe format; Dempsey v. RTC)", "In a criminal case where the accused pleaded guilty, the court may order him, as part of the civil liability, to recognize the child as his natural child even if the issue of recognition was not specifically heard and tried.", False,
     "Dempsey v. RTC (1988): reversible error. Recognition is governed by the Civil Code and the Family Code; where it was not specifically and fully heard and tried, it cannot be ordered as part of the civil liability.", topic="filiat")

# ---- Legitimation (FC 177–182)
MTC = "Uribe CivRev Midterm (with Prof's answer)"
p.pair("samplex", f"{MTC} #4",
       "If A & B were married in 1989 with a verbal agreement for a conjugal partnership of gains, a donation in consideration of marriage by A to B in excess of 20% of his present property is void.",
       "Children conceived and born outside of wedlock of parents who, at the time of the birth of the former, were not disqualified by any impediment to marry each other may be legitimated.",
       False, False,
       "Prof's answer: both FALSE (B). No. 1: a verbal settlement is void, so the ACP governs (Art. 75) and the one-fifth cap of Art. 84 applies only to a regime other than ACP. No. 2: Art. 177 reckons the absence of impediment at the time of CONCEPTION, not birth; and Sir stressed that 'may be' still needs another requirement, a subsequent valid marriage of the parents.",
       key="The class answered D (No. 2 true); Prof's answer was B.", topic="filiat")
p.tf("samplex", f"{Q5} #3 (= Quiz No. 4 TF3)", "Children conceived and born outside of wedlock may be legitimated.", True,
     "Art. 177: they 'may be' legitimated if, at conception, the parents were not disqualified by any impediment (or only because either or both were below 18), and they later validly marry (Art. 178). Sir: answer only what is asked (not the retroactive effect), and note 'may', not 'will'. An impediment that arises only at birth, after a clean conception, does not bar legitimation.", topic="filiat")
p.tf("samplex", f"{Q5} #4 (= Quiz No. 4 TF4)", "The effects of legitimation shall retroact to the time of the child's birth.", True,
     "Verbatim Art. 180.", topic="filiat")
p.tf("samplex", "Uribe Quiz No. 4 TF5", "Legitimation may be impugned only by those who are prejudiced in their rights within one year from the time their cause of action accrues.", False,
     "Art. 182: within FIVE years from the time their cause of action accrues.", topic="filiat")
p.tf("samplex", f"{QC3} TF7", "The annulment of a voidable marriage shall not affect the legitimation.", True,
     "Verbatim Art. 178, 2nd sentence. If the subsequent marriage is VOID, there is no legitimation (2010 Bar: Venus).", topic="filiat")
p.tf("samplex", f"{QC3} TF8", "The legitimation of children who died before the celebration of the marriage shall benefit their descendants.", True,
     "Verbatim Art. 181, a consequence of the retroactivity in Art. 180.", topic="filiat")
p.pair("samplex", f"{MT} Part One #9",
       "In case of death, absence or unsuitability of the parents, substitute parental authority shall be exercised by the oldest brother or sister.",
       "Only children conceived or born outside of wedlock of parents who, at the time of the conception of the former, were not capacitated to marry each other may be legitimated.",
       False, False,
       "No. 1 is FALSE: Art. 214: by the surviving grandparent (the oldest brother or sister over 21 comes next, Art. 216). No. 2 is FALSE: Art. 177 says conceived AND born outside of wedlock, of parents who were NOT DISQUALIFIED BY ANY IMPEDIMENT (impediment, not capacity), and since R.A. 9858 also parents disqualified only because either or both were below 18.", topic="filiat")
p.mcq("samplex", f"{MT} Part Two #47",
      "Under the family code, these children can be legitimated:",
      ["Adulterous.", "Bigamous.", "Incestuous.", "All of the above.", "None of the above."], "e",
      "Each was conceived when the parents were disqualified by an impediment to marry each other (an existing marriage, or a relationship under Arts. 37–38), so none can be legitimated (Art. 177).", topic="filiat")
p.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "X, a married man, cohabited with Y, an unmarried woman. Their relation bore them BB, a baby boy. Subsequently, after X became a widower, he married Y. Was BB legitimated by that marriage?",
      ["Yes, since his parents are now lawfully married.", "Yes, since he is an innocent party and the marriage rectified the wrong done him.", "No, since once illegitimate, a child shall always remain illegitimate.", "No, since his parents were not qualified to marry each other when he was conceived."], "d",
      "Art. 177: the impediment (X's existing marriage) is tested at conception; its later disappearance does not help. C is wrong because legitimable illegitimate children do become legitimated.", topic="filiat")
p.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "X and Y, although not suffering from any impediment, cohabited as husband and wife without the benefit of marriage. Following the birth of their child, the couple got married. A year after, however, the court annulled the marriage and issued a decree of annulment. What is the present status of the child?",
      ["Legitimated", "Illegitimate", "Natural child", "Legitimate"], "a",
      "Art. 178: 'The annulment of a voidable marriage shall not affect the legitimation.'", topic="filiat")
p.tf("bar", "UP BOC – 2010 Bar (adapted)", "B and G, with no impediment, had a child, Venus, and then married each other without a marriage license; the marriage was later declared void. Venus remains a legitimated child.", False,
     "Bar answer: Venus is illegitimate. Art. 178 requires a subsequent VALID marriage; only the annulment of a voidable marriage leaves the legitimation intact. A void marriage legitimates no one.", topic="filiat")
p.tf("bar", "UP BOC – 2009 Bar (True or False)", "A dead child can be legitimated.", True,
     "Bar answer: the law does not require the child to be alive at the parents' marriage (Art. 177), and Art. 181 provides that the legitimation of children who died before the marriage benefits their descendants.", topic="filiat")
p.tf("bar", "QuAMTO – 2018 Bar (adapted)", "Sabina was born of an illicit relationship while her father, Sinclair, was married to another. After his wife died, Sinclair married Sabina's mother. Sabina was legitimated by that marriage.", False,
     "Bar answer: at Sabina's conception her parents were disqualified by an impediment (Sinclair's existing marriage), so she cannot be legitimated (Art. 177); she remains illegitimate (Art. 165). (Their marriage without a license, claiming 20 years of cohabitation, would be void anyway, since the cohabitation was not free of impediment.)", topic="filiat")
p.tf("recit", f"{TSR} (adapted)", "A child conceived when both parents were 16 years old and single cannot be legitimated by their subsequent valid marriage when they reach 18, because they were disqualified to marry at the time of conception.", False,
     "Art. 177, as amended by R.A. 9858: '… or were so disqualified only because either or both of them were below eighteen (18) years of age, may be legitimated.' Sir: 'AGE is not legal impediment but capacity … so long as the marriage is a valid marriage.'", topic="filiat")
p.mcq("recit", f"{SIT} (adapted to MCQ)",
      "A and B, both 25 and single, lived together, and C was conceived. Before C's birth, B married X. C was born during that marriage, and X later died. A and B then married each other. Under Sir's analysis, was C legitimated?",
      ["No, because C was born while B was married to X", "Yes, because the law requires only that there was no impediment at the time of conception", "No, because legitimation requires conception and birth outside of wedlock", "Yes, because A acknowledged C"], "b",
      "Sir (2018): 'Law only requires that the child was CONCEIVED during the time when there was no legal impediment to marriage. No issue as to impediments during the birth. 38, 37: legal impediments.' (Note that C, born during B's marriage to X, is also presumed X's child under Art. 164 until that is overthrown; see the reviewer.)",
      key="Sir's recorded answer; the Art. 164 presumption in favor of X is an issue to flag in an essay.", topic="filiat")
p.tf("new", "New (Uribe format; FC 177)", "Children conceived and born outside of wedlock of parents who, at the time of conception of the former, were not disqualified by any impediment to marry each other will be legitimated.", False,
     "Art. 177: 'MAY be legitimated'. Legitimation still requires a subsequent valid marriage between the parents (Art. 178). Sir in Quiz 5: 'Will be legitimated and not may be legitimated' was the error.", topic="filiat")
p.tf("new", "New (Uribe format; FC 178)", "Legitimation shall take place by a subsequent valid marriage between parents. The annulment of a voidable marriage shall not affect the legitimation.", True,
     "Verbatim Art. 178. If the subsequent marriage is void, there is no legitimation.", topic="filiat")
p.mcq("new", "New (FC 177)",
      "X, married to Y, had a child, C, with Z, who was single. After Y died, X married Z. Was C legitimated?",
      ["Yes, by the subsequent valid marriage of X and Z", "Yes, retroactive to C's birth", "No, because X was disqualified by an impediment (his existing marriage) at the time of C's conception", "No, because X did not acknowledge C"], "c",
      "Art. 177: the impediment is tested at conception; its later disappearance does not help (Tolentino). Tolentino notes the inconsistency: had X and Z contracted a void bigamous marriage, C would have been legitimate under Art. 54 if that marriage was under Art. 53.", topic="filiat")
p.mcq("new", "New (FC 180–181)",
      "Which statement on the effects of legitimation is correct?",
      ["Legitimation takes effect from the date of the subsequent marriage", "Legitimation of a child who died before the marriage benefits no one",
       "Legitimation retroacts to the time of the child's birth, and the legitimation of children who died before the marriage benefits their descendants", "Legitimated children have the rights of illegitimate children until they reach majority"], "c",
      "Arts. 180 and 181. Art. 179: legitimated children enjoy the same rights as legitimate children.", topic="filiat")
p.tf("new", "New (Uribe format; FC 182)", "Legitimation may be impugned by any interested party within four years from the time the cause of action accrues.", False,
     "Art. 182: 'only by those who are PREJUDICED IN THEIR RIGHTS, within FIVE years from the time their cause of action accrues.' (The syllabus misprints the article as 162.)", topic="filiat")
p.write("12_patern.json")
