from qb import Bank, ABS, ABS_MID

b = Bank("cpg", "C")
Q4 = "Uribe CivRev 2025 Quiz 4 (Sep 25, 2025)"
MID = "Uribe CivRev Midterms (class discussion)"
QC = "Uribe Quiz compilation (Studocu)"
TFC = "Uribe samplex – True or False compilation (scanned)"

FRUITS = ("Art. 117(3): the conjugal partnership includes 'the fruits, natural, industrial, or civil, due or received during the marriage from the common property, as well as the NET FRUITS FROM THE EXCLUSIVE PROPERTY OF EACH SPOUSE.' "
          "Rentals are civil fruits. It does not matter whether the exclusive property was acquired by gratuitous or onerous title, which is why options with 'only' are wrong. 'Community property' belongs to the ACP, not the CPG, so those options are the 'worst answers' (Uribe).")

# ---------------- samplex ----------------
b.tf("samplex", f"{QC} TF 8", "The conjugal partnership shall be governed by the rules of co-ownership in all that is not in conflict with what is expressly determined in this Chapter or by the spouses in their marriage settlements.", False,
     "Art. 108: '… governed by the rules on the CONTRACT OF PARTNERSHIP in all that is not in conflict …' Co-ownership is the suppletory law for the ACP (Art. 90).")
b.mcq("samplex", f"{QC} MCQ 17; Civ Rev samplex (scanned) MCQ 17; Uribe samplex – Quiz #1 (scanned) MCQ 17",
      "The conjugal partnership shall be liable for all debts and obligations contracted during the marriage by the designated administrator-spouse for the benefit of the conjugal partnership of gains. In case of insufficiency of said assets, the spouses shall be liable:",
      ["Solidarily", "Jointly", "Alternatively", "Cumulatively"], "a",
      "Art. 121, last par.: 'If the conjugal partnership is insufficient to cover the foregoing liabilities, the spouses shall be SOLIDARILY liable for the unpaid balance with their separate properties.' (Same rule for the ACP, Art. 94.) 'Jointly' was the old rule under the Civil Code and partnership principles (PNB v. Quintos).")
b.mcq("samplex", f"{Q4} #11; {MID} #46",
      "The fruits from the exclusive property of a spouse shall form part of the:",
      ["exclusive properties of a spouse in a conjugal partnership of gains", "conjugal partnership properties only if the property was acquired by gratuitous title",
       "community properties if property was acquired by gratuitous title", "community properties if property was acquired by onerous title", "none of the above"], "e",
      "In a CPG, the fruits of exclusive property are conjugal (Art. 117(3)), so A is wrong, and B is wrong because of 'only' (the manner of acquisition is irrelevant). Uribe: 'Pag sinabing community property, it should be clear that the regime is ACP.' In the ACP, the fruits of property excluded under Art. 92(1) or (3) are also excluded, so they are the spouse's separate property regardless of the manner of acquisition. C and D are therefore both wrong.",
      "The CivRev midterms version (#46) words B–D with 'only' ('community properties only if …'). The answer is still E.")
b.mcq("samplex", f"{Q4} #14",
      "In a conjugal partnership of gains, without a marriage settlement, the rentals from the exclusive property of a spouse shall form part of the:",
      ["exclusive properties of a spouse", "conjugal partnership properties only if the property was acquired by gratuitous title",
       "conjugal partnership properties only if the property was acquired by onerous title", "community properties if property was acquired by gratuitous title",
       "community properties if property was acquired by onerous title", "none of the above"], "f",
      FRUITS + " Sir: 'the worse option D or E. Kasi ang topic ay conjugal partnership of gains tapos ang sagot ay community property.'")
b.mcq("samplex", f"{MID} #31",
      "In a conjugal partnership of gains, without a marriage settlement, the rentals from the exclusive property of a spouse shall form part of the:",
      ["exclusive properties of a spouse", "conjugal properties only if the property was acquired by gratuitous title",
       "conjugal properties only if the property was acquired by onerous title", "community properties if property was acquired by onerous title", "none of the above"], "e",
      FRUITS)
b.mcq("samplex", f"{MID} #49",
      "In a conjugal partnership of gains, without a marriage settlement, the rentals from the exclusive property of a spouse shall form part of the:",
      ["exclusive properties of a spouse", "conjugal partnership properties only if the property was acquired by gratuitous title",
       "conjugal partnership properties only if the property was acquired by onerous title", "community properties if property was acquired by gratuitous title", "none of the above"], "e",
      FRUITS)
