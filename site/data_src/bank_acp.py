from qb import Bank, ABS, ABS_MID

b = Bank("acp", "A")
Q4 = "Uribe CivRev 2025 Quiz 4 (Sep 25, 2025)"
MID = "Uribe CivRev Midterms (class discussion)"
Q3S = "Uribe samplex – Quiz #3 (scanned, handwritten key)"
QC = "Uribe Quiz compilation (Studocu)"
TFC = "Uribe samplex – True or False compilation (scanned)"

EXCL = ("Art. 92 excludes only: (1) property acquired DURING the marriage by gratuitous title, with its fruits and income, unless the donor, testator or grantor provides otherwise; "
        "(2) property for personal and exclusive use of either spouse, except jewelry, which is community property; and (3) property acquired BEFORE the marriage by a spouse who has LEGITIMATE descendants by a FORMER marriage, with its fruits and income.")

# ---------------- samplex ----------------
b.tf("samplex", f"{Q4} #8; {QC} TF 9; {TFC} #30", "The community property shall consist of all the property owned by the spouses at the time of the celebration of the marriage or acquired thereafter.", False,
     "Art. 91 begins 'Unless otherwise provided in this Chapter or in the marriage settlements'. " + EXCL + " Uribe (Quiz 4): mention the exclusion for property owned AT THE TIME of the celebration (Art. 92(3)), not only the exclusions for property acquired during the marriage. And property acquired by gratuitous title is not always separate, because the donor may provide that it forms part of the community.")
b.tf("samplex", "Uribe – PFR Answer Key Quiz 3 #13", "The community property shall consist of all the property owned by the spouses at the time of celebration of marriage.", False,
     "Art. 91: '… shall consist of all the property owned by the spouses at the time of the celebration of the marriage OR ACQUIRED THEREAFTER', and this is still subject to 'Unless otherwise provided in this Chapter or in the marriage settlements' (Art. 92 exclusions).")
b.mcq("samplex", f"{Q4} #12",
      "This shall be excluded from the community property:",
      ["Property acquired during the marriage by onerous title by either spouse", "Property acquired before the marriage by gratuitous title by either spouse",
       "Jewelry for the personal and exclusive use of a spouse", "All of the above", "None of the above"], "e",
      "A: property acquired during the marriage is presumed community (Art. 93), and onerous title is not an Art. 92 exclusion. B: property owned at the celebration is community property however acquired (Art. 91). The gratuitous-title exclusion in Art. 92(1) covers only acquisitions DURING the marriage. C: 'jewelry shall form part of the community property' even if for personal and exclusive use (Art. 92(2)).")
b.mcq("samplex", f"{Q4} #18; {MID} #47",
      "This shall be excluded from the community property:",
      ["Property acquired during the marriage by onerous title by either spouse", "Property acquired during the marriage by gratuitous title",
       "Property acquired before the marriage by gratuitous title by either spouse", "Jewelry for personal and exclusive use", "None of the above"], "e",
      "B is the tempting choice but is not absolutely an exclusion. Art. 92(1) excludes gratuitous acquisitions during the marriage 'unless it is expressly provided by the donor, testator or grantor that they shall form part of the community property'. Uribe: 'This cannot be B because the donor or testator may still specify …' A is presumed community (Art. 93). C is community under Art. 91, since what matters is that it was owned at the celebration, however acquired. D is community (Art. 92(2), jewelry).",
      "The CivRev midterms version (#47) words option D as 'Property acquired before the marriage by gratuitous title by either spouse' and has no jewelry option. The answer is still E.")
b.mcq("samplex", f"{Q4} #20",
      "A parcel of land is presumed to belong to the community property if:",
      ["it was acquired by gratuitous title", "it was acquired by onerous title", "it was acquired before the marriage", "it was registered during the marriage", "none of the above"], "e",
      "Art. 93: 'Property acquired DURING THE MARRIAGE is presumed to belong to the community, unless it is proved that it is one of those excluded therefrom.' The manner of acquisition (A, B) does not trigger the presumption, and property owned before the marriage (C) is community by force of Art. 91, not by presumption. Registration (D) is not acquisition, because the land may have been acquired before the marriage and only registered during it. The correct trigger is not among the choices.")
b.mcq("samplex", f"{QC} MCQ 6 (Quiz #3 set)",
      "A parcel of land is presumed to belong to the community if:",
      ["Acquired by gratuitous title", "Acquired by onerous title", "Acquired before the marriage", "Acquired during the marriage", "Registered during the marriage"], "d",
      "Art. 93: property acquired DURING the marriage is presumed to belong to the community unless proved to be excluded. The presumption is triggered by the time of acquisition, not by the title or by registration.")
