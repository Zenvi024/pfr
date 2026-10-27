from qb import Bank

# ============ ADOPTION THROUGH CIVIL REGISTER (syllabus XIV–XXII) ============
QC1 = "Uribe Quiz Compilation, Set 1"
QC3 = "Uribe Quiz Compilation, Set 3 (= Quiz No. 4)"
Q4R = "Uribe Quiz No. 4 (Civil Law Reviewer copy)"
CRS = "Civ Rev samplex quiz"
CRT = "Civ Rev samplex T/F compilation"
MT = "Uribe Midterm Exam (Civ Rev samplex)"
Q2 = "Uribe CivRev 2025 Quiz 2 (Aug 28, 2025)"
Q2C = "Uribe CivRev 2025 Quiz 2, continuation (Sep 4, 2025)"
Q3K = "PFR Quiz 3 answer key"
AD = "Uribe CivRev 2025 adoption quiz discussion"
SUC = "Uribe succession quiz compilation"

# ---------------------------------- ADOPTION ----------------------------------
a = Bank("adopt", "AD")
a.tf("samplex", f"{QC3} TF2; {CRT} #46", "Only minors may be adopted.", False,
     "FC 183, 2nd par. already allowed adults in the cases provided (FC 187(1)): a child by nature of the adopter or his spouse, or one consistently treated as the adopter's own during minority. R.A. 11642, Sec. 22(c), (d), (h): an illegitimate child by a qualified adopter, a Filipino of legal age treated as their own for at least 3 years, a relative of the adopter. Key note: 'Illegitimate child may be adopted by parent regardless of age.'")
a.tf("samplex", f"{Q4R} TF6", "The adopter must be at least sixteen years older than the adoptee.", False,
     "The 16-year gap may be waived when the adopter is the biological parent of the adoptee or the spouse of the adoptee's parent (R.A. 8552, Sec. 7; R.A. 11642, Sec. 21(a)). Discussion: 'This is just the general rule. There are exceptions.'")
a.tf("samplex", f"{AD} (legal age item)", "A Filipino citizen of legal age, in possession of full civil capacity and legal rights, may adopt.", False,
     "Under R.A. 11642, Sec. 21(a), the adopter must be at least TWENTY-FIVE. Sir: 'Kung sinabi mong at least of legal age, pwede na 19 or 18. But when the law requires 25, kung 24 palang siya, di pa siya pwedeng mag-adopt.' (Under R.A. 8552 and the FC, legal age was enough, which still governs petitions filed then.)")
a.tf("samplex", f"{Q2} #7", "Husband and wife must jointly adopt if one seeks to adopt his own illegitimate child.", False,
     "Sir: 'The law provides that consent is only needed and not adopt jointly. Consent ≠ Joint Adoption.' One spouse may adopt alone (1) the legitimate child of the other, (2) his own illegitimate child, with the other spouse's consent, or (3) if legally separated (R.A. 8552, Sec. 7; R.A. 11642, Sec. 21).")
a.mcq("samplex", f"{QC3} MC8; {CRS} #19",
      "In case of adoption, husband and wife shall exercise joint parental authority in the following cases, except:",
      ["If husband and wife jointly adopt", "One spouse adopts the [legitimate] child of the other", "One spouse seeks to adopt his own illegitimate child", "All of the above", "None of the above"], "c",
      "Joint parental authority: joint adoption, or one spouse adopting the legitimate child of the other (FC 186; R.A. 11642, Sec. 42). Key note on (c): 'the adopting spouse needs the consent of the other, but this doesn't mean that they must jointly adopt. Consent does not lead to parental authority.' (Some copies print (b) as 'the illegitimate child of the other'; the law says legitimate.)")
a.mcq("samplex", f"{CRS} #17", "The consent of the following is required to the adoption, except:",
      ["Adoptee, if 10 years old or over", "Biological parents of adoptee, if known", "Spouse of adopter", "Parents of adopter", "All of the above", "None of the above"], "d",
      "Sec. 9, R.A. 8552; Sec. 23, R.A. 11642: the adoptee 10 or over; biological parents or guardian; legitimate and adopted children 10 or over; illegitimate children 10 or over living with the adopter; spouses of the adopter and adoptee. The adopter's parents are not listed. Sir: under R.A. 11642 the adoptee inherits from the adopter's parents (Sec. 41), yet their consent is not required.")
a.mcq("samplex", f"{QC3} MC6", "The consent of the following is not required, except:",
      ["Adoptee, if 7 years or over", "Siblings of adoptee, if known", "Spouse of adoptee", "Parents of adopter", "All of the above", "None of the above"], "c",
      "The spouse of the person to be adopted must consent (an adult may be adopted, so he may be married). The age for the adoptee's consent is 10, not 7; the adoptee's siblings and the adopter's parents are not listed.")
a.mcq("samplex", f"{QC3} MC7; {CRS} #18", "The following are necessary for a Filipino to be able to adopt, except:",
      ["Of legal age", "Of good moral character", "Has not been convicted of any crime involving moral turpitude", "Emotionally and psychologically capable of caring for children", "None of the above"], "a",
      "Sir's basis in the 2025 discussion: (a), because R.A. 11642 requires the adopter to be at least 25; legal age is not enough. Under R.A. 8552 (and older keys) the answer was (e) none of the above. One copy of this item reads 'not been convicted of a crime with penalty of more than 6 years', which is also not the statutory test (moral turpitude).",
      key="Older keys: (e). Sir's R.A. 11642 discussion: (a).")
a.mcq("samplex", f"{QC3} MC9; {CRS} #20", "The following are necessary for an alien to be able to adopt, except:",
      ["In a position to support and care for his children", "Of good moral character", "Has not been convicted of any crime involving moral turpitude", "Emotionally and psychologically capable of caring for children", "None of the above"], "e",
      "An alien must have the same qualifications as a Filipino adopter, plus residence (3 years under R.A. 8552; 5 under R.A. 11642), diplomatic relations, and the home country's recognition of the adoption. All four listed are required. Key: 'None of the above.' (The residency requirement may be waived in three cases.)")
a.tf("samplex", f"{CRT} #47", "Legitimate and illegitimate children and descendants and the surviving spouse of the adopted shall inherit from the adopted, in accordance with the ordinary rules of legal or intestate succession.", True,
     "Verbatim FC 190(1). 'This is a verbatim provision.'")
a.tf("samplex", f"{Q4R} TF7", "When the surviving spouse or the illegitimate children of the adopted concur with the adopters, they shall divide the entire estate in equal shares, one-half to be inherited by the spouse or the illegitimate children of the adopted and the other half, by the adopters.", True,
     "Verbatim FC 190(3).")
a.tf("samplex", "Old Uribe quiz (pre-R.A. 11642 key)", "Domestic adoption is essentially judicial.", False,
     "Keyed TRUE in an old quiz (FC, R.A. 8552: decree by the court). Under R.A. 11642 (2022) domestic adoption is ADMINISTRATIVE: the NACC issues the Order of Adoption, appealable to the Court of Appeals. Answer with the current law, noting the old key if allowed.",
     key="Old key TRUE; under R.A. 11642, FALSE.")