b.mcq("samplex", f"{QC} MCQ 7 (Quiz #3 set); Uribe samplex – Quiz #3 MCQ 7",
      "Fruits from exclusive property of a spouse shall form part of the:",
      ["Exclusive property of spouse in CPG", "CPG property ONLY if prop acquired by gratuitous title", "ACP property ONLY if prop acquired by gratuitous title",
       "ACP property ONLY if prop acquired by onerous title", "None of the above"], "e",
      "In the CPG, all net fruits of exclusive property are conjugal regardless of title (Art. 117(3)), so A and B are wrong. In the ACP, fruits of excluded property follow the property: Art. 92(1) (gratuitous acquisitions during the marriage) and Art. 92(3) (property of a spouse with legitimate descendants by a former marriage) exclude 'the fruits as well as the income'. Otherwise the property itself is community, and so are its fruits. The test is never 'only if acquired by onerous or gratuitous title', so C and D are wrong.")
b.mcq("samplex", f"{Q4} #15",
      "A parcel of land is not presumed to belong to the conjugal partnership if:",
      ["it was acquired by gratuitous title", "it was acquired by onerous title", "it was acquired during the marriage", "it was registered during the marriage", "none of the above"], "e",
      "Art. 116: 'All property acquired during the marriage, whether the acquisition appears to have been made, contracted or registered in the name of one or both spouses, is presumed to be conjugal unless the contrary is proved.' Sir: A and B are immaterial, because land acquired during the marriage is presumed conjugal whatever the title (a gratuitous acquisition is a ground to REBUT the presumption under Art. 109(2), not a reason it never arises). C is the 'worst answer', since acquisition during the marriage is exactly what triggers the presumption. D: registration during the marriage does not necessarily mean acquisition during the marriage.")
b.mcq("samplex", f"{MID} #30",
      "In a conjugal partnership of gains, without a marriage settlement, this property shall NOT form part of the conjugal partnership properties:",
      ["the rentals from the exclusive property of a spouse", "a property acquired by gratuitous title during the marriage", "a property acquired by onerous title during the marriage",
       "a property acquired by onerous title before the marriage", "none of the above"], "d",
      "D: property brought to the marriage as one's own is exclusive (Art. 109(1)), however it was acquired. A is conjugal (Art. 117(3)). C is conjugal (Art. 117(1)). On B, Uribe: 'not necessarily … the testator may have expressly provided' that it go to the partnership. Because 'shall NOT form part' is absolute, B fails.")
b.pair("samplex", f"{MID} pair #17 (Prof's answer: D)",
       "Property bought on installments paid partly from exclusive funds of either or both spouses and partly from conjugal funds belongs to the conjugal partnership.",
       "A bigamous marriage falling under Article 41 may be void even if there is a judicial declaration of presumptive death and all the essential and formal requisites are present.",
       False, True,
       "No. 1 is FALSE. Art. 118: such property 'belongs to the buyer or buyers if full ownership was vested before the marriage and to the conjugal partnership if such ownership was vested during the marriage', with reimbursement either way upon liquidation. No. 2 is TRUE. Even with a judicial declaration of presumptive death, the subsequent marriage is void if both spouses to it acted in bad faith (Art. 44).",
       stem=ABS_MID)
b.tf("samplex", f"{TFC} #5", "That which is brought to the marriage as his or her own, shall be the exclusive property of each spouse.", True,
     "Verbatim Art. 109(1), the CPG rule on exclusive property. Under a CPG, what each spouse owns at the celebration remains his or her own, and only the fruits enter the partnership.",
     "The compilation keys this TRUE as a codal statement. It is the CPG rule. Under the ACP, the same property would be community (Art. 91). If the item specifies the ACP, the answer flips to False.")

