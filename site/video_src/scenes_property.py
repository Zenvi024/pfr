# Video explainer 2: Property Relations I–V (FC 74–148)
SCENES = []
def S(kicker, title, body, steps):
    SCENES.append({"kicker": kicker, "title": title, "body": body, "steps": steps})

# ---------------------------------------------------------------- 0 title
S("", "", """
<div class="titlecard">
  <div class="tk">Persons and Family Relations · Atty. Uribe</div>
  <h1>Property Relations<br>Between Husband and Wife</h1>
  <div class="tsub">Family Code, Articles 74 to 148</div>
  <div class="road r5">
    <div data-s="1"><b>I</b>Settlements &amp; Donations<small>Arts. 74–87</small></div>
    <div data-s="1"><b>II</b>Absolute Community<small>Arts. 88–104</small></div>
    <div data-s="1"><b>III</b>Conjugal Partnership<small>Arts. 105–133</small></div>
    <div data-s="1"><b>IV</b>Separation of Property<small>Arts. 134–146</small></div>
    <div data-s="1"><b>V</b>Unions Without Marriage<small>Arts. 147–148</small></div>
  </div>
</div>""", [
 "This is your explainer on property relations between husband and wife: Articles seventy-four to one forty-eight of the Family Code, for Attorney Uribe's class.",
 "We'll go through Sir's five parts. One, marriage settlements and donations by reason of marriage. Two, the absolute community of property. Three, the conjugal partnership of gains. Four, separation of property. And five, property regimes of unions without marriage. I'll flag his quiz traps and his situationers along the way.",
])

# ---------------------------------------------------------------- 1 Art 74-75
S("Part I · Marriage Settlements", "Arts. 74–75: what governs, and the default", """
<div class="codal">The property relationship between husband and wife shall be governed in the following order: (1) By <b>marriage settlements executed before the marriage</b>; (2) By the provisions of this Code; and (3) By the local custom.<span class="src">Art. 74, FC</span></div>
<div class="steps3" data-s="0">
  <div><b>1</b>Marriage settlement</div><div><b>2</b>Family Code</div><div><b>3</b>Local custom</div>
</div>
<div class="row">
 <div class="card" data-s="1"><h4>No settlement, or a void regime (Art. 75)</h4><p>Married <b>on or after Aug. 3, 1988</b> → <b>ACP</b></p><p>Married <b>before</b> → <b>CPG</b> (Civil Code; FC rules apply too, without impairing vested rights)</p></div>
 <div class="trap" data-s="2"><span class="chip red">QUIZ 4 TRAPS</span><ul><li>"governed <b>primarily by the Family Code</b>" → False: the settlement comes first</li><li>"No settlement → ACP", with no date given → False: it could be a pre-1988 marriage (CPG)</li><li>"If False, discuss why it is false, not why it is true"</li></ul></div>
</div>""", [
 "Article seventy-four sets the order of governing rules: first, the marriage settlement executed before the marriage; second, the Family Code; and third, local custom.",
 "If there's no settlement, or the regime agreed on is void, Article seventy-five gives the default: absolute community of property for marriages on or after August third, nineteen eighty-eight, and conjugal partnership of gains for marriages before that date.",
 "Sir loves this in quizzes. A statement that property relations are governed primarily by the Family Code is false, because the settlement comes first. And a statement that a couple with no settlement is under absolute community is false if the date of the marriage isn't given, because a pre-nineteen eighty-eight marriage defaults to the conjugal partnership. Remember his rule: if your answer is false, explain why it's false, not why it would be true.",
])

# ---------------------------------------------------------------- 2 Arts 76-80
S("Part I · Marriage Settlements", "Arts. 76–80: form, minors, and governing law", """
<div class="codal">The marriage settlements and any modification thereof shall be <b>in writing, signed by the parties and executed before the celebration of the marriage</b>. They shall not prejudice third persons unless they are <b>registered</b> in the local civil registry where the marriage contract is recorded <b>as well as</b> in the proper registries of properties.<span class="src">Art. 77, FC</span></div>
<div class="row3">
 <div class="trap" data-s="1"><span class="chip red">TRAPS</span><ul><li>"in a <b>public instrument</b>" → False</li><li>"executed <b>during</b>" / "<b>may</b> be made before" → False</li><li>Modification after the wedding only via Arts. 66, 67, 128, 135, 136 (all need the court)</li></ul></div>
 <div class="uribe" data-s="2"><span class="chip blue">URIBE</span> Married <b>December 1989</b>; B was 19, and her parents weren't parties. Valid? <b>Depends on the date</b>: RA 6809 took effect <b>Dec. 18, 1989</b>. Before that, B was a minor, so Art. 78 required her parents as parties.</div>
 <div class="card" data-s="3"><h4>Art. 80</h4><p>Absent a contrary stipulation, <b>Philippine law</b> governs, regardless of where they married or live (not if both are aliens).</p></div>
</div>""", [
 "Form. Under Article seventy-seven, a marriage settlement must be in writing, signed by the parties, and executed before the celebration of the marriage. It binds third persons only if registered in the local civil registry and in the proper registries of property.",
 "These are graded false every time: in a public instrument; executed during the celebration; or may be made before the celebration. Executing it before the wedding is mandatory. After the wedding, a settlement can be modified only through the court routes in Articles sixty-six, sixty-seven, one twenty-eight, one thirty-five and one thirty-six.",
 "Sir's minor situationer: a couple married in December nineteen eighty-nine, and the bride was nineteen, with her parents not parties to the settlement. Valid? It depends on the exact date. Republic Act sixty-eight oh nine lowered the age of majority effective December eighteenth, nineteen eighty-nine. Before that, she was a minor, and Article seventy-eight required the persons who must consent to the marriage to be parties to the settlement.",
 "And under Article eighty, absent a contrary stipulation, Philippine law governs the property relations of Filipino spouses, wherever they married or live. A quiz statement that drops the words absent a contrary stipulation is false.",
])

