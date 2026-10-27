"""Adoption through civil register drill cards (syllabus XIV–XXII).

Run after drills_pr.py and drills_fam.py. Idempotent: removes any earlier LT cards
and the grids defined here before appending.
"""
import json, os
from drills_pr import one_span

H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, "..", "data", "drill")

# ---------------------------------------------------------------- cloze
C = [
 # adoption
 ("adopt", "Sec. 21(a), R.A. 11642", "Any Filipino citizen at least [[twenty-five]] (25) years of age, who is in possession of full civil capacity and legal rights …", ["25", "twenty five"], "R.A. 8552 and the FC: of legal age."),
 ("adopt", "Sec. 21(a), R.A. 11642", "… has not been convicted of any crime involving [[moral turpitude]] …", [], "Not 'a crime punishable by more than six years'."),
 ("adopt", "Sec. 21(a), R.A. 11642", "… at least [[sixteen]] (16) years older than the adoptee …", ["16"], "Waivable for the biological parent or the spouse of the adoptee's parent."),
 ("adopt", "Sec. 21(a), R.A. 11642", "Provided, That the requirement of sixteen (16)-years difference … may be waived when the adopter is the biological parent of the adoptee, or is the [[spouse of the adoptee's parent]];", ["spouse of the adoptees parent"], "Two waivers only."),
 ("adopt", "Sec. 21(e), R.A. 11642", "Foreign nationals who are permanent or habitual residents of the Philippines for at least [[five]] (5) years …", ["5"], "Three years under R.A. 8552."),
 ("adopt", "Sec. 21, R.A. 11642", "Spouses shall jointly adopt, except … (b) If one spouse seeks to adopt own illegitimate child: Provided, That the other spouse has signified [[consent]] thereto;", [], "Consent, not joint adoption (Uribe Quiz 2 #7)."),
 ("adopt", "Sec. 21, R.A. 11642", "Spouses shall jointly adopt, except … (c) If the spouses are [[legally separated]] from each other.", [], "Third exception."),
 ("adopt", "Sec. 22(d), R.A. 11642", "A Filipino of legal age if, prior to the adoption, said person has been consistently considered and treated by the adopters as their own child for a period of at least [[three]] (3) years;", ["3"], "R.A. 8552: during minority."),
 ("adopt", "Sec. 22(g), R.A. 11642", "A child whose biological or adoptive parents have died: Provided, That no proceedings shall be initiated within [[six]] (6) months from the time of death of said parents;", ["6"], "Six months."),
 ("adopt", "Sec. 23(a), R.A. 11642", "The written consent of the following … (a) The adoptee, if [[ten]] (10) years of age or over;", ["10"], "Younger children are counseled and consulted."),
 ("adopt", "Sec. 41, R.A. 11642", "The legitimate filiation that is created between the adopter and adoptee shall be extended to the adopter's parents, adopter's legitimate siblings, and legitimate [[descendants]].", [], "New under R.A. 11642."),
 ("adopt", "Sec. 47, R.A. 11642", "Adoption, being in the best interest of the child, shall not be subject to rescission by the [[adopter]].", ["adopters", "adopter(s)"], "He may only disinherit (NCC 919)."),
 ("adopt", "Sec. 4, R.A. 11222", "… provided, further, That such person or persons has or have filed a petition for adoption with an application for the rectification of the simulated birth record within [[ten]] (10) years from the effectivity of this Act …", ["10"], "Ten-year window."),
 # support
 ("support", "Art. 194, FC", "Support comprises everything indispensable for sustenance, dwelling, clothing, medical attendance, education and transportation, in keeping with the [[financial capacity of the family]].", ["financial capacity"], "Measure of support."),
 ("support", "Art. 194, FC", "The education … shall include his schooling or training for some profession, trade or vocation, even [[beyond the age of majority]].", ["beyond majority"], "2010 Bar."),
 ("support", "Art. 196, FC", "… except only when the need for support of the brother or sister, being of age, is due to a cause imputable to the claimant's [[fault or negligence]].", ["fault or negligence"], "Uribe Quiz 2 #5."),
 ("support", "Art. 199, FC", "Whenever two or more persons are obliged to give support, the liability shall devolve upon the following persons in the order herein provided: (1) The spouse; (2) The [[descendants]] in the nearest degree; (3) The ascendants in the nearest degree; and (4) The brothers and sisters.", [], "S-D-A-B."),
 ("support", "Art. 200, FC", "When the obligation to give support falls upon two or more persons, the payment of the same shall be divided between them in proportion to the [[resources]] of each.", ["resources of each"], "Not equally."),
 ("support", "Art. 200, FC", "… unless the concurrent obligees should be the spouse and a child subject to parental authority, in which case the [[child]] shall be preferred.", [], "Child over spouse."),
 ("support", "Art. 203, FC", "The obligation to give support shall be demandable from the time the person who has a right to receive the same needs it for maintenance, but it shall not be paid except from the date of [[judicial or extra-judicial demand]].", ["judicial or extrajudicial demand"], "No arrears before demand."),
 ("support", "Art. 203, FC", "Payment shall be made within the first [[five]] days of each corresponding month …", ["5"], "Not fifteen (Quiz Set 3 TF3)."),
 ("support", "Art. 204, FC", "The person obliged to give support shall have the [[option]] to fulfill the obligation either by paying the allowance fixed, or by receiving and maintaining in the family dwelling the person who has a right to receive support.", [], "Option (Quiz Set 3 TF4)."),
 ("support", "Art. 204, FC", "The latter alternative cannot be availed of in case there is a [[moral or legal obstacle]] thereto.", ["moral or legal"], "E.g., abduction-marriage, a married daughter."),
 ("support", "Art. 206, FC", "… the latter shall have a right to claim the same from the former, unless it appears that he gave it without [[intention of being reimbursed]].", ["intention to be reimbursed"], "Quiz No. 4 TF10."),
 # parental authority
 ("pa", "Art. 211, FC", "The father and the mother shall jointly exercise parental authority over the persons of their common children. In case of disagreement, the [[father's]] decision shall prevail, unless there is a judicial order to the contrary.", ["father", "fathers"], "Also for the child's property (Art. 225)."),
 ("pa", "Art. 213, FC", "No child under [[seven]] years of age shall be separated from the mother unless the court finds compelling reasons to order otherwise.", ["7"], "Tender-age presumption."),
 ("pa", "Art. 214, FC", "In case of death, absence or unsuitability of the parents, [[substitute]] parental authority shall be exercised by the surviving grandparent.", [], "Not special (Uribe Quiz 2 #6)."),
 ("pa", "Art. 214, FC", "… substitute parental authority shall be exercised by the surviving [[grandparent]].", [], "Singular (Quiz Set 3 TF10)."),
 ("pa", "Art. 216(2), FC", "The oldest brother or sister, over [[twenty-one]] years of age, unless unfit or disqualified;", ["21", "twenty one"], "Still 21 in the text."),
 ("pa", "Art. 218, FC", "Authority and responsibility shall apply to all authorized activities whether inside or [[outside]] the premises of the school, entity or institution.", [], "2010 Bar field trip."),
 ("pa", "Art. 219, FC", "Those given the authority and responsibility under the preceding Article shall be principally and [[solidarily]] liable for damages caused by the acts or omissions of the unemancipated minor.", [], "Parents: subsidiarily."),
 ("pa", "Art. 224, FC", "The measures referred to in the preceding article may include the commitment of the child for not more than [[thirty]] days in entities or institutions engaged in child care …", ["30"], "Thirty days."),
 ("pa", "Art. 225, FC", "Where the market value of the property or the annual income of the child exceeds [[P50,000]], the parent concerned shall be required to furnish a bond …", ["50,000", "50000", "₱50,000", "fifty thousand"], "Bond of at least 10%."),
 ("pa", "Art. 230, FC", "The authority is [[automatically]] reinstated upon service of the penalty or upon pardon or amnesty of the offender.", [], "Civil interdiction."),
 ("pa", "Art. 232, FC", "If the person exercising parental authority has subjected the child or allowed him to be subjected to sexual abuse, such person shall be [[permanently]] deprived by the court of such authority.", [], "Permanent deprivation."),
 ("pa", "Art. 233, FC", "In no case shall the school administrator, teacher or individual engaged in child care exercising special parental authority inflict [[corporal punishment]] upon the child.", [], "No exception."),
 # emancipation / SJP
 ("eman", "Art. 234, FC (R.A. 6809)", "Emancipation takes place by the attainment of majority. Unless otherwise provided, majority commences at the age of [[eighteen]] years.", ["18"], "The only mode now."),
 ("eman", "Art. 236, FC (R.A. 6809)", "Contracting marriage shall require parental consent until the age of [[twenty-one]].", ["21", "twenty one"], "Advice from 21 to 25 (Art. 15)."),
 ("eman", "Art. 243, FC", "A preliminary conference shall be conducted by the judge personally [[without]] the parties being assisted by counsel.", [], "Counsel later, if useful."),
 ("eman", "Art. 247, FC", "The judgment of the court shall be [[immediately final and executory]].", [], "Certiorari, not appeal."),
 # names
 ("names", "Art. 364, NCC", "Legitimate and legitimated children shall principally use the surname of the [[father]].", [], "Principally."),
 ("names", "Art. 371, NCC", "In case of annulment of marriage, and the wife is the [[guilty]] party, she shall resume her maiden name and surname.", [], "The innocent wife may choose."),
 ("names", "Art. 372, NCC", "When legal separation has been granted, the wife shall [[continue]] using her name and surname employed before the legal separation.", ["continue using"], "Mandatory."),
 ("names", "Art. 374, NCC", "In case of identity of names and surnames, the [[younger]] person shall be obliged to use such additional name or surname as will avoid confusion.", [], "Younger."),
 ("names", "Art. 375, NCC", "In case of identity of names and surnames between ascendants and descendants, the word \"Junior\" can be used only by a [[son]].", [], "Grandsons: middle name or Roman numerals."),
 ("names", "Art. 376, NCC", "No person can change his name or surname without [[judicial authority]].", [], "Now subject to R.A. 9048 for first names."),
 ("names", "Art. 379, NCC", "The employment of pen names or stage names is permitted, provided it is done in [[good faith]] and there is no injury to third persons.", [], "Cannot be usurped."),
 # absence
 ("absence", "Art. 384, NCC", "Two years having elapsed without any news about the absentee or since the receipt of the last news, and [[five]] years in case the absentee has left a person in charge of the administration of his property, his absence may be declared.", ["5"], "2 or 5."),
 ("absence", "Art. 386, NCC", "The judicial declaration of absence shall not take effect until [[six months]] after its publication in a newspaper of general circulation.", ["6 months"], "Six months."),
 ("absence", "Art. 390, NCC", "After an absence of [[seven]] years, it being unknown whether or not the absentee still lives, he shall be presumed dead for all purposes, except for those of succession.", ["7"], "Seven."),
 ("absence", "Art. 390, NCC", "If he disappeared after the age of [[seventy-five]] years, an absence of five years shall be sufficient in order that his succession may be opened.", ["75", "seventy five"], "Samplex: 76 → 5 years."),
 ("absence", "Art. 391, NCC", "The following shall be presumed dead for all purposes, [[including]] the division of the estate among the heirs: …", [], "Including succession."),
 ("absence", "Art. 392, NCC", "… he shall recover his property in the condition in which it may be found, and the price of any property that may have been alienated or the property acquired therewith; but he cannot claim either [[fruits or rents]].", ["fruits nor rents"], "Good-faith possessors keep them."),
 ("absence", "Art. 41, FC", "… unless before the celebration of the subsequent marriage, the prior spouse had been absent for [[four]] consecutive years and the spouse present has a well-founded belief that the absent spouse was already dead.", ["4"], "Two years in danger of death."),
 # funerals
 ("funerals", "Art. 305, NCC", "In case of ascendants, the [[paternal]] shall have a better right.", [], "Descendants or siblings of the same degree: the oldest."),
 ("funerals", "Art. 307, NCC", "The funeral shall be in accordance with the [[expressed wishes]] of the deceased.", [], "Then religious beliefs."),
 ("funerals", "Art. 309, NCC", "Any person who shows disrespect to the dead, or wrongfully interferes with a funeral shall be liable to the family of the deceased for damages, [[material and moral]].", [], "Both."),
 # civil register
 ("civreg", "Art. 410, NCC", "The books making up the civil register and all documents relating thereto shall be considered public documents and shall be [[prima facie]] evidence of the facts therein contained.", [], "Not conclusive."),
 ("civreg", "Art. 412, NCC", "No entry in a civil register shall be changed or corrected, without a [[judicial order]].", [], "Except R.A. 9048/10172."),
 ("civreg", "Rule 108, Sec. 4", "The court shall also cause the order to be published once a week for [[three]] (3) consecutive weeks in a newspaper of general circulation in the province.", ["3"], "Three weeks."),
 ("civreg", "Rule 108, Sec. 5", "The civil registrar and any person having or claiming any interest under the entry whose cancellation or correction is sought may, within [[fifteen]] (15) days from notice of the petition, or from the last date of publication of such notice, file his opposition thereto.", ["15"], "Fifteen days."),
 ("civreg", "Sec. 2(3), R.A. 9048 (as amended)", "Provided, however, That no correction must involve the change of nationality, [[age]], or status of the petitioner.", [], "So: not the year of birth."),
]

