from qb import Bank, ABS

# ======================= THE FAMILY (FC 149–151) and THE FAMILY HOME (FC 152–162) =======================
f = Bank("family", "F")
MT = "Uribe Midterm Exam (Civ Rev samplex)"
TSR = "Uribe CivRev 2025 recitation (Sep 27, 2025)"
SIT = "Uribe recitation situationer (Sep 18, 2018)"

# ---- Art. 149–151
f.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Janice and Jennifer are sisters. Janice sued Jennifer and Laura, Jennifer's business partner for recovery of property with damages. The complaint did not allege that Janice exerted earnest efforts to come to a compromise with the defendants and that such efforts failed. The judge dismissed the complaint outright for failure to comply with a condition precedent. Is the dismissal in order?",
      ["No, since Laura is a stranger to the sisters, Janice has no moral obligation to settle with her.", "Yes, since court should promote amicable settlement among relatives.",
       "Yes, since members of the same family, as parties to the suit, are required to exert earnest efforts to settle their disputes before coming to court.", "No, the family council, which would ordinarily mediate the dispute, has been eliminated under the Family Code."], "a",
      "Art. 151 applies only to suits between members of the same family. When a stranger (Laura) is a co-party, the requirement does not apply (Gonzales v. Lopez; Hontiveros v. RTC; Uribe's 2018 situationer: 'There is a stranger'). Besides, the defect is not jurisdictional and should not be the basis of an outright dismissal (Heirs of Favis).")
f.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "The wife filed a case of legal separation against her husband on the ground of sexual infidelity without previously exerting earnest efforts to come to a compromise with him. The judge dismissed the case for having been filed without complying with a condition precedent. Is the dismissal proper?",
      ["No, efforts at a compromise will only deepen the wife's anguish.", "No, since legal separation like validity of marriage is not subject to compromise agreement for purposes of filing.",
       "Yes, to avoid a family feud that is hurtful to everyone.", "Yes, since the dispute could have been settled with the parties agreeing to legal separation."], "b",
      "Art. 151, last paragraph: the rule does not apply to cases that may not be compromised under the Civil Code. NCC 2035 bars compromise on the validity of a marriage or a legal separation and on any ground for legal separation.")
f.mcq("recit", f"{SIT} (adapted to MCQ)",
      "A filed an action for support against X and Y, A being the illegitimate child of X, and Y being the spouse of X. The case went up to the Supreme Court, where X raised for the first time the defense that the action cannot prosper because A failed to allege that earnest efforts toward a compromise were made. Decide.",
      ["The action must be dismissed because Art. 151 is mandatory.", "The defense fails: it is only a ground for a motion to dismiss and is not jurisdictional, and Y is a stranger under Art. 150.",
       "The case must be remanded so that A can amend the complaint.", "The defense prospers because support is a family matter."], "b",
      "Uribe's 2018 answer: 'The defense of lack of earnest efforts is only a ground for a Motion to Dismiss. Also, this is not jurisdictional. There is a stranger to the suit who does not fall under family relations (Art. 150).' Y is A's stepmother, a relative by affinity. Also, future support cannot be compromised (NCC 2035(4); Wainwright-Versoza).")
f.tf("recit", f"{SIT} (follow-up)", "In the same case (A, the illegitimate child of X, sued X and X's spouse Y for support), if X had timely filed a motion to dismiss for failure to allege earnest efforts toward a compromise, the motion should be granted.", False,
     "Sir's answer to the follow-up ('Assuming X filed an MTD, will the action prosper?'): 'No. There is a stranger.' The motion fails because Y is not a member of A's family under Art. 150, and future support is not compromisable anyway.")
f.tf("recit", f"{TSR} (adapted)", "If A filed an action for a sum of money against his father X and his mother Y, and the verified complaint does not allege that earnest efforts toward a compromise were made and failed, the defendants may move to dismiss the complaint under Art. 151.", True,
     "All the parties are members of the same family (parents and children, Art. 150(2)), and a money claim is compromisable. In class, Sir first stressed that the facts did not say Y was A's mother; do not assume facts. Assuming Y is the mother, the contention is tenable under Art. 151.")