a.mcq("recit", f"{AD} (law governing)", "A petition for adoption was filed in 2019 under R.A. 8552 by a 22-year-old Filipino. R.A. 11642 took effect while it was pending. Which statement is correct?",
      ["The petition must be dismissed because the adopter is below 25", "The law in force when the petition was filed governs, so the petitioner's qualification under R.A. 8552 is respected",
       "The petitioner must refile with the NACC", "The petition is automatically converted to an administrative one and the 25-year rule applies"], "b",
      "Sir: 'If the petition was filed during the effectivity of those laws, those laws will apply whether or not that petition should be granted.' Republic v. Miller; Republic v. CA & Bobiles (vested right to adopt). R.A. 11642, Sec. 56 lets pending judicial petitions be withdrawn and refiled to avail of the Act, but does not require it.")
a.mcq("bar", "2014 Bar (adapted)", "Spouses Esteban and Maria raised their minor nieces Faith and Hope. Esteban died; Maria married Daniel, a British national living in the Philippines for two years. With Daniel's permission, Maria alone petitioned to adopt the girls. How should the petition be resolved?",
      ["Granted, because Daniel consented", "Granted, because the girls are Maria's relatives within the 4th degree", "Dismissed, because spouses must adopt jointly and none of the exceptions applies", "Granted, because Esteban raised the girls"], "c",
      "Joint adoption is mandatory except when one spouse adopts the legitimate child of the other, his or her own illegitimate child (with the other's consent), or when they are legally separated (In re Adoption of Lim). Daniel would also have to qualify as an alien adopter in his own right.")
a.mcq("bar", "2012 Bar; In re Adoption of Michelle Lim (adapted)", "Monina, a widow, married Angel, an American, and alone petitioned to adopt Michelle (25) and Michael (18), whose births she and her late husband had simulated. Angel consented. Is dismissal proper?",
      ["No; the adoptees are emancipated, so joint parental authority is unnecessary", "No; Angel's consent suffices", "Yes; spouses must adopt jointly, and Angel must himself qualify as an alien adopter", "Yes; adults can never be adopted"], "c",
      "Lim (2009): 'shall' makes joint adoption mandatory; parental authority is only one effect of adoption, so the adoptees' majority does not matter; Olario's consent cannot substitute for his own qualifications (residency and certification).")
a.mcq("bar", "2003 Bar (adapted)", "Lina, a former Filipino now an American citizen, and her American husband want to jointly adopt Lina's minor brother. They have never lived in the Philippines. May they?",
      ["Yes, both qualify because Lina is a former Filipino", "Lina qualifies (residency waived for a former Filipino adopting a relative within the 4th degree), but her husband must meet the residency requirement; without it they cannot adopt", "No, aliens can never adopt", "Yes, if the brother consents"], "b",
      "Each spouse in a joint adoption must be qualified (Republic v. Toledano). The husband's residency is waived only if he adopts jointly with a FILIPINO spouse a relative of that spouse; Lina is no longer Filipino.")
a.mcq("bar", "2010 Bar (adapted)", "Rex and Lea have children aged 14 and 8. Rex has a 10-year-old illegitimate child by another woman. Lea obtained a decree of legal separation. Whose consent does Rex need to adopt his illegitimate child?",
      ["Lea, the 14-year-old, the 8-year-old and the adoptee", "The 14-year-old, the 10-year-old adoptee, and the adoptee's biological mother", "Only the adoptee's biological mother", "Lea and the adoptee only"], "b",
      "Legitimate children 10 or over, the adoptee 10 or over, and the biological parent. The 8-year-old is only counseled. Lea's consent is unnecessary after legal separation; without it, Rex could still adopt alone but with Lea's consent.")
a.tf("new", "New (R.A. 11642, Sec. 22(g))", "Proceedings for the adoption of a child whose biological parents have died may be initiated one month after their death.", False,
     "No proceedings within SIX MONTHS from the time of death of the parents (Sec. 22(g); also R.A. 8552, Sec. 8(f)).")
a.tf("new", "New (R.A. 11642, Sec. 41)", "Under R.A. 11642, the legitimate filiation created by adoption is limited to the adopter and the adoptee.", False,
     "Sec. 41 extends it to the adopter's parents, legitimate siblings and legitimate descendants. Under the FC and R.A. 8552 the relationship was personal to adopter and adopted (2007 Bar: an adopted granddaughter could not represent).")
a.tf("new", "New (R.A. 11642, Sec. 47)", "The adopter may petition for the rescission of the adoption on any ground for disinheritance.", False,
     "Since R.A. 8552, adoption is not subject to rescission by the adopter; he may only disinherit the adoptee for causes in NCC 919 (Sec. 47; Lahom v. Sibulo).")
a.mcq("new", "New (R.A. 11642, Sec. 47)", "Under R.A. 11642, which is NOT a ground for the adoptee to rescind the adoption?",
      ["Repeated physical or verbal maltreatment by the adopter despite counseling", "Attempt on the life of the adoptee", "Abandonment and failure to comply with parental obligations", "The adopter's remarriage"], "d",
      "Sec. 47 lists three grounds. (R.A. 8552, Sec. 19 also had 'sexual assault or violence'.)")
a.mcq("new", "New (Lahom v. Sibulo)", "Spouses adopted their nephew in 1972. In 1999, after R.A. 8552 took effect, the widow sought to rescind the adoption because he neglected her and refused to use her surname. What is the ruling?",
      ["Granted, since the right to rescind vested in 1972", "Denied; R.A. 8552 removed the adopter's right to rescind, and in any case the action had prescribed; she may disinherit him instead", "Granted, because neglect is a ground for disinheritance", "Denied, because only the adoptee's biological parents may rescind"], "b",
      "Lahom v. Sibulo (2003).")
a.mcq("new", "New (Tamargo v. CA)", "A 10-year-old boy living with his natural parents shot a playmate after a petition for his adoption had been filed but before the decree. Who is liable for damages?",
      ["The adopters, because the decree retroacts to the filing of the petition", "The natural parents, who had actual custody when the act was done", "The State", "No one, since parental authority was in transition"], "b",
      "Tamargo (1992): retroactivity benefits the child; it does not impose liability on adopters who had no custody yet.")
a.mcq("new", "New (Cang v. CA)", "When may the written consent of a biological parent to the adoption be dispensed with?",
      ["When the parent lives abroad", "When the parent has abandoned the child, or is insane or hopelessly intemperate", "When the adopters are wealthier", "When the parent is divorced"], "b",
      "Cang v. CA (1998); Duncan v. CFI. Abandonment means a settled purpose to forgo all parental duties; occasional support and letters negate it.")
a.mcq("new", "New (Sec. 41; Stephanie Garcia)", "Honorato adopted his illegitimate daughter Stephanie, whose mother is Gemma Astorga Garcia. May Stephanie use 'Garcia' as her middle name?",
      ["No, an adoptee may use only the adopter's surname", "Yes; no law prohibits it, and it preserves her maternal lineage", "Only with the mother's written consent", "Only if Honorato is married to Gemma"], "b",
      "In re Adoption of Stephanie Nathy Astorga Garcia (2005); 1996, 2006, 2012 Bar.")
a.mcq("new", "New (R.A. 11222, Secs. 4–5)", "Which is NOT a condition for availing of rectification of a simulated birth record without liability under R.A. 11222?",
      ["The simulation was made before the law took effect", "The simulation was for the best interest of the child", "The child was consistently considered and treated as their own", "The petition is filed within 10 years from the law's effectivity", "The simulating parents are related to the child within the 4th degree"], "e",
      "Sec. 4 lists the first four. For the administrative route (Sec. 5), the child must also have lived with them for at least 3 years before effectivity, and a CDCLAA must issue. Kinship is not required.")
