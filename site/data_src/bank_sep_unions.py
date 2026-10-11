from qb import Bank, ABS, ABS_MID

# ======================= SEPARATION OF PROPERTY (FC 134–146) =======================
s = Bank("sep", "S")
Q4 = "Uribe CivRev 2025 Quiz 4 (Sep 25, 2025)"

s.mcq("samplex", f"{Q4} #13",
      "The property regime of the spouses married in 1999 will be complete separation of property if:",
      ["no marriage settlement was executed", "the marriage settlement is void",
       "one of the contracting parties is a surviving spouse who contracted a subsequent marriage without liquidating the community property", "all of the above", "none of the above"], "c",
      "A and B lead to ACP for a 1999 marriage (Art. 75). C is the mandatory regime under Art. 103 (Art. 130 for a CPG): 'Should the surviving spouse contract a subsequent marriage without compliance with the foregoing requirements, a mandatory regime of complete separation of property shall govern the property relations of the subsequent marriage.' In the Quiz 4 discussion, liquidation is required so the legitimes of the heirs can be delivered and the debts of the deceased paid, and mandatory separation protects those heirs.")
s.mcq("bar", "UP BOC – 2012 Bar MCQ",
      "Separation of property between spouses during the marriage may take place only:",
      ["by agreement of the spouses.", "If one of the spouses has given ground for legal separation.", "Upon order of the court.", "If one spouse has abandoned the other."], "c",
      "Art. 134: 'In the absence of an express declaration in the marriage settlements, the separation of property between spouses during the marriage shall not take place except by JUDICIAL ORDER.' Even voluntary separation requires a joint petition approved by the court (Art. 136). Grounds and abandonment (B, D) are only causes the court considers (Arts. 101, 128, 135).")
s.mcq("bar", "QuAMTO – 2005 Bar (adapted to MCQ)",
      "Gabby and Mila married in 1990 after executing a registered marriage settlement adopting the conjugal partnership of gains. In 1995, they signed a private document dissolving their conjugal partnership and agreeing on complete separation of property. Gabby later acquired a mansion and an agricultural land registered exclusively in his name. What is the status of the 1995 agreement and of Gabby's later acquisitions?",
      ["The agreement is valid; the later acquisitions are Gabby's exclusive property.", "The agreement is void; the CPG subsists, and the later acquisitions are presumed conjugal.",
       "The agreement is voidable; the later acquisitions are co-owned.", "The agreement is valid between the spouses but not against creditors."], "b",
      "Art. 134: separation during the marriage takes place only by judicial order, so the CPG is not dissolved by the spouses' mere agreement, and the 1995 document is void (see also Art. 76 on modifications). Properties later acquired, though registered in Gabby's name alone, are presumed conjugal (Art. 116). In the bar answer, they are answerable for Mila's obligations to the extent of Art. 121, except the family home.")
s.tf("recit", "Uribe recitation situationer (2018)", "If a petition for separation of property was filed, for this petition to prosper, the petitioner must allege and thereafter prove a sufficient cause for separation of property.", False,
     "Art. 134: judicial separation of property 'may either be VOLUNTARY or for sufficient cause'. In a voluntary separation (Art. 136), the spouses file a joint verified petition without alleging any cause. Would this not prejudice creditors? No, because they are listed in the petition and notified, and the court takes protective measures (Art. 136). In any case, 'the separation of property shall not prejudice the rights previously acquired by creditors' (Art. 140).")
s.tf("recit", "Uribe recitation situationer (2018)", "There can be a regime of separation of property only if so agreed upon by the parties in their marriage settlements.", False,
     "Uribe disagreed: not only by settlement (Arts. 143–146). Separation also arises by mandate of law, when the surviving spouse remarries without liquidating (Arts. 103, 130); after legal separation, which dissolves the regime (Art. 63(2)), and after reconciliation unless the spouses revive their regime (Art. 66(2)); and by judicial separation of property, after which 'the provisions on complete separation of property shall apply' (Art. 138).")
s.tf("new", "New (Uribe format; FC 134)", "In the absence of an express declaration in the marriage settlements, the separation of property between spouses during the marriage shall not take place except by judicial order. Such judicial separation of property may either be voluntary or for sufficient cause.", True,
     "Verbatim Art. 134.")
s.tf("new", "New (Uribe format; FC 135(6))", "It is a sufficient cause for judicial separation of property that at the time of the petition, the spouses have been separated in fact for at least six months and reconciliation is highly improbable.", False,
     "Art. 135(6): separated in fact 'for at least ONE YEAR' and reconciliation is highly improbable.")