# ---------------------------------------------------------------- 3 Arts 81-85
S("Part I · Donations by Reason of Marriage", "Arts. 81–85: donations propter nuptias", """
<div class="split">
 <div>
  <div class="codal small">Donations by reason of marriage are those which are made <b>before</b> its celebration, <b>in consideration</b> of the same, and <b>in favor of</b> one or both of the future spouses.<span class="src">Art. 82, FC</span></div>
  <div class="card" data-s="1"><h4>Form: same as ordinary donations</h4><p>Movable over <b>₱5,000</b> → writing. Immovable → <b>public document</b>. Sir: "Walang binago ang FC."</p></div>
  <div class="trap" data-s="2"><span class="chip red">ART. 81</span> No marriage → donations in the settlement are <b>void</b>, not "revocable" and not "revoked by operation of law".</div>
 </div>
 <div>
  <div class="card" data-s="3"><h4>Art. 84: the one-fifth cap</h4><p>Regime <b>other than ACP</b> → future spouses can't donate to each other <b>in the settlement</b> more than <b>⅕ of present property</b>. Only the <b>excess</b> is void. Future property → rules on wills.</p></div>
  <div class="uribe" data-s="4"><span class="chip blue">URIBE</span> Under ACP there's no ⅕ cap. "Does it follow that there is no limit? <b>NO</b>": legitimes and other limits on donations still apply.</div>
  <div class="card" data-s="5"><h4>Art. 85: encumbered property</h4><p>Sold at foreclosure for less → the <b>donee</b> isn't liable for the deficiency; sold for more → the donee gets the excess.</p></div>
 </div>
</div>""", [
 "Donations by reason of marriage, under Article eighty-two, are made before the celebration, in consideration of the marriage, and in favor of one or both future spouses. In Quiz four, a statement that said made by one or both of the future spouses was false. Anyone may be the donor; the future spouses are the donees.",
 "As to form, nothing changed. Sir says the Family Code didn't alter the formalities, so the Civil Code rules apply: a movable worth over five thousand pesos needs a writing, and an immovable needs a public document.",
 "If the marriage doesn't take place, Article eighty-one makes the stipulations in the settlement, including donations in it, void. Not revocable, and not revoked by operation of law. Sir: there's nothing to revoke if it's void.",
 "Article eighty-four is his favorite one-fifth item. If the regime is other than absolute community, the future spouses can't donate to each other in their settlement more than one fifth of their present property, and only the excess is void. Donations of future property follow the rules on wills.",
 "But Sir warns: just because there's no one-fifth cap under absolute community doesn't mean there's no limit. The rules on legitimes and donations still apply.",
 "And Article eighty-five: if donated property is encumbered and is foreclosed for less than the debt, the donee is not liable for the deficiency. If it sells for more, the donee gets the excess. The trap swaps donee for donor.",
])

# ---------------------------------------------------------------- 4 Arts 86-87
S("Part I · Donations by Reason of Marriage", "Arts. 86–87: revocation, and gifts between spouses", """
<div class="split">
 <div>
  <h3 class="mini">Art. 86: the donor may revoke…</h3>
  <ol class="ol6" data-s="0">
   <li>Marriage not celebrated or declared void <small>(except settlement donations → Art. 81)</small></li>
   <li>Married without the parents' <b>consent</b> <small>(not "advice")</small></li>
   <li>Marriage annulled, and the <b>donee</b> acted in bad faith</li>
   <li>Legal separation, the <b>donee</b> being the guilty spouse</li>
   <li><b>Resolutory</b> condition fulfilled <small>(not "suspensive")</small></li>
   <li>Ingratitude of the donee</li>
  </ol>
 </div>
 <div>
  <div class="codal small" data-s="1">Every donation or grant of gratuitous advantage, direct or indirect, between the spouses during the marriage shall be <b>void</b>, except <b>moderate gifts</b> … on the occasion of any <b>family rejoicing</b>. The prohibition shall also apply to persons living together as husband and wife without a valid marriage.<span class="src">Art. 87, FC</span></div>
  <div class="card case" data-s="2"><h4>Matabuena v. Cervantes (1971)</h4><p>A donation between common-law partners is void too: policy and morality demand the same prohibition.</p></div>
  <div class="uribe" data-s="2"><span class="chip blue">URIBE</span> A ₱30-million Rolls-Royce from the husband to the wife: "moderate" is relative to the family's means.</div>
 </div>
</div>""", [
 "Article eighty-six lists six grounds for the donor to revoke: the marriage isn't celebrated or is declared void, except donations in the settlement, which Article eighty-one already voids; the marriage took place without the parents' consent; the marriage is annulled and the donee acted in bad faith; legal separation, with the donee as the guilty spouse; a resolutory condition is fulfilled; and the donee's ingratitude. In Quiz four, each wrong option changed one word: advice for consent, donor for donee, or suspensive for resolutory.",
 "Article eighty-seven: donations between spouses during the marriage are void, except moderate gifts on the occasion of family rejoicing. The prohibition also covers couples living together without a valid marriage.",
 "That last sentence codifies Matabuena versus Cervantes, where a donation between common-law partners was struck down. And in Sir's Rolls-Royce situationer, a thirty-million-peso car given to the wife: is that moderate? It depends on the family's means. Moderation is relative.",
])