a.tf("new", "New (R.A. 11642, Sec. 54(b))", "Under R.A. 11642, simulation of birth is punished by imprisonment of eight years and one day to ten years and a fine not exceeding ₱50,000.", True,
     "Sec. 54(b). Other violations (coercing consent, noncompliance with procedures, exposing the child to danger) carry 6 years and 1 day to 12 years and/or ₱50,000 to ₱200,000 (Sec. 54(a)).")
a.write("13_adopt.json")

# ---------------------------------- SUPPORT ----------------------------------
s = Bank("support", "SU")
s.tf("samplex", f"{QC3} TF3", "Payment for support shall be made within the first 15 days of each corresponding month.", False,
     "Art. 203: within the first FIVE days of each corresponding month. 'False. Codal provision.'")
s.tf("samplex", f"{Q4R} TF8", "Payment shall be made within the first five days of each corresponding month or when the recipient dies, his heirs shall not be obliged to return what he has received in advance.", True,
     "Verbatim Art. 203, 3rd par.")
s.tf("samplex", f"{QC3} TF4; {CRT} #50", "The person obliged to give support shall fulfill the obligation by paying the allowance fixed.", False,
     "Art. 204: he has the OPTION to pay the allowance fixed OR to receive and maintain the recipient in the family dwelling, unless there is a moral or legal obstacle. 'There are other ways within which such obligation may be met.'")
s.tf("samplex", f"{Q4R} TF9; {CRT} #39", "The person obliged to give support shall fulfill the obligation by receiving and maintaining in the family dwelling the person who has a right to receive support.", False,
     "Art. 204: an option, not a duty; and the dwelling alternative is unavailable when there is a moral or legal obstacle. Discussion: 'The person obliged to give support has an option.'")
s.tf("samplex", f"{QC3} TF9; {Q2} #5; {Q3K}", "Brothers and sisters not legitimately related, whether of the full or half-blood, are likewise bound to support each other.", False,
     "Art. 196 continues: 'except only when the need for support of the brother or sister, being of age, is due to a cause imputable to the claimant's fault or negligence.' Sir: don't attack the premise ('brothers and sisters not legitimately related, whether of the full or half-blood' is correct); the unqualified conclusion is what is false. The Art. 196 exception does not apply to ascendants and descendants.")
s.tf("samplex", f"{Q4R} TF10", "When, without the knowledge of the person obliged to give support, it is given by a stranger, the latter shall have a right to claim the same from the former.", False,
     "Art. 206 adds: 'unless it appears that he gave it without intention of being reimbursed.'")
s.tf("samplex", f"{CRT} #48", "When the obligation to give support falls upon two or more persons, the payment of the same shall be divided between them in proportion to the resources of each.", True,
     "Verbatim Art. 200, 1st par.")
s.mcq("samplex", f"{Q2C}", "If the spouse has no capacity to support or is dead, the children are required to give support:",
      ["Equally", "In proportion to the resources of each", "In the order of their birth", "Only the eldest", "None of the above"], "b",
      "Art. 200: 'divided between them in proportion to the resources of each'. Sir rejected 'equally' and also the answer that it passes automatically to brothers and sisters: after the spouse come the descendants (Art. 199).")
s.mcq("samplex", "Uribe quiz (Civ Rev samplex) MC20; OCR copy reads 'to Melitona'", "Natividad is the widow of Mariano. Melitona is her mother. Rupert is her grandchild. Generoso is her brother. Crescente is her nephew. Who will first be compelled to give support to Natividad?",
      ["Melitona", "Rupert", "Generoso", "Crescente"], "b",
      "Art. 199: (1) spouse (dead), (2) descendants in the nearest degree (grandchild Rupert, there being no children mentioned), (3) ascendants (Melitona), (4) brothers and sisters (Generoso). A nephew is not obliged at all (Art. 195).",
      key="The scanned copy reads 'support to Melitona', which cannot be right since Melitona is an option; read as support to Natividad.")
s.mcq("samplex", f"{MT} Part Two #34", "The obligation of mutual support between spouses ceases after the following, except:",
      ["Dissolution of the marriage by the death of a spouse", "Declaration of nullity", "Annulment of marriage", "Legal separation", "None of the above"], "e",
      "Death ends the marriage and the obligation; Art. 198: 'After the final judgment granting the petition [for legal separation, annulment or nullity], the obligation of mutual support between the spouses ceases.' In legal separation the court MAY order the guilty spouse to support the innocent one, but that is a discretionary order, not mutual support.")
s.mcq("bar", "2011 Bar", "Spouses X and Y have a minor daughter, Z, who needs support for her education. Both X and Y are financially distressed. Z's other relatives are financially capable. From whom may Z first rightfully demand support?",
      ["Grandfather", "Brother", "Uncle", "First cousin"], "a",
      "Art. 199: after the parents, the ascendants in the nearest degree come before brothers and sisters; uncles and cousins are not obliged. Lim v. Lim: grandparents are liable on the parents' inability, not only on default.")
s.mcq("bar", "2011 Bar", "Is the wife who leaves her husband without just cause entitled to support?",
      ["No, because the wife must always be submissive and respectful to the husband", "Yes; the marriage not having been dissolved, the husband continues to have an obligation to support his wife",
       "No, because in leaving the conjugal home without just cause, she forfeits her right to support", "Yes, since the right to receive support is not subject to any condition"], "c",
      "UPLC answer (C). Separate maintenance presupposes a justifiable cause to live apart (Lerma; Goitia).")
s.mcq("bar", "2008 Bar (adapted)", "Andrew, unmarried, has a daughter Amy (30) by Brenda, sons Jon and Ryan by Carla, lives with Jane (Elena's daughter by another man), and with Sandy, whom he and Fe 'informally adopted'. In his old age, from whom may Andrew claim support?",
      ["All five", "Amy, Jon and Ryan only", "Amy, Jon, Ryan and Sandy", "Only the legitimate children"], "b",
      "Jane is not his child; Sandy was never legally adopted. His illegitimate children owe him support (Art. 195(4)). Amy, Jon and Ryan also owe each other support under Art. 196 (subject to its exception).")
s.tf("new", "New (Uribe format; Art. 194)", "The education of the person entitled to be supported shall include his schooling or training for some profession, trade or vocation, but only until the age of majority.", False,
     "Art. 194: 'even beyond the age of majority'. 2010 Bar: children aged 18 and 19 who squandered their education fund may still ask for support.")
s.tf("new", "New (Uribe format; Art. 198)", "During the proceedings for legal separation, annulment or declaration of nullity, the spouses and their children shall be supported from their separate properties.", False,
     "Art. 198: from the properties of the absolute community or the conjugal partnership.")
s.tf("new", "New (Uribe format; Art. 200)", "When the spouse and a child subject to parental authority claim support at the same time from one person who cannot satisfy both, the spouse shall be preferred.", False,
     "Art. 200, last par.: the CHILD shall be preferred. Tolentino: the preference applies when support comes from the obligor's separate property, not from the ACP or CPG.")