s.tf("new", "New (Uribe format; FC 135)", "In cases where the spouse of the petitioner has been sentenced to a penalty which carries with it civil interdiction, has been judicially declared an absentee, or has been decreed to have lost parental authority, the presentation of the final judgment against the guilty or absent spouse shall be enough basis for the grant of the decree of judicial separation of property.", True,
     "Art. 135, last par., referring to grounds (1), (2) and (3).")
s.mcq("new", "New (FC 135)",
      "Which of the following is NOT among the sufficient causes for judicial separation of property under Article 135?",
      ["The spouse of the petitioner has been sentenced to a penalty which carries with it civil interdiction",
       "The spouse granted the power of administration in the marriage settlements has abused that power",
       "The spouse of the petitioner has been sentenced to imprisonment of more than six years, even if pardoned",
       "The spouse of the petitioner has been judicially declared an absentee"], "c",
      "C paraphrases a ground for LEGAL SEPARATION (Art. 55(4)), not judicial separation of property. Art. 135 refers to a penalty 'which carries with it civil interdiction' (A). B is Art. 135(5) and D is Art. 135(2).")
s.tf("new", "New (Uribe format; FC 136)", "The spouses may jointly file a verified petition with the court for the voluntary dissolution of the absolute community or the conjugal partnership of gains, and for the separation of their common properties, provided they allege a sufficient cause therefor.", False,
     "Art. 136 requires no cause for a voluntary separation. What it requires is that all creditors of the community or partnership, and the personal creditors of each spouse, 'be listed in the petition and notified of the filing thereof.'")
s.pair("new", "New (Uribe format; FC 137–138)",
       "During the pendency of the proceedings for separation of property, the absolute community or the conjugal partnership shall pay for the support of the spouses and their children.",
       "After dissolution of the absolute community or of the conjugal partnership by judicial separation of property, the provisions on the absolute community shall again apply to properties acquired thereafter.",
       True, False,
       "No. 1 is TRUE (Art. 137, 2nd par.). No. 2 is FALSE. Art. 138: 'After dissolution of the absolute community or of the conjugal partnership, the provisions on COMPLETE SEPARATION OF PROPERTY shall apply.' The former regime returns only if the court revives it on motion (Art. 141).")
s.tf("new", "New (Uribe format; FC 139–140)", "The separation of property shall not prejudice the rights previously acquired by creditors.", True,
     "Verbatim Art. 140. Art. 139 also requires the petition and the final judgment to be recorded in the proper local civil registries and registries of property.")
s.mcq("new", "New (FC 141)",
      "In which of the following instances may the spouses file a motion for a decree reviving the former property regime after a judicial separation of property?",
      ["When the spouses who have been separated in fact for at least one year reconcile and resume common life", "When one spouse remarries",
       "When the creditors of the spouses so request", "When the spouses execute a private agreement to revive the regime"], "a",
      "Art. 141(6). The revival is by motion in the same proceeding where separation was decreed, and Art. 67 governs it (agreement under oath listing the properties contributed and retained and all known creditors, filed in court with notice to creditors). A private agreement alone (D) is not enough.")
s.tf("new", "New (Uribe format; FC 141(7))", "When after voluntary dissolution of the absolute community or conjugal partnership has been judicially decreed upon the joint petition of the spouses, they agree to the revival of the former property regime, another voluntary separation of property may thereafter be granted.", False,
     "Art. 141(7): '… No voluntary separation of property may thereafter be granted.' The spouses get only one revival after a voluntary separation.")
s.mcq("new", "New (FC 142)",
      "The court may transfer the administration of all classes of exclusive property of a spouse to the other spouse in the following cases, EXCEPT:",
      ["when one spouse becomes the guardian of the other", "when one spouse is judicially declared an absentee",
       "when one spouse is sentenced to a penalty which carries with it civil interdiction", "when the spouses have been separated in fact for six months"], "d",
      "Art. 142: (1) guardian of the other; (2) judicially declared absentee; (3) civil interdiction; (4) fugitive from justice or in hiding as an accused in a criminal case. If the other spouse is not qualified, the court appoints a suitable person.")
s.tf("new", "New (Uribe format; FC 144)", "Separation of property may refer to present or future property or both. It may be total or partial. In the latter case, the property not agreed upon as separate shall pertain to the conjugal partnership of gains.", False,
     "Art. 144: '… shall pertain to the ABSOLUTE COMMUNITY.'")