# ---------------- bar ----------------
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Audrey, single, bought a parcel of land in Malolos City from Franco for P1 Million. A contract was executed between them which already vested upon Audrey full ownership of the property, although payable in monthly installments for a period of four (4) years. One (1) year after the execution of the contract, Audrey got married to Arnel. They executed a marriage settlement whereby they agreed that their properties shall be governed by the regime of conjugal partnership of gains. Thereafter, subsequent installments were paid from the conjugal partnership funds. Is the land conjugal or paraphernal?",
      ["The land is conjugal because the installments were paid from the conjugal partnership funds.", "The land is paraphernal because ownership thereof was acquired before the marriage.",
       "The land is both conjugal and paraphernal funds of installments were paid from both the personal funds of Audrey and the conjugal partnership funds.", "The land is paraphernal because it was Audrey who purchased the same."], "b",
      "Art. 118: property bought on installments 'belongs to the buyer or buyers if full ownership was vested before the marriage'. The partnership's payments are reimbursed upon liquidation. D gives the wrong reason, because the test is when ownership vested, not who purchased.")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "A husband by chance discovered hidden treasure on the paraphernal property of his wife. Who owns the discovered treasure?",
      ["The half pertaining to the husband (finder) belongs to the conjugal partnership.", "The half pertaining to the wife (as owner) belongs to the conjugal partnership.",
       "One half shall belong to the husband as finder and the other half shall belong to the wife as owner of the property.", "a and b"], "d",
      "Art. 117(4): 'The share of either spouse in the hidden treasure which the law awards to the finder OR owner of the property where the treasure is found' is conjugal. Under NCC 438, half goes to the finder and half to the owner, and here both halves fall to a spouse, so both are conjugal.")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Before Karen married Karl, she inherited P5 million from her deceased mother which amount she brought into the marriage. She later used part of the money to buy a new Mercedes Benz in her name, which Karen and her husband used as a family car. Is the car a conjugal or Karen's exclusive property?",
      ["It is conjugal property since the spouses use it as a family car.", "It is Karen's exclusive property since it is in her name.",
       "It is conjugal property having been bought during the marriage.", "It is Karen's exclusive property since she bought it with her own money."], "d",
      "Art. 109(4): 'That which is purchased with exclusive money of the wife or of the husband' is exclusive. The money was brought to the marriage as her own (Art. 109(1)). Family use (A) and registration in her name (B) are not the test, and acquisition during the marriage (C) raises only a rebuttable presumption (Art. 116), which the source of funds rebuts. (This assumes a CPG. Under an ACP, the inherited money brought into the marriage would be community property.)")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "When does the regime of conjugal partnership of gains begin to exist?",
      ["At the moment the parties take and declare each other as husband and wife before officiating officer.", "At the time the spouses acquire properties through joint efforts.",
       "On the date the future spouses executed their marriage settlements because this is the starting point of their marital relationship.", "On the date agreed upon by the future spouses in their marriage settlements since their agreement is the law between them."], "a",
      "Art. 107, in relation to Art. 88: the regime commences 'at the precise moment that the marriage is celebrated. Any stipulation, express or implied, for the commencement of the … regime at any other time shall be void.' This rules out C and D.")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Josie owned a lot worth P5 million prior to her marriage to Rey. Subsequently, their conjugal partnership spent P3 million for the construction of a house on the lot. The construction resulted in an increase in the value of the house and lot to P9 million. Who owns the house and the lot?",
      ["Josie and the conjugal partnership of gains will own both on a 50-50 basis.",
       "Josie will own both since the value of the house and the increase in the property's value is less than her lot's value; but she is to reimburse conjugal partnership expenses.",
       "Josie still owns the lot, it being her exclusive property, but the house belongs to the conjugal partnership.",
       "The house and lot shall both belong to the conjugal partnership, with Josie entitled to reimbursement for the value of the lot."], "b",
      "Art. 120: when 'the cost of the improvement made by the conjugal partnership and any resulting increase in value are more than the value of the property at the time of the improvement', the entire property becomes conjugal, subject to reimbursement. 'Otherwise, said property shall be retained in ownership by the owner-spouse, likewise subject to reimbursement of the cost of the improvement.' The UP BOC answer is B.",
      "The figures are close (₱3M cost plus a ₱1M increase above the cost, against a ₱5M lot), which is why the BOC keyed B. Know the test, not the arithmetic.")
b.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Solomon sold his coconut plantation to Aragon, Inc. for P100 million, payable in installments of P10 million per month with 6% interest per annum. Solomon married Lorna after 5 months and they chose conjugal partnership of gains to govern their property relations. When they married, Aragon had an unpaid balance of P50 million plus interest in Solomon's favor. To whom will Aragon's monthly payments go after the marriage?",
      ["The principal shall go to the conjugal partnership but the interests to Solomon.", "Both principal and interests shall go to Solomon since they are his exclusive properties.",
       "Both principal and interests shall go to the conjugal partnership since these become due after the marriage.", "The principal shall go to Solomon but the interests to the conjugal partnership."], "d",
      "Art. 119: when a credit payable over time belongs to one spouse, 'the sums which may be collected during the marriage in partial payments or by installments on the principal shall be the exclusive property of the spouse. However, interests falling due during the marriage on the principal shall belong to the conjugal partnership.'")