s.tf("new", "New (Uribe format; Art. 203)", "The obligation to give support shall be demandable from the time the person who has a right to receive the same needs it for maintenance, and shall be paid from that time.", False,
     "Art. 203: demandable from need, but 'it shall not be paid except from the date of judicial or extra-judicial demand.'")
s.tf("new", "New (Art. 205)", "The right to receive support as well as any money or property obtained as such support shall not be levied upon on attachment or execution.", True,
     "Verbatim Art. 205. But the excess of contractual or testamentary support over legal support may be levied (Art. 208).")
s.mcq("new", "New (Arts. 195–196)", "Which of the following persons are NOT legally obliged to support each other?",
      ["A grandmother and her illegitimate granddaughter", "Legitimate half-brothers", "A man and his mother-in-law", "A father and his illegitimate son"], "c",
      "Relatives by affinity are not in Art. 195 (Pelayo v. Lauron: the parents-in-law do not answer for the daughter-in-law's medical bills; the husband does).")
s.mcq("new", "New (Canonizado v. Benitez)", "A wife who had a judgment for support later obtained a well-paying job. Which statement is correct?",
      ["Her right to support is extinguished permanently", "The demandability of support is suspended while she does not need it, but the right subsists and the judgment may be enforced again", "The judgment for support is final and cannot be touched", "The husband may recover all past payments"], "b",
      "Canonizado (1984): the old NCC 303 circumstances 'do not affect the right to support between spouses but only the action to make it demandable'; 'a judgment for support is never final'.")
s.mcq("new", "New (support pendente lite)", "In a wife's action for legal separation, the husband opposes her application for support pendente lite by alleging, without evidence, that she committed adultery. What should the court do?",
      ["Deny support pendente lite outright", "Grant it, because adultery must be established by competent evidence, not merely alleged", "Suspend the case until the criminal case for adultery is decided", "Order the husband to pay only half"], "b",
      "Reyes v. Ines-Luciano; Sanchez v. Zulueta (the court should let him present evidence, and decide on the kind of evidence it deems sufficient). If adultery is established prima facie, support pendente lite is denied (Lerma).")
s.mcq("new", "New (Art. 197)", "From what property is the support of a spouse's illegitimate child taken?",
      ["The absolute community, as a charge", "The separate property of the parent-spouse; if none, the community advances it, to be deducted from his share at liquidation", "The separate property of the other spouse", "The family home"], "b",
      "Arts. 197, 94(9), 122.")
s.mcq("new", "New (Art. 207 vs. 206)", "A father unjustly refuses to support his minor child, who urgently needs surgery. A neighbor pays for it. May the neighbor recover from the father?",
      ["No, because he paid with the father's knowledge", "Yes, under Art. 207: any third person may furnish support when the obligor unjustly refuses, with right of reimbursement", "No, because the neighbor is not a relative", "Only if the father later consents"], "b",
      "Art. 207 does not require that the obligor be unaware; it applies particularly to parents who refuse to support minor children. Art. 206 (without knowledge, by a stranger) is the other route.")
s.write("14_support.json")

# ------------------------------ PARENTAL AUTHORITY ------------------------------
p = Bank("pa", "PA")
p.tf("samplex", f"{Q2} #6; {Q3K} #20", "In case of death, absence or unsuitability of the parents, special parental authority shall be exercised by the surviving grandparent.", False,
     "That is SUBSTITUTE parental authority (Arts. 214, 216). Special parental authority belongs to the school, its administrators and teachers, or those engaged in child care (Art. 218).")
p.tf("samplex", f"{QC3} TF10", "In case of death, absence or unsuitability of the parents, substitute parental authority shall be exercised by the surviving grandparents.", False,
     "Art. 214: 'the surviving GRANDPARENT. In case several survive, the one designated by the court.' Key: 'Grandparent only, the surviving, or the one appointed by the court, not grandparents.'")
p.tf("new", "New (Uribe format; Art. 211)", "The father and the mother shall jointly exercise parental authority over the persons of their common children. In case of disagreement, the court shall decide.", False,
     "Art. 211: the FATHER's decision shall prevail, unless there is a judicial order to the contrary. Same rule for the child's property (Art. 225).")
p.tf("new", "New (Uribe format; Art. 212)", "The remarriage of the surviving parent shall terminate his or her parental authority over the children.", False,
     "Art. 212: remarriage 'shall not affect' parental authority, unless the court appoints another person as guardian of the children's person or property.")
p.tf("new", "New (Uribe format; Art. 213)", "No child under seven years of age shall be separated from the mother unless the court finds compelling reasons to order otherwise.", True,
     "Art. 213, 2nd par. (also NCC 363). Compelling reasons: neglect, abandonment, unemployment, immorality, habitual drunkenness, drug addiction, maltreatment, insanity, highly communicable disease (Perez v. CA; 2006 Bar).")
p.tf("new", "New (Uribe format; Art. 210)", "Parental authority and responsibility may be renounced or transferred by a public instrument.", False,
     "Art. 210: not renounced or transferred 'except in the cases authorized by law' (adoption, guardianship, surrender to a children's home: Eslao).")
p.tf("new", "New (Uribe format; Art. 216)", "In default of parents or a judicially appointed guardian, the oldest brother or sister over eighteen years of age shall exercise substitute parental authority ahead of the surviving grandparent.", False,
     "Art. 216: (1) the surviving grandparent, (2) the oldest brother or sister OVER TWENTY-ONE, unless unfit or disqualified, (3) the child's actual custodian over 21.")
p.tf("new", "New (Uribe format; Art. 219)", "The school, its administrators and teachers shall be subsidiarily liable for damages caused by the acts or omissions of the unemancipated minor under their supervision.", False,
     "Art. 219: PRINCIPALLY and SOLIDARILY liable. The PARENTS, judicial guardians or substitutes are subsidiarily liable.")
p.tf("new", "New (Uribe format; Art. 233)", "The school administrator or teacher exercising special parental authority may inflict reasonable corporal punishment upon the child.", False,
     "Art. 233: 'In no case' may they inflict corporal punishment.")
p.tf("new", "New (Uribe format; Art. 215)", "No descendant shall be compelled, in a criminal case, to testify against his parents and grandparents, without exception.", False,
     "Art. 215: except when the testimony is indispensable in a crime against the descendant or by one parent against the other.")
p.tf("new", "New (Uribe format; Art. 225)", "Where the market value of the property or the annual income of the child exceeds ₱50,000, the parent concerned shall furnish a bond of not less than ten per cent of the value of the property or annual income.", True,
     "Art. 225, 2nd par.")
p.tf("new", "New (Uribe format; Art. 230)", "Parental authority suspended upon conviction of a crime carrying civil interdiction is revived only by a final judgment of the court.", False,
     "Art. 230: AUTOMATICALLY reinstated upon service of the penalty or upon pardon or amnesty.")
p.tf("new", "New (Uribe format; Art. 232)", "If the person exercising parental authority has subjected the child to sexual abuse, such person shall be permanently deprived by the court of such authority.", True,
     "Art. 232. Compare Art. 231(4): acts of lasciviousness are a ground for suspension (or deprivation if serious).")
p.mcq("bar", "2004 Bar (adapted)", "Which statement correctly distinguishes substitute from special parental authority?",
      ["Both displace the parents' authority", "Substitute parental authority displaces parental authority; special parental authority concurs with it and lasts only while the child is in the school's custody",
       "Special parental authority displaces parental authority", "Both are exercised only by relatives"], "b", "2004 Bar suggested answer.")