b.mcq("samplex", f"{Q3S} MCQ 10; {QC} MCQ 18; Civ Rev samplex (scanned) MCQ 18; {MID} #48",
      "This shall be excluded from the community property:",
      ["Property acquired during the marriage by onerous title by either spouse", "Property acquired before the marriage by either spouse who has legitimate descendants by a former marriage",
       "Property acquired before the marriage by gratuitous title by either spouse", "Jewelry", "None of the above"], "b",
      "Art. 92(3) verbatim: 'Property acquired before the marriage by either spouse who has legitimate descendants by a former marriage, and the fruits as well as the income, if any, of such property.' The purpose is to protect the legitimes of the children of the first marriage. A is community (Arts. 91, 93), C is community (Art. 91), and D is community (Art. 92(2)).")
b.mcq("samplex", f"{MID} #34 (Prof's answer: B)",
      "This shall be excluded from the community property:",
      ["Property acquired during the marriage by onerous title by either spouse", "Property acquired before the marriage by either spouse who has a child by a prior marriage.",
       "Property acquired before the marriage by gratuitous title by either spouse", "Jewelry for personal and exclusive use", "None of the above"], "b",
      "Uribe accepted B. The class worried that Art. 92(3) requires LEGITIMATE descendants. Sir: 'pero kung may kasal edi legit. Therefore the child is legit. So covered siya ng exclusion.' A child by a prior MARRIAGE is legitimate (Art. 164). D: jewelry is community property even if for personal use, and even if acquired before the marriage.",
      "The class answer was B, with a dissent for E. Sir's answer was B. Compare the older item worded 'who has a child BEFORE the marriage', which does not guarantee legitimacy.")
b.mcq("samplex", f"{QC} MCQ 10 (Quiz #3 set, compilation wording)",
      "This shall be excluded from the community property:",
      ["Property acquired during the marriage by onerous title by either spouse", "Property acquired before marriage by either spouse who has a child before the marriage",
       "Property acquired before the marriage by gratuitous title by either spouse", "Jewelry", "None of the above"], "e",
      "Art. 92(3) requires LEGITIMATE descendants BY A FORMER MARRIAGE. A child born 'before the marriage' may be illegitimate (born to an unmarried parent), so option B is not absolutely an exclusion. Contrast the CivRev midterms version 'a child by a prior marriage', which Uribe accepted because a child of a marriage is legitimate. A, C and D are community property (Arts. 91, 92(2), 93).",
      "No key accompanies this wording in the compilation. The scanned Quiz #3 itself reads 'who has legitimate descendants by another marriage' (keyed B). If you meet the 'child before the marriage' wording, answer E and explain the difference.")
b.pair("samplex", f"{MID} pair #1 (Prof's answer: A)",
       "A petition for the adoption under the Domestic Administrative Adoption Act may prosper even if the petitioner, who is an alien, has not resided in the Philippines for three years prior to the filing of the petition and the child to be adopted is an illegitimate child of his Filipino spouse.",
       "In the absence of a marriage settlement, a parcel of land inherited by A during his marriage to B in 1989 will be his separate property.",
       True, True,
       "Uribe's answer: both TRUE. No. 1: the residency requirement for alien adopters may be waived in specified cases, which include adopting a relative within the fourth civil degree as a former Filipino and adopting the child of one's Filipino spouse (Del Rosario's point in class). No. 2: the 1989 marriage without a settlement is under ACP. Land inherited by A DURING the marriage is excluded from the community under Art. 92(1). Sir rejected the class's 'False' answer: 'Kaya lang ang argument is false because the testator may have provided in the will that it should be a community property. Ang mali dun is inherited by A … Siya lang nagmana. Otherwise, dapat nakalagay inherited by the spouses.'",
      "The class answer was B (both false). Sir corrected it to A. For No. 1, the class notes cite RA 8552, Sec. 7 (the 'Domestic Administrative Adoption Act' is RA 11642). Read the adoption part as Sir's answer only; it is outside property relations.",
      stem=ABS_MID)
b.pair("samplex", f"{MID} pair #2 (Prof's answer: B)",
       "The spouses will have joint parental authority if an illegitimate child of one of them is adopted.",
       "The rentals from a building inherited by B during her marriage to A in 1989 will be a community property in the absence of a marriage settlement.",
       False, False,
       "No. 1 is FALSE. If one spouse adopts his or her own illegitimate child, the other spouse's consent is needed but that spouse is not a co-adopter. Joint parental authority follows only when the spouses jointly adopt or one adopts the legitimate child of the other. Sir: 'Consent is not equivalent to being a petitioner.' No. 2 is FALSE. The 1989 marriage is under ACP, and property inherited during the marriage is excluded together with 'the fruits as well as the income thereof' (Art. 92(1)). Rentals are civil fruits, so they are B's separate property. Under a CPG, they would be conjugal (Art. 117(3)).",
      stem=ABS_MID)