b.mcq("bar", "QuAMTO – 2012 Bar (adapted to MCQ)",
      "Maria, wife of Pedro, withdrew P5 Million from their conjugal funds. With this money, she constructed a building on a lot which she inherited from her father. Is the building conjugal or paraphernal?",
      ["Conjugal, because it was built with conjugal funds", "Paraphernal, because accessory follows the principal",
       "It depends: if the cost of the building and the resulting increase in value exceed the value of the lot, both become conjugal; otherwise both remain paraphernal, with reimbursement either way", "Co-owned by Maria and the partnership in proportion to their contributions"], "c",
      "Art. 120 ('reverse accession', applicable only to the CPG). If the improvement's cost and the resulting increase in value exceed the value of the land at the time of the improvement, the entire property becomes conjugal, subject to reimbursing Maria the value of the lot. Otherwise Maria keeps both, subject to reimbursing the partnership the cost. Ownership vests only upon reimbursement at liquidation.")
b.mcq("bar", "QuAMTO – 2022 Bar (adapted to MCQ)",
      "Before marrying in 2000, Nonoy and Daday agreed in a marriage settlement on the conjugal partnership of gains. During the marriage, they acquired land using conjugal funds, titled in the name of 'Nonoy, married to Daday'. Nonoy sold it to Barby without Daday's knowledge or consent, claiming her consent was unnecessary since the land was registered in his name. Is the sale valid?",
      ["Yes, because the title is in Nonoy's name.", "Yes, because 'married to Daday' is merely descriptive.",
       "No, because the land is conjugal and was sold without Daday's consent.", "Voidable within ten years at Daday's instance."], "c",
      "Art. 116: property acquired during the marriage is presumed conjugal 'whether the acquisition appears to have been made, contracted or registered in the name of one or both spouses'. Registration in one name does not destroy its conjugal nature (Cordova v. Ty, 2021). Under Art. 124, disposition without the other spouse's written consent or court authority is void. D states the old NCC rule (Arts. 166, 173), which does not apply to a 2000 marriage.")
b.mcq("bar", "QuAMTO – 2006 Bar (adapted to MCQ)",
      "Spouses Biong and Linda agreed to sell their house to Ray for P2 Million. Biong signed the deed of sale and received the manager's check, but Linda, who was abroad, refused to sign upon her return, saying she had changed her mind. Linda sued to nullify the deed of sale. Will the suit prosper?",
      ["No, because Biong, as administrator, may sell alone.", "No, because Ray is a buyer in good faith.",
       "Yes, because the sale of community or conjugal property requires the written consent of both spouses.", "Yes, but Linda must pay Ray damages."], "c",
      "Arts. 96 and 124: disposition of community or conjugal property without the written consent of the other spouse or court authority is void (Abalos v. Macatangay, 2004). Biong's consent alone is insufficient, and Linda's refusal shows she never accepted the continuing offer. Ray, who is not in bad faith, may recover the ₱2M, and damages may be had only on proof of bad faith (Arts. 19, 21 NCC).")
b.mcq("bar", "QuAMTO – 2008 Bar (adapted to MCQ)",
      "Adam, a building contractor, unearthed on Blas's lot a vault of old notes and coins worth P100 million. Assuming that either or both Adam and Blas are adjudged as owners as finder and owner of the land, will the notes and coins be deemed part of their absolute community or conjugal partnership with their respective spouses?",
      ["No, they are the exclusive property of Adam and Blas.", "Yes, they will be part of the absolute community or conjugal partnership of the respective marriages.",
       "Only Blas's share, as owner of the land, will be community or conjugal.", "Only Adam's share, as finder, will be community or conjugal."], "b",
      "ACP: property acquired during the marriage is community (Arts. 91, 93). CPG: 'the share of either spouse in the hidden treasure which the law awards to the finder or owner' is conjugal (Art. 117(4)), as is property acquired by chance (Art. 106).")

# ---------------- recitation ----------------
b.mcq("recit", "Uribe CivRev recitation (2025), situation 9",
      "A and B were married on January 1 at 5 PM. At 10 AM of the same day, X died; in his will, X gave a parcel of land to A. In their marriage settlement, A and B had agreed on a conjugal partnership of gains. What is the nature of the parcel of land?",
      ["Conjugal property, because it was acquired on the day of the marriage", "Exclusive property of A, because it was brought to the marriage as his own",
       "Community property", "Property of X's estate until probate"], "b",
      "Uribe: 'I did not ask you to whom the property should belong. I asked you the nature of the property.' Successional rights are transmitted at death, at 10 AM (Art. 777, NCC). The CPG commenced at the precise moment of the celebration, at 5 PM (Arts. 88, 107). A therefore brought the land to the marriage as his own, so it is exclusive (Art. 109(1)). Compare the same facts with an ORAL CPG agreement: the settlement is void, the regime is ACP, and the land becomes community property (CivRev midterms #25).")