p.mcq("bar", "2003 Bar (adapted)", "During class hours, while the teacher chatted with other teachers in the corridor, a 7-year-old pupil blinded a classmate with a ball pen in a fight. Who are liable?",
      ["Only the pupil's parents", "The teacher and school authorities, principally and solidarily; the pupil's parents, subsidiarily", "Only the teacher", "No one, because the pupil is below 9"], "b",
      "Arts. 218–219; the teacher was negligent in leaving the class.")
p.mcq("bar", "2010 Bar (adapted)", "Rozanno, 16, drove classmates on a school field trip at his teacher's request in May 1989 and caused a fatal collision. Who is liable?",
      ["Only Rozanno", "The school, its administrators and teachers under Arts. 218–219 (an authorized activity outside the premises), with Rozanno's parents subsidiarily liable", "Only the jeepney driver", "The parents only, because the trip was outside the school"], "b",
      "Special parental authority covers 'all authorized activities whether inside or outside the premises'. Had it happened in 1994 (Rozanno 21), Arts. 218–221 would not apply.")
p.mcq("bar", "2023 Bar (adapted)", "Anita, an entertainer in a men's club, has a one-year-old daughter, Marisol, by Billy, her patron. She provides a house, a nanny and necessities. Billy petitions for custody, citing her work. How should the court rule?",
      ["For Billy, because Anita's work is immoral", "For Anita: the illegitimate child is under her sole parental authority, the child is below seven, and her work alone is not a compelling reason", "Joint custody", "For the maternal grandmother"], "b",
      "Art. 176; Art. 213, 2nd par.; Perez v. CA. Compare the 2024 Bar (a mother's lesbian relationship is not by itself a compelling reason).")
p.mcq("new", "New (Briones v. Miguel)", "The father of an illegitimate child recognized the child and is far richer than the mother. Who has parental authority and custody?",
      ["The father, because he recognized the child", "The mother, unless she is shown unfit; recognition gives the father a ground for support and visitation, not custody", "Both jointly", "The court must choose the richer parent"], "b",
      "Briones v. Miguel (2004); David v. CA; Art. 176.")
p.mcq("new", "New (Salvosa v. IAC)", "When is a student 'in the custody' of the school for purposes of NCC 2180?",
      ["Only while in the classroom", "Whenever he is enrolled", "While at attendance in the school, including recess time", "Only during authorized activities outside the school"], "c",
      "Salvosa: protective and supervisory custody 'for as long as they are at attendance in the school, including recess time'. A student who shot someone on campus when he should have been home was not in the school's custody.")
p.mcq("new", "New (Amadora v. CA)", "A student went to the school auditorium after classes had formally ended to submit a required report and was shot by a classmate. Under NCC 2180, who may be liable?",
      ["The rector, the principal and the dean of boys", "The teacher-in-charge, if negligent, because the student was in the school's custody for a legitimate purpose", "No one, because classes had ended", "The school itself under Art. 2180"], "b",
      "Amadora (1988). The heads exercised only general authority; the school itself is not directly liable under NCC 2180 (but see Art. 218–219).")
p.mcq("new", "New (St. Mary's v. Carpitanos)", "During a school enrollment drive, a student died when a jeep driven by a minor turned over because its steering wheel guide detached. Is the school liable under Arts. 218–219?",
      ["Yes, always, because it was a school activity", "No, because the school's negligence was not the proximate cause of the accident", "Yes, solidarily with the jeep owner", "No, because enrollment drives are not authorized activities"], "b",
      "St. Mary's Academy v. Carpitanos (2002).")
p.mcq("new", "New (Lindain v. CA)", "A widow, as legal administrator of her minor children's land, sold it without court approval to buyers who knew this. What is the status of the sale?",
      ["Valid, because parents are natural guardians", "Void as to the children; a legal administrator has only powers of possession and management, and disposition requires judicial approval", "Voidable at the buyers' option", "Valid if the price was fair"], "b",
      "Lindain (1992); Hebron v. Loyola; Tolentino on Art. 225.")
p.mcq("new", "New (Arts. 228–229)", "Which causes parental authority to terminate PERMANENTLY?",
      ["Adoption of the child", "Appointment of a general guardian", "Emancipation of the child", "Judicial declaration of absence of the parent"], "c",
      "Art. 228: death of the parents, death of the child, emancipation. The others (Art. 229) terminate it 'unless subsequently revived by a final judgment'.")
p.mcq("new", "New (Art. 231)", "Which is NOT a ground for the suspension of parental authority under Art. 231?",
      ["Treating the child with excessive harshness or cruelty", "Giving the child corrupting orders, counsel or example", "Compelling the child to beg", "Refusing consent to the child's marriage"], "d",
      "Salvaña v. Gaela: refusing consent to an unemancipated child's marriage is not a ground to deprive parents of authority. The fourth Art. 231 ground is subjecting the child to acts of lasciviousness.")
p.mcq("new", "New (Medina v. Makabali; Luna)", "Which statement is correct on the custody of children?",
      ["A final judgment awarding custody to the biological parents must always be executed", "The child's welfare is paramount; it may override procedural rules and even the parents' right to custody", "Biological parents always prevail over foster parents", "A child's wishes are never considered"], "b",
      "Luna v. IAC (execution stayed when the child threatened to kill herself); Medina v. Makabali (a mother who deserted her child lost custody to the doctor who raised him).")
p.mcq("new", "New (Art. 236 / NCC 2180)", "Julio, 18, living with his parents, killed Jake with his father's gun taken from an unlocked drawer. Are Julio's parents liable to Jake's heirs?",
      ["No, Julio is emancipated", "Yes; Art. 236 preserves the parents' NCC 2180 responsibility for children below 21 living in their company", "Only if Julio is insolvent", "Only the father"], "b",
      "1993 Bar. Tolentino criticizes this as 'responsibility without authority'.")
p.write("15_pa.json")

# --------------------------- EMANCIPATION; SUMMARY PROCEEDINGS ---------------------------
e = Bank("eman", "EM")
e.tf("samplex", f"{Q2} #3", "Any contracting party between the age of twenty-one and twenty-five shall be obliged to ask their parents or guardian for consent upon the intended marriage.", False,
     "ADVICE, not consent (Art. 15). Consent is for parties between 18 and 21 (Arts. 14, 236). Sir added: a 19-year-old previously married needs no consent, Art. 14 covering only those 'not having been emancipated by a previous marriage'.")
e.tf("new", "New (Uribe format; Art. 234)", "Emancipation takes place by the attainment of majority, by the marriage of the minor, or by the recording in the civil register of an agreement in a public instrument between the parent and the minor at least eighteen years of age.", False,
     "That was the FC as enacted. R.A. 6809 (1989) amended Art. 234: emancipation takes place by the attainment of majority at 18; the other two modes were abolished.")
e.tf("new", "New (Uribe format; Art. 236)", "Emancipation shall terminate parental authority over the person and property of the child who shall then be qualified and responsible for all acts of civil life, save the exceptions established by existing laws in special cases.", True,
     "Art. 236, 1st par., as amended by R.A. 6809. The exceptions: parental consent to marry until 21, and the parents' NCC 2180 responsibility for children below 21.")