# ---------------------------------------------------------------- 5 ACP 88-93
S("Part II · Absolute Community", "Arts. 88–93: what's in, what's out", """
<div class="split">
 <div>
  <div class="codal small"><b>Unless otherwise provided in this Chapter or in the marriage settlements</b>, the community property shall consist of <b>all the property owned by the spouses at the time of the celebration of the marriage or acquired thereafter</b>.<span class="src">Art. 91, FC</span></div>
  <div class="card" data-s="1"><h4>Excluded (Art. 92)</h4><ol><li>Acquired <b>during</b> the marriage by <b>gratuitous title</b>, with fruits and income, unless the giver says otherwise</li><li>For personal and exclusive use, <b>except jewelry</b></li><li>Owned before the marriage by a spouse with <b>legitimate descendants by a former marriage</b>, with fruits and income</li></ol></div>
 </div>
 <div>
  <div class="card" data-s="0"><h4>Basics</h4><p>Begins at the <b>precise moment</b> of the celebration (Art. 88). No waiver during the marriage, except upon <b>judicial separation</b>; then by <b>public instrument</b> (Art. 89). Suppletory rules: <b>co-ownership</b> (Art. 90).</p></div>
  <div class="trap" data-s="2"><span class="chip red">MOST REPEATED TRAP</span> Art. 91 quoted <b>without</b> "unless otherwise provided…" → <b>False</b>. Jewelry is never excluded.</div>
  <div class="trap" data-s="3"><span class="chip red">ART. 93</span> "Presumed community if (a) gratuitous (b) onerous (c) before the marriage (d) <b>registered</b> during the marriage (e) none" → <b>E</b>. The trigger is <u>acquired</u> during the marriage.</div>
 </div>
</div>""", [
 "Part two, the absolute community. It begins at the precise moment the marriage is celebrated; no waiver is allowed during the marriage except on judicial separation of property, and then only by a public instrument; and the suppletory rules are those on co-ownership.",
 "Under Article ninety-one, the community consists of all property owned at the celebration or acquired after, unless otherwise provided. Article ninety-two lists three exclusions: property acquired during the marriage by gratuitous title, with its fruits, unless the giver says otherwise; property for personal and exclusive use, except jewelry; and property owned before the marriage by a spouse who has legitimate descendants by a former marriage, with its fruits.",
 "His most repeated trap quotes Article ninety-one without the opening qualifier, unless otherwise provided in this Chapter or in the marriage settlements. Without it, the statement is false. And jewelry is never excluded, even if only one spouse uses it.",
 "The presumption in Article ninety-three applies to property acquired during the marriage. In Quiz four, the options were gratuitous, onerous, before the marriage, and registered during the marriage, and the answer was none of the above. Registration is not acquisition.",
])

# ---------------------------------------------------------------- 6 ACP 94-95
S("Part II · Absolute Community", "Arts. 94–95: charges on the community", """
<div class="split">
 <div>
  <div class="card" data-s="0"><h4>Art. 94: highlights</h4><ul>
   <li>(1) Support of the spouses, common children, and <b>legitimate</b> children of either</li>
   <li>(2)–(3) Debts for the benefit of the community; without consent, to the extent the <b>family benefited</b></li>
   <li>(5) Preservation of separate property <b>used by the family</b></li>
   <li>(7) Antenuptial debts that <b>redounded</b> to the family's benefit</li>
   <li>(9) Debts not benefiting the family, support of <b>illegitimate</b> children, liability for crimes: <b>advanced</b>, then deducted at liquidation</li></ul>
   <p>Insufficient? Spouses <b>solidarily</b> liable, <b>except (9)</b>.</p></div>
 </div>
 <div>
  <div class="trap" data-s="1"><span class="chip red">MIDTERM TRAP</span> "liable for all expenses for mere preservation … upon the separate property of either spouse" → <b>False</b>: it omits "<b>used by the family</b>". Sir: it's not "benefit".</div>
  <div class="uribe" data-s="2"><span class="chip blue">URIBE</span> "Is any expense chargeable to ACP but not CPG?" <b>Support of illegitimate children</b> (Art. 94(9)). In an ACP, a spouse usually has no separate property, so the community advances it.</div>
  <div class="card" data-s="3"><h4>Art. 95: gambling</h4><p>Losses → the losing spouse alone. Winnings → the community.</p></div>
 </div>
</div>""", [
 "Article ninety-four lists the community's charges. The highlights: support of the spouses, their common children, and the legitimate children of either spouse; debts for the community's benefit, and debts contracted without consent to the extent the family benefited; expenses to preserve separate property that is used by the family; antenuptial debts that redounded to the family's benefit; and, in paragraph nine, debts that didn't benefit the family, support of illegitimate children, and liabilities from crimes, which the community advances and then deducts from that spouse's share at liquidation. If the community is insufficient, the spouses are solidarily liable, except for paragraph nine.",
 "A midterm item said the community is liable for all expenses for mere preservation of the separate property of either spouse. False: it omits used by the family. And Sir corrected a student who said benefit of the family; the codal word here is used.",
 "Sir also asked: is there an expense chargeable to the absolute community but not to the conjugal partnership? Support of a spouse's illegitimate children. Under absolute community, almost everything becomes community property, so the spouse usually has nothing separate to pay from, and the community advances it.",
 "And Article ninety-five: gambling losses are borne by the losing spouse alone, while winnings go to the community.",
])