b.mcq("recit", "Uribe CivRev recitation (2025), situation 11; Uribe recitation situationer (2018)",
      "Five years before his marriage to B, A bought a house and lot payable in equal monthly installments for ten years, paying with his salary. After the marriage, both spouses' salaries paid the amortizations until full payment. Six years after the wedding, A died. Under a conjugal partnership of gains, will the house and lot form part of A's estate?",
      ["Yes, always, because A bought it before the marriage.", "No, always, because the price was fully paid during the marriage.",
       "It depends on whether full ownership vested in A before the marriage (absolute sale) or only upon full payment during the marriage (conditional sale).", "It depends on who paid the larger part of the price."], "c",
      "Art. 118 looks to when full ownership vested. Uribe corrected the student who assumed that ownership passed only on full payment: 'Di naman necessarily true. Even if the price is paid by installments, it may still be an absolute sale … the ownership may be passed prior to the marriage.' Also: 'Sale on installment does not change the nature of the contract.' If ownership vested before the marriage, the property is A's (part of his estate), and the partnership is reimbursed. If it vested during the marriage, the property is conjugal, and A's estate is reimbursed. (Under ACP, the property is community either way.)")
b.mcq("recit", "Uribe recitation situationer (2018)",
      "A, a moneylender, lent X P1 million at 24% per annum, payable in two years. One year later, A married B under the conjugal partnership of gains. X paid in full only three years from the loan. Who is entitled to the principal and to the interest that fell due during the marriage?",
      ["Both to A", "Both to the conjugal partnership", "The principal to A; the interest falling due during the marriage to the conjugal partnership", "The principal to the conjugal partnership; the interest to A"], "c",
      "Art. 119: installments or partial payments on the principal collected during the marriage are the exclusive property of the creditor-spouse, but 'interests falling due during the marriage on the principal shall belong to the conjugal partnership.' Uribe: 'What matters most? The principal amount. It goes to the spouse.' (Under ACP, all of it would be community property.)")

# ---------------- new ----------------
b.tf("new", "New (Uribe format; FC 106)", "Under the regime of conjugal partnership of gains, the husband and wife place in a common fund the proceeds, products, fruits and income from their separate properties and those acquired by either or both spouses through their efforts or by chance, and, upon dissolution of the marriage or of the partnership, the net gains or benefits obtained by either or both spouses shall be divided equally between them, unless otherwise agreed in the marriage settlements.", True,
     "Verbatim Art. 106.")
b.tf("new", "New (Uribe format; FC 106)", "Under the regime of conjugal partnership of gains, the husband and wife place in a common fund all their properties at the time of the celebration of the marriage.", False,
     "That describes the ACP (Art. 91). In the CPG, what is placed in the common fund is the 'proceeds, products, fruits and income from their separate properties' and what is acquired through their efforts or by chance (Art. 106). The separate properties themselves remain exclusive (Art. 109).")
b.tf("new", "New (Uribe format; FC 109(3))", "That which is acquired by right of redemption, by barter or by exchange with property belonging to only one of the spouses shall form part of the conjugal partnership.", False,
     "Art. 109(3): it is the EXCLUSIVE property of that spouse (real subrogation). Cf. Plata v. Yatco: a subsequent conveyance of paraphernal property does not make it conjugal absent proof that conjugal funds paid for it.")
b.tf("new", "New (Uribe format; FC 110)", "Either spouse may, during the marriage, transfer the administration of his or her exclusive property to the other by means of a private instrument.", False,
     "Art. 110, 2nd par.: '… by means of a PUBLIC instrument, which shall be recorded in the registry of property of the place the property is located.'")
b.tf("new", "New (Uribe format; FC 111)", "A spouse of age may mortgage, encumber, alienate or otherwise dispose of his or her exclusive property, without the consent of the other spouse, and appear alone in court to litigate with regard to the same.", True,
     "Verbatim Art. 111.")
b.tf("new", "New (Uribe format; FC 112)", "The alienation of any exclusive property of a spouse administered by the other automatically terminates the administration over such property and the proceeds of the alienation shall be turned over to the owner-spouse.", True,
     "Verbatim Art. 112.")
b.tf("new", "New (Uribe format; FC 113)", "Property donated or left by will to the spouses jointly, without designation of determinate shares, shall pertain to the conjugal partnership.", False,
     "Art. 113: such property pertains to the donee-spouses 'as his or her own exclusive property, and in the absence of designation, SHARE AND SHARE ALIKE, without prejudice to the right of accretion when proper.'")