s.pair("new", "New (Uribe format; FC 145–146)",
       "Under the regime of separation of property, each spouse shall own, dispose of, possess, administer and enjoy his or her own separate estate, without need of the consent of the other.",
       "Under the regime of separation of property, the liabilities of the spouses to creditors for family expenses shall be joint.",
       True, False,
       "No. 1 is TRUE (Art. 145). No. 2 is FALSE. Art. 146: although the spouses bear family expenses between themselves in proportion to their income, 'the liabilities of the spouses to creditors for family expenses shall, however, be SOLIDARY.'")
s.tf("new", "New (Uribe format; FC 146)", "Under the regime of separation of property, both spouses shall bear the family expenses equally.", False,
     "Art. 146: 'in proportion to their income, or, in case of insufficiency or default thereof, to the current market value of their separate properties.'")
s.mcq("new", "New (Garcia v. Manzano; Lacson v. San Jose-Lacson)",
      "Spouses separated in fact executed a compromise agreement dissolving their conjugal partnership and dividing their properties, which the court approved after notice. No creditor was prejudiced. Is the dissolution valid?",
      ["No, because the conjugal partnership can be dissolved only by death or legal separation.", "No, because spouses can never agree on the dissolution of their regime.",
       "Yes, because the law allows the dissolution of the conjugal partnership during the marriage provided judicial sanction is secured.", "Yes, even without court approval, since the agreement is the law between the parties."], "c",
      "Lacson v. San Jose-Lacson: 'The law allows separation of property of the spouses and the dissolution of their conjugal partnership provided judicial sanction is secured beforehand.' Garcia v. Manzano: the creditors must be notified so they may protect their interests. Under the FC, this is voluntary judicial separation of property (Art. 136).")
s.mcq("new", "New (De la Cruz v. De la Cruz, 22 SCRA 333)",
      "H left the conjugal dwelling but continued to manage the conjugal properties diligently and to support his wife and children. W petitioned for separation of property on the ground of abandonment. Will the petition prosper?",
      ["Yes, because H left the conjugal dwelling.", "Yes, because separation in fact is a ground for judicial separation of property.",
       "No, because mere physical separation, with continued diligent administration and support, is not abandonment.", "No, because only the husband may petition for separation of property."], "c",
      "De la Cruz v. De la Cruz: where there is 'only physical separation', and the husband 'continues to manage the conjugal properties with the same zeal … and religiously gives support', the petition fails. The remedies 'are designed to protect the conjugal partnership from waste and shield the wife from want.' Under the FC, separation in fact becomes a cause only if it has lasted at least one year and reconciliation is highly improbable (Art. 135(6)).")
s.write("09_sep.json")

# ======================= UNIONS WITHOUT MARRIAGE (FC 147–148) =======================
u = Bank("unions", "U")
TS = "Uribe CivRev recitation (2025)"

u.mcq("bar", "QuAMTO – 2024 Bar; Uribe CivRev 2025 class slide (adapted to MCQ)",
      "In 2021, Jesse and Celeste got married. After a year, Jesse took all their savings and abandoned Celeste for his paramour Diana. Jesse asked Diana to quit her job. Diana hesitated because she has no money and is drowning in debts. Yet, Jesse promised to provide for all of Diana's needs. Jesse and Diana then lived together. The following day, they bought a brand-new car exclusively registered under Diana's name. Celeste sued to recover the vehicle, claiming it is part of their community property. Diana countered that she and Jesse are co-owners. Can Celeste recover the vehicle from Diana?",
      ["No, because the car is registered in Diana's name.", "No, because Diana and Jesse are co-owners in equal shares under Article 147.",
       "Yes, because under Article 148 Diana must prove actual contribution, which she could not have made, and the funds came from the community property.", "Yes, but only one-half of the car."], "c",
      "Jesse is married to Celeste, so he and Diana are not capacitated to marry each other, and Art. 148 governs: only property acquired through their 'actual joint contribution of money, property, or industry' is co-owned. Diana was jobless and in debt, so she could not have contributed. The money came from the spouses' savings, which are community property (Arts. 75, 91, 93). In any event, Jesse's share in any co-ownership 'shall accrue to the absolute community' (Art. 148, 2nd par.). Registration in Diana's name is not proof of ownership. Uribe: support the claim with facts and law ('the money used was the salary only of the husband … Diana has no money').")
u.mcq("recit", f"{TS} (follow-up to the Jesse–Celeste–Diana problem)",
      "In the Jesse–Celeste–Diana problem, would it matter if Diana, though she had no money, did all the cooking, laundry and housekeeping for Jesse while they lived together?",
      ["Yes, she would be deemed to have contributed and would own one-half of the car.", "Yes, she would be entitled to reimbursement for her services.",
       "No, because under Article 148 contributions in the form of care and maintenance of the household are not considered.", "No, because she is not Jesse's wife."], "c",
      "Uribe: 'NO, Art. 148, contribution by way of maintenance of the household does not matter. It is only available if it would fall under 147.' Cariño v. Cariño: under Art. 148, 'contributions in the form of care of the home, children and household, or spiritual or moral inspiration, are excluded.' D gives a wrong reason, because even under Art. 147 the parties are not spouses.")