# ---------------------------------------------------------------- one-word changes
A = [
 ("adopt", "Sec. 21, R.A. 11642", "If one spouse seeks to adopt own illegitimate child: Provided, That the other spouse has signified consent thereto;",
  "If one spouse seeks to adopt own illegitimate child: Provided, That the other spouse has joined the petition;", "Consent only."),
 ("adopt", "Sec. 23(c), R.A. 11642", "The legitimate and adopted children, ten (10) years of age or over, of the adopters, if any;",
  "The legitimate and adopted children, seven (7) years of age or over, of the adopters, if any;", "Ten."),
 ("adopt", "Sec. 47, R.A. 11642", "Adoption, being in the best interest of the child, shall not be subject to rescission by the adopter.",
  "Adoption, being in the best interest of the child, shall be subject to rescission by the adopter.", "No rescission by the adopter."),
 ("adopt", "Sec. 42, R.A. 11642", "Except in cases where the biological parent is the spouse of the adopter, all legal ties between the biological parents and the adoptee shall be severed …",
  "Except in cases where the biological parent is the sibling of the adopter, all legal ties between the biological parents and the adoptee shall be severed …", "Spouse of the adopter."),
 ("support", "Art. 196, FC", "Brothers and sisters not legitimately related, whether of the full or half-blood, are likewise bound to support each other to the full extent set forth in Article 194, except only when the need for support of the brother or sister, being of age, is due to a cause imputable to the claimant's fault or negligence.",
  "Brothers and sisters not legitimately related, whether of the full or half-blood, are likewise bound to support each other to the full extent set forth in Article 194, except only when the need for support of the brother or sister, being a minor, is due to a cause imputable to the claimant's fault or negligence.", "Being of age."),
 ("support", "Art. 198, FC", "During the proceedings for legal separation or for annulment of marriage, and for declaration of nullity of marriage, the spouses and their children shall be supported from the properties of the absolute community or the conjugal partnership.",
  "During the proceedings for legal separation or for annulment of marriage, and for declaration of nullity of marriage, the spouses and their children shall be supported from their separate properties.", "From the common property."),
 ("support", "Art. 198, FC", "However, in case of legal separation, the court may order that the guilty spouse shall give support to the innocent one, specifying the terms of such order.",
  "However, in case of legal separation, the court shall order that the guilty spouse shall give support to the innocent one, specifying the terms of such order.", "May: discretionary."),
 ("support", "Art. 200, FC", "However, in case of urgent need and by special circumstances, the judge may order only one of them to furnish the support provisionally, without prejudice to his right to claim from the other obligors the share due from them.",
  "However, in case of urgent need and by special circumstances, the judge may order only one of them to furnish the support permanently, without prejudice to his right to claim from the other obligors the share due from them.", "Provisionally."),
 ("support", "Art. 203, FC", "Payment shall be made within the first five days of each corresponding month or when the recipient dies, his heirs shall not be obliged to return what he has received in advance.",
  "Payment shall be made within the first fifteen days of each corresponding month or when the recipient dies, his heirs shall not be obliged to return what he has received in advance.", "Five days."),
 ("support", "Art. 207, FC", "When the person obliged to support another unjustly refuses or fails to give support when urgently needed by the latter, any third person may furnish support to the needy individual, with right of reimbursement from the person obliged to give support.",
  "When the person obliged to support another unjustly refuses or fails to give support when urgently needed by the latter, any relative may furnish support to the needy individual, with right of reimbursement from the person obliged to give support.", "Any third person."),
 ("pa", "Art. 212, FC", "The remarriage of the surviving parent shall not affect the parental authority over the children, unless the court appoints another person to be the guardian of the person or property of the children.",
  "The remarriage of the surviving parent shall terminate the parental authority over the children, unless the court appoints another person to be the guardian of the person or property of the children.", "Shall not affect."),
 ("pa", "Art. 213, FC", "The Court shall take into account all relevant considerations, especially the choice of the child over seven years of age, unless the parent chosen is unfit.",
  "The Court shall take into account all relevant considerations, especially the choice of the child over ten years of age, unless the parent chosen is unfit.", "Seven."),
 ("pa", "Art. 215, FC", "No descendant shall be compelled, in a criminal case, to testify against his parents and grandparents, except when such testimony is indispensable in a crime against the descendant or by one parent against the other.",
  "No descendant shall be compelled, in a civil case, to testify against his parents and grandparents, except when such testimony is indispensable in a crime against the descendant or by one parent against the other.", "Criminal case."),
 ("pa", "Art. 219, FC", "The parents, judicial guardians or the persons exercising substitute parental authority over said minor shall be subsidiarily liable.",
  "The parents, judicial guardians or the persons exercising substitute parental authority over said minor shall be solidarily liable.", "Subsidiarily."),
 ("pa", "Art. 226, FC", "The right of the parents over the fruits and income of the child's property shall be limited primarily to the child's support and secondarily to the collective daily needs of the family.",
  "The right of the parents over the fruits and income of the child's property shall be limited primarily to the child's support and secondarily to the collective daily needs of the parents.", "Secondarily the collective daily needs of the FAMILY, not the parents."),
 ("pa", "Art. 228, FC", "Parental authority terminates permanently: (1) Upon the death of the parents; (2) Upon the death of the child; or (3) Upon emancipation of the child.",
  "Parental authority terminates permanently: (1) Upon the death of the parents; (2) Upon the death of the child; or (3) Upon adoption of the child.", "Adoption is Art. 229 (revivable)."),
 ("eman", "Art. 236, FC", "Nothing in this Code shall be construed to derogate from the duty or responsibility of parents and guardians for children and wards below twenty-one years of age mentioned in the second and third paragraphs of Article 2180 of the Civil Code.",
  "Nothing in this Code shall be construed to derogate from the duty or responsibility of parents and guardians for children and wards below eighteen years of age mentioned in the second and third paragraphs of Article 2180 of the Civil Code.", "Below 21."),
 ("eman", "Art. 240, FC", "Claims for damages by either spouse, except costs of the proceedings, may be litigated only in a separate action.",
  "Claims for damages by either spouse, including costs of the proceedings, may be litigated only in a separate action.", "Except costs."),
 ("names", "Art. 370, NCC", "A married woman may use: (1) Her maiden first name and surname and add her husband's surname …",
  "A married woman shall use: (1) Her maiden first name and surname and add her husband's surname …", "May."),
 ("names", "Art. 371, NCC", "If she is the innocent spouse, she may resume her maiden name and surname.",
  "If she is the innocent spouse, she shall resume her maiden name and surname.", "May."),
 ("names", "Art. 373, NCC", "A widow may use the deceased husband's surname as though he were still living, in accordance with article 370.",
  "A widow shall use the deceased husband's surname as though he were still living, in accordance with article 370.", "May."),
 ("names", "Art. 365, NCC", "An adopted child shall bear the surname of the adopter.",
  "An adopted child may bear the surname of the adopter.", "Shall."),
 ("absence", "Art. 383, NCC", "In the appointment of a representative, the spouse present shall be preferred when there is no legal separation.",
  "In the appointment of a representative, the eldest child shall be preferred when there is no legal separation.", "The spouse present."),
 ("absence", "Art. 390, NCC", "After an absence of seven years, it being unknown whether or not the absentee still lives, he shall be presumed dead for all purposes, except for those of succession.",
  "After an absence of seven years, it being unknown whether or not the absentee still lives, he shall be presumed dead for all purposes, including those of succession.", "Except succession."),
 ("absence", "Art. 391(2), NCC", "A person in the armed forces who has taken part in war, and has been missing for four years;",
  "A person in the armed forces who has taken part in war, and has been missing for two years;", "Four."),
 ("funerals", "Art. 305, NCC", "In case of descendants of the same degree, or of brothers and sisters, the oldest shall be preferred.",
  "In case of descendants of the same degree, or of brothers and sisters, the youngest shall be preferred.", "Oldest."),
 ("funerals", "Art. 310, NCC", "The construction of a tombstone or mausoleum shall be deemed a part of the funeral expenses, and shall be chargeable to the conjugal partnership property, if the deceased is one of the spouses.",
  "The construction of a tombstone or mausoleum shall be deemed a part of the funeral expenses, and shall be chargeable to the exclusive property, if the deceased is one of the spouses.", "Conjugal partnership."),
 ("civreg", "Art. 411, NCC", "However, the civil registrar may exempt himself from such liability if he proves that he has taken every reasonable precaution to prevent the unlawful alteration.",
  "However, the civil registrar may exempt himself from such liability if he proves that he has taken some reasonable precaution to prevent the unlawful alteration.", "Every reasonable precaution."),
 ("civreg", "Rule 108, Sec. 3", "When cancellation or correction of an entry in the civil register is sought, the civil registrar and all persons who have or claim any interest which would be affected thereby shall be made parties to the proceeding.",
  "When cancellation or correction of an entry in the civil register is sought, the civil registrar and all persons who have or claim any interest which would be affected thereby may be made parties to the proceeding.", "Shall: indispensable parties."),
]

