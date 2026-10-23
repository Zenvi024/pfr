"""Family, family home, paternity and filiation drill cards (FC 149–182).

Run after drills_pr.py (which rebuilds the drill files from orig_drill/). Idempotent:
removes any earlier FM cards before appending.
"""
import json, os
from drills_pr import one_span

H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, "..", "data", "drill")

# ---------------------------------------------------------------- cloze
C = [
 ("family", "Art. 149, FC", "Consequently, family relations are governed by [[law]] and no custom, practice or agreement destructive of the family shall be recognized or given effect.", [], "Not by custom or agreement."),
 ("family", "Art. 150, FC", "Family relations include those: (1) Between husband and wife; (2) Between parents and children; (3) Among other [[ascendants and descendants]]; and (4) Among brothers and sisters, whether of the full or half-blood.", ["ascendants & descendants"], "The item some reviewers drop: there are four."),
 ("family", "Art. 150, FC", "Family relations include those … (4) Among brothers and sisters, whether of the [[full or half-blood]].", ["full or half blood"], "In-laws, nephews and cousins are not on the list (Gayon)."),
 ("family", "Art. 151, FC", "No suit between members of the same family shall prosper unless it should appear from the [[verified]] complaint or petition that earnest efforts toward a compromise have been made, but that the same have failed.", [], "Verified complaint or petition."),
 ("family", "Art. 151, FC", "This rule shall not apply to cases which may not be the subject of [[compromise]] under the Civil Code.", [], "NCC 2035: status, validity of marriage/LS, LS grounds, future support, jurisdiction, future legitime."),
 ("family", "Art. 2035(4), NCC", "No compromise upon the following questions shall be valid: … (4) [[Future]] support;", [], "Support in arrears may be compromised (Wainwright-Versoza)."),
 ("famhome", "Art. 152, FC", "The family home, constituted jointly by the husband and the wife or by an [[unmarried head of a family]], is the dwelling house where they and their family reside, and the land on which it is situated.", ["unmarried head of the family"], "Who may constitute."),
 ("famhome", "Art. 152, FC", "The family home … is the dwelling house where they and their family reside, [[and]] the land on which it is situated.", [], "'And', not 'or' (Uribe midterm #7)."),
 ("famhome", "Art. 153, FC", "The family home is deemed constituted on a house and lot from the time it is [[occupied]] as a family residence.", ["occupied as a family residence"], "No judicial or extrajudicial constitution needed under the FC."),
 ("famhome", "Art. 153, FC", "From the time of its constitution and so long as any of its beneficiaries [[actually resides]] therein, the family home continues to be such and is exempt from execution, forced sale or attachment …", ["actually reside", "resides"], "Actual residence of any beneficiary."),
 ("famhome", "Art. 154(2), FC", "Their parents, ascendants, descendants, brothers and sisters, whether the relationship be legitimate or illegitimate, who are living in the family home and who depend upon the [[head of the family]] for legal support.", [], "A grandchild supported by his own parents is not a beneficiary (Patricio v. Dario)."),
 ("famhome", "Art. 155(2), FC", "The family home shall be exempt from execution, forced sale or attachment except: … (2) For debts incurred [[prior to]] the constitution of the family home;", ["before"], "Siari Valley; Modequillo."),
 ("famhome", "Art. 155(3), FC", "… (3) For debts secured by mortgages on the premises [[before or after]] such constitution;", [], "Fortaleza v. Lapitan."),
 ("famhome", "Art. 155(4), FC", "… (4) For debts due to laborers, mechanics, architects, builders, materialmen and others who have rendered service or furnished material for the [[construction]] of the building.", [], "Construction only (Tolentino would add repairs and improvements)."),
 ("famhome", "Art. 156, FC", "The family home must be part of the properties of the absolute community or the conjugal partnership, or of the exclusive properties of either spouse [[with the latter's consent]].", ["with the consent of the latter"], "The clause dropped in Uribe midterm #10."),
 ("famhome", "Art. 157, FC", "The actual value of the family home shall not exceed, at the time of its constitution, the amount of [[three hundred thousand]] pesos in urban areas, and two hundred thousand pesos in rural areas …", ["300,000", "300000", "P300,000", "₱300,000"], "Urban ₱300,000; rural ₱200,000."),
 ("famhome", "Art. 158, FC", "The family home may be sold, alienated, donated, assigned or encumbered by the owner or owners thereof with the written consent of the person constituting the same, the latter's spouse, and a [[majority]] of the beneficiaries of legal age.", [], "Majority, of legal age, in writing."),
 ("famhome", "Art. 159, FC", "The family home shall continue despite the death of one or both spouses or of the unmarried head of the family for a period of [[ten]] years or for as long as there is a minor beneficiary …", ["10"], "And no partition unless the court finds compelling reasons."),
 ("famhome", "Art. 159, FC", "… and the heirs cannot partition the same unless the court finds [[compelling reasons]] therefor.", [], "Applies regardless of who owns the property."),
 ("famhome", "Art. 160, FC", "At the execution sale, no bid below the [[value allowed for a family home]] shall be considered.", ["value allowed"], "Proceeds: Art. 157 amount first, then judgment and costs, excess to debtor."),
 ("famhome", "Art. 161, FC", "For purposes of availing of the benefits of a family home as provided for in this Chapter, a person may constitute, or be the beneficiary of, only [[one]] family home.", ["1"], "Art. 161 is new."),
 ("patern", "Art. 163, FC", "The filiation of children may be by [[nature]] or by adoption. Natural filiation may be legitimate or illegitimate.", [], "Kinds of filiation."),
 ("patern", "Art. 164, FC", "Children conceived [[or]] born during the marriage of the parents are legitimate.", [], "'Or', not 'and'."),
 ("patern", "Art. 164, FC", "… provided, that both of them authorized or ratified such insemination in a [[written instrument]] executed and signed by them before the birth of the child.", ["written"], "Written, not public (2025 Quiz 2 trap)."),
 ("patern", "Art. 164, FC", "… in a written instrument executed and signed by them [[before the birth]] of the child.", ["before birth"], "Not after the birth."),
 ("patern", "Art. 165, FC", "Children conceived [[and]] born outside a valid marriage are illegitimate, unless otherwise provided in this Code.", [], "'And', not 'or' (Quiz Set 1 TF6)."),
 ("patern", "Art. 166(1), FC", "That it was physically impossible for the husband to have sexual intercourse with his wife within the first [[120]] days of the 300 days which immediately preceded the birth of the child …", ["one hundred twenty"], "300 − 120 = 180, the minimum viable gestation."),
 ("patern", "Art. 166(1)(c), FC", "… (c) serious illness of the husband, which [[absolutely]] prevented sexual intercourse;", [], "Andal v. Macaraig: tuberculosis is not enough."),
 ("patern", "Art. 166(2), FC", "That it is proved that for [[biological or other scientific]] reasons, the child could not have been that of the husband, except in the instance provided in the second paragraph of Article 164;", ["biological or scientific"], "Blood test exclusion (Jao); DNA."),
 ("patern", "Art. 167, FC", "The child shall be considered legitimate although the mother may have [[declared against its legitimacy]] or may have been sentenced as an adulteress.", ["declared against its legitimacy"], "The mother's word is irrelevant."),
 ("patern", "Art. 168(1), FC", "A child born before [[one hundred eighty]] days after the solemnization of the subsequent marriage is considered to have been conceived during the former marriage, provided it be born within three hundred days after the termination of the former marriage;", ["180"], "Two conditions: < 180 days of 2nd marriage AND within 300 days of termination."),
 ("patern", "Art. 168(2), FC", "A child born after one hundred eighty days following the celebration of the subsequent marriage is considered to have been conceived during [[such]] marriage, even though it be born within the three hundred days after the termination of the former marriage.", ["the subsequent", "the second"], "Second husband."),
 ("patern", "Art. 169, FC", "The legitimacy or illegitimacy of a child born after three hundred days following the termination of the marriage shall be proved by [[whoever alleges]] such legitimacy or illegitimacy.", [], "No presumption either way."),
 ("patern", "Art. 170, FC", "The action to impugn the legitimacy of the child shall be brought within [[one year]] from the knowledge of the birth or its recording in the civil register, if the husband or, in a proper case, any of his heirs, should reside in the city or municipality where the birth took place or was recorded.", ["1 year", "one (1) year"], "2 years elsewhere in PH; 3 years abroad."),
 ("patern", "Art. 170, FC", "… the period shall be two years if they should reside in the Philippines; and [[three]] years if abroad.", ["3"], "Abroad."),
 ("patern", "Art. 170, FC", "If the birth of the child has been concealed from or was unknown to the husband or his heirs, the period shall be counted from the discovery or knowledge of the birth of the child or of the fact of registration of said birth, whichever is [[earlier]].", [], "Earlier, not later."),
 ("patern", "Art. 171(2), FC", "The heirs of the husband may impugn the filiation of the child … (2) If he should die after the filing of the complaint without having [[desisted]] therefrom;", [], "The other cases: death before the period expires; child born after his death."),
 ("patern", "Art. 176, FC", "The legitime of [[each]] illegitimate child shall consist of one-half of the legitime of a legitimate child.", [], "Each, of a (one) legitimate child (Quiz 5 #5)."),
 ("patern", "Art. 176, FC", "However, illegitimate children [[may]] use the surname of their father if their filiation has been expressly recognized by the father …", [], "Permissive (Grande v. Antonio; Barcelote)."),
 ("filiat", "Art. 172, FC", "The filiation of legitimate children is established by any of the following: (1) The record of birth appearing in the civil register or a [[final judgment]]; …", [], "Primary evidence."),
 ("filiat", "Art. 172, FC", "(2) An admission of legitimate filiation in a public document or a private [[handwritten]] instrument and signed by the parent concerned.", [], "Handwritten AND signed."),
 ("filiat", "Art. 172, FC", "In the absence of the foregoing evidence, the legitimate filiation shall be proved by: (1) The [[open and continuous]] possession of the status of a legitimate child; …", ["open & continuous"], "Secondary evidence (Mendoza v. CA)."),
 ("filiat", "Art. 173, FC", "The action to claim legitimacy may be brought by the child during his or her lifetime and shall be transmitted to the heirs should the child die during minority or in a state of insanity. In these cases, the heirs shall have a period of [[five]] years within which to institute the action.", ["5"], "Imprescriptible for the child."),
 ("filiat", "Art. 175, FC", "The action must be brought within the same period specified in Article 173, except when the action is based on the second paragraph of Article 172, in which case the action may be brought during the [[lifetime]] of the alleged parent.", ["lifetime of the alleged parent"], "Sir: 'may' — DNA after death (Aquino; Yap)."),
 ("filiat", "Art. 177, FC", "Children conceived and born outside of wedlock of parents who, at the time of [[conception]] of the former, were not disqualified by any impediment to marry each other …", ["the conception"], "Conception, not birth (Uribe midterm #4)."),
 ("filiat", "Art. 177, FC", "… or were so disqualified only because either or both of them were below [[eighteen]] (18) years of age, may be legitimated.", ["18"], "R.A. 9858."),
 ("filiat", "Art. 178, FC", "Legitimation shall take place by a subsequent [[valid]] marriage between parents. The annulment of a voidable marriage shall not affect the legitimation.", [], "Void marriage: no legitimation."),
 ("filiat", "Art. 180, FC", "The effects of legitimation shall retroact to the time of the child's [[birth]].", [], "Not the marriage."),
 ("filiat", "Art. 182, FC", "Legitimation may be impugned only by those who are prejudiced in their rights, within [[five]] years from the time their cause of action accrues.", ["5"], "Not one year (Quiz No. 4 TF5)."),
]