u.mcq("recit", f"{TS} (rule of thumb)",
      "A and B, first cousins, married each other and lived together. The marriage was later declared void as against public policy. Following Uribe's rule of thumb, what governs their property relations?",
      ["Absolute community of property", "Conjugal partnership of gains", "Article 147", "Article 148"], "c",
      "Uribe's rule of thumb: 'if one of them or both of them is or are married to other persons, a third person will be affected by the cohabitation or marriage (bigamous or adulterous in character): 148 will apply. All other grounds that will make a marriage void, as long as no 3rd person will be affected, 147 will apply.' First cousins: the marriage is void for public policy (Art. 38(1)), but no third person is affected, so Art. 147 applies. A void marriage never has an ACP or CPG.",
      "Textually, Art. 147 requires parties 'capacitated to marry each other', and some commentators therefore put a union with an Art. 37/38 impediment under Art. 148. On Uribe's exam, apply his rule of thumb and give the reason (no third person affected).")
u.mcq("recit", f"{TS}",
      "Under Article 147, how are the wages and salaries of the parties earned during their cohabitation owned, even if one of them merely gambled day and night and earned nothing?",
      ["In proportion to their actual contributions", "Exclusively by the party who earned them", "By them in equal shares", "By the common children"], "c",
      "Art. 147: 'their wages and salaries shall be owned by them in EQUAL SHARES'. Uribe confirmed this applies 'regardless of actual monetary contribution', even if one partner 'nagsusugal lang araw-araw at gabi-gabi … it does not matter.' For other property acquired through work or industry, co-ownership rules apply: equal shares are presumed, but proof of different contributions governs, except that care of the household counts as a joint contribution.")
u.mcq("bar", "QuAMTO – 2023 Bar (adapted to MCQ)",
      "Santiago and Lucia, both single, lived together as common-law spouses from 2000 and acquired several properties, mainly from the earnings of Lucia's salon and water refilling business. The purchase records were destroyed by Typhoon Ondoy. In 2023, Lucia filed a case claiming she is entitled to all of the properties. Is Lucia correct?",
      ["Yes, because the purchases came from her business.", "Yes, because Santiago failed to prove his contribution.",
       "No, because properties acquired during their cohabitation are presumed obtained by their joint efforts and owned in equal shares, and care of the household is a contribution.", "No, because the properties belong to the State."], "c",
      "Assuming they were capacitated to marry each other, Art. 147 applies. In the absence of proof to the contrary, properties acquired while they lived together are presumed obtained by their joint efforts and owned equally, and a party whose efforts consisted in the care and maintenance of the family and household is deemed to have contributed (Paterno v. Paterno, 2020; Barrido v. Nonato, 2014). The burden is on Lucia, and she has no records. (If they were not capacitated, Art. 148 would require proof of Santiago's actual contribution.)")
u.mcq("bar", "QuAMTO – 2018 Bar (adapted to MCQ)",
      "Sancho and Sandy, both single, married after agreeing in a marriage settlement on the conjugal partnership of gains. Their marriage was later declared void on the ground of psychological incapacity of both. What property regime will be liquidated, and is their child Shalimar entitled to the delivery of presumptive legitime?",
      ["Conjugal partnership of gains; yes", "Absolute community of property; yes", "Co-ownership under Article 147; no", "Co-ownership under Article 148; yes"], "c",
      "A void marriage never had a CPG, so the settlement's chosen regime never took effect. The parties were capacitated, and the marriage is void under Art. 36, so Art. 147 governs. The obligation to deliver presumptive legitimes under Arts. 50–51 applies to the liquidation of an ACP or CPG in annulled marriages and Art. 40 void marriages, not to an Art. 147 co-ownership (Valdes v. RTC, 1996; Diño v. Diño, 2011). In the liquidation, Sancho takes the land paid from his salary (Sandy's care of the household was not shown), and Sandy takes the jewelry bought with her lottery winnings, which are not from 'work or industry'.")