b.tf("new", "New (Uribe format; FC 115)", "Retirement benefits, pensions, annuities, gratuities, usufructs and similar benefits shall be governed by the rules on gratuitous or onerous acquisitions as may be proper in each case.", True,
     "Verbatim Art. 115. Example: Berciles v. GSIS, where retirement premiums not shown to have been paid from exclusive funds were presumed conjugal.")
b.tf("new", "New (Uribe format; FC 116)", "All property acquired during the marriage, whether the acquisition appears to have been made, contracted or registered in the name of one or both spouses, is conclusively presumed to be conjugal.", False,
     "Art. 116: 'is presumed to be conjugal UNLESS THE CONTRARY IS PROVED.' The presumption is rebuttable (Laperal v. Katigbak), though only by strong, clear and convincing evidence (Andrade v. Tan).")
b.mcq("new", "New (FC 117)",
      "Which of the following is NOT conjugal partnership property?",
      ["Salaries of the husband earned during the marriage", "Rentals during the marriage from a building inherited by the wife",
       "A house and lot inherited by the wife during the marriage", "Winnings of the husband from betting during the marriage"], "c",
      "The inherited house and lot is the wife's exclusive property (Art. 109(2), gratuitous title during the marriage). But its rentals are conjugal (Art. 117(3)). Salaries are conjugal under Art. 117(2), and winnings under Art. 117(7).")
b.tf("new", "New (Uribe format; FC 117(6))", "Livestock existing upon the dissolution of the partnership in excess of the number of each kind brought to the marriage by either spouse shall be conjugal partnership property.", True,
     "Verbatim Art. 117(6).")
b.tf("new", "New (Uribe format; FC 119)", "Whenever an amount or credit payable within a period of time belongs to one of the spouses, the interests falling due during the marriage on the principal shall be the exclusive property of the creditor-spouse.", False,
     "Art. 119: the installments on the PRINCIPAL are exclusive, but 'interests falling due during the marriage on the principal shall belong to the conjugal partnership.'")
b.pair("new", "New (Uribe format; FC 120)",
       "When the cost of the improvement made by the conjugal partnership on the separate property of a spouse and any resulting increase in value are more than the value of the property at the time of the improvement, the entire property shall belong to the conjugal partnership, subject to reimbursement of the value of the property of the owner-spouse at the time of the improvement.",
       "In such case, the ownership of the entire property shall be vested in the conjugal partnership at the time the improvement is completed.",
       True, False,
       "No. 1 is TRUE (Art. 120, 2nd par.). No. 2 is FALSE. Art. 120, last par.: 'the ownership of the entire property shall be vested UPON THE REIMBURSEMENT, which shall be made at the time of the LIQUIDATION of the conjugal partnership.' Maramba v. Lozano: until the value is paid at liquidation, ownership of the land stays with the owner-spouse.")
b.pair("new", "New (Uribe format; FC 121–122)",
       "The conjugal partnership shall be liable for all taxes and expenses for mere preservation made during the marriage upon the separate property of either spouse only if the property is used by the family.",
       "The payment of personal debts contracted by either spouse before the marriage may be enforced against the partnership assets after the responsibilities enumerated in Article 121 have been covered, if the spouse who is bound should have no exclusive property or if it should be insufficient.",
       False, True,
       "No. 1 is FALSE. Art. 121(5) has NO 'used by the family' qualifier. That qualifier appears only in the ACP counterpart, Art. 94(5). No. 2 is TRUE (Art. 122, 3rd par.). At liquidation, that spouse is charged for what was paid.")
b.mcq("new", "New (Luzon Surety Co. v. de Garcia, 30 SCRA 111)",
      "Without his wife's consent, H signed as guarantor of a third person's loan, thinking it would enhance his business reputation. The debtor defaulted. Is the conjugal partnership liable?",
      ["Yes, because H is the administrator of the partnership.", "Yes, because the obligation was contracted during the marriage.",
       "No, because the benefit to the family must be clear and not fanciful or remote.", "No, because a guaranty is always a personal obligation."], "c",
      "Luzon Surety v. de Garcia: 'The benefit accruing to the family must be clear and not fanciful and remote before the conjugal partnership can be held liable.' Enhancing the husband's reputation is too remote. Art. 121(3) carries this forward: debts without the other spouse's consent are chargeable only 'to the extent that the family may have benefited'.")
b.mcq("new", "New (Carlos v. Abelardo, 380 SCRA 361)",
      "W borrowed money from her parents to buy a house and lot that became the conjugal home. H refused to sign the acknowledgment of the loan. Is H liable?",
      ["No, because he did not consent to the loan.", "No, because the loan is W's personal obligation.",
       "Yes, solidarily with W, because the loan redounded to the benefit of the family.", "Yes, but only up to one-half of the loan."], "c",
      "Carlos v. Abelardo: the loan 'redounded to the benefit of the family because it was used to purchase the house and lot which became the conjugal home … under Art. 121 of the Family Code, he shall be solidarily liable for such loan together with his wife.'")