# ---------------------------------------------------------------- spot the change
A = [
 ("family", "Art. 149, FC", "Consequently, family relations are governed by law and no custom, practice or agreement destructive of the family shall be recognized or given effect.",
  "Consequently, family relations are governed by custom and no custom, practice or agreement destructive of the family shall be recognized or given effect.", "Governed by law."),
 ("family", "Art. 151, FC", "No suit between members of the same family shall prosper unless it should appear from the verified complaint or petition that earnest efforts toward a compromise have been made, but that the same have failed.",
  "No suit between members of the same family shall prosper unless it should appear from the complaint or petition that earnest efforts toward a compromise have been made, but that the same have failed.", "Verified complaint or petition."),
 ("family", "Art. 151, FC", "If it is shown that no such efforts were in fact made, the same case must be dismissed.",
  "If it is shown that no such efforts were in fact made, the same case may be dismissed.", "Must be dismissed (if timely raised)."),
 ("famhome", "Art. 152, FC", "The family home, constituted jointly by the husband and the wife or by an unmarried head of a family, is the dwelling house where they and their family reside, and the land on which it is situated.",
  "The family home, constituted jointly by the husband and the wife or by an unmarried head of a family, is the dwelling house where they and their family reside, or the land on which it is situated.", "House AND land (Uribe midterm #7)."),
 ("famhome", "Art. 153, FC", "The family home is deemed constituted on a house and lot from the time it is occupied as a family residence.",
  "The family home is deemed constituted on a house and lot from the time it is registered as a family residence.", "Occupied, not registered."),
 ("famhome", "Art. 154(2), FC", "Their parents, ascendants, descendants, brothers and sisters, whether the relationship be legitimate or illegitimate, who are living in the family home and who depend upon the head of the family for legal support.",
  "Their parents, ascendants, descendants, brothers and sisters, whether the relationship be legitimate or illegitimate, who are living in the family home or who depend upon the head of the family for legal support.", "Living there AND dependent."),
 ("famhome", "Art. 155(3), FC", "For debts secured by mortgages on the premises before or after such constitution;",
  "For debts secured by mortgages on the premises before such constitution;", "Before OR AFTER."),
 ("famhome", "Art. 157, FC", "The actual value of the family home shall not exceed, at the time of its constitution, the amount of three hundred thousand pesos in urban areas, and two hundred thousand pesos in rural areas …",
  "The actual value of the family home shall not exceed, at the time of the levy, the amount of three hundred thousand pesos in urban areas, and two hundred thousand pesos in rural areas …", "At the time of its constitution."),
 ("famhome", "Art. 158, FC", "… with the written consent of the person constituting the same, the latter's spouse, and a majority of the beneficiaries of legal age.",
  "… with the written consent of the person constituting the same, the latter's spouse, and all of the beneficiaries of legal age.", "A majority."),
 ("famhome", "Art. 159, FC", "This rule shall apply regardless of whoever owns the property or constituted the family home.",
  "This rule shall apply only if the deceased owned the property or constituted the family home.", "Regardless of ownership."),
 ("famhome", "Art. 160, FC", "At the execution sale, no bid below the value allowed for a family home shall be considered.",
  "At the execution sale, no bid below the judgment debt shall be considered.", "Below the value allowed for a family home (Art. 157)."),
 ("famhome", "Art. 160, FC", "The excess, if any, shall be delivered to the judgment debtor.",
  "The excess, if any, shall be delivered to the judgment creditor.", "To the debtor; the Art. 157 amount is applied first, then the judgment and costs."),
 ("patern", "Art. 164, FC", "Children conceived or born during the marriage of the parents are legitimate.",
  "Children conceived and born during the marriage of the parents are legitimate.", "Conceived OR born."),
 ("patern", "Art. 164, FC", "Children conceived as a result of artificial insemination of the wife with the sperm of the husband or that of a donor or both are likewise legitimate children of the husband and his wife …",
  "Children conceived as a result of artificial insemination of the wife with the sperm of the husband are likewise legitimate children of the husband and his wife …", "Husband's OR a donor's sperm, or both."),
 ("patern", "Art. 164, FC", "… provided, that both of them authorized or ratified such insemination in a written instrument executed and signed by them before the birth of the child.",
  "… provided, that both of them authorized or ratified such insemination in a public instrument executed and signed by them before the birth of the child.", "Written, not public (2025 Quiz 2)."),
 ("patern", "Art. 165, FC", "Children conceived and born outside a valid marriage are illegitimate, unless otherwise provided in this Code.",
  "Children conceived or born outside a valid marriage are illegitimate, unless otherwise provided in this Code.", "Conceived AND born (Quiz Set 1 TF6)."),
 ("patern", "Art. 166(1), FC", "… within the first 120 days of the 300 days which immediately preceded the birth of the child …",
  "… within the first 180 days of the 300 days which immediately preceded the birth of the child …", "120, not 180 (2025 Quiz 5 #14)."),
 ("patern", "Art. 166(1)(c), FC", "serious illness of the husband, which absolutely prevented sexual intercourse;",
  "serious illness of the husband, which prevented sexual intercourse;", "ABSOLUTELY prevented."),
 ("patern", "Art. 167, FC", "The child shall be considered legitimate although the mother may have declared against its legitimacy or may have been sentenced as an adulteress.",
  "The child shall be considered illegitimate if the mother may have declared against its legitimacy or may have been sentenced as an adulteress.", "Legitimate, although …"),
 ("patern", "Art. 168(1), FC", "A child born before one hundred eighty days after the solemnization of the subsequent marriage is considered to have been conceived during the former marriage, provided it be born within three hundred days after the termination of the former marriage;",
  "A child born before one hundred eighty days after the solemnization of the subsequent marriage is considered to have been conceived during the subsequent marriage, provided it be born within three hundred days after the termination of the former marriage;", "Conceived during the FORMER marriage."),
 ("patern", "Art. 170, FC", "… if the husband or, in a proper case, any of his heirs, should reside in the city or municipality where the birth took place or was recorded.",
  "… if the husband or, in a proper case, any of his heirs, should reside in the country where the birth took place or was recorded.", "City or municipality (2025 Quiz 5 #16)."),
 ("patern", "Art. 170, FC", "… the period shall be counted from the discovery or knowledge of the birth of the child or of the fact of registration of said birth, whichever is earlier.",
  "… the period shall be counted from the discovery or knowledge of the birth of the child or of the fact of registration of said birth, whichever is later.", "Whichever is EARLIER."),
 ("patern", "Art. 176, FC", "The legitime of each illegitimate child shall consist of one-half of the legitime of a legitimate child.",
  "The legitime of each illegitimate child shall consist of one-third of the legitime of a legitimate child.", "One-half of the legitime of A (one) legitimate child; and it is the legitime of EACH illegitimate child (Quiz 5 #5)."),
 ("patern", "Art. 176, FC", "However, illegitimate children may use the surname of their father if their filiation has been expressly recognized by the father …",
  "However, illegitimate children shall use the surname of their father if their filiation has been expressly recognized by the father …", "MAY, not shall."),
 ("filiat", "Art. 172, FC", "(2) An admission of legitimate filiation in a public document or a private handwritten instrument and signed by the parent concerned.",
  "(2) An admission of legitimate filiation in a public document or a private instrument and signed by the parent concerned.", "Private HANDWRITTEN instrument."),
 ("filiat", "Art. 173, FC", "The action to claim legitimacy may be brought by the child during his or her lifetime …",
  "The action to claim legitimacy may be brought by the child within five years from majority …", "During his or her lifetime; the 5 years are for the heirs."),
 ("filiat", "Art. 175, FC", "… except when the action is based on the second paragraph of Article 172, in which case the action may be brought during the lifetime of the alleged parent.",
  "… except when the action is based on the first paragraph of Article 172, in which case the action may be brought during the lifetime of the alleged parent.", "Second paragraph (secondary evidence)."),
 ("filiat", "Art. 177, FC", "Children conceived and born outside of wedlock of parents who, at the time of conception of the former, were not disqualified by any impediment to marry each other …",
  "Children conceived and born outside of wedlock of parents who, at the time of birth of the former, were not disqualified by any impediment to marry each other …", "At CONCEPTION (Uribe midterm #4)."),
 ("filiat", "Art. 178, FC", "Legitimation shall take place by a subsequent valid marriage between parents.",
  "Legitimation shall take place by a subsequent marriage between parents.", "VALID marriage."),
 ("filiat", "Art. 180, FC", "The effects of legitimation shall retroact to the time of the child's birth.",
  "The effects of legitimation shall retroact to the time of the parents' marriage.", "To the child's BIRTH."),
 ("filiat", "Art. 182, FC", "Legitimation may be impugned only by those who are prejudiced in their rights, within five years from the time their cause of action accrues.",
  "Legitimation may be impugned only by those who are prejudiced in their rights, within one year from the time their cause of action accrues.", "Five years (Quiz No. 4 TF5)."),
]