# ---------------------------------------------------------------- 7 ACP 96-101
S("Part II · Absolute Community", "Arts. 96–101: administration, and when it ends", """
<div class="split">
 <div>
  <div class="codal small">Administration and enjoyment <b>jointly</b>. In case of disagreement, the <b>husband's decision shall prevail</b>, subject to the wife's recourse to the court <b>within five years</b> from the contract. Disposition or encumbrance <b>without court authority or the other's written consent</b> is <b>void</b>, but is a <b>continuing offer</b>.<span class="src">Art. 96, FC (paraphrased)</span></div>
  <div class="card" data-s="1"><h4>Arts. 97–98</h4><p>Either spouse may will his or her interest. No donation of community property without consent, except <b>moderate</b> ones for charity or family rejoicing or distress.</p></div>
 </div>
 <div>
  <div class="card" data-s="2"><h4>Terminates (Art. 99)</h4><ol><li>Death</li><li>Decree of <b>legal separation</b></li><li>Annulment or declaration of nullity</li><li>Judicial separation of property</li></ol></div>
  <div class="uribe" data-s="2"><span class="chip blue">URIBE</span> In a <b>void</b> marriage, there was never an ACP: "Kapag void, co-ownership ang magogovern. There is nothing to dissolve."</div>
  <div class="card" data-s="3"><h4>Separation in fact; abandonment (Arts. 100–101)</h4><p>The regime is unaffected. A spouse who left without just cause gets no support. After <b>three months</b> without information, abandonment is <b>prima facie presumed</b> (not conclusive).</p></div>
 </div>
</div>""", [
 "Administration is joint under Article ninety-six. If the spouses disagree, the husband's decision prevails, subject to the wife's recourse to the court within five years from the contract. A disposition or encumbrance without the other spouse's written consent or court authority is void, but it is treated as a continuing offer that the other spouse may still accept.",
 "Either spouse may dispose of his or her interest by will. But neither may donate community property without the other's consent, except moderate donations for charity, or on occasions of family rejoicing or distress.",
 "Under Article ninety-nine, the community ends upon death, a decree of legal separation, annulment or a declaration of nullity, or judicial separation of property. But Sir stresses: if the marriage is void, there never was an absolute community. Co-ownership under Article one forty-seven or one forty-eight governs, and there's nothing to dissolve.",
 "Mere separation in fact doesn't end the regime, but a spouse who leaves without just cause loses the right to support. And a spouse gone three months without informing the family is only prima facie presumed to have no intention of returning. A quiz statement that says deemed is false.",
])

# ---------------------------------------------------------------- 8 ACP liquidation
S("Part II · Absolute Community", "Arts. 102–104: liquidation", """
<ol class="steps v6" data-s="0">
 <li><b>Inventory</b> community and exclusive property</li>
 <li><b>Pay debts</b> of the community (spouses solidary for any balance)</li>
 <li><b>Return</b> each spouse's remaining exclusive property</li>
 <li><b>Divide</b> the net remainder equally (forfeiture: net profits = <u>increase in market value</u>)</li>
 <li><b>Presumptive legitimes</b> to the common children</li>
 <li><b>Conjugal dwelling</b> to the spouse the majority of the children choose (below 7 → mother)</li>
</ol>
<div class="row">
 <div class="card" data-s="1"><h4>Upon death (Art. 103)</h4><p>Liquidate in the estate proceeding, or within <b>one year</b> (ACP). Otherwise later dispositions are void, and if the survivor remarries without liquidating → <b>mandatory complete separation</b> for the new marriage.</p></div>
 <div class="trap" data-s="2"><span class="chip red">PERIOD TRAP</span> ACP <b>one year</b> (Art. 103) vs. CPG <b>six months</b> (Art. 130). Tolentino's book prints "one year" for Art. 130: follow the codal.</div>
</div>
<div class="card case" data-s="3"><h4>Art. 104 · Delizo v. Delizo (1976)</h4><p>Two marriages liquidated together: when it's unclear which community owns what, divide <b>in proportion to the capital and duration</b> of each.</p></div>""", [
 "On liquidation, Article one oh two sets six steps: inventory; pay the community's debts, with the spouses solidarily liable for any balance; return each spouse's exclusive property; divide the net remainder equally; deliver the common children's presumptive legitimes; and award the conjugal dwelling to the spouse the majority of the children choose, with children below seven deemed to choose the mother. If a share is forfeited, the net profits are only the increase in market value from the wedding to dissolution.",
 "On death, Article one oh three requires liquidation in the estate proceeding, or within one year. Otherwise, later dispositions of the community property are void. And if the survivor remarries without liquidating, a mandatory regime of complete separation governs the new marriage, to protect the heirs of the deceased.",
 "Watch the period. Absolute community: one year. Conjugal partnership: six months, under Article one thirty. Tolentino's book prints one year for both; answer with the codal.",
 "And Article one oh four, applied in Delizo versus Delizo: when two marriages of the same person are liquidated together and you can't tell which community owns a property, divide it in proportion to the capital and duration of each.",
])

# ---------------------------------------------------------------- 9 CPG what is exclusive/conjugal
S("Part III · Conjugal Partnership", "Arts. 109 and 117: exclusive vs. conjugal", """
<div class="split">
 <div>
  <div class="card good" data-s="0"><h4>Exclusive (Art. 109)</h4><ol><li>Brought to the marriage</li><li>Acquired during the marriage by <b>gratuitous</b> title</li><li>By redemption, barter or exchange with exclusive property</li><li>Bought with <b>exclusive money</b></li></ol></div>
  <div class="card" data-s="0"><h4>Nature</h4><p>Applies by settlement, or by default to pre-Aug. 3, 1988 marriages. Suppletory: <b>partnership</b> rules (Art. 108), not co-ownership.</p></div>
 </div>
 <div>
  <div class="card mid" data-s="1"><h4>Conjugal (Art. 117)</h4><ol><li>Onerous acquisitions at the common fund's expense</li><li>Labor, industry, work, profession</li><li><b>Fruits</b> of common property, and <b>net fruits of exclusive property</b></li><li>Hidden treasure shares</li><li>Occupation (fishing, hunting)</li><li>Excess livestock</li><li>Winnings</li></ol></div>
  <div class="trap" data-s="2"><span class="chip red">ASKED 5+ TIMES</span> In a CPG, <b>rentals from a spouse's exclusive property</b> → <b>conjugal</b>, however the property was acquired.</div>
 </div>
</div>""", [
 "Part three, the conjugal partnership of gains. It applies by settlement, or by default to marriages before August third, nineteen eighty-eight, and its suppletory rules are those on partnership, not co-ownership. The core idea: each spouse keeps what he or she brings or receives gratuitously, and the partnership gets the gains.",
 "Article one oh nine lists the exclusive property: what each brings to the marriage; what each acquires during the marriage by gratuitous title; what is acquired by redemption, barter or exchange with exclusive property; and what is bought with exclusive money. Article one seventeen lists the conjugal property: onerous acquisitions from the common fund; earnings from labor or profession; fruits of common property and the net fruits of each spouse's exclusive property; and shares in hidden treasure, occupation, excess livestock and winnings.",
 "That third item is the trap Sir has asked at least five times. In a conjugal partnership, rentals from a spouse's exclusive property are conjugal, regardless of how that property was acquired.",
])