b.pair("samplex", f"{MID} pair #3 (Prof's answer: B)",
       "If X died in 1987, the marriage between X and Y may be valid even if there was no marriage license if they cohabited as husband and wife for six years prior to the marriage and their cohabitation was not entirely free from legal impediment.",
       "The absolute community of property shall be liable for all expenses for mere preservation made during marriage upon the separate property of either spouse.",
       False, False,
       "No. 1 is FALSE per Uribe: the Civil Code rule (Art. 76, NCC) is 'mas strict' and requires that the parties, 'being unmarried', lived together for at least five years. Under Niñal v. Bayadog, the five years immediately preceding the marriage must be free of legal impediment. No. 2 is FALSE. Art. 94(5) is limited to taxes and expenses for mere preservation 'upon the separate property of either spouse USED BY THE FAMILY'. Sir: the requirement is not that the expense 'benefit the family'. 'Ang term is used. Basta ginagamit.'",
      "The class answer was B. A dissent argued C (No. 1 true under the Civil Code because the NCC text lacks the 'no legal impediment' clause). Sir's answer was F for No. 1.",
      stem=ABS_MID)
b.mcq("samplex", f"{MID} #25",
      "In the will of X, a parcel of land was validly bequeathed to A who was married to B at 5PM on June 1, 2019. A and B orally agreed for a conjugal partnership of gains. At 10AM on June 1, 2019, X died. This parcel of land will form part of the:",
      ["conjugal partnership property", "community property", "separate property of A", "estate of X", "property of the State"], "b",
      "Successional rights are transmitted from the moment of death (Art. 777, NCC), so A owned the land from 10 AM. The oral settlement is void (Art. 77), so the regime is ACP (Art. 75). ACP commences at the precise moment the marriage is celebrated (Art. 88), at 5 PM, and consists of all property owned by the spouses at the time of the celebration (Art. 91). The Art. 92(1) exclusion does not apply, because the land was acquired BEFORE, not during, the marriage. D is wrong because the land left X's estate at his death.")
b.mcq("samplex", f"{MID} essay C(1) (adapted to MCQ)",
      "A inherited a parcel of land from his grandfather in 1989. Thereafter, A married B without a marriage settlement. In 1995, A died intestate survived by B; C, their son; D and E, his children with his girlfriend Y before his marriage to B; and F and G, his parents. Is the land the separate or exclusive property of A?",
      ["Yes, because it was acquired by gratuitous title.", "Yes, because A has children by another woman.",
       "No, it is community property of A and B.", "No, it is co-owned by A and his children."], "c",
      "The marriage was after August 3, 1988 with no settlement, so the regime is ACP (Art. 75). Property owned at the celebration is community property however acquired (Art. 91). The gratuitous-title exclusion in Art. 92(1) covers only acquisitions DURING the marriage. Art. 92(3) does not apply, because D and E are illegitimate, not legitimate descendants by a former marriage. Uribe: '90% got it wrong.' Next step (essay C(2)): split the land in two first. B takes one-half as her share of the community, and only the other half is A's estate.")
b.mcq("samplex", f"{MID} essay B (adapted to MCQ)",
      "Bong and Liza were married on September 2, 1987. Bong died on August 2, 1989, survived by Liza and their daughter Imee. Thereafter, Liza married Rudy; they orally agreed to adopt the conjugal partnership of gains. Before her marriage to Rudy, Liza had inherited from her father a parcel of land that was being rented out. A year after the solemnization of the marriage, Liza died. Will the rentals, from the solemnization of the marriage of Liza and Rudy until her death, form part of her estate?",
      ["No, because the rentals are community property of Liza and Rudy.", "No, because the rentals are conjugal partnership property.",
       "Yes, because the land and its fruits are excluded from the community, Liza having a legitimate descendant by a former marriage.", "Yes, because inherited property is always exclusive."], "c",
      "Uribe's 'three/four-level' analysis. (1) The relevant marriage is Liza and Rudy's, which was after 1989, so the Family Code governs, not the Civil Code. (2) The oral CPG agreement is void (Art. 77), so the regime is ACP (Art. 75). (3) The land owned at the celebration would ordinarily be community property (Art. 91), but Liza has a legitimate descendant (Imee) by a former marriage, so Art. 92(3) excludes the land 'and the fruits as well as the income' of it. (4) The rentals are her separate property and form part of her estate.",
      "The class answer reached 'yes' through the mandatory separation rule (an unliquidated prior regime, Arts. 103 and 130). The facts do not say whether Bong's estate was liquidated. Sir's discussion used Art. 92(3), which gives the same answer whether or not there was a liquidation.")