GRIDS = [
 {"id": "glate", "topic": "absence", "title": "Adoption to civil register: numbers", "src": "R.A. 11642; FC 194–253; NCC 364–413; Rule 108",
  "cols": [{"h": "Number", "t": "num"}],
  "rows": [
   {"h": "Minimum age of a Filipino adopter under R.A. 11642", "c": [["25", "twenty-five"]]},
   {"h": "Required age gap, adopter over adoptee (years)", "c": [["16", "sixteen"]]},
   {"h": "Alien adopter's residence under R.A. 11642 (years)", "c": [["5", "five"]]},
   {"h": "Age from which the adoptee's written consent is required", "c": [["10", "ten"]]},
   {"h": "Months after the parents' death before adoption proceedings may begin", "c": [["6", "six"]]},
   {"h": "Support: payment within the first how many days of each month", "c": [["5", "five"]]},
   {"h": "Child's age below which he is not separated from the mother (Art. 213)", "c": [["7", "seven"]]},
   {"h": "Maximum days of commitment as a disciplinary measure (Art. 224)", "c": [["30", "thirty"]]},
   {"h": "Child's property or income above which the parent posts a bond (₱)", "c": [["50000", "50,000", "₱50,000", "P50,000"]]},
   {"h": "Age of majority (R.A. 6809)", "c": [["18", "eighteen"]]},
   {"h": "Age until which parental consent is needed to marry", "c": [["21", "twenty-one"]]},
   {"h": "Years without news before absence may be declared (no administrator)", "c": [["2", "two"]]},
   {"h": "Same, if he left an administrator (years)", "c": [["5", "five"]]},
   {"h": "Months after publication before the declaration of absence takes effect", "c": [["6", "six"]]},
   {"h": "Absence for presumed death, all purposes except succession (years)", "c": [["7", "seven"]]},
   {"h": "Absence to open succession, ordinary case (years)", "c": [["10", "ten"]]},
   {"h": "Absence to open succession if he disappeared after 75 (years)", "c": [["5", "five"]]},
   {"h": "Art. 391 (danger of death), all purposes (years)", "c": [["4", "four"]]},
   {"h": "Rule 108: weeks of publication", "c": [["3", "three"]]},
   {"h": "Rule 108: days to file an opposition", "c": [["15", "fifteen"]]},
  ]},
 {"id": "gsupord", "topic": "support", "title": "Order of support (Art. 199) and funerals (Art. 305)", "src": "Arts. 199–200, FC; Art. 305, NCC",
  "cols": [{"h": "Rank", "t": "pick"}],
  "rows": [
   {"h": "The spouse", "c": ["1st"]},
   {"h": "Descendants in the nearest degree", "c": ["2nd"]},
   {"h": "Ascendants in the nearest degree", "c": ["3rd"]},
   {"h": "Brothers and sisters", "c": ["4th"]},
   {"h": "Uncles, nephews, cousins, in-laws", "c": ["Not obliged"]},
  ]},
 {"id": "gpakinds", "topic": "pa", "title": "Kinds of parental authority", "src": "Arts. 211–219, 233, FC",
  "cols": [{"h": "Who", "t": "pick"}, {"h": "Effect on the parents' authority", "t": "pick"}, {"h": "Liability for the minor's acts", "t": "pick"}],
  "rows": [
   {"h": "Parental", "c": ["Father and mother (mother alone for an illegitimate child)", "Is the parents' authority", "Liable unless diligence of a good father of a family (Art. 221; NCC 2180)"]},
   {"h": "Substitute", "c": ["Surviving grandparent; oldest sibling over 21; actual custodian over 21", "Displaces it", "Subsidiarily liable when the child is under special authority (Art. 219)"]},
   {"h": "Special", "c": ["School, administrators, teachers; child-care institutions", "Concurs with it", "Principally and solidarily liable (Art. 219)"]},
  ]},
 {"id": "gcorr", "topic": "civreg", "title": "Which remedy for the civil register?", "src": "R.A. 9048/10172; Rules 103 and 108",
  "cols": [{"h": "Remedy", "t": "pick"}],
  "rows": [
   {"h": "Misspelled first name", "c": ["R.A. 9048 (civil registrar)"]},
   {"h": "Change of first name habitually used", "c": ["R.A. 9048 (civil registrar)"]},
   {"h": "Wrong day and month of birth", "c": ["R.A. 10172 (civil registrar)"]},
   {"h": "Wrong year of birth", "c": ["Rule 108 (court)"]},
   {"h": "Wrong sex entry, patently clerical", "c": ["R.A. 10172 (civil registrar)"]},
   {"h": "Parents' marital status (legitimacy)", "c": ["Rule 108, adversarial"]},
   {"h": "Citizenship", "c": ["Rule 108, adversarial"]},
   {"h": "Change of surname, no error in the record", "c": ["Rule 103 (court)"]},
  ]},
 {"id": "gnames", "topic": "names", "title": "The wife's surname", "src": "Arts. 370–373, NCC",
  "cols": [{"h": "Rule", "t": "pick"}],
  "rows": [
   {"h": "Married", "c": ["May use husband's surname (3 forms)"]},
   {"h": "Annulment, guilty wife", "c": ["Shall resume maiden name"]},
   {"h": "Annulment, innocent wife", "c": ["May resume or keep husband's surname"]},
   {"h": "Legal separation", "c": ["Shall continue the name used before"]},
   {"h": "Widow", "c": ["May use husband's surname as if alive"]},
  ]},
]