u.mcq("bar", "QuAMTO – 2016 Bar (adapted to MCQ)",
      "Bernard and Dorothy lived together as common-law spouses although both were capacitated to marry. Dorothy worked abroad and regularly sent money to Bernard, who used it to buy a lot. Bernard later sold the lot without Dorothy's consent. Will Dorothy's suit to nullify the sale prosper?",
      ["No, because the lot is registered in Bernard's name.", "No, because common-law spouses are not co-owners.",
       "Yes, unless the buyer is a buyer in good faith and for value, because neither party may dispose of his or her share in property acquired during cohabitation without the other's consent.", "Yes, in all cases, even against a buyer in good faith."], "c",
      "Art. 147, 3rd par.: 'Neither party can encumber or dispose by acts inter vivos of his or her share in the property acquired during cohabitation and owned in common, without the consent of the other, until after the termination of their cohabitation.' The UPLC answer adds the protection of buyers in good faith. The answer is the same even if Dorothy were jobless and only cared for the family and household, since those efforts are deemed a joint contribution.")
u.mcq("bar", "QuAMTO – 2015 Bar (adapted to MCQ)",
      "Bert and Joe, both male and single, lived together as common-law spouses for 20 years. Bert worked while Joe kept house and raised a boy they took in. They acquired real estate registered in both names as co-owners. Can Article 147 apply so that all the properties are presumed acquired by their joint industry and owned in equal shares?",
      ["Yes, because they lived together exclusively for 20 years.", "Yes, because Joe's care of the home is a contribution.",
       "No, because Article 147 applies only to a man and a woman capacitated to marry each other.", "No, because Bert is the only one who worked."], "c",
      "Art. 147 applies only when 'a man and a woman who are capacitated to marry each other live exclusively with each other as husband and wife.' Under Arts. 1 and 2, marriage is between a man and a woman, so Art. 147's presumptions do not apply. Their rights depend on ordinary co-ownership and proof of contribution (here, the properties are titled in both names as co-owners).")
u.mcq("bar", "QuAMTO – 2010 Bar (adapted to MCQ)",
      "In 1997, B and G started living together without the benefit of marriage, both being capacitated to marry each other, and acquired a residential lot. In 2001, they married without a license; the marriage was later declared void. To whom should the lot be awarded?",
      ["To B, who paid for it", "To G, who cared for the household", "To B and G as co-owners in equal shares", "To their child, Venus"], "c",
      "No ACP or CPG was ever established, so the Art. 147 special co-ownership applies. The lot, acquired during the cohabitation, is presumed acquired through their joint work and industry and owned in equal shares. Care and maintenance of the family counts. There is no forfeiture, because neither party is shown to be in bad faith.")
u.tf("bar", "UP BOC – 2009 Bar TF", "If there is no marriage settlement, the salary of a 'spouse' in an adulterous marriage belongs to the conjugal partnership of gains.", False,
     "In an adulterous relationship, the salary of the married partner belongs to the absolute community or conjugal partnership of that partner and his or her LAWFUL spouse. Under Art. 148, the paramour becomes a co-owner only of what was acquired by actual joint contribution, and is deemed not to have contributed to earning the married partner's salary.")
u.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "When A and B married, they chose conjugal partnership of gains to govern their property relations. After 3 years, B succeeded in getting her marriage to A annulled on ground of the latter's psychological incapacity. What liquidation procedure will they follow in disposing of their assets?",
      ["They will follow the rule governing the liquidation of a conjugal partnership of gains where the party who acted in bad faith forfeits his share in the net profits.",
       "Since the marriage has been declared void, the rule for liquidation of absolute community of property shall be followed.",
       "The liquidation of a co-ownership applies since the annulment brought their property relation under the chapter on property regimes without marriage.",
       "The law on liquidation of partnerships applies."], "c",
      "A marriage 'annulled' for psychological incapacity is actually void (Art. 36), so no CPG existed, and the property relations fall under Art. 147, liquidated as a co-ownership (Valdes v. RTC). The BOC answer is C.",
      "The question loosely says 'annulled'. Psychological incapacity makes a marriage void, not voidable. Answer as the BOC did, but use the correct term in an essay.")
u.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Venecio and Ester lived as common-law spouses since both have been married to other persons from whom they had been separated in fact for several years. Hardworking and bright, each earned incomes from their respective professions and enterprises. What is the nature of their incomes?",
      ["Conjugal since they earned the same while living as husband and wife.", "Separate since their property relations with their legal spouses are still subsisting.",
       "Co-ownership since they agreed to work for their mutual benefit.", "Communal since they earned the same as common-law spouses."], "b",
      "Art. 148 governs, since both are married to others. Wages and salaries belong to the earner and, through him or her, to the ACP or CPG of the subsisting valid marriage. Separation in fact does not dissolve those regimes (Arts. 100, 127).")