# ---------------- bar ----------------
b.mcq("bar", "QuAMTO – 2017 Bar; QuAMTO – 2012 Bar (Danny and Elsa) (adapted to MCQ)",
      "Danny and Elsa were married in 2002. In 2012, Elsa left the conjugal home and her two minor children with Danny to live with her paramour. In 2015, Danny sold without Elsa's consent a parcel of land registered in his name that he had purchased prior to the marriage. Danny used the proceeds of the sale to pay for his children's tuition fees. The sale is:",
      ["valid, because the land is Danny's exclusive property registered in his name", "valid, because the proceeds were used for the children's education",
       "voidable at Elsa's instance within five years", "void, because the land is community property and was sold without Elsa's consent or court authority"], "d",
      "No settlement and a 2002 marriage, so ACP (Art. 75). The land Danny owned at the celebration became community property (Art. 91) despite registration in his name, and no Art. 92 exclusion applies. Disposition without the other spouse's written consent or court authority is void (Art. 96). Elsa's abandonment does not dispense with consent. Under Art. 100(2), Danny needed judicial authorization in a summary proceeding.")
b.mcq("bar", "QuAMTO – 2015 Bar (Marco and Gina) (adapted to MCQ)",
      "Marco and Gina were married in 1989. In 1999, Gina left Marco and lived with another man, leaving their two school-age children with Marco. Needing money for their education, Marco sold, without Gina's consent, a parcel of land registered in his name which he had purchased before the marriage. Is the sale valid, void, or voidable?",
      ["Valid, because the land was purchased before the marriage", "Void, because the land belongs to the absolute community and Gina did not consent",
       "Voidable, because Gina may ratify it", "Valid, because Gina abandoned the family"], "b",
      "Same analysis as the 2017 Danny-and-Elsa problem. 1989 with no settlement is ACP. Land owned at the celebration is community (Art. 91). A sale without the other spouse's consent is void, though it is a continuing offer that the other spouse's acceptance or court authorization may perfect (Art. 96).")
b.mcq("bar", "QuAMTO – 2025 Bar (adapted to MCQ)",
      "A and B got married in 1991 without a prenuptial agreement. In 1997, A forged B's signature on a promissory note and on a real estate mortgage constituted over three parcels of land acquired during their marriage. A failed to pay; the bank foreclosed and bought the lands. B sued to nullify the mortgage and the certificate of sale. Is B correct?",
      ["No, because the parcels are registered in A's name.", "No, because the bank is a mortgagee in good faith.",
       "Yes, because the mortgage of community property without B's consent is void.", "Yes, but only as to B's one-half share."], "c",
      "No settlement and a 1991 marriage, so ACP (Art. 75). Lands acquired during the marriage are presumed community (Art. 93). An encumbrance without the other spouse's consent or court authority is void (Art. 96). It is only a continuing offer, which B never accepted. The foreclosure and sale built on the void mortgage are also void (UPLC answer, citing PNB v. Reyes, Jr., 2016). The whole mortgage is void, not just half of it.")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "The husband assumed sole administration of the family's mango plantation since his wife worked abroad. Subsequently, without his wife's knowledge, the husband entered into an antichretic transaction with a company, giving it possession and management of the plantation with power to harvest and sell the fruits and to apply the proceeds to the payment of a loan he got. What is the standing of the contract?",
      ["It is void in the absence of the wife's consent.", "It is void absent an authorization from the court.",
       "The transaction is void and can neither be ratified by the wife nor authorized by the court.",
       "It is considered a continuing offer by the parties, perfected only upon the wife's acceptance or the court's authorization."], "d",
      "Arts. 96 and 124, 2nd par.: the powers of a sole administrator 'do not include disposition or encumbrance without authority of the court or the written consent of the other spouse … However, the transaction shall be construed as a continuing offer on the part of the consenting spouse and the third person, and may be perfected as a binding contract upon the acceptance by the other spouse or authorization by the court before the offer is withdrawn.'")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "May a spouse freely donate communal or conjugal property without the consent of the other?",
      ["Absolutely not, since the spouses co-own such property.", "Yes, for properties that the family may spare, regardless of value.",
       "Yes, provided the donation is moderate and intended for charity or family rejoicing.", "Yes, in a donation mortis causa that the donor may still revoke in his lifetime."], "c",
      "Arts. 98 and 125: 'Neither spouse may donate any community [conjugal] property without the consent of the other. However, either spouse may, without the consent of the other, make moderate donations … for charity or on occasions of family rejoicing or family distress.'")