# ---------------------------------------------------------------- grids
GRIDS = [
 {"id": "gfam", "topic": "patern", "title": "Family, family home, filiation: numbers", "src": "Arts. 150, 157, 159, 166, 168, 170, 173, 177, 182, FC",
  "cols": [{"h": "Number", "t": "num"}],
  "rows": [
   {"h": "Family relations enumerated in Art. 150", "c": [["4", "four"]]},
   {"h": "Maximum value of an urban family home at constitution (₱)", "c": [["300000", "300,000", "₱300,000", "P300,000"]]},
   {"h": "Maximum value of a rural family home at constitution (₱)", "c": [["200000", "200,000", "₱200,000", "P200,000"]]},
   {"h": "Years the family home continues after the constitutors' death (absent a minor beneficiary)", "c": [["10", "ten"]]},
   {"h": "Art. 166(1): the first how many days of the 300 before birth", "c": [["120"]]},
   {"h": "Art. 168: days after the subsequent marriage that divide 1st from 2nd husband", "c": [["180"]]},
   {"h": "Days after termination beyond which Art. 169 applies", "c": [["300"]]},
   {"h": "Period to impugn: husband lives in the city/municipality of birth or recording (years)", "c": [["1", "one"]]},
   {"h": "Period to impugn: elsewhere in the Philippines (years)", "c": [["2", "two"]]},
   {"h": "Period to impugn: abroad (years)", "c": [["3", "three"]]},
   {"h": "Heirs' period to claim legitimacy when the child died a minor or insane (years)", "c": [["5", "five"]]},
   {"h": "Age below which parents' disqualification does not bar legitimation (R.A. 9858)", "c": [["18", "eighteen"]]},
   {"h": "Period to impugn legitimation (years)", "c": [["5", "five"]]},
  ]},
 {"id": "gchild", "topic": "patern", "title": "Legitimate, illegitimate, legitimated", "src": "Arts. 164–182, FC; R.A. 9255, 9858",
  "cols": [{"h": "Legitimate", "t": "pick"}, {"h": "Illegitimate", "t": "pick"}, {"h": "Legitimated", "t": "pick"}],
  "rows": [
   {"h": "Basis of status", "c": ["Conceived or born during a valid marriage (Art. 164)", "Conceived and born outside a valid marriage (Art. 165)", "No impediment at conception + subsequent valid marriage (Arts. 177–178)"]},
   {"h": "Surname", "c": ["Father's and mother's", "Mother's; may use father's if expressly recognized", "Same as legitimate"]},
   {"h": "Parental authority", "c": ["Joint, both parents", "Mother alone", "Joint, both parents (same as legitimate)"]},
   {"h": "Legitime", "c": ["Full legitime of a legitimate child", "One-half of a legitimate child's legitime", "Full (same rights as legitimate, Art. 179)"]},
   {"h": "Who may attack the status, and when", "c": ["Husband (heirs in Art. 171 cases); 1/2/3 years", "Filiation must be proved by the child (Art. 175)", "Those prejudiced in their rights; 5 years"]},
  ]},
 {"id": "gimp", "topic": "patern", "title": "Who may impugn legitimacy?", "src": "Arts. 167, 170–171, FC; Liyao; Yap v. Yap",
  "cols": [{"h": "May impugn?", "t": "pick"}],
  "rows": [
   {"h": "The husband, within the Art. 170 period", "c": ["Yes"]},
   {"h": "His heirs, the husband having died before his period expired", "c": ["Yes, Art. 171(1)"]},
   {"h": "His heirs, the husband having let his period lapse while alive", "c": ["No, the status is fixed"]},
   {"h": "The mother", "c": ["No, Art. 167"]},
   {"h": "The child", "c": ["Traditionally no (Liyao); Yap v. Yap now allows proof of filiation with the biological father"]},
   {"h": "The alleged biological father", "c": ["No"]},
  ]},
 {"id": "gproof", "topic": "filiat", "title": "Proof of filiation", "src": "Arts. 172, 175, FC; cases",
  "cols": [{"h": "Kind", "t": "pick"}, {"h": "After the alleged parent's death (illegitimate child)?", "t": "pick"}],
  "rows": [
   {"h": "Record of birth signed by the father", "c": ["Primary", "Yes"]},
   {"h": "Final judgment", "c": ["Primary", "Yes"]},
   {"h": "Admission in a public document, signed", "c": ["Primary", "Yes"]},
   {"h": "Private handwritten instrument, signed", "c": ["Primary", "Yes"]},
   {"h": "Open and continuous possession of status", "c": ["Secondary", "No (Art. 175), but Sir disagrees"]},
   {"h": "DNA test and other means under the Rules of Court", "c": ["Secondary", "No (Art. 175), but see Aquino; Yap"]},
   {"h": "Baptismal certificate", "c": ["Not proof of filiation", "Not proof of filiation"]},
  ]},
]