e.tf("new", "New (Art. 236)", "Contracting marriage shall require parental consent until the age of eighteen.", False,
     "Until TWENTY-ONE (Art. 236, 2nd par.).")
e.tf("new", "New (Art. 243)", "In summary judicial proceedings under the Family Code, the preliminary conference shall be conducted by the judge personally, with the parties assisted by counsel.", False,
     "Art. 243: WITHOUT the parties being assisted by counsel; counsel may assist at succeeding conferences and hearings if the court deems it useful.")
e.tf("new", "New (Art. 247)", "The judgment of the court in a summary proceeding under the Family Code shall be immediately final and executory.", True,
     "Art. 247. Hence no appeal; the remedy is certiorari (Republic v. Bermudez-Lorino; Republic v. Granada, on Art. 41 declarations of presumptive death).")
e.tf("new", "New (Art. 240)", "Claims for damages by either spouse may be litigated in the summary proceeding for judicial authorization.", False,
     "Art. 240: only in a separate action, except costs of the proceedings.")
e.mcq("new", "New (Art. 245)", "In a petition under Art. 239, the spouse whose consent is sought does not appear despite the court's efforts. What may the court do?",
      ["Dismiss the petition", "Proceed ex parte and render judgment, endeavoring to protect the non-appearing spouse's interests", "Order the arrest of the spouse", "Declare the spouse absent"], "b", "Arts. 244–245.")
e.mcq("new", "New (Art. 253)", "Which of these is NOT among the articles whose petitions follow the summary procedure under Art. 253?",
      ["Art. 41 (presumptive death for remarriage)", "Art. 69 (family domicile)", "Art. 73 (objection to profession)", "Art. 36 (psychological incapacity)"], "d",
      "Art. 253: Arts. 41, 51, 69, 73, 96, 124 and 217. Nullity under Art. 36 is an ordinary action.")
e.mcq("new", "New (Art. 241, 250)", "Where is a petition for judicial authorization under Art. 239 filed?",
      ["Only where the petitioner resides", "In the family court or RTC where either spouse resides, upon proof of notice to the other spouse", "Where the property is located", "In the Court of Appeals"], "b",
      "Art. 241. Petitions involving parental authority (Arts. 223, 225) are filed where the child resides (Art. 250).")
e.write("16_eman.json")

# ---------------------------------- SURNAMES ----------------------------------
n = Bank("names", "NM")
n.tf("new", "New (Uribe format; Art. 370)", "A married woman shall use her husband's surname.", False,
     "Art. 370: she MAY use it in one of three ways; it is permissive (Tolentino; Remo v. Sec. of Foreign Affairs).")
n.tf("new", "New (Uribe format; Art. 371)", "In case of annulment of marriage, the wife, whether guilty or innocent, shall resume her maiden name and surname.", False,
     "Only the GUILTY wife shall resume; the innocent wife MAY resume or keep the husband's surname, unless the court decrees otherwise or either of them remarries.")
n.tf("new", "New (Uribe format; Art. 372)", "When legal separation has been granted, the wife may resume her maiden name and surname.", False,
     "Art. 372: she SHALL CONTINUE using the name and surname she employed before the legal separation; the marriage bond subsists.")
n.tf("new", "New (Uribe format; Art. 373)", "A widow may use the deceased husband's surname as though he were still living.", True,
     "Art. 373; optional (Tolentino).")
n.tf("new", "New (Uribe format; Art. 375)", "In case of identity of names and surnames between ascendants and descendants, the word 'Junior' can be used by a son or grandson.", False,
     "Only by a SON. Grandsons and other direct male descendants add a middle name or the mother's surname, or Roman numerals II, III (Art. 375).")
n.tf("new", "New (Uribe format; Art. 374)", "In case of identity of names and surnames, the older person shall be obliged to use such additional name or surname as will avoid confusion.", False,
     "The YOUNGER person (Art. 374).")
n.tf("new", "New (Art. 365; Johnston)", "An adopted child shall bear the surname of the adopter, which, for a married woman adopting alone, means her surname by marriage.", False,
     "Johnston v. Republic: the adopter's OWN original surname, not the one acquired by marriage; using the husband's would suggest he adopted too.")
n.tf("new", "New (FC 176 as amended by R.A. 9255)", "Illegitimate children expressly recognized by the father in the record of birth shall use the surname of their father.", False,
     "They MAY use it (permissive): Grande v. Antonio (2014). The father cannot compel it.")
n.mcq("new", "New (Naldoza)", "A mother whose husband abandoned the family petitions to change her legitimate minor sons' surname to her own. Should it be granted?",
      ["Yes, the mother has parental authority", "No; it may suggest illegitimacy and erase evidence of paternal ancestry; the children may decide when they can choose for themselves", "Yes, if the father is a swindler", "Only if the father consents in writing"], "b", "Naldoza v. Republic (1982).")
n.mcq("new", "New (Llaneta v. Agrava)", "Teresita, born after her mother's husband Serafin Ferrer died, was known all her life as 'Teresita Ferrer', and Serafin's kin approved. May she change her registered surname to Ferrer?",
      ["No, it gives a false impression of family relationship", "Yes; the false-impression rule applies only when the change would probably prejudice the family or the community, and a sudden shift would cause confusion", "No, only legitimate children may use Ferrer", "Yes, but only through R.A. 9048"], "b", "Llaneta v. Agrava (1974).")
n.mcq("new", "New (Tolentino v. CA)", "Arturo's second wife sued to stop his first wife, divorced from him during the Japanese occupation, from using the surname Tolentino. What is the ruling?",
      ["Injunction granted: only the current wife may use the surname", "Injunction denied: the action prescribed, and mere use of the surname without legal injury to the petitioner is not usurpation", "Injunction granted because divorce is not recognized", "The first wife must pay damages"], "b", "Tolentino v. CA (1988).")
n.mcq("new", "New (Legamia v. IAC)", "A woman who lived with a married man for 20 years used his surname, without sinister purpose, in claiming benefits for their son after his death. Did she violate the anti-alias law (C.A. 142)?",
      ["Yes, she used a name not registered at birth", "No; the law is construed in light of our tolerant culture, and she acted without sinister purpose or material gain for herself", "Yes, unless she married him later", "No, because she was his widow"], "b", "Legamia (1984). See also Ursua and People v. Estrada: an alias must be used publicly and habitually.")
n.mcq("new", "New (Art. 377; Dapar)", "Which is NOT an element of usurpation of name under Art. 377?",
      ["Actual use of another's name by the defendant", "The use is unauthorized", "The use is to designate personality or identify a person", "Proof of actual pecuniary damage to the owner of the name"], "d",
      "Dapar v. Biascan. Tolentino: actual injury need not be proved; there is always potential harm from confusion of identity.")
n.mcq("new", "New (Art. 376; Tolentino)", "Which is a sufficient cause for a judicial change of name?",
      ["A condition in a will that the heir take the testator's surname", "The petitioner's mere preference", "The name is ridiculous, tainted with dishonor, or extremely difficult to write or pronounce", "A desire to drop a middle name because the family is moving abroad"], "c",
      "Tolentino's list. The will condition is not enough by itself; Wang (2005) denied dropping a middle name for convenience abroad.")