b.tf("bar", "UP BOC – 2007 Bar TF", "An individual, while single, purchases a house and lot in 1990, and borrows money in 1992 to repair it. In 1995, such individual gets married while the debt is still being paid. After the marriage, the debt is still the responsibility of such individual.", False,
     "The ACP is liable for 'ante-nuptial debts of either spouse insofar as they have redounded to the benefit of the family' (Art. 94(7)). Alternatively, the house and lot became community property at the 1995 wedding (Art. 91), since no Art. 92(3) facts appear, and the community is liable for 'all taxes, liens, charges and expenses, including major or minor repairs, upon the community property' (Art. 94(4)).")

# ---------------- recitation ----------------
b.mcq("recit", "Uribe CivRev recitation (2025), situation 10; Uribe recitation situationer (2018)",
      "Before their marriage, A inherited a building from his father. After the solemnization, A and B spent P5 million to retrofit the building. Will the expense be chargeable to the absolute community or the conjugal partnership of the spouses?",
      ["Always chargeable to A alone, because the building is his exclusive property.", "Always chargeable to the absolute community or conjugal partnership.",
       "It depends: under CPG it is chargeable to the partnership whether or not the building is used by the family; under ACP, if the building is A's separate property, only if it is used by the family.",
       "It is chargeable to the spouses jointly in proportion to their incomes."], "c",
      "First classify the property, then the regime. ACP: the building is community property unless excluded (e.g., Art. 92(3)). If it is separate, the community bears preservation expenses only if the property is 'used by the family' (Art. 94(5)). CPG: the building is A's exclusive property (Art. 109(1)), and the partnership is liable for 'all taxes and expenses for mere preservation made during the marriage upon the separate property of either spouse', with no 'used by the family' qualifier (Art. 121(5)). Uribe's reason: in the CPG the fruits of the exclusive property go to the partnership (Art. 117(3)), so the partnership shoulders its preservation.")
b.mcq("recit", "Uribe recitation situationer (2018)",
      "A inherited a parcel of land from his grandfather before his marriage to B, solemnized in late 1988 without a marriage settlement. A has a child with X who was born after A's marriage to B. What is the status of the land?",
      ["Exclusive property of A, because it was inherited", "Exclusive property of A, because he has a child by another woman",
       "Community property of A and B", "Co-owned by A and his child"], "c",
      "A marriage after August 3, 1988 without a settlement is under ACP (Art. 75), so property owned at the celebration is community (Art. 91). The mode of acquisition does not matter: 'the mode of acquisition does not affect its inclusion to the community property.' Art. 92(3) does not apply, because the child is illegitimate, not a legitimate descendant by a former marriage.",
      "Sir's question began 'if the marriage was solemnized in 1988'. If it was before August 3, 1988, the regime would be CPG and the land would be A's exclusive property (Art. 109(1)). The item fixes the date as 'late 1988'.")
b.mcq("recit", "Uribe recitation situationer (2018)",
      "A and B entered into a marriage settlement adopting the conjugal partnership of gains, stipulating that the regime shall commence on the date of the settlement. The marriage was solemnized 15 days later, in 1989, at 5 PM. X died at 9 AM on the same day of the solemnization, leaving in his will a parcel of land to A. After the solemnization, A died. Will the parcel of land form part of A's estate?",
      ["No, it is conjugal because the regime commenced on the date of the settlement.", "Yes, entirely, because it is A's exclusive property; the stipulation on commencement is void.",
       "Only one-half, because it is conjugal.", "No, because it belongs to X's estate."], "b",
      "Arts. 88 and 107: the regime commences 'at the precise moment that the marriage is celebrated. Any stipulation, express or implied, for the commencement of the community regime at any other time shall be void.' A acquired the land at 9 AM, at X's death (Art. 777, NCC), before the CPG began at 5 PM, so A brought it to the marriage as his own (Art. 109(1)). It is entirely his and forms part of his estate.")
b.mcq("recit", "Uribe CivRev recitation (2025), situation 1; Uribe recitation situationer (2018)",
      "X died survived by his wife Y and other heirs. A few days after his death, the heirs discovered a TCT over a parcel of land registered in the name of X. As counsel of Y, who wants you to protect her interest, what is your BEST argument as to this parcel of land?",
      ["That the land is presumed community or conjugal property because it is registered in X's name", "That the land is not owned by X at all but by Y (e.g., bought with Y's exclusive funds, with X holding title only in trust)",
       "That Y is entitled to the whole land as surviving spouse", "That the land should be partitioned equally among all heirs"], "b",
      "Uribe: the best argument is that the land is not X's but your client's, for example because it was purchased with Y's exclusive money, or because X held title only as trustee (implied trust). The next best argument is that it is community or conjugal property, which gives Y 50% as her share plus her share as heir. That argument requires showing that the land was acquired during the marriage, because the presumption (Arts. 93, 116) is not automatic. A misstates the presumption, which is triggered by acquisition during the marriage, not by registration.")