f.tf("new", "New (Uribe format; FC 149)", "The family, being the foundation of the nation, is a basic social institution which public policy cherishes and protects. Consequently, family relations are governed by law and no custom, practice or agreement destructive of the family shall be recognized or given effect.", True,
     "Verbatim Art. 149.")
f.tf("new", "New (Uribe format; FC 149)", "Family relations are governed by law and by the customs of the place, and no agreement destructive of the family shall be recognized or given effect.", False,
     "Art. 149: family relations are governed by LAW, and 'no CUSTOM, practice or agreement destructive of the family shall be recognized or given effect.' Customs are not a source that governs family relations.")
f.mcq("new", "New (FC 150)",
      "Which of the following is NOT among the family relations enumerated in Article 150 of the Family Code?",
      ["Between husband and wife", "Among other ascendants and descendants", "Among brothers and sisters, whether of the full or half-blood", "Between a person and his brother-in-law"], "d",
      "Art. 150 lists four: (1) husband and wife; (2) parents and children; (3) other ascendants and descendants; (4) brothers and sisters, full or half-blood. Relatives by affinity are not included, and the list is strictly construed (Gayon v. Gayon). Note that some reviewers drop item (3); the official text has it.")
f.tf("new", "New (Uribe format; FC 150)", "Family relations include those between parents and children, and among brothers and sisters, whether of the full or half-blood, but not those between grandparents and grandchildren.", False,
     "Art. 150(3): 'Among other ascendants and descendants.' Grandparents and grandchildren are family under Art. 150. Watch reviewers that list only three items.")
f.tf("new", "New (Uribe format; FC 151)", "No suit between members of the same family shall prosper unless it should appear from the verified complaint or petition that earnest efforts toward a compromise have been made, but that the same have failed.", True,
     "Verbatim Art. 151, first sentence. It continues: 'If it is shown that no such efforts were in fact made, the same case must be dismissed. This rule shall not apply to cases which may not be the subject of compromise under the Civil Code.'")
f.tf("new", "New (Uribe format; FC 151)", "The failure to allege in the complaint that earnest efforts toward a compromise have been made is a jurisdictional defect which the court may raise motu proprio at any stage of the proceedings.", False,
     "It is a condition precedent, not a jurisdictional requirement. If not raised in a motion to dismiss or the answer, it is waived, and the court cannot dismiss motu proprio on that ground (Heirs of Favis, Sr. v. Gonzales, 2014; Rule 9, Sec. 1).")
f.pair("new", "New (Uribe format; FC 151, NCC 2035)",
       "A suit between a man and his nephew over a parcel of land requires an allegation in the verified complaint that earnest efforts toward a compromise have been made and have failed.",
       "An action for future support between spouses requires an allegation that earnest efforts toward a compromise have been made and have failed.",
       False, False,
       "No. 1 is FALSE: uncles and nephews are not in Art. 150, which is strictly construed (Gayon v. Gayon: 'a sister-in-law, nephew or niece is not included'). No. 2 is FALSE: future support cannot be compromised (NCC 2035(4)), so the earnest-efforts requirement does not apply (Wainwright-Versoza v. Versoza).")
f.mcq("new", "New (NCC 2035)",
      "Under Article 2035 of the Civil Code, a compromise is valid on which of the following?",
      ["The civil status of persons", "Support in arrears", "Any ground for legal separation", "Future legitime"], "b",
      "NCC 2035 bars compromise on (1) civil status, (2) validity of a marriage or a legal separation, (3) any ground for legal separation, (4) FUTURE support, (5) jurisdiction of courts, and (6) future legitime. Support already due (in arrears) may be compromised.")
f.mcq("new", "New (Arroyo v. CA)",
      "A husband filed a complaint for adultery against his wife and her paramour, who were convicted. He later manifested that he had pardoned his wife and was no longer interested in the case. What is the effect?",
      ["The case must be dismissed because adultery is a private crime", "The conviction stands, because a pardon must precede the institution of the criminal action, and control of the case has passed to the public prosecutor",
       "Only the wife is acquitted", "The paramour alone remains liable"], "b",
      "Arroyo v. CA (1991): once the complaint is filed, control passes to the public prosecutor; enforcement of the adultery law protects the basic social institutions of marriage and the family, in which the State has the strongest interest. A pardon must be given before the institution of the action.")