b.mcq("new", "New (BA Finance Corp. v. CA, 161 SCRA 608)",
      "After abandoning his family, H obtained a loan for his own purposes, falsely representing that his wife had authorized him to bind her business, which was conjugal property. May the conjugal property be held liable?",
      ["Yes, because it is registered in the wife's name only as administrator.", "Yes, because all debts during the marriage are conjugal.",
       "No, because the obligation did not redound to the benefit of the conjugal partnership.", "No, because the wife may always repudiate the husband's debts."], "c",
      "BA Finance v. CA: registration in one spouse's name does not destroy the property's conjugal nature, but for conjugal property to answer, the husband's obligation 'must have redounded to the benefit of the conjugal partnership.' It was contracted for his own benefit after he had abandoned the family.")
b.mcq("new", "New (Torela; Dela Peña v. Avila; Andrade v. Tan)",
      "In a suit over land registered in the name of the deceased husband, his widow invokes the presumption that the land is conjugal. What must she first prove?",
      ["That the land was paid for with conjugal funds", "That the land was acquired during the marriage", "That the land is registered in both spouses' names", "That the husband had no other property"], "b",
      "Proof of acquisition during the marriage is 'a condition sine qua non for the application of the presumption' (Torela v. Torela). Proof that conjugal funds were used is NOT required (Castro v. Miat; Dela Peña v. Avila). Once the presumption applies, it may be rebutted only by strong, clear, categorical and convincing evidence (Andrade v. Tan).")
b.mcq("new", "New (Magallon v. Montejo; Go-Bangayan v. Bangayan)",
      "A TCT states that the land is registered in the name of 'Martin, married to Epifania'. What is the legal effect of the phrase 'married to Epifania'?",
      ["It proves that the land is conjugal property of Martin and Epifania.", "It is merely descriptive of Martin's civil status.",
       "It makes Epifania a co-owner of record.", "It creates a conclusive presumption of conjugality."], "b",
      "Magallon v. Montejo: the phrase 'is merely descriptive of the civil status' of the registered owner 'and does not necessarily prove that the land is conjugal property.' Go-Bangayan applied the same rule under Art. 148.")
b.mcq("new", "New (Felipe v. Heirs of Aldon; Heirs of Aguilar-Reyes v. Mijares)",
      "In 1983, during a marriage governed by the conjugal partnership of gains under the Civil Code, the husband sold a conjugal lot without the wife's consent. Under the Civil Code, the sale is:",
      ["void", "voidable, and may be annulled by the wife during the marriage and within ten years from the transaction", "unenforceable", "valid, the husband being the administrator"], "b",
      "NCC Arts. 166 and 173: the wife may, during the marriage and within ten years from the transaction, ask the court to annul the contract (Felipe v. Heirs of Aldon; Heirs of Aguilar-Reyes v. Mijares). Under the Family Code (Art. 124), a sale after August 3, 1988 without consent is VOID instead, though it operates as a continuing offer.")
b.mcq("new", "New (Calimlim-Canullas v. Fortun; Maramba v. Lozano)",
      "During the marriage, the conjugal partnership built a house on a lot that the husband had inherited before the marriage. Under the Civil Code rule applied in Calimlim-Canullas v. Fortun, which is correct?",
      ["The lot remains the husband's and the house is conjugal.", "Both the house and the lot become conjugal, subject to reimbursement of the value of the lot to the husband.",
       "Both remain the husband's exclusive property.", "The house and lot are co-owned in proportion to the values contributed."], "b",
      "Calimlim-Canullas, under NCC 158: buildings constructed at conjugal expense on land belonging to one spouse 'also pertain to the partnership, but the value of the land shall be reimbursed to the spouse who owns the same.' Maramba v. Lozano adds that the ownership of the land does not change until its value is paid, which can be demanded only at liquidation. Under Art. 120 FC, the outcome depends on whether the cost plus increase in value exceeds the value of the land.")
b.mcq("new", "New (Santero v. CFI of Cavite, 153 SCRA 728)",
      "During the liquidation of the conjugal partnership dissolved by the husband's death, his children, all of age and gainfully employed, asked for support from the common mass. Are they entitled?",
      ["No, because the Rules of Court limit allowances to minor or incapacitated children.", "No, because they are gainfully employed.",
       "Yes, because the substantive law grants support to the surviving spouse and the children without distinction.", "Yes, but only if they live with the surviving spouse."], "c",
      "Santero: the Civil Code (now Art. 133 FC) grants support 'to the surviving spouse and to the children during the liquidation … without distinction'. That they are of age, employed or married 'is of no moment'. The procedural rule cannot impair the substantive right. The support is an advance on their shares, and 'spouse' means the legitimate spouse.")