# ---------------- new ----------------
b.tf("new", "New (Uribe format; FC 88)", "The absolute community of property between spouses shall commence at the precise moment that the marriage is celebrated. Any stipulation, express or implied, for the commencement of the community regime at any other time shall be voidable.", False,
     "Art. 88: any such stipulation 'shall be VOID', not voidable.")
b.tf("new", "New (Uribe format; FC 89)", "No waiver of rights, shares and effects of the absolute community of property during the marriage can be made except in case of legal separation.", False,
     "Art. 89: '… except in case of JUDICIAL SEPARATION OF PROPERTY.' Legal separation dissolves the regime (Art. 63(2)), but the exception in Art. 89 refers to judicial separation of property (Arts. 134–138).")
b.pair("new", "New (Uribe format; FC 89)",
       "When the waiver of rights in the absolute community takes place upon a judicial separation of property, or after the marriage has been dissolved or annulled, the same shall appear in a public instrument and shall be recorded as provided in Article 77.",
       "The creditors of the spouse who made such waiver may petition the court to annul the waiver in its entirety.",
       True, False,
       "No. 1 is TRUE (Art. 89, 2nd par.). No. 2 is FALSE. The creditors may petition the court 'to RESCIND the waiver to the EXTENT of the amount sufficient to cover the amount of their credits.' The remedy is rescission (accion pauliana), and only to the extent of their credits.")
b.tf("new", "New (Uribe format; FC 90)", "The provisions on the contract of partnership shall apply to the absolute community of property between the spouses in all matters not provided for in the Chapter on the absolute community.", False,
     "Art. 90: the provisions on CO-OWNERSHIP are suppletory to the ACP. The contract of partnership is suppletory to the CPG (Art. 108).")
b.tf("new", "New (Uribe format; FC 92(2))", "Property for personal and exclusive use of either spouse, including jewelry, shall be excluded from the community property.", False,
     "Art. 92(2): '… However, jewelry shall form part of the community property.'")
b.tf("new", "New (Uribe format; FC 93)", "Property acquired during the marriage is conclusively presumed to belong to the community.", False,
     "Art. 93: the presumption holds 'unless it is proved that it is one of those excluded therefrom.' It is a disputable presumption.")
b.tf("new", "New (Uribe format; FC 95)", "Whatever may be lost during the marriage in any game of chance, betting, sweepstakes, or any other kind of gambling, whether permitted or prohibited by law, shall be borne by the loser and shall not be charged to the community but any winnings therefrom shall form part of the community property.", True,
     "Verbatim Art. 95.")
b.tf("new", "New (Uribe format; FC 95)", "Losses in gambling permitted by law shall be charged to the community, while losses in prohibited gambling shall be borne by the loser.", False,
     "Art. 95 makes no distinction. Losses in any kind of gambling, 'whether permitted or prohibited by law', are borne by the loser.")
b.mcq("new", "New (FC 94)",
      "Which of the following is NOT chargeable to the absolute community of property?",
      ["Expenses to enable either spouse to commence or complete a professional or vocational course", "Ante-nuptial debts of either spouse insofar as they have redounded to the benefit of the family",
       "Expenses for mere preservation of the separate property of a spouse which is not used by the family", "Expenses of litigation between the spouses, unless the suit is found to be groundless"], "c",
      "Art. 94(5) covers taxes and expenses for mere preservation of separate property only if it is 'USED BY THE FAMILY'. A is Art. 94(6), B is Art. 94(7), and D is Art. 94(10).")
b.pair("new", "New (Uribe format; FC 94)",
       "The absolute community of property shall be liable for ante-nuptial debts of either spouse insofar as they have redounded to the benefit of the family.",
       "If the community property is insufficient to cover its liabilities, the spouses shall be solidarily liable for the unpaid balance with their separate properties, including the support of illegitimate children of either spouse.",
       True, False,
       "No. 1 is TRUE (Art. 94(7)). No. 2 is FALSE. The last paragraph of Art. 94 makes the spouses solidarily liable 'EXCEPT those falling under paragraph (9)', which includes the support of illegitimate children, other ante-nuptial debts, and liabilities for crimes or quasi-delicts. Those are charged to the community only as advances deducted from the debtor-spouse's share.")