def main():
    files = {n: json.load(open(os.path.join(OUT, n))) for n in ("cloze.json", "alter.json", "grids.json")}
    cl = [x for x in files["cloze.json"] if not x["id"].startswith("CZ-LT")]
    al = [x for x in files["alter.json"] if not x["id"].startswith("AL-LT")]
    gr = [x for x in files["grids.json"] if x["id"] not in {g["id"] for g in GRIDS}]
    for i, (t, art, text, acc, why) in enumerate(C, 1):
        assert text.count("[[") == 1 and text.count("]]") == 1, text
        cl.append({"id": f"CZ-LT{i}", "topic": t, "art": art, "text": text, "accept": acc, "why": why})
    for i, (t, art, o, a, why) in enumerate(A, 1):
        assert one_span(o, a), (art, o, a)
        al.append({"id": f"AL-LT{i}", "topic": t, "art": art, "original": o, "altered": a, "why": why})
    gr += GRIDS
    for name, data in (("cloze.json", cl), ("alter.json", al), ("grids.json", gr)):
        ids = [x["id"] for x in data]
        assert len(ids) == len(set(ids)), name
        json.dump(data, open(os.path.join(OUT, name), "w"), ensure_ascii=False, indent=1)
    print(f"cloze +{len(C)} = {len(cl)}; alter +{len(A)} = {len(al)}; grids +{len(GRIDS)} = {len(gr)}")


if __name__ == "__main__":
    main()