# ---------------------------------------------------------------- 10 Art 116 presumption
S("Part III · Conjugal Partnership", "Art. 116: the presumption of conjugality", """
<div class="codal">All property acquired <b>during the marriage</b>, whether the acquisition appears to have been made, contracted or registered in the name of one or both spouses, is <b>presumed to be conjugal unless the contrary is proved</b>.<span class="src">Art. 116, FC</span></div>
<div class="row3">
 <div class="card case" data-s="1"><h4>Proof of acquisition first</h4><p><b>Torela; Dela Peña v. Avila; Andrade v. Tan:</b> whoever invokes the presumption must first prove the property was acquired <b>during</b> the marriage. The source of funds need not be shown.</p></div>
 <div class="card case" data-s="2"><h4>"Married to"</h4><p><b>Magallon v. Montejo:</b> "married to …" in a title is merely <b>descriptive</b> of civil status; it doesn't make the property conjugal.</p></div>
 <div class="uribe" data-s="3"><span class="chip blue">URIBE</span> You're the widow's counsel, and the TCT is in the husband's name. Best argument: it's <b>hers</b> (bought with her money). Next best: it's conjugal. And answer what's asked: the <b>nature</b> of the property, not just who gets it.</div>
</div>""", [
 "Article one sixteen: all property acquired during the marriage is presumed conjugal unless the contrary is proved, even if it's registered in only one spouse's name.",
 "But the presumption needs a foundation. In Torela, Dela Peña versus Avila, and Andrade versus Tan, the Court held that whoever invokes it must first prove the property was acquired during the marriage. Once that's shown, you don't need to prove the source of the funds.",
 "And in Magallon versus Montejo, a title saying married to so-and-so merely describes civil status. It doesn't prove the property is conjugal.",
 "Sir's situationer: you're counsel for the widow, and the title is in the late husband's name. Your best argument is that the land is hers alone, bought with her money. Your next best argument is that it's conjugal. And always answer the question asked: if he asks the nature of the property, say exclusive or conjugal, not just who gets it.",
])

# ---------------------------------------------------------------- 11 Arts 118-120
S("Part III · Conjugal Partnership", "Arts. 118–120: installments, credits, improvements", """
<div class="split">
 <div>
  <div class="card" data-s="0"><h4>Installments (Art. 118)</h4><p>Paid partly from exclusive and partly from conjugal funds → belongs to the buyer if <b>full ownership vested before</b> the marriage; to the partnership if it vested <b>during</b>. Reimburse either way.</p></div>
  <div class="card" data-s="1"><h4>Credits (Art. 119)</h4><p>Collections on the <b>principal</b> → the creditor-spouse. <b>Interest</b> falling due during the marriage → the partnership.</p></div>
 </div>
 <div>
  <div class="card" data-s="2"><h4>Art. 120: improvements on separate property</h4>
   <p>Compare <b>cost + increase in value</b> with the <b>value of the property</b> at the time of the improvement:</p>
   <div class="cmp"><div><b>Bigger</b> → whole property becomes <b>conjugal</b>; reimburse the owner-spouse</div><div><b>Not bigger</b> → owner-spouse <b>keeps</b> it; reimburse the cost</div></div>
   <p>Ownership vests only upon <b>reimbursement at liquidation</b>.</p></div>
  <div class="card ex" data-s="3"><h4>Example</h4><p>Lot ₱5M; house costs ₱3M and adds ₱1M → ₱4M &lt; ₱5M → spouse keeps the lot and house; reimburses ₱3M.</p></div>
 </div>
</div>""", [
 "Property bought on installments, under Article one eighteen, belongs to the buyer if full ownership vested before the marriage, and to the partnership if it vested during the marriage, with reimbursement either way. A midterm pair statement saying it always belongs to the partnership was false.",
 "For credits payable in installments, under Article one nineteen, collections on the principal belong to the creditor-spouse, while interest falling due during the marriage goes to the partnership.",
 "Article one twenty is reverse accession. When the partnership improves one spouse's separate property, compare the cost of the improvement plus the resulting increase in value with the value of the property at the time of the improvement. If the improvement side is bigger, the whole property becomes conjugal, subject to reimbursing the owner-spouse. Otherwise, the owner-spouse keeps it and reimburses the cost. Either way, ownership vests only upon reimbursement at liquidation.",
 "For example: a lot worth five million; the partnership builds a house costing three million that adds one million in value. Four million is less than five, so the spouse keeps the lot and house and reimburses the three million.",
])