u.mcq("bar", "QuAMTO – 2000, 1997, 1992 Bar (adapted to MCQ)",
      "In 1989, Rico, a widower, cohabited with Cora, a widow; they bought rice land from their combined earnings. After they separated, Rico lived with Mabel, then 16, who kept house while Rico, a salaried employee, bought coconut land from his savings. They separated after a year, and Rico married Letty. Who owned the coconut land before Rico's marriage to Letty, and under what rule?",
      ["Rico and Mabel in equal shares, under Article 147", "Rico alone, because Article 148 applies and Mabel made no actual contribution",
       "Rico and Mabel in proportion to their contributions, under Article 147", "Mabel alone, as the one who kept house"], "b",
      "Mabel, at 16, was not capacitated to marry, so Art. 148 governs. Only actual joint contributions count, and her housekeeping does not. Rico was the exclusive owner, and the land became community property of Rico and Letty upon their marriage (Art. 91). By contrast, the rice land was co-owned by Rico and Cora under Art. 147, both being capacitated. Letty's mango orchard, bought during the marriage, belongs to their ACP.")
u.mcq("bar", "QuAMTO – 2000 Bar (adapted to MCQ)",
      "Tony, a bank vice-president, and Susan, an entertainer who stopped working and merely kept house, lived together as husband and wife for five years from 1989. Tony bought a house and lot from his salary. Would it make a difference to Susan's rights if Tony could not marry Susan because he was legally separated from his wife, Alice?",
      ["No, Susan is a co-owner in equal shares in either case.", "Yes; under Article 148, Susan's housekeeping is not a contribution, so she has no share.",
       "Yes; Susan would own the whole house and lot.", "No, because legal separation dissolves the marriage."], "b",
      "If capacitated, Art. 147 makes them co-owners in equal shares, since Susan's care of the household counts. A legally separated spouse is still married, so Art. 148 applies, and Susan, who made no actual contribution, has no share. If Tony cohabited with Susan after the decree of legal separation, the house and lot is his exclusive property (his regime with Alice having been dissolved). If before, it belongs to his ACP or CPG with Alice.")
u.mcq("bar", "QuAMTO – 1997 Bar (adapted to MCQ)",
      "Luis and Rizza, both single and 26, lived together as husband and wife for twenty years; Luis worked, Rizza kept house. Their properties are: (a) P200,000 in savings from Luis's salary; (b) a house and lot worth P500,000 bought with P200,000 from the sale of palay harvested from Luis's hacienda and P300,000 from rentals of Rizza's building; and (c) a car worth P100,000 donated to Rizza by her parents. How is the car owned?",
      ["Equally by Luis and Rizza", "By Rizza alone", "In proportion to their contributions", "By the common children"], "b",
      "Under Art. 147, only wages and salaries (shared equally) and property acquired through work or industry (co-ownership) are common. The car was acquired by gratuitous title, so it is Rizza's alone. In the UPLC answer, the savings are divided equally, and the house and lot, bought from fruits of separate properties, is shared in proportion: Luis two-fifths, Rizza three-fifths.")
u.mcq("bar", "QuAMTO – 1991 Bar (adapted to MCQ)",
      "In June 1985, James married Mary. In September 1988, he also married Ophelia, with whom he had two children and acquired a residential lot. Mary died in July 1989; in July 1990 James married Shirley. What property regime governed the union of James and Ophelia?",
      ["Absolute community of property", "Conjugal partnership of gains", "Article 147 special co-ownership", "Article 148 co-ownership limited to actual joint contribution"], "d",
      "The marriage to Ophelia was bigamous and void, and James was not capacitated to marry her. Under Art. 148, only property acquired through actual joint contribution is co-owned, in proportion to the contributions (presumed equal absent proof), and James's share accrues to his CPG with Mary for as long as that marriage subsisted.")

# recitation and new
u.mcq("recit", "Uribe recitation situationer (2018)",
      "The marriage between A and B was declared void. During the cohabitation, A saved P1 million in a bank and bought a condominium unit from his income, registered in his name. B inherited a parcel of land from her grandmother. Who owns the inherited land?",
      ["A and B in equal shares under Article 147", "A and B in proportion to contributions under Article 148", "B alone, under either Article 147 or 148", "A alone"], "c",
      "Neither co-ownership covers property acquired by gratuitous title. Art. 147 covers wages and salaries and property acquired 'through their work or industry', and Art. 148 covers property acquired through 'actual joint contribution'. So the land is B's alone. The savings and the condo depend on why the marriage was void (Uribe: 'Depends why marriage was declared void, Art. 147 & 148'). Under 147, they are shared equally, with B's care of the household counting. Under 148, they are A's unless B proves actual contribution.")