b.mcq("new", "New (FC 94(9))",
      "During the marriage, H was held civilly liable for a quasi-delict. H has no exclusive property. Under the absolute community regime:",
      ["the community is not liable at all", "the community shall pay, and the payment is chargeable to H's share upon liquidation",
       "the community shall pay without any reimbursement", "W is solidarily liable with her separate property"], "b",
      "Art. 94(9): liabilities incurred by either spouse by reason of a crime or quasi-delict, 'in case of absence or insufficiency of the exclusive property of the debtor-spouse', are paid by the community, but 'the payment of which shall be considered as advances to be deducted from the share of the debtor-spouse upon liquidation.' Solidary liability of the separate properties does not extend to par. (9) items.")
b.tf("new", "New (Uribe format; FC 96)", "The administration and enjoyment of the community property shall belong to both spouses jointly. In case of disagreement, the husband's decision shall prevail, subject to recourse to the court by the wife for proper remedy, which must be availed of within five years from the date of the contract implementing such decision.", True,
     "Verbatim Art. 96, 1st par. (The same text appears in Art. 124 for the CPG.)")
b.tf("new", "New (Uribe format; FC 96)", "In case of disagreement on the administration of the community property, the husband's decision shall prevail, subject to recourse to the court by the wife within one year from the date of such decision.", False,
     "Art. 96: the wife's recourse 'must be availed of within FIVE YEARS from the date of the CONTRACT IMPLEMENTING such decision', not one year from the decision.")
b.tf("new", "New (Uribe format; FC 96)", "A disposition or encumbrance of community property by the administrator-spouse without the authority of the court or the written consent of the other spouse is voidable.", False,
     "Art. 96: 'In the absence of such authority or consent, the disposition or encumbrance shall be VOID.' It is construed, however, as a continuing offer that the other spouse's acceptance or the court's authorization can perfect before it is withdrawn.")
b.tf("new", "New (Uribe format; FC 97)", "Either spouse may dispose by will of his or her interest in the community property.", True,
     "Verbatim Art. 97. A will takes effect at death, which dissolves the community. The testator disposes only of his or her share in the net assets, not of specific community property as a whole.")
b.tf("new", "New (Uribe format; FC 98)", "Either spouse may, without the consent of the other, make moderate donations from the community property for charity or on occasions of family rejoicing or family distress.", True,
     "Verbatim second sentence of Art. 98. Compare Art. 87 (gifts BETWEEN spouses): only 'moderate gifts … on the occasion of any family rejoicing'.")
b.mcq("new", "New (FC 99)",
      "The absolute community terminates upon any of the following, EXCEPT:",
      ["the death of either spouse", "a decree of legal separation", "the separation in fact of the spouses for more than one year", "judicial separation of property during the marriage"], "c",
      "Art. 99: death, a decree of legal separation, annulment or declaration of nullity, and judicial separation of property. Separation in fact 'shall not affect the regime of absolute community' (Art. 100), except in three respects. It may, however, be a cause for judicial separation of property if it has lasted at least one year and reconciliation is highly improbable (Art. 135(6)).")
b.tf("new", "New (Uribe format; FC 101)", "A spouse is deemed to have abandoned the other when he or she has left the conjugal dwelling without intention of returning, and the spouse who has left the conjugal dwelling for a period of three months shall be conclusively presumed to have no intention of returning.", False,
     "Art. 101: such a spouse 'shall be PRIMA FACIE presumed to have no intention of returning'. It is a disputable presumption, not a conclusive one.")
b.mcq("new", "New (FC 101)",
      "H left the conjugal dwelling without just cause and has failed to give support. Which remedy is NOT available to W under Article 101?",
      ["receivership", "judicial separation of property", "authority to be the sole administrator of the absolute community", "dissolution of the marriage"], "d",
      "Art. 101 gives the aggrieved spouse three remedies: receivership, judicial separation of property, or authority to be the sole administrator, 'subject to such precautionary conditions as the court may impose.' Abandonment never dissolves the marriage. At most it is a ground for legal separation if it lasts more than one year without justifiable cause (Art. 55(10)).")
b.tf("new", "New (Uribe format; FC 102(4))", "For purposes of computing the net profits subject to forfeiture under Articles 43(2) and 63(2), the said profits shall be the increase in value between the market value of the community property at the time of the celebration of the marriage and the market value at the time of its dissolution.", True,
     "Verbatim last sentence of Art. 102(4). In the ACP, 'net profits' for forfeiture purposes are only this increase in value, not the guilty spouse's whole share in the net assets.")