# ---------------------------------------------------------------- 12 Arts 121-125
S("Part III · Conjugal Partnership", "Arts. 121–125: charges and administration", """
<div class="split">
 <div>
  <div class="card" data-s="0"><h4>Charges (Arts. 121–122)</h4><p>Mirror Art. 94, with differences: preservation of separate property <b>without</b> a "used by the family" condition; no "except (9)" in the solidary-liability clause. Personal debts only if they <b>benefited the family</b>; fines and support of illegitimate children are <b>subsidiary</b>, charged at liquidation.</p></div>
  <div class="card case" data-s="1"><h4>Benefit to the family</h4><p><b>Luzon Surety:</b> the benefit must be "clear and not fanciful and remote." <b>Carlos v. Abelardo:</b> a loan used to buy the family home → the partnership is liable, and the husband solidarily.</p></div>
 </div>
 <div>
  <div class="card" data-s="2"><h4>Administration (Art. 124)</h4><p>Same as Art. 96: joint; the husband prevails (5 years); disposition without consent or court authority → <b>void</b>, a continuing offer.</p></div>
  <div class="conflict" data-s="3"><span class="chip red">WHICH RULE?</span><p>Under the <b>Civil Code</b> such a sale was only <b>voidable</b>, within 10 years (<b>Felipe v. Aldon; Aguilar-Reyes v. Mijares</b>). The <b>date of the sale</b> decides: after Aug. 3, 1988 → void.</p></div>
 </div>
</div>""", [
 "The charges on the partnership in Articles one twenty-one and one twenty-two mirror Article ninety-four, with differences. The preservation of separate property has no used by the family condition, and the solidary liability clause has no exception for advances. Personal debts are chargeable only if they benefited the family, while fines and support of illegitimate children are paid subsidiarily and charged at liquidation.",
 "On benefit to the family: in Luzon Surety versus de Garcia, the benefit must be clear and not fanciful or remote. In Carlos versus Abelardo, a loan used to buy the family home benefited the family, so the husband was solidarily liable.",
 "Administration under Article one twenty-four is the same as Article ninety-six: joint, the husband's decision prevails subject to the wife's five-year recourse, and a disposition without written consent or court authority is void, though it's a continuing offer.",
 "Know the transition. Under the Civil Code, a sale of conjugal property without consent was only voidable, within ten years, as in Felipe versus Heirs of Aldon and Aguilar-Reyes versus Mijares. The date of the sale decides which rule applies: a sale after August third, nineteen eighty-eight is void.",
])

# ---------------------------------------------------------------- 13 Arts 126-133
S("Part III · Conjugal Partnership", "Arts. 126–133: dissolution and liquidation", """
<ol class="steps v9" data-s="0">
 <li>Inventory</li><li>Credit the partnership's <b>advances</b> for personal debts</li><li><b>Reimburse</b> each spouse's exclusive funds used</li>
 <li>Pay conjugal <b>debts</b></li><li>Return <b>exclusive</b> property</li><li>Indemnify lost or deteriorated <b>movables</b></li>
 <li>Divide <b>net profits</b> equally</li><li>Presumptive legitimes</li><li>Conjugal dwelling</li>
</ol>
<div class="row3">
 <div class="card" data-s="1"><h4>Termination</h4><p>Arts. 126–128 mirror the ACP: death, legal separation, annulment or nullity, judicial separation; separation in fact and abandonment.</p></div>
 <div class="card" data-s="2"><h4>Death (Art. 130)</h4><p>Estate proceeding or <b>six months</b>; otherwise dispositions are void; remarriage without liquidation → <b>mandatory separation</b>.</p></div>
 <div class="card case" data-s="3"><h4>Art. 133 · Santero</h4><p>Support from the common mass during liquidation goes to the survivor and the children "without distinction", even if of age.</p></div>
</div>""", [
 "The conjugal partnership ends on the same events as the absolute community, and separation in fact and abandonment work the same way.",
 "Liquidation under Article one twenty-nine has nine steps: inventory; credit the partnership for advances it made on personal debts; reimburse each spouse for exclusive funds used; pay the conjugal debts; return the exclusive property; indemnify lost or deteriorated movables that were used for the family; divide the net profits equally; deliver presumptive legitimes; and award the conjugal dwelling.",
 "On death, Article one thirty: liquidate in the estate proceeding or within six months, not one year. Otherwise later dispositions are void, and remarriage without liquidation triggers mandatory separation of property.",
 "And under Article one thirty-three, as applied in Santero, the survivor and the children receive support from the common mass during liquidation, without distinction, even if the children are of age.",
])

# ---------------------------------------------------------------- 14 Separation 134-136
S("Part IV · Separation of Property", "Arts. 134–136: separation during the marriage", """
<div class="codal">In the absence of an express declaration in the marriage settlements, the separation of property between spouses during the marriage shall not take place <b>except by judicial order</b>. Such judicial separation of property may either be <b>voluntary or for sufficient cause</b>.<span class="src">Art. 134, FC</span></div>
<div class="row">
 <div class="card" data-s="1"><h4>Sufficient causes (Art. 135)</h4><ol><li>Civil interdiction of the other spouse</li><li>Judicially declared absentee</li><li>Loss of parental authority</li><li>Abandonment or failure of obligations</li><li>Abuse of administration granted in the settlement</li><li>Separated in fact <b>at least one year</b>, reconciliation highly improbable</li></ol><p class="note">(1)–(3): the final judgment is enough.</p></div>
 <div>
  <div class="card" data-s="2"><h4>Voluntary (Art. 136)</h4><p>A <b>joint verified petition</b>; no cause needed, but all creditors must be <b>listed and notified</b>.</p></div>
  <div class="trap" data-s="3"><span class="chip red">2005 BAR · GABBY &amp; MILA</span> A private document dissolving their CPG is <b>void</b>; the CPG subsists. Separation needs a <b>court order</b>.</div>
 </div>
</div>""", [
 "Part four, separation of property. Article one thirty-four: unless the settlement expressly provides otherwise, separation during the marriage happens only by judicial order. It may be voluntary or for sufficient cause.",
 "Article one thirty-five lists six causes: civil interdiction, judicial declaration of absence, or loss of parental authority of the other spouse, where the final judgment is enough; abandonment or failure to comply with marital obligations; abuse of the power of administration granted in the settlement; and separation in fact for at least one year, with reconciliation highly improbable. Watch the number: one year here, but three months for the abandonment presumption.",
 "A voluntary separation under Article one thirty-six is by joint verified petition. No cause is needed, but all creditors must be listed in the petition and notified.",
 "In the twenty oh five bar, Gabby and Mila signed a private document dissolving their conjugal partnership and adopting complete separation. It was void; the partnership continued. Separation during the marriage needs a court order.",
])