# ---- Family home
f.pair("samplex", f"{MT} Part One #7",
       "A marriage solemnized in 1990 between collateral blood relatives whether legitimate or illegitimate, up to the fourth civil degree is incestuous and void from the beginning.",
       "The family home, constituted jointly by the husband and the wife or by an unmarried head of a family, is the dwelling house where they and their family resides, or the land on which it is situated.",
       False, False,
       "No. 1 is FALSE: collateral relatives up to the fourth civil degree fall under Art. 38(1) (void for reasons of public policy); only brothers and sisters (Art. 37(2)) make the marriage incestuous. No. 2 is FALSE: Art. 152 says the dwelling house 'AND the land on which it is situated.' The printed explanation adds: 'SC: If the land is not owned by the spouses who are the owners of the house, they could not have constituted a family home.' (In 2025 Sir questioned that SC line in recitation; see the reviewer.)",
       topic="famhome")
f.pair("samplex", f"{MT} Part One #10",
       "The family home must be part of the properties of the absolute community or the conjugal partnership.",
       "Children conceived and born before the judgment of annulment or absolute nullity of the marriage under Article 36 has become final and executory shall be considered legitimate.",
       False, True,
       "No. 1 is FALSE: Art. 156 adds 'or of the exclusive properties of either spouse with the latter's consent', and an unmarried head of a family may constitute it on his or her own property (also the conditional sale on installments). No. 2 is TRUE: Art. 54 says 'conceived OR born'; a child conceived AND born before finality is covered a fortiori. (The scan's answer letter is illegible; this follows the printed explanation for No. 1.)",
       topic="famhome")
f.mcq("samplex", f"{MT} Part Two #42",
      "The family home shall NOT be exempt from execution, forced sale or attachment except:",
      ["For nonpayment of taxes.", "For debts incurred prior to the constitution of the family home.", "For debts due to laborers who have rendered service for the construction of the building.",
       "For debts due to laborers who have rendered service for the repair and improvements of the building.", "None of the above."], "d",
      "Read the stem as 'the family home is exempt except …' and find the choice that is NOT an Art. 155 exception. (a), (b) and (c) are Arts. 155(1), (2) and (4). Art. 155(4) covers service or material 'for the CONSTRUCTION of the building'; repairs and improvements are not mentioned, so (d) is the odd one out. Another circulated key marks (e); that is right only if 'construction' is read to include repairs and improvements, as Tolentino suggests.",
      key="Keys differ: one copy of this midterm marks (e); the R-set version marks (d). This bank follows the codal reading (d).", topic="famhome")
f.tf("samplex", "Uribe Quiz No. 3 (NCC Samplex) TF6", "Brothers and sisters of the spouses who constituted the family home are beneficiaries of such family home.", False,
     "Art. 154(2): brothers and sisters are beneficiaries only if they 'are living in the family home and … depend upon the head of the family for legal support.' The statement omits both qualifiers, so it is not absolutely true.", topic="famhome")
f.mcq("bar", "UP BOC – 2011 Bar MCQ",
      "Spouses A and B leased a piece of land belonging to B's parents for 25 years. The spouses built their house on it worth P300,000.00. Subsequently, in a case that C filed against A and B, the court found the latter liable to C for P200,000.00. When the sheriff was attaching their house for the satisfaction of the judgment, A and B claimed that it was exempt from execution, being a family home. Is this claim correct?",
      ["Yes, because while B's parents own the land, they agreed to have their daughter build her family home on it.", "No, because there is no judicial declaration that it is a family home.",
       "No, since the land does not belong to A and B, it cannot qualify as a family home.", "Yes, because the A and B's family actually lives in that house."], "c",
      "Arts. 152 and 156: the family home is the dwelling house AND the land, and it must be on property of the ACP/CPG, a spouse's exclusive property (with consent), or the unmarried head's own property. Uribe disagrees with this line in recitation (the dwelling house alone, e.g., a condo unit, should qualify), but his own midterm key and the bar answer follow it. B is wrong: no judicial declaration is needed under the FC (Art. 153).",
      topic="famhome")