b.mcq("new", "New (FC 102(6))",
      "In the partition of the absolute community, unless otherwise agreed upon, the conjugal dwelling and the lot on which it is situated shall be adjudicated to:",
      ["the spouse who contributed more to its acquisition", "the innocent spouse",
       "the spouse with whom the majority of the common children choose to remain", "the wife, in all cases"], "c",
      "Art. 102(6) (and Art. 129(9) for the CPG). Children below seven are deemed to have chosen the mother unless the court decides otherwise. If there is no majority, the court decides in the children's best interests.")
b.tf("new", "New (Uribe format; FC 103)", "If no judicial settlement proceeding is instituted, the surviving spouse shall liquidate the community property either judicially or extra-judicially within six months from the death of the deceased spouse.", False,
     "Art. 103 (ACP): 'within ONE YEAR from the death of the deceased spouse.' The six-month period is in Art. 130, for the CPG.")
b.tf("new", "New (Uribe format; FC 103)", "Should the surviving spouse contract a subsequent marriage without liquidating the community property of the terminated marriage as required by law, a mandatory regime of complete separation of property shall govern the property relations of the subsequent marriage.", True,
     "Art. 103, last par. (Art. 130, last par. for the CPG). The subsequent marriage is valid, but the regime is fixed by law whatever settlement the new spouses execute.")
b.mcq("new", "New (FC 103)",
      "W's husband died in 2020. No judicial settlement proceeding was instituted and W did not liquidate their absolute community. In 2022, W sold a parcel of community land. The sale is:",
      ["valid, as W is the surviving spouse", "valid as to W's half only", "void", "voidable at the instance of the heirs"], "c",
      "Art. 103, 2nd par.: if no liquidation is made within one year from the death, 'any disposition or encumbrance involving the community property of the terminated marriage shall be void.'")
b.mcq("new", "New (FC 104; Delizo v. Delizo, 69 SCRA 216)",
      "N contracted two marriages before the Family Code, and both property regimes are being liquidated at the same time. The evidence does not show to which marriage certain existing properties belong. How should they be divided?",
      ["Equally between the two communities", "Entirely to the second community, being the later one",
       "Between the different communities in proportion to the capital and duration of each", "To N's estate exclusively"], "c",
      "Art. 104 (Art. 131 for the CPG): 'In case of doubt as to which community the existing properties belong, the same shall be divided between the different communities in proportion to the capital and duration of each.' In Delizo v. Delizo, under NCC 189, the total mass was divided by the duration of each conjugal partnership (18/64 and 46/64).")
b.mcq("new", "New (Spouses Abrenica v. Law Firm of Abrenica, G.R. No. 180572, 2012)",
      "Atty. A, who has legitimate children by his first marriage, acquired two vehicles and a house and lot before marrying J (no marriage settlement). A judgment creditor of A levied on these properties. J objected, claiming they are community property of her marriage to A. Is J correct?",
      ["Yes, because property owned at the time of the celebration of the marriage is community property.", "Yes, because the properties are presumed community property.",
       "No, because property acquired before the marriage by a spouse with legitimate descendants by a former marriage is excluded from the community.", "No, because the properties are registered in A's name."], "c",
      "Abrenica: 'Art. 92, par. (3) of the Family Code excludes from the community property the property acquired before the marriage of a spouse who has legitimate descendants by a former marriage; and the fruits and the income, if any, of that property. Neither these two vehicles nor the house and lot belong to the second marriage.'")
b.mcq("new", "New (FC 92(1))",
      "During their marriage under the absolute community regime, H inherited a farm from his uncle. The will says nothing about the community. The farm yields rentals. To whom do the farm and the rentals belong?",
      ["Both to the community", "The farm to H, the rentals to the community", "Both to H as his separate property", "Both to H and his uncle's other heirs"], "c",
      "Art. 92(1) excludes property acquired during the marriage by gratuitous title 'and the fruits as well as the income thereof', unless the testator expressly provides that they shall form part of the community. Compare CPG, where the farm is exclusive (Art. 109(2)) but its net fruits are conjugal (Art. 117(3)).")
b.tf("new", "New (Uribe recitation situationer, 2018)", "The declaration of nullity of a marriage, like annulment and legal separation, results in the dissolution of the absolute community or conjugal partnership of the parties.", False,
     "Uribe: 'No. With annulment, there will be a dissolution. Kapag void, co-ownership ang magogovern. There is nothing to dissolve.' A void marriage never had an ACP or CPG. The parties' property relations were governed all along by Art. 147 or 148. (Art. 50 applies the liquidation rules of Art. 43(2) to marriages declared void under Art. 40, a special case.)",
     "Art. 99(3) and Art. 126(3) list 'when the marriage is annulled or declared void' as causes of termination, so a purely codal reading could call the statement true. Sir's point is about void marriages generally. Explain both if asked.")

b.write("07_acp.json")