# ---------------------------------------------------------------- 15 Separation 137-146
S("Part IV · Separation of Property", "Arts. 137–146: effects, revival, the separate regime", """
<div class="split">
 <div>
  <div class="card" data-s="0"><h4>Effects (Arts. 137–140)</h4><p>Liquidate; support pendente lite from the common property; <b>complete separation</b> thereafter; record the decree; creditors' prior rights are preserved.</p></div>
  <div class="card" data-s="1"><h4>Revival (Art. 141)</h4><p>By <b>motion</b> in the same proceeding, on seven grounds; the agreement must be <b>under oath</b> (Art. 67). After reviving a voluntary separation, no further voluntary separation.</p></div>
  <div class="uribe" data-s="2"><span class="chip blue">URIBE</span> Is a settlement the only route to separation? <b>No</b>: also mandatory separation (Arts. 103, 130), after legal separation, and by judicial decree.</div>
 </div>
 <div>
  <div class="card" data-s="3"><h4>The regime of separation (Arts. 143–146)</h4><ul><li>Present or future, total or partial; the rest → <b>absolute community</b></li><li>Each spouse administers and disposes of his or her own property <b>without consent</b></li><li>Family expenses <b>in proportion to income</b>, then to market value</li><li>Liability to creditors for family expenses: <b>solidary</b></li></ul></div>
  <div class="trap" data-s="4"><span class="chip red">FORM LADDER</span> Settlement: writing. Waiver of share: public instrument. Revival: <b>under oath</b>, filed in court.</div>
 </div>
</div>""", [
 "When the court decrees separation, the regime is liquidated; support pending the case comes from the common property; complete separation governs after that; the decree is recorded; and creditors' prior rights are preserved.",
 "The former regime may be revived under Article one forty-one, by motion in the same proceeding, on any of seven grounds, with an agreement under oath. And after a voluntary separation has been revived, no further voluntary separation is allowed.",
 "Sir asked whether a settlement is the only way to get separation of property. No. Separation also arises by law when a survivor remarries without liquidating, after legal separation, and by judicial decree.",
 "Under the regime of separation, Articles one forty-three to one forty-six: it may cover present or future property, wholly or partly, and whatever isn't separated falls under the absolute community, not the conjugal partnership. Each spouse manages and disposes of his or her own property without the other's consent. Family expenses are shared in proportion to income, and the spouses are solidarily liable to creditors for them.",
 "And remember the form ladder Sir likes to test: a settlement needs only a writing; a waiver of one's share needs a public instrument; and a revival agreement must be under oath and filed in court.",
])

# ---------------------------------------------------------------- 16 147 or 148
S("Part V · Unions Without Marriage", "147 or 148? The threshold question", """
<div class="flow">
  <div class="q" data-s="0">Is there a <b>valid</b> marriage?<small>Valid or voidable → their ACP or CPG, not Arts. 147–148</small></div>
  <div class="arrow" data-s="1">→</div>
  <div class="q" data-s="1">Is either party <b>married to someone else</b>?<small>Yes → <b>Art. 148</b> (a third person is affected)</small></div>
  <div class="arrow" data-s="2">→</div>
  <div class="q" data-s="2">Capacitated to marry <b>each other</b>, living <b>exclusively</b> together?<small>Yes → <b>Art. 147</b>. No → Art. 148</small></div>
</div>
<div class="row">
 <div class="uribe" data-s="3"><span class="chip blue">URIBE · RULE OF THUMB</span> "If one or both of them is married to other persons, a third person will be affected … <b>148</b> will apply. All other grounds that make a marriage void, as long as no third person will be affected, <b>147</b>." So first cousins who married → 147.</div>
 <div class="tol" data-s="4"><span class="chip gold">CONFLICT</span> Many commentators (Tolentino; <i>Cariño</i>) put <b>any</b> impediment between the parties (first cousins, under 18) under <b>148</b>. For Sir, apply his test and say why.</div>
</div>""", [
 "Part five, unions without marriage. Start with the threshold question. Is there a valid marriage? If the marriage is valid, or voidable and not yet annulled, the spouses have an absolute community or conjugal partnership, and Articles one forty-seven and one forty-eight don't apply.",
 "If there's no valid marriage, ask whether either party is married to someone else. If so, it's Article one forty-eight.",
 "Otherwise, ask whether they're capacitated to marry each other and living exclusively with each other as husband and wife. If yes, it's Article one forty-seven; if not, Article one forty-eight.",
 "Sir's rule of thumb: if one or both are married to other persons, a third person is affected, and Article one forty-eight applies. For every other ground of nullity where no third person is affected, apply Article one forty-seven. So first cousins who married fall under one forty-seven, in his view.",
 "But many commentators, including Tolentino, put any impediment between the parties themselves, like first cousins or a party under eighteen, under Article one forty-eight, since one forty-seven requires capacity to marry each other. In Sir's class, apply his test and explain why.",
])