f.mcq("recit", f"{TSR} (adapted to MCQ)",
      "X and Y constituted their house and lot in the province as their family home. Their son A and his wife B work in Metro Manila and left their 5-year-old child with X and Y, sending money for his care. X and Y died in an accident. How long does the house and lot remain a family home under Art. 159?",
      ["Until the grandchild reaches 18, i.e., about 13 years", "For 10 years from the death, unless there is a beneficiary who is still a minor, the grandchild not being a beneficiary",
       "It ceases immediately upon the death of X and Y", "For as long as the grandchild lives in it"], "b",
      "Sir: 'the premise of the answer is the child is a beneficiary … This child is not a beneficiary because he is not relying on the grandparents for support. He is only living in the family home.' Under Art. 154 a relative must live in the home AND depend on the head of the family for legal support (Patricio v. Dario III, 2006). So the minor-beneficiary extension does not apply; the 10-year rule of Art. 159 does (if there are other beneficiaries).",
      topic="famhome")
f.tf("recit", f"{SIT}", "A family home may be constituted in a property which is neither owned by one of the constituting parties nor is a community or a conjugal property.", True,
     "The 2018 class's recorded answer is 'Yes', in line with Sir's policy view (the family home is the family's dwelling; e.g., condo units) and Art. 156, 2nd par. (property bought on a conditional sale on installments, where the vendor still owns it). Caution: the codal rule in Art. 156, par. 1 and the SC line (followed in Sir's own midterm key and the 2011 bar) are stricter.",
     key="Uribe's recitation view; on a codal quiz the stricter Art. 156 reading may be keyed instead.", topic="famhome")
f.tf("recit", f"{SIT} (adapted)", "Sps. X and Y invited their son A and his wife to build their house on a lot owned by X and Y. A and his wife later incurred a debt; the house and lot were levied upon, and only during the case did A and his wife claim that the property cannot be levied upon because it is their family home. The defense is tenable.", False,
     "Sir's 2018 answer: 'No, case in the syllabus. They should have opposed the levy.' The exemption is a personal right that must be invoked and proved at the time of the levy or within a reasonable time; it is not the sheriff's duty to presume it (Spouses De Mesa v. Acero, 2012).", topic="famhome")
f.mcq("bar", "UP BOC – 2014 Bar (adapted to MCQ)",
      "Mariano died intestate in 2000, survived by his wife Leonora and children Danilo and Carlito. He left a residential house and lot. Leonora and Danilo want to partition it. Carlito opposes under Art. 159, alleging that his minor child Lucas still lives in the premises. Is Carlito's contention tenable?",
      ["Yes, because the family home continues as long as there is a minor beneficiary.", "No, because Lucas is not a beneficiary: his legal support is primarily his father Carlito's obligation, not his grandmother's.",
       "Yes, because the heirs cannot partition the family home within 20 years.", "No, because Art. 159 applies only if the deceased constituted the family home judicially."], "b",
      "Patricio v. Dario III (2006): a beneficiary must (1) be among those listed in Art. 154, (2) live in the family home, and (3) depend on the head of the family for legal support. Lucas meets the first two but not the third. Partition may be granted.", topic="famhome")
f.tf("bar", "UP BOC – 2010 Bar (True or False)", "X, a widower, died leaving a will stating that the house and lot where he lived cannot be partitioned for as long as the youngest of his four children desires to stay there. As coheirs and co-owners, the other three may demand partition anytime.", False,
     "NCC 1083 allows a testator to prohibit partition for up to 20 years. Even without a will, if the house and lot was their family home, Art. 159 bars partition for 10 years or as long as there is a minor beneficiary living in the family home, unless the court finds compelling reasons.", topic="famhome")
f.tf("new", "New (Uribe format; FC 152)", "The family home, constituted jointly by the husband and the wife or by an unmarried head of a family, is the dwelling house where they and their family reside, and the land on which it is situated.", True,
     "Verbatim Art. 152.", topic="famhome")
f.tf("new", "New (Uribe format; FC 153)", "The family home is deemed constituted on a house and lot from the time it is registered as such in the Registry of Property.", False,
     "Art. 153: 'from the time it is OCCUPIED as a family residence.' Judicial or extrajudicial constitution and recording were Civil Code requirements (Ramos v. Pangilinan: 'After the effectiveness of the Family Code, this requirement … is erased').", topic="famhome")