b.mcq("new", "New (Beumer v. Amores, G.R. No. 195670, 2012)",
      "After the nullity of his marriage to a Filipina, a foreign national sought reimbursement of the money he spent buying lands titled in his wife's name, knowing that aliens cannot own land. Will his claim prosper?",
      ["Yes, on the ground of unjust enrichment.", "Yes, as his share in the conjugal partnership.",
       "No, because he knowingly entered into an unconstitutional transaction and equity will not aid him.", "No, because the lands are presumed paraphernal."], "c",
      "Beumer v. Amores: he 'acquired no right whatsoever over the subject properties by virtue of its unconstitutional purchase … equity as a rule will follow the law and will not permit that to be done indirectly which, because of public policy, cannot be done directly.' Under NCC 1412, the law leaves the parties where it finds them.")
b.mcq("new", "New (People v. Lagrimas, 29 SCRA 153)",
      "H was convicted and ordered to pay civil indemnity to the victim's heirs. H has no exclusive property. May the indemnity be enforced against the conjugal partnership before its liquidation?",
      ["No, never.", "No, only upon liquidation.",
       "Yes, after the responsibilities enumerated in Article 121 (formerly NCC 161) have been covered, with H charged at liquidation for what was paid.", "Yes, and without any charge to H's share."], "c",
      "People v. Lagrimas (NCC 163, now Art. 122): fines and indemnities may be enforced against the partnership assets even while it subsists, after the preferential responsibilities are covered, if the spouse has no or insufficient exclusive property. Otherwise the accused would escape civil liability and the victim's heirs 'would be made to suffer still further'.")
b.mcq("new", "New (Ansaldo v. Sheriff, 64 Phil. 115)",
      "When does the right of a spouse to one-half of the conjugal partnership property vest?",
      ["At the celebration of the marriage", "Upon the acquisition of each conjugal property", "Upon the dissolution of the marriage, when the conjugal partnership is also dissolved", "Upon registration of the property"], "c",
      "Ansaldo: 'The right of the husband or wife to one-half of the property of the conjugal partnership does not vest until the dissolution of the marriage, when the conjugal partnership is also dissolved.' Before that, it is a mere inchoate right.")
b.tf("new", "New (Uribe format; FC 130)", "Upon the termination of the marriage by death, if no judicial settlement proceeding is instituted, the surviving spouse shall liquidate the conjugal partnership property either judicially or extra-judicially within one year from the death of the deceased spouse.", False,
     "Art. 130 (CPG): 'within SIX MONTHS from the death … If upon the lapse of the six-month period no liquidation is made, any disposition or encumbrance involving the conjugal partnership property of the terminated marriage shall be void.' One year is the ACP period (Art. 103).")
b.tf("new", "New (Uribe format; FC 129(6))", "Unless the owner had been indemnified from whatever source, the loss or deterioration of movables used for the benefit of the family, belonging to either spouse, even due to fortuitous event, shall be paid to said spouse from the conjugal funds, if any.", True,
     "Verbatim Art. 129(6). This step has no counterpart in the ACP liquidation (Art. 102).")
b.mcq("new", "New (FC 129)",
      "Upon dissolution of the conjugal partnership, what is divided equally between the spouses (absent a different agreement, waiver or forfeiture)?",
      ["All the properties of the spouses", "The net assets of the community", "The net remainder of the conjugal partnership properties, which constitute the profits", "Only the fruits of the exclusive properties"], "c",
      "Art. 129(7): 'The net remainder of the conjugal partnership properties shall constitute the PROFITS, which shall be divided equally …' In the ACP, it is the 'net assets' (Art. 102(4)). Before the division, the CPG liquidation credits advances to the partnership, reimburses each spouse for exclusive funds or property used, pays the debts, returns the exclusive properties, and indemnifies the loss of movables used for the family.")
b.tf("new", "New (Uribe format; FC 133)", "From the common mass of property, support shall be given to the surviving spouse and to the children during the liquidation of the inventoried property and until what belongs to them is delivered; but from this shall be deducted that amount received for support which exceeds the fruits or rents pertaining to them.", True,
     "Verbatim Art. 133. See Santero v. CFI (the children are entitled even if of age or employed; 'spouse' means the legitimate spouse).")

b.write("08_cpg.json")