u.tf("new", "New (Uribe format; FC 147)", "When a man and a woman who are capacitated to marry each other live exclusively with each other as husband and wife without the benefit of marriage, their wages and salaries shall be owned by them in proportion to their respective contributions.", False,
     "Art. 147: their wages and salaries 'shall be owned by them in EQUAL SHARES'. It is the property acquired through their work or industry that is governed by the rules on co-ownership, where proven contributions matter, subject to the presumption of equal shares and the rule on care of the household.")
u.tf("new", "New (Uribe format; FC 147)", "For purposes of Article 147, a party who did not participate in the acquisition by the other party of any property shall be deemed to have contributed jointly in the acquisition thereof if the former's efforts consisted in the care and maintenance of the family and of the household.", True,
     "Verbatim Art. 147, 2nd par., last sentence. This is the key difference from Art. 148.")
u.tf("new", "New (Uribe format; FC 147)", "Under Article 147, neither party can encumber or dispose by acts inter vivos of his or her share in the property acquired during cohabitation and owned in common, without the consent of the other, until after the termination of their cohabitation.", True,
     "Verbatim Art. 147, 3rd par.")
u.tf("new", "New (Uribe format; FC 147)", "When only one of the parties to a void marriage is in good faith, the share of the party in bad faith in the co-ownership shall be forfeited in favor of the innocent party.", False,
     "Art. 147, 4th par.: forfeited 'in favor of their COMMON CHILDREN'. If any or all of them default or waive, each vacant share goes to their respective surviving descendants. Only in the absence of descendants does the share go to the innocent party. In all cases, the forfeiture takes place upon termination of the cohabitation.")
u.tf("new", "New (Uribe format; FC 148)", "In cases of cohabitation not falling under Article 147, only the properties acquired by both of the parties through their actual joint contribution of money, property, or industry shall be owned by them in common in proportion to their respective contributions. In the absence of proof to the contrary, their contributions and corresponding shares are presumed to be equal.", True,
     "Verbatim Art. 148, 1st par. Note that the presumption of equal shares presupposes proof that both actually contributed (Ventura v. Abuda; Borromeo v. Descallar).")
u.tf("new", "New (Uribe format; FC 148)", "Under Article 148, the rules on forfeiture of the share of the party in bad faith shall not apply if both parties are in bad faith.", False,
     "Art. 148, last par.: 'The foregoing rules on forfeiture shall likewise apply EVEN IF BOTH PARTIES ARE IN BAD FAITH.'")
u.pair("new", "New (Uribe format; FC 148)",
       "Under Article 148, if one of the parties is validly married to another, his or her share in the co-ownership shall accrue to the absolute community or conjugal partnership existing in such valid marriage.",
       "Under Article 148, the efforts of a party consisting in the care and maintenance of the family and household shall be deemed a contribution to the acquisition of property.",
       True, False,
       "No. 1 is TRUE (Art. 148, 2nd par.). No. 2 is FALSE. That rule appears only in Art. 147. Under Art. 148, 'contributions in the form of care of the home, children and household, or spiritual or moral inspiration, are excluded' (Cariño v. Cariño).")
u.mcq("new", "New (Maxey v. CA, 129 SCRA 187)",
      "Under Article 144 of the Civil Code (now Article 147), if only the man works and the woman takes care of the children and the household during their cohabitation, how is the property acquired during the cohabitation owned?",
      ["By the man alone", "By both, in proportion to their monetary contributions", "By both, on a fifty-fifty basis", "By the common children"], "c",
      "Maxey v. CA: 'Even if it is only the man who works, the property acquired during the man and wife relationship belongs through a fifty-fifty sharing to the two of them.' The woman's 'real contribution' includes 'caring for the children, administering the household, husbanding scarce resources, freeing her husband from household tasks.'")
u.mcq("new", "New (Juaniza v. Jose, 89 SCRA 306)",
      "E, a married man, lived with R and registered a jeepney in his own name. The jeepney figured in a collision, and the victims sought to hold R liable as a co-owner of the jeepney. Is R a co-owner?",
      ["Yes, because she lived with E as his wife.", "Yes, under Article 144 of the Civil Code.",
       "No, because the co-ownership under Article 144 requires that the parties not be incapacitated to marry; the jeepney belongs to E's conjugal partnership with his legal wife.", "No, because the jeepney is registered in E's name."], "c",
      "Juaniza v. Jose: the co-ownership under NCC 144 'requires that the man and the woman living together must not in any way be incapacitated to contract marriage.' E was legally married to another, so R 'cannot be a co-owner of the jeepney. The jeepney belongs to the conjugal partnership of Jose and his legal wife.' Art. 148 now codifies this.")