def main():
    files = {n: json.load(open(os.path.join(OUT, n))) for n in ("cloze.json", "alter.json", "grids.json")}
    cl = [x for x in files["cloze.json"] if not x["id"].startswith("CZ-FM")]
    al = [x for x in files["alter.json"] if not x["id"].startswith("AL-FM")]
    gr = [x for x in files["grids.json"] if x["id"] not in {g["id"] for g in GRIDS}]
    for i, (t, art, text, acc, why) in enumerate(C, 1):
        assert text.count("[[") == 1 and text.count("]]") == 1, text
        cl.append({"id": f"CZ-FM{i}", "topic": t, "art": art, "text": text, "accept": acc, "why": why})
    for i, (t, art, o, a, why) in enumerate(A, 1):
        assert one_span(o, a), (art, o, a)
        al.append({"id": f"AL-FM{i}", "topic": t, "art": art, "original": o, "altered": a, "why": why})
    gr += GRIDS
    for name, data in (("cloze.json", cl), ("alter.json", al), ("grids.json", gr)):
        json.dump(data, open(os.path.join(OUT, name), "w"), ensure_ascii=False, indent=1)
    print(f"cloze +{len(C)} = {len(cl)}; alter +{len(A)} = {len(al)}; grids +{len(GRIDS)} = {len(gr)}")


if __name__ == "__main__":
    main()