n.mcq("new", "New (Art. 379)", "Which statement on pen names and stage names is correct?",
      ["They are prohibited by C.A. 142", "They are permitted if used in good faith without injury to third persons, and cannot be usurped", "They may be used in dealings with the government", "They may be used to open bank accounts"], "b",
      "Art. 379; C.A. 142 as amended allows pseudonyms for literary, cinema, television, radio, entertainment and athletic purposes. Tolentino: never in relations with the State.")
n.write("17_names.json")

# ----------------------------------- ABSENCE -----------------------------------
b = Bank("absence", "AB")
b.mcq("samplex", f"{SUC} #16", "X, who was not in danger of death, disappeared at the age of 76. It being unknown whether or not he still lives, he shall be presumed dead for purposes of succession after an absence of:",
      ["1 year", "5 years", "7 years", "10 years", "2 years from disappearance"], "b",
      "Art. 390, 2nd par.: 'If he disappeared after the age of seventy-five years, an absence of five years shall be sufficient in order that his succession may be opened.'")
b.mcq("samplex", f"{SUC} #19 (second set)", "X, in danger of death, disappeared at the age of 76. It being unknown whether or not he still lives, he shall be presumed dead for purposes of succession after an absence of:",
      ["One year", "5 years", "Seven years", "10 years", "2 years", "4 years from his disappearance"], "f",
      "Art. 391(3): a person in danger of death whose existence has not been known for four years is presumed dead for all purposes, including the division of the estate. Age is irrelevant in Art. 391.")
b.mcq("samplex", f"{SUC} #19 (third set)", "X, who was not in danger of death, disappeared at age 69. It being unknown whether or not he lives, he is presumed dead for succession after an absence of:",
      ["1 year", "5 years", "7 years", "10 years", "2 years from disappearance"], "d", "Art. 390, 2nd par.: ten years (he was not over 75).")
b.tf("samplex", f"{SUC} TF10", "The absentee shall not be presumed dead for the purpose of opening his succession till after an absence of ten years.", False,
     "Keyed FALSE. The sentence copies Art. 390, 2nd par., but drops the rest: five years suffice if he disappeared after 75, and four years under Art. 391 if he disappeared in danger of death. Sir's 'absolutely true' standard makes it false.",
     key="Keyed FALSE although it copies the first sentence of Art. 390, 2nd par.")
b.tf("new", "New (Uribe format; Art. 384)", "Two years having elapsed without any news about the absentee or since the receipt of the last news, and five years in case the absentee has left a person in charge of the administration of his property, his absence may be declared.", True, "Verbatim Art. 384.")
b.tf("new", "New (Uribe format; Art. 386)", "The judicial declaration of absence shall take effect upon its publication in a newspaper of general circulation.", False, "Art. 386: not until SIX MONTHS after its publication.")
b.tf("new", "New (Uribe format; Art. 385)", "The relatives or friends of the absentee may ask for the declaration of absence.", False,
     "Art. 385 lists: (1) the spouse present, (2) the heirs instituted in a will, (3) the relatives who may succeed by intestacy, (4) those with a right over his property subordinated to his death. A FRIEND may only ask for a provisional representative (Art. 381).")
b.tf("new", "New (Uribe format; Art. 390)", "After an absence of seven years, it being unknown whether or not the absentee still lives, he shall be presumed dead for all purposes.", False, "Art. 390: 'for all purposes, EXCEPT for those of succession.'")
b.tf("new", "New (Uribe format; Art. 391)", "A person on board a vessel lost during a sea voyage, who has not been heard of for four years since the loss of the vessel, shall be presumed dead for all purposes except the division of his estate.", False,
     "Art. 391: 'for all purposes, INCLUDING the division of the estate among the heirs.'")
b.tf("new", "New (Uribe format; Art. 392)", "If the absentee appears, he shall recover his property in the condition in which it may be found, together with its fruits and rents.", False, "Art. 392: 'but he cannot claim either fruits or rents.'")
b.tf("new", "New (Art. 388)", "The wife appointed administratrix of her absent husband's property may alienate or encumber it in the course of administration.", False, "Art. 388: not without judicial authority.")
b.mcq("new", "New (FC 41)", "For the spouse present to remarry, how long must the absent spouse have been missing under ordinary circumstances (no danger of death)?",
      ["Two years", "Four consecutive years", "Seven years", "Ten years"], "b",
      "FC 41: four consecutive years and a well-founded belief of death, plus a summary judicial declaration of presumptive death; two years if there was danger of death under Art. 391.")
b.mcq("new", "New (Reyes v. Alejandro; Tol-Noquera)", "Which statement on the declaration of absence is correct?",
      ["It is always required before a spouse may administer the absentee's property, in a separate prior case", "It is needed when the absentee has property to be administered, and the petition may be combined with one for administration", "It is needed merely to establish the fact of absence", "Only the spouse may ask for it"], "b",
      "Reyes v. Alejandro; Tol-Noquera v. Villamor; Peyer v. Martinez. The rules protect the absentee's property, not the administrator.")
b.mcq("new", "New (Eastern Shipping v. Lucero)", "The ship's last messages reported that it was sinking and the crew abandoning ship; nothing more was heard. Two months later, the captain's wife claims his monthly allotments, arguing he cannot be presumed dead until four years pass. Is she right?",
      ["Yes, Art. 391(1) requires four years", "No; where facts lead to a moral certainty of death, the presumption yields to the preponderance of evidence, so she gets death benefits instead", "Yes, until a court declares him dead", "No, because seven years are required"], "b", "Eastern Shipping Lines v. Lucero (1983), citing Joaquin v. Navarro.")
b.mcq("new", "New (Art. 393; Tolentino's example)", "X disappeared in 1940. Y died in 1942 instituting X as heir. In 1950 X's children claim the inheritance. What must they prove?",
      ["That X is now dead", "That X was alive when Y died in 1942", "That seven years have passed", "Nothing; the presumption of death suffices"], "b",
      "Art. 393: whoever claims a right of a person whose existence is not recognized must prove that he was living when his existence was necessary to acquire it.")
b.write("18_absence.json")

# ----------------------------------- FUNERALS -----------------------------------
fu = Bank("funerals", "FU")
fu.tf("new", "New (Uribe format; Art. 305)", "In case of ascendants, the maternal shall have a better right to make arrangements for the funeral of a relative.", False, "Art. 305: the PATERNAL shall have a better right.")
fu.tf("new", "New (Uribe format; Art. 305)", "In case of descendants of the same degree, or of brothers and sisters, the oldest shall be preferred.", True, "Art. 305.")
fu.tf("new", "New (Uribe format; Art. 307)", "The funeral shall be in accordance with the religious beliefs of the deceased; in their absence, his expressed wishes shall determine the funeral rites.", False,
     "Reversed. Art. 307: first his EXPRESSED WISHES; in their absence, his religious beliefs or affiliation; in doubt, the person obliged decides after consulting the family.")
fu.tf("new", "New (Uribe format; Art. 310)", "The construction of a tombstone or mausoleum shall be deemed a part of the funeral expenses, and shall be chargeable to the conjugal partnership property, if the deceased is one of the spouses.", True, "Verbatim Art. 310.")
fu.tf("new", "New (Art. 309)", "Any person who shows disrespect to the dead, or wrongfully interferes with a funeral, shall be liable to the family of the deceased for moral damages only.", False, "Art. 309: damages, MATERIAL AND MORAL.")
fu.mcq("new", "New (Eugenio v. Velez)", "Vitaliana died single, without descendants or ascendants. Her common-law husband and her full-blood siblings both claim the body for burial. Who has the right?",
      ["The common-law husband, as her 'spouse'", "Her siblings: 'spouse' in the Civil Code means a lawfully wedded spouse", "Whoever has possession", "The municipal authorities"], "b", "Eugenio v. Velez (1990).")