u.mcq("new", "New (Vda. de Consuegra v. GSIS; Gomez v. Lipana)",
      "J married R. While that marriage subsisted, he married B in good faith. Both marriages were celebrated under the old law, and the second was never judicially declared void before J's death. How are J's retirement benefits divided between the first and second wives, under the rule applied in Vda. de Consuegra v. GSIS?",
      ["All to the first wife", "All to the second wife and her children", "One-half to the second wife (her share in the property acquired with her), the other half to the conjugal partnership of the first marriage", "Equally among all the children"], "c",
      "Consuegra, following Gomez v. Lipana: since the first marriage was never dissolved, its conjugal partnership never ceased. 'The only just and equitable solution in this case would be to recognize the right of the second wife to her share of one-half in the property acquired by her and her husband and consider the other half as pertaining to the conjugal partnership of the first marriage.'")
u.mcq("new", "New (Yap v. CA, 145 SCRA 229)",
      "M validly married T, and later contracted a void second marriage with N. Under Yap v. CA, is N entitled to a share in M's estate as his 'wife'?",
      ["Yes, as a legal heir", "Yes, one-half of the estate", "No; only the legal wife shares in the estate", "Yes, equally with T"], "c",
      "Yap v. CA: the second marriage was void under the Marriage Law, and the second 'wife' got no share in the husband's estate. Only the legal wife did.")
u.mcq("new", "New (Cariño v. Cariño, 351 SCRA 127)",
      "Under Article 148, as explained in Cariño v. Cariño, which of the following is correct?",
      ["Wages and salaries earned by each party are owned in equal shares.", "Wages and salaries earned by each party belong to him or her exclusively.",
       "Care of the home and children counts as a contribution.", "All property acquired during cohabitation is presumed co-owned in equal shares."], "b",
      "Cariño: in the Art. 148 regime (bigamous marriages, adulterous relationships, concubinage, both parties married to others, multiple alliances), 'the properties acquired by the parties through their actual joint contribution shall belong to the co-ownership. Wages and salaries earned by each party belong to him or her exclusively. Then too, contributions in the form of care of the home, children and household, or spiritual or moral inspiration, are excluded.'")
u.mcq("new", "New (Go-Bangayan v. Bangayan; Ventura v. Abuda)",
      "B, validly married to A, lived with S under a void marriage. Properties were titled in the name of 'B, married to S'. S claims co-ownership but offers no proof of her actual contribution. Is S a co-owner?",
      ["Yes, because the title names her as B's wife.", "Yes, because contributions are presumed equal.",
       "No, because 'married to' is merely descriptive, and without proof of actual contribution there is no co-ownership under Article 148.", "No, because S is in bad faith."], "c",
      "Go-Bangayan: 'the words married to preceding the name of a spouse are merely descriptive of the civil status of the registered owner. Such words do not prove co-ownership. Without proof of actual contribution from either or both spouses, there can be no co-ownership under Article 148.' Ventura v. Abuda: 'Presumptions of co-ownership and equal contribution do not apply' until actual contribution is proved.")
u.mcq("new", "New (Salas, Jr. v. Aguila, G.R. No. 202370, 2013)",
      "The marriage of J and E was declared void on the ground of psychological incapacity. Properties acquired during their union were later discovered. On what basis should they be partitioned?",
      ["Conjugal partnership of gains", "Absolute community of property", "Co-ownership under Article 147", "Article 148, upon proof of actual contribution"], "c",
      "Salas v. Aguila: for a marriage void under Art. 36 between capacitated parties, 'property acquired during the marriage is prima facie presumed to have been obtained through the couple's joint efforts and governed by the rules on co-ownership.' The partition was sustained 'but on the basis of co-ownership and not on the regime of conjugal partnership of gains.'")
u.mcq("new", "New (FC 147 vs 148)",
      "Which of the following unions is governed by Article 148 rather than Article 147?",
      ["A man and a woman, both single and of age, living together without marriage", "Spouses whose marriage was declared void for lack of a marriage license",
       "A married man living with his paramour", "Spouses whose marriage was declared void on the ground of psychological incapacity"], "c",
      "Art. 148 covers cohabitation 'not falling under' Art. 147, i.e., where the parties are not capacitated to marry each other, as with a married man and his paramour (Cariño). A, B and D involve parties capacitated to marry each other, living exclusively as husband and wife without marriage or under a void marriage, so Art. 147 applies.")
u.write("10_unions.json")