f.tf("new", "New (Uribe format; FC 153)", "From the time of its constitution and so long as any of its beneficiaries actually resides therein, the family home continues to be such and is exempt from execution, forced sale or attachment except as hereinafter provided and to the extent of the value allowed by law.", True,
     "Verbatim Art. 153, second sentence.", topic="famhome")
f.mcq("new", "New (Modequillo v. Breva)",
      "In 1976, X incurred a liability for damages in a vehicular accident. Judgment became final in 1988, after the Family Code took effect, and the sheriff levied on the house and lot X's family had occupied since 1969 (never constituted as a family home under the Civil Code). Is the property exempt?",
      ["Yes, because Art. 162 makes the Family Code apply to existing family residences", "Yes, because the family home is deemed constituted from the time of occupancy in 1969",
       "No, because existing residences became family homes only prospectively, and the liability was incurred before the constitution", "No, because a family home must be judicially constituted"], "c",
      "Modequillo v. Breva (1990): Art. 162 does not make Arts. 152–153 retroactive; existing family residences are 'prospectively entitled to the benefits accorded to a family home under the Family Code.' The debt arose before the constitution, so Art. 155(2) applies.", topic="famhome")
f.mcq("new", "New (FC 154)",
      "Who among the following is a beneficiary of the family home constituted by spouses H and W?",
      ["H's brother, who lives in the house but is employed and supports himself", "W's mother, who lives in the house and depends on H and W for support",
       "H's nephew, who lives in the house and depends on H for support", "W's adult daughter, who depends on H and W for support but lives in a dormitory in another city"], "b",
      "Art. 154(2): parents, ascendants, descendants, brothers and sisters, legitimate or illegitimate, 'who are living in the family home and who depend upon the head of the family for legal support.' A fails dependence; C is not within the listed relationships; D fails residence.", topic="famhome")
f.tf("new", "New (Uribe format; FC 154)", "The beneficiaries of a family home include the parents, ascendants, descendants, brothers and sisters of the husband and wife, provided the relationship is legitimate, who are living in the family home and who depend upon the head of the family for legal support.", False,
     "Art. 154(2): 'whether the relationship be legitimate OR ILLEGITIMATE.'", topic="famhome")
f.mcq("new", "New (FC 155)",
      "The family home is exempt from execution, forced sale or attachment, EXCEPT for:",
      ["debts incurred after the constitution of the family home", "debts secured by mortgages on the premises before or after such constitution",
       "debts due to a credit card company", "debts due to the family's household helpers"], "b",
      "Art. 155: (1) nonpayment of taxes; (2) debts incurred PRIOR to the constitution; (3) debts secured by mortgages on the premises before or after such constitution; (4) debts due to laborers, mechanics, architects, builders, materialmen and others for the construction of the building.", topic="famhome")
f.mcq("new", "New (Siari Valley v. Lucasan)",
      "While a money judgment against D was on appeal, D occupied his house and lot as a family residence and claimed it was exempt because the judgment debt was still disputed. Is the house and lot exempt from execution once the judgment becomes final?",
      ["Yes, because the debt was not yet final when the family home was constituted", "Yes, because a disputed debt is not a debt",
       "No, because the obligation was incurred before the constitution; whether disputed or inchoate is immaterial", "No, because family homes are never exempt from money judgments"], "c",
      "Siari Valley Estates v. Lucasan (1960): the rule protects creditors against debtors who constitute a family home to defeat their claims; 'it would be immaterial if the debt incurred be undisputed or inchoate.' The money judgment is a 'debt' under Art. 155(2) (then NCC 243(2)).", topic="famhome")
f.tf("new", "New (Uribe format; FC 156)", "Property that is the subject of a conditional sale on installments where ownership is reserved by the vendor only to guarantee payment of the purchase price may be constituted as a family home.", True,
     "Verbatim Art. 156, second paragraph.", topic="famhome")