fu.mcq("new", "New (Valino v. Adriano)", "A married man separated in fact from his wife lived for years with Fe, who paid his medical and funeral expenses and buried him in her family's mausoleum over the wife's objection. Who had the right to make the funeral arrangements?",
      ["Fe, because she paid", "Fe, because she was closer to him", "The surviving legal spouse, then the descendants, ascendants and siblings, to the exclusion of the live-in partner", "The children only"], "c", "Valino v. Adriano (2014); Art. 305 with FC 199.")
fu.mcq("new", "New (Art. 308; Tolentino)", "A hospital performed an autopsy to determine the cause of death, without the consent of the widow and with no official order. Is it liable?",
      ["No, autopsies are always allowed", "Yes; a private autopsy requires the consent of those entitled to the corpse", "No, if it was for scientific purposes", "Yes, but only criminally"], "b",
      "Art. 308; Tolentino: an official autopsy (disease control, crime) may be ordered without consent, but a private one may not.")
fu.write("19_funerals.json")

# -------------------------------- CIVIL REGISTER --------------------------------
c = Bank("civreg", "CR")
c.tf("new", "New (Uribe format; Art. 412)", "No entry in a civil register shall be changed or corrected without a judicial order.", False,
     "Not absolutely true since R.A. 9048 (as amended by R.A. 10172): clerical or typographical errors, changes of first name or nickname, and the day and month of birth or sex (patent errors) may be corrected by the civil registrar or consul general.",
     key="Verbatim Art. 412; FALSE only because of R.A. 9048/10172. If the question asks about the Civil Code text alone, it is TRUE.")
c.tf("new", "New (Uribe format; Art. 410)", "The books making up the civil register and all documents relating thereto shall be considered public documents and shall be conclusive evidence of the facts therein contained.", False, "Art. 410: PRIMA FACIE evidence.")
c.tf("new", "New (Uribe format; Art. 411)", "Every civil registrar shall be civilly responsible for any unauthorized alteration made in any civil register, without exception.", False,
     "Art. 411: he may exempt himself by proving that he took every reasonable precaution to prevent the unlawful alteration.")
c.tf("new", "New (Rule 108, Sec. 4)", "In a Rule 108 proceeding, the order fixing the hearing shall be published once a week for three consecutive weeks in a newspaper of general circulation in the province.", True, "Rule 108, Sec. 4. Opposition within 15 days from notice or the last publication (Sec. 5).")
c.tf("new", "New (R.A. 9048 as amended)", "The year of birth may be corrected administratively by the civil registrar as a clerical error.", False,
     "R.A. 10172 allows only the DAY AND MONTH of birth; 'no correction must involve the change of nationality, AGE, or status'.")
c.tf("new", "New (Art. 408)", "Voluntary emancipation of a minor and judicial determination of filiation are among the acts and events to be entered in the civil register.", True,
     "Art. 408(14), (15). (Voluntary emancipation is now obsolete under R.A. 6809, but the item remains in the text.)")
c.mcq("new", "New (Republic v. Valencia)", "May substantial errors in the civil register, such as citizenship or the parents' marital status, be corrected under Rule 108?",
      ["No, Rule 108 covers clerical errors only", "Yes, provided the proceeding is adversarial: all affected parties are impleaded and notified, with publication and an opportunity to oppose", "Yes, in a summary hearing", "Only by the civil registrar"], "b", "Republic v. Valencia (1986); Republic v. Marcos (strict compliance).")
c.mcq("new", "New (Labayo-Rowe)", "A mother filed a Rule 108 petition, notifying only the civil registrar, to change the entry of her marriage in her children's birth records to 'not married'. What is the ruling?",
      ["Granted, as a clerical correction", "Denied as to the marital status: it changes the children's legitimacy, a substantial matter requiring an adversarial proceeding with all affected parties", "Granted if she proves she never married", "Dismissed for lack of a marriage certificate"], "b",
      "Labayo-Rowe v. Republic (1988): Rule 108 'shall not diminish, increase or modify substantive rights'. See also Republic v. Ontuca (2020).")
c.mcq("new", "New (R.A. 9048, Sec. 4)", "Which is NOT a ground for an administrative change of first name under R.A. 9048?",
      ["The first name is ridiculous, tainted with dishonor or extremely difficult to write or pronounce", "The new first name has been habitually and continuously used and the petitioner is publicly known by it", "The change will avoid confusion", "The petitioner wants to match the name of a celebrity"], "d", "R.A. 9048, Sec. 4.")
c.mcq("new", "New (Cagandahan; R.A. 10172)", "Which change of the sex entry may be made administratively?",
      ["A change based on sex reassignment surgery", "A change for an intersex person who matured as male", "A correction where it is patently clear that the entry was a clerical or typographical error", "Any change, if the person is of age"], "c",
      "R.A. 10172 (with medical certification of no sex change). Cagandahan (intersex) needed Rule 108; Silverio (sex reassignment) was denied for lack of a law.")
c.mcq("new", "New (Braza)", "The widow and legitimate children of Pablo file a Rule 108 petition to correct the birth record of Patrick, recorded as Pablo's legitimated son by Lucille, on the ground that Pablo's marriage to Lucille was bigamous. What is the ruling?",
      ["Granted, because a bigamous marriage is void", "Dismissed: it is a collateral attack on a marriage and on legitimation, which must be raised in a direct action by the proper party", "Granted if Lucille does not oppose", "Referred to the civil registrar"], "b", "Braza v. City Civil Registrar (2009).")
c.mcq("new", "New (Bartolome v. Republic)", "A man whose birth record says 'Feliciano Bartholome' files a Rule 103 petition to be named 'Ruben Bartolome'. What is the proper first step?",
      ["Rule 103 in the RTC", "Rule 108 in the RTC", "An administrative petition under R.A. 9048 for the first name and the misspelled surname; courts only after denial", "A petition with the PSA in Manila only"], "c",
      "Bartolome v. Republic (2019); Republic v. Sali. But courts are not divested of jurisdiction (Republic v. Felix).")
c.mcq("new", "New (Republic v. Magpayo)", "Claiming his parents never married, Julian filed a Rule 103 petition in Quezon City to delete his parents' marriage entry and his father's name from his Makati birth record. What is the ruling?",
      ["Valid, since Rule 103 covers change of name", "Void: a change of status needs a Rule 108 petition where the registry is located, impleading the civil registrar and all affected persons", "Valid if the father consents", "Void because only the father may file"], "b", "Republic v. Magpayo (2011).")
c.mcq("new", "New (Olaybar)", "Merlinda discovered she was recorded as married to a foreigner she never met, her identity apparently having been stolen. What is her remedy?",
      ["A petition for declaration of nullity under Art. 35", "Rule 108, to cancel the wife's entries in the marriage certificate, in an adversarial proceeding", "R.A. 9048 before the civil registrar", "Annulment for fraud"], "b",
      "Republic v. Olaybar (2014): there was no marriage to declare void; Rule 108 is the appropriate adversary proceeding.")
c.write("20_civreg.json")