# ---------------------------------------------------------------- 17 147 vs 148 table
S("Part V · Unions Without Marriage", "Art. 147 vs. Art. 148", """
<div class="tight">
<table data-s="0">
 <tr><th></th><th>Art. 147</th><th>Art. 148</th></tr>
 <tr><td>Wages and salaries</td><td><b>Equal</b> shares</td><td>The <b>earner</b>'s</td></tr>
 <tr><td>Property acquired during cohabitation</td><td>Co-owned; <b>presumed</b> joint and equal</td><td>Co-owned <b>only</b> if there's <b>actual joint contribution</b>, in proportion</td></tr>
 <tr data-s="1"><td>Care of the household</td><td><b>Counts</b> as contribution</td><td><b>Doesn't</b> count</td></tr>
 <tr data-s="1"><td>Forfeiture of the bad-faith share</td><td>→ common children → descendants → innocent party</td><td>→ the ACP or CPG of the valid marriage; applies <b>even if both are in bad faith</b></td></tr>
</table>
<div class="row3">
 <div class="card case" data-s="2"><h4>147 cases</h4><p><b>Maxey</b> (NCC 144): equal sharing even if only the man worked. <b>Salas v. Aguila</b>: presumption applies. <b>Valdes</b>: an Art. 36 marriage → liquidate as co-ownership.</p></div>
 <div class="card case" data-s="3"><h4>148 cases</h4><p><b>Juaniza:</b> the man was married to another, so his partner was no co-owner; the jeepney was his conjugal property. <b>Cariño:</b> the bigamous "wife" gets nothing without contribution. <b>Go-Bangayan:</b> "married to" is descriptive.</p></div>
 <div class="uribe" data-s="4"><span class="chip blue">URIBE</span> A saved ₱1M from wages; a condo was bought with A's income; B inherited land. "It depends on why the marriage was void." Under 147, the savings and condo are shared; under 148, they're A's. The inherited land is B's either way.</div>
</div></div>""", [
 "Now compare the two articles. Under Article one forty-seven, wages and salaries are owned in equal shares, and property acquired during the cohabitation is co-owned and presumed acquired by joint efforts, in equal shares. Under Article one forty-eight, wages belong to the earner, and there's co-ownership only of property acquired by actual joint contribution, in proportion to the contributions.",
 "Under one forty-seven, a party who cared for the family and household is deemed to have contributed; under one forty-eight, that doesn't count. And a bad-faith party's share is forfeited: under one forty-seven, to the common children, then descendants, then the innocent party; under one forty-eight, to the community or partnership of the valid marriage, and the forfeiture applies even if both parties are in bad faith.",
 "Article one forty-seven cases: in Maxey, decided under the old Article one forty-four, the partners shared equally even though only the man worked. Salas versus Aguila applied the presumption of joint acquisition. And Valdes holds that an Article thirty-six void marriage is liquidated as a co-ownership.",
 "Article one forty-eight cases: in Juaniza versus Jose, the man was married to someone else, so his partner could not be a co-owner of the jeepney; it belonged to his conjugal partnership with his legal wife. In Cariño, the bigamous second wife got nothing without proof of contribution. And in Go-Bangayan, married to in a title was merely descriptive.",
 "Sir's situationer pulls it together. A marriage is declared void. During the cohabitation, A saved a million pesos from his wages, a condo was bought with his income, and B inherited land. Who owns what? It depends on why the marriage was void. Under one forty-seven, the savings and condo are shared equally; under one forty-eight, they're A's unless B proves contribution. Either way, the inherited land is B's alone.",
])

# ---------------------------------------------------------------- 18 recap
S("Recap", "Ten things to say in recitation", """
<ol class="recap">
 <li data-s="0">Order: <b>settlement → Family Code → custom</b>; default ACP only if married on or after <b>Aug. 3, 1988</b></li>
 <li data-s="0">Settlement: <b>writing, signed, before</b> the wedding (not a public instrument)</li>
 <li data-s="0">DPN: "<b>in favor of</b>" the future spouses; ⅕ cap only if <b>other than ACP</b>; Art. 81 → <b>void</b></li>
 <li data-s="1">Art. 91 needs "<b>unless otherwise provided</b>"; jewelry is never excluded</li>
 <li data-s="1">Presumption = acquired <b>during</b> the marriage, not "registered"</li>
 <li data-s="1">Preservation of separate property: ACP needs "<b>used by the family</b>"</li>
 <li data-s="2">CPG: rentals of exclusive property are <b>conjugal</b>; Art. 120 cost + increase vs. value</li>
 <li data-s="2">Liquidate after death: ACP <b>1 year</b>, CPG <b>6 months</b></li>
 <li data-s="3">Separation during the marriage needs a <b>court order</b>; one year in fact</li>
 <li data-s="3">147 vs. 148: is a <b>third person affected</b>? Wages equal vs. earner's</li>
</ol>""", [
 "Let's recap. One: the order is settlement, Family Code, then custom, and the default is absolute community only for marriages on or after August third, nineteen eighty-eight. Two: a settlement must be in writing, signed, and executed before the wedding; not a public instrument. Three: donations are in favor of the future spouses; the one-fifth cap applies only to regimes other than absolute community; and Article eighty-one makes them void, not revocable.",
 "Four: Article ninety-one needs its qualifier, and jewelry is never excluded. Five: the presumption is triggered by acquisition during the marriage, not registration. Six: under absolute community, preservation of separate property is chargeable only if the property is used by the family.",
 "Seven: in the conjugal partnership, rentals of exclusive property are conjugal, and Article one twenty compares cost plus increase with the property's value. Eight: after death, liquidate within one year for absolute community and six months for the conjugal partnership.",
 "Nine: separation during the marriage needs a court order, and separation in fact as a cause requires at least one year. And ten: for unions without marriage, ask whether a third person is affected; wages are shared equally under one forty-seven but belong to the earner under one forty-eight. Good luck in recitation.",
])