f.tf("new", "New (Uribe format; FC 157)", "The actual value of the family home shall not exceed, at the time of its constitution, the amount of three hundred thousand pesos in rural areas, and two hundred thousand pesos in urban areas.", False,
     "Art. 157: ₱300,000 in URBAN areas and ₱200,000 in RURAL areas. Urban areas include chartered cities and municipalities whose annual income at least equals that legally required for chartered cities.", topic="famhome")
f.tf("new", "New (Uribe format; FC 157, Eulogio v. Bell)", "In determining whether the family home exceeds the value allowed by law, its present market value at the time of the levy is controlling.", False,
     "Art. 157 refers to the actual value 'at the time of its constitution' (Eulogio v. Bell, 2015: the basis is the actual value at the time of constitution, not its present market value). Under Art. 160, an increase from voluntary improvements is also considered.", topic="famhome")
f.mcq("new", "New (FC 158)",
      "The family home may be sold, alienated, donated, assigned or encumbered by the owner with the written consent of:",
      ["all the beneficiaries", "the person constituting the same, the latter's spouse, and a majority of the beneficiaries of legal age",
       "the person constituting the same and all the beneficiaries of legal age", "the court"], "b",
      "Art. 158. In case of conflict, the court decides.", topic="famhome")
f.tf("new", "New (Uribe format; FC 159)", "The family home shall continue despite the death of one or both spouses or of the unmarried head of the family for a period of ten years or for as long as there is a minor beneficiary, and the heirs cannot partition the same unless the court finds compelling reasons therefor.", True,
     "Verbatim Art. 159, first sentence. It adds: 'This rule shall apply regardless of whoever owns the property or constituted the family home.'", topic="famhome")
f.tf("new", "New (Uribe format; FC 159)", "The family home shall continue despite the death of the spouses for a period of ten years or for as long as there is a minor beneficiary, but only if the property belongs to the deceased spouses.", False,
     "Art. 159: 'This rule shall apply REGARDLESS of whoever owns the property or constituted the family home.'", topic="famhome")
f.pair("new", "New (Uribe format; FC 160)",
       "When a creditor whose claim is not among those mentioned in Article 155 obtains a judgment in his favor, and he has reasonable grounds to believe that the family home is actually worth more than the maximum amount fixed by law, he may apply to the court which rendered the judgment for an order directing the sale of the property under execution.",
       "At the execution sale, the proceeds shall be applied first to the liabilities under the judgment and the costs, and then to the amount mentioned in Article 157.",
       True, False,
       "No. 1 is TRUE (Art. 160, first sentence). No. 2 is FALSE: 'The proceeds shall be applied FIRST to the amount mentioned in Article 157, and THEN to the liabilities under the judgment and the costs. The excess, if any, shall be delivered to the judgment debtor.' Also: 'no bid below the value allowed for a family home shall be considered.'", topic="famhome")
f.tf("new", "New (Uribe format; FC 161)", "For purposes of availing of the benefits of a family home, a person may constitute, or be the beneficiary of, only one family home.", True,
     "Verbatim Art. 161.", topic="famhome")
f.mcq("new", "New (De Mesa v. Acero; Salazar v. Felias)",
      "Which statement on claiming the family-home exemption is correct?",
      ["The sheriff must determine on his own whether levied property is a family home", "The claim may be raised at any time, even years after the auction sale has become final",
       "The claimant must invoke and prove the exemption at the time of the levy or within a reasonable time thereafter", "Occupancy of a house by a family conclusively establishes that it is a family home"], "c",
      "De Mesa v. Acero (2012): the exemption is a personal right that may be waived or barred by laches; 'it is not the sheriff's duty to presume or raise the status of the subject property as a family home.' Salazar v. Felias (2018): the claim must be backed by evidence that the home was duly constituted, by the proper persons, resided in by the family, on the proper property, and within the value limit.", topic="famhome")
f.tf("new", "New (Uribe format; FC 155(3), Fortaleza v. Lapitan)", "Spouses who voluntarily mortgaged their family home to a bank may successfully invoke the family-home exemption to stop the foreclosure sale.", False,
     "Art. 155(3): the family home is not exempt 'for debts secured by mortgages on the premises before or after such constitution' (Fortaleza v. Lapitan, 2012; Equitable PCI Bank v. OJ-Mark Trading, 2010).", topic="famhome")
f.write("11_family.json")
