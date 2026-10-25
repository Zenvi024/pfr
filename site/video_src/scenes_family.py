# Video explainer: Family, Family Home, Paternity & Filiation (FC 149-182)
# Each scene: title (kicker), html body, and a list of narration steps.
# Elements with data-s="k" appear at step k (step 0 = first narration line).

SCENES = []
def S(kicker, title, body, steps):
    SCENES.append({"kicker": kicker, "title": title, "body": body, "steps": steps})

# ---------------------------------------------------------------- 0 title
S("", "", """
<div class="titlecard">
  <div class="tk">Persons and Family Relations · Atty. Uribe</div>
  <h1>The Family, the Family Home,<br>and Paternity &amp; Filiation</h1>
  <div class="tsub">Family Code, Articles 149 to 182</div>
  <div class="road">
    <div data-s="1"><b>1</b>The Family<small>Arts. 149–151</small></div>
    <div data-s="1"><b>2</b>The Family Home<small>Arts. 152–162</small></div>
    <div data-s="1"><b>3</b>Legitimacy &amp; Impugning<small>Arts. 163–171</small></div>
    <div data-s="1"><b>4</b>Proof &amp; Legitimation<small>Arts. 172–182</small></div>
  </div>
</div>""", [
 "This is your explainer on the family, the family home, and paternity and filiation: Articles one forty-nine to one eighty-two of the Family Code, for Attorney Uribe's class.",
 "We'll go in four parts. First, the family and the earnest efforts rule. Second, the family home. Third, legitimacy and the action to impugn it. And fourth, proof of filiation and legitimation. Along the way, I'll flag Sir's favorite traps, and the points where his view differs from the codal or from Tolentino.",
])

# ---------------------------------------------------------------- 1 Art 149
S("Part 1 · The Family", "Article 149: governed by law", """
<div class="codal big">The family, being the <b>foundation of the nation</b>, is a basic social institution which public policy cherishes and protects. Consequently, family relations are <b>governed by law</b> and <b>no custom, practice or agreement destructive of the family</b> shall be recognized or given effect.<span class="src">Art. 149, FC</span></div>
<div class="row">
  <div class="card" data-s="1"><h4>So, in a T/F item…</h4><p>"Family relations are governed by custom or the parties' agreement" → <b class="no">False</b></p><p>A custom destructive of the family, however long practiced → <b class="no">no effect</b></p></div>
  <div class="card case" data-s="2"><h4>Arroyo v. CA (1991)</h4><p>Once the adultery complaint is filed, <b>control passes to the public prosecutor</b>. A pardon must come <b>before</b> filing. The State's interest in marriage and the family is "of the most fundamental kind."</p></div>
</div>""", [
 "Article one forty-nine sets the policy. The family is the foundation of the nation and a basic social institution. So family relations are governed by law, and no custom, practice or agreement destructive of the family is recognized.",
 "The trap is simple. If a statement says family relations are governed by custom, or by the agreement of the parties, it is false. It's law that governs.",
 "Arroyo versus Court of Appeals shows the policy at work. In an adultery case, once the offended spouse files the complaint, control passes to the public prosecutor, and a pardon given after filing does not end the case. The State's interest in marriage and the family is, in the Court's words, of the most fundamental kind.",
])

# ---------------------------------------------------------------- 2 Art 150
S("Part 1 · The Family", "Article 150: four family relations", """
<div class="split">
 <div>
  <div class="codal">Family relations include those:<br>(1) Between <b>husband and wife</b>;<br>(2) Between <b>parents and children</b>;<br>(3) Among <b>other ascendants and descendants</b>; and<br>(4) Among <b>brothers and sisters</b>, whether of the full or half-blood.<span class="src">Art. 150, FC</span></div>
  <div class="trap" data-s="1"><span class="chip red">TRAP</span> Count them: <b>four</b>. Some reviewers print only three and drop "other ascendants and descendants", so grandparents and grandchildren <b>are</b> family.</div>
 </div>
 <div>
  <div class="fam">
   <div class="inside"><div class="lbl ok">Inside: family</div><span>Spouses</span><span>Parents ↔ children</span><span>Grandparents ↔ grandchildren</span><span>Siblings (full or half)</span></div>
   <div class="outside" data-s="2"><div class="lbl no">Outside: strangers</div><span>Brothers- &amp; sisters-in-law</span><span>Parents-in-law, step-relations</span><span>Uncles, aunts, nephews, nieces</span><span>Cousins</span></div>
  </div>
  <p class="note" data-s="2">The list is <b>exclusive</b> and <b>strictly construed</b> (Gayon v. Gayon).</p>
 </div>
</div>""", [
 "Article one fifty lists who counts as family: husband and wife, parents and children, other ascendants and descendants, and brothers and sisters, whether of the full or half blood.",
 "Count them. There are four. Some student reviewers print only three and drop other ascendants and descendants. That item matters: grandparents and grandchildren are family.",
 "Everyone else is a stranger for this purpose: in-laws, step relations, uncles and aunts, nephews and nieces, and cousins. The list is exclusive and is strictly construed, as the Court said in Gayon versus Gayon.",
])

# ---------------------------------------------------------------- 3 Art 151
S("Part 1 · The Family", "Article 151: earnest efforts toward a compromise", """
<div class="codal">No suit between members of the same family shall prosper unless it should appear from the <b>verified complaint or petition</b> that <b>earnest efforts toward a compromise</b> have been made, but that the same have failed. If it is shown that no such efforts were in fact made, the same case <b>must be dismissed</b>. This rule shall not apply to cases which <b>may not be the subject of compromise</b> under the Civil Code.<span class="src">Art. 151, FC</span></div>
<div class="flow">
  <div class="q" data-s="1">Are <b>all</b> parties family?<small>No → Art. 151 out (Gayon: sister-in-law, nephews)</small></div>
  <div class="arrow" data-s="2">→</div>
  <div class="q" data-s="2">Is it compromisable?<small>No → out. NCC 2035: status, validity of marriage or LS, LS grounds, <b>future support</b>, jurisdiction, <b>future legitime</b> (Wainwright-Versoza)</small></div>
  <div class="arrow" data-s="3">→</div>
  <div class="q" data-s="3">Raised in the MTD or answer?<small>No → <b>waived</b>; not jurisdictional; no motu proprio dismissal (Heirs of Favis)</small></div>
</div>
<div class="uribe" data-s="4"><span class="chip blue">URIBE</span> A, the illegitimate child of X, sues X and X's wife Y for support. The defense of no earnest efforts, first raised in the Supreme Court, fails: it's only a ground for a motion to dismiss, and Y is a <b>stranger</b>. Also: <b>don't assume facts</b>. If the problem doesn't say Y is the mother, don't treat her as family.</div>
""", [
 "Article one fifty-one is the earnest efforts rule. A suit between members of the same family will not prosper unless the verified complaint or petition shows that earnest efforts toward a compromise were made and failed. But the rule does not apply to matters that cannot be compromised.",
 "Run three questions. First, are all the parties family? If even one party is a stranger, like the sister-in-law and nephews in Gayon, Article one fifty-one does not apply.",
 "Second, is the subject compromisable? Under Article twenty thirty-five of the Civil Code, you cannot compromise civil status, the validity of a marriage or legal separation, any ground for legal separation, future support, the jurisdiction of courts, or future legitime. So in Wainwright-Versoza, an action for future support needed no allegation of earnest efforts.",
 "Third, did the defendant raise it on time? Earnest efforts is a condition precedent, not a jurisdictional requirement. If it isn't raised in a motion to dismiss or the answer, it is waived, and the court cannot dismiss on its own. That's Heirs of Favis versus Gonzales.",
 "Sir tested this with a situationer. A, the illegitimate child of X, sued X and X's wife Y for support, and X raised lack of earnest efforts only in the Supreme Court. The defense fails: it's only a ground for a motion to dismiss, and Y, the stepmother, is a stranger. And remember his warning: don't assume facts that aren't given.",
])

# ---------------------------------------------------------------- 4 FH what/who
S("Part 2 · The Family Home", "What it is, and who may constitute it", """
<div class="split">
 <div>
  <div class="codal">The family home, constituted <b>jointly by the husband and the wife</b> or by an <b>unmarried head of a family</b>, is the <b>dwelling house</b> where they and their family reside, <b>and the land</b> on which it is situated.<span class="src">Art. 152, FC</span></div>
  <div class="card" data-s="1"><h4>On what property? (Art. 156)</h4><ul><li>ACP or CPG property</li><li>Exclusive property of a spouse, <b>with that spouse's consent</b></li><li>The unmarried head's <b>own</b> property</li><li>Property on a <b>conditional sale on installments</b></li></ul><p>Only <b>one</b> family home per person (Art. 161).</p></div>
 </div>
 <div>
  <div class="conflict" data-s="2"><span class="chip red">CONFLICT</span><p><b>Uribe in recitation:</b> the house alone, like a condo unit, should be enough. "Kahit dwelling house can be constituted as family home by itself."</p><p data-s="3"><b>But his own midterm key</b> marks "…the dwelling house <u>or</u> the land" <b>false</b>: if the spouses don't own the land, there's no family home. The 2011 bar agrees.</p><p data-s="3"><b>Written quiz:</b> follow the codal. <b>Recitation:</b> give both.</p></div>
 </div>
</div>""", [
 "Part two, the family home. Under Article one fifty-two, it is constituted jointly by the husband and wife, or by an unmarried head of a family. It is the dwelling house where they reside, and the land on which it stands.",
 "Article one fifty-six says it must be on property of the absolute community or conjugal partnership, or on the exclusive property of either spouse with that spouse's consent, or on the unmarried head's own property. There's one exception: property bought on a conditional sale on installments. And a person may have only one family home.",
 "Here is a conflict to know. In recitation, Sir argues that the house alone should qualify. Many families in Metro Manila live in condominium units and don't own the land.",
 "But Sir's own midterm key marked false a statement saying the dwelling house or the land, because the codal says house and land, and the Supreme Court requires ownership of the land. The twenty eleven bar answer agrees. So on a written quiz, follow the codal. In recitation, give both views.",
])

# ---------------------------------------------------------------- 5 FH when
S("Part 2 · The Family Home", "When it is constituted: occupancy", """
<div class="codal">The family home is deemed constituted on a house and lot <b>from the time it is occupied as a family residence</b>. From the time of its constitution and so long as any of its beneficiaries <b>actually resides</b> therein, the family home continues to be such and is exempt from execution, forced sale or attachment…<span class="src">Art. 153, FC</span></div>
<div class="tl">
  <div class="ev grey" data-s="1"><b>Civil Code era</b><span>Judicial or extrajudicial constitution, effective on <b>recording</b></span></div>
  <div class="ev red" data-s="1"><b>Aug. 3, 1988</b><span>Family Code: <b>occupancy</b> is enough</span></div>
  <div class="ev blue" data-s="2"><b>Art. 162</b><span>Existing residences covered <b>prospectively</b> only</span></div>
</div>
<div class="card case" data-s="2"><h4>Modequillo v. Breva (1990)</h4><p>A 1976 tort liability; a levy after the Family Code took effect. Not exempt. Article 162 is not retroactive: the debt was incurred <b>before</b> the home became a family home.</p></div>
<div class="tol" data-s="3"><span class="chip gold">TOLENTINO</span> The occupancy rule is "too simple, and may give rise to fraud against creditors."</div>""", [
 "When is a family home constituted? Article one fifty-three: from the time it is occupied as a family residence. And it stays a family home as long as any beneficiary actually lives there.",
 "That's a change. Under the Civil Code, you needed a judicial or extrajudicial constitution, and it took effect only on recording. Under the Family Code, from August third, nineteen eighty-eight, occupancy is enough.",
 "What about homes occupied before nineteen eighty-eight? Article one sixty-two applies the chapter to existing residences, but only prospectively. In Modequillo versus Breva, the liability arose from a nineteen seventy-six accident, so it was a debt incurred before the home became a family home, and the property was not exempt.",
 "Tolentino criticizes the occupancy rule as too simple, saying it may open the door to fraud against creditors.",
])

# ---------------------------------------------------------------- 6 beneficiaries
S("Part 2 · The Family Home", "Beneficiaries: three requisites", """
<div class="codal">The beneficiaries of a family home are: (1) The husband and wife, or an unmarried person who is the head of a family; and (2) Their parents, ascendants, descendants, brothers and sisters, whether the relationship be <b>legitimate or illegitimate</b>, who are <b>living in the family home</b> and who <b>depend upon the head of the family for legal support</b>.<span class="src">Art. 154, FC</span></div>
<div class="steps3">
  <div data-s="1"><b>1</b>Listed relationship</div>
  <div data-s="1"><b>2</b>Living in the home</div>
  <div data-s="1"><b>3</b>Dependent on the <u>head</u> for support</div>
</div>
<div class="uribe" data-s="2"><span class="chip blue">URIBE</span> Spouses X and Y die. Their 5-year-old grandchild lives in the home, but his parents in Manila send money for him. Is he a beneficiary who extends the family home? <b>No</b>: "He is only living in the family home." That's <b>Patricio v. Dario</b>, and the 2014 bar.</div>""", [
 "Who are the beneficiaries? Under Article one fifty-four, first, the spouses or the unmarried head of the family. Second, their parents, ascendants, descendants, and brothers and sisters, legitimate or illegitimate, who live in the family home and depend on the head of the family for legal support.",
 "So for a relative, there are three requisites: a listed relationship, actual residence in the home, and dependence on the head of the family for support.",
 "Sir loves this situationer. The grandparents die in an accident. Their five-year-old grandchild lives in the house, but his parents, who work in Manila, send money for his care. Is he a minor beneficiary who extends the family home? No. He's only living there, and he doesn't depend on the grandparents for support. That's Patricio versus Dario, and it was asked in the twenty fourteen bar.",
])

# ---------------------------------------------------------------- 7 exemptions & value & consent
S("Part 2 · The Family Home", "Exemptions, value, and alienation", """
<div class="split">
 <div>
  <h3 class="mini">Art. 155: NOT exempt for… <span class="mnem">T · P · M · B</span></h3>
  <div class="tiles4">
   <div data-s="0"><b>T</b>Taxes</div>
   <div data-s="0"><b>P</b>Debts <u>prior</u> to constitution</div>
   <div data-s="0"><b>M</b>Mortgages, before <u>or after</u></div>
   <div data-s="0"><b>B</b>Builders, for the <u>construction</u></div>
  </div>
  <div class="card case" data-s="1"><h4>Siari Valley v. Lucasan (1960)</h4><p>A judgment debt still on appeal is a prior "debt". A disputed or inchoate debt still counts.</p></div>
 </div>
 <div>
  <div class="bars" data-s="2">
   <div class="bar"><span>Urban</span><i style="width:100%"></i><b>₱300,000</b></div>
   <div class="bar"><span>Rural</span><i style="width:66%"></i><b>₱200,000</b></div>
   <p class="note">Actual value <b>at the time of constitution</b> (Art. 157)</p>
  </div>
  <div class="card" data-s="3"><h4>To sell, donate or mortgage (Art. 158)</h4><p><b>Written</b> consent of the constitutor, his or her spouse, and a <b>majority</b> of the beneficiaries <b>of legal age</b>.</p></div>
 </div>
</div>""", [
 "Article one fifty-five lists the debts for which even a family home can be executed upon. Remember T, P, M, B. Taxes. Debts incurred prior to the constitution. Debts secured by a mortgage on the premises, before or after the constitution. And debts to builders, laborers and materialmen for the construction of the building.",
 "In Siari Valley Estates versus Lucasan, a judgment debt that was still on appeal when the family home was constituted was still a prior debt. It doesn't matter that it was disputed.",
 "Next, value. Under Article one fifty-seven, the family home cannot exceed three hundred thousand pesos in urban areas, or two hundred thousand pesos in rural areas, measured at the time of its constitution, not its market value today.",
 "And to sell, donate or mortgage it, Article one fifty-eight requires the written consent of the person who constituted it, his or her spouse, and a majority of the beneficiaries of legal age. Not all of them, and not the minors.",
])

# ---------------------------------------------------------------- 8 159, 160, claiming
S("Part 2 · The Family Home", "After death, execution sales, and claiming it", """
<div class="split">
 <div>
  <div class="codal small">The family home shall continue despite the death of one or both spouses or of the unmarried head of the family for a period of <b>ten years or for as long as there is a minor beneficiary</b>, and the heirs <b>cannot partition</b> the same unless the court finds <b>compelling reasons</b>… This rule shall apply <b>regardless of whoever owns</b> the property.<span class="src">Art. 159, FC</span></div>
  <div class="card" data-s="1"><h4>Art. 160: execution sale (urban example)</h4>
   <div class="seg"><i class="g" style="flex:300">₱300k exempt amount</i><i class="r" style="flex:300">₱300k creditor</i><i class="y" style="flex:150">₱150k</i></div>
   <p>Bid ₱750,000; judgment ₱300,000. No bid below the family-home value is considered. Proceeds go: Art. 157 amount first, then the judgment and costs, then the excess to the debtor.</p></div>
 </div>
 <div>
  <div class="card case" data-s="2"><h4>De Mesa v. Acero (2012)</h4><p>The exemption is a <b>personal right</b>: invoke and prove it at the levy, or within a reasonable time. "It is not the sheriff's duty to presume" it. Delay means waiver or laches.</p></div>
  <div class="card case" data-s="3"><h4>Salazar v. Felias (2018)</h4><p>Prove that it was duly constituted, by the right persons, resided in, on the right property, and within the value limit.</p></div>
 </div>
</div>""", [
 "What happens when the constitutors die? Under Article one fifty-nine, the family home continues for ten years, or for as long as there is a minor beneficiary, and the heirs cannot partition it unless the court finds compelling reasons. This applies regardless of who owns the property.",
 "Article one sixty lets an ordinary creditor reach only the excess value. Say an urban family home sells for seven hundred fifty thousand pesos, and the judgment is three hundred thousand. The first three hundred thousand, the exempt amount, is applied first; then three hundred thousand goes to the creditor; and the remaining one hundred fifty thousand goes back to the debtor. And no bid below the family home value is even considered.",
 "Finally, you must claim the exemption. In De Mesa versus Acero, the Court said it's a personal right: it must be invoked and proved at the levy or within a reasonable time, and it is not the sheriff's duty to presume it.",
 "And in Salazar versus Felias, the claimant must prove that the home was duly constituted, by the proper persons, actually resided in, on the proper kind of property, and within the value limit.",
])

# ---------------------------------------------------------------- 9 legitimate
S("Part 3 · Legitimacy", "Who are legitimate", """
<div class="codal">Children <b>conceived or born during the marriage</b> of the parents are legitimate.<span class="src">Art. 164, FC (1st par.)</span></div>
<div class="tl3">
  <div class="mar"><span>Valid marriage</span></div>
  <div class="ln l1" data-s="1"><i>conceived</i>──────▶<i>born</i> <b>legitimate</b></div>
  <div class="ln l2" data-s="1"><i>conceived</i>────▶<i>born</i> <b>legitimate</b></div>
  <div class="ln l3" data-s="1"><i>conceived</i>──────▶<i>born</i> <b>legitimate</b></div>
</div>
<div class="row">
 <div class="card" data-s="2"><h4>Also legitimate</h4><ul><li>Art. 54: void under <b>Art. 36</b> (before the judgment is final), and subsequent marriages void under <b>Art. 53</b></li><li>Voidable marriages, before the decree is final</li><li>Adopted and legitimated children</li></ul></div>
 <div class="uribe" data-s="3"><span class="chip blue">URIBE</span> Art. 54 covers <b>only</b> Arts. 36 and 53. If the marriage is void for no license, the children are illegitimate. Don't argue "best interest of the child." <br>T/F: "must be conceived or born during the marriage" → <b>False</b>.</div>
</div>""", [
 "Part three, legitimacy. The core rule is Article one sixty-four: children conceived or born during the marriage of the parents are legitimate.",
 "Notice the word or. A child conceived before the wedding but born during the marriage is legitimate. So is a child conceived during the marriage but born after it ends, for example after the husband dies.",
 "Some children are legitimate even though the marriage is defective. Under Article fifty-four, children of a marriage void for psychological incapacity under Article thirty-six, conceived or born before the judgment becomes final, are legitimate. So are children of a subsequent marriage void under Article fifty-three. Children of voidable marriages, adopted children and legitimated children are legitimate too.",
 "Sir stresses that the Article fifty-four exception covers only Articles thirty-six and fifty-three. If the marriage is void for lack of a license, the children are illegitimate, and don't argue the best interest of the child. And in Quiz five, the statement that a legitimate child must be conceived or born during the marriage was false, because of these other legitimate children.",
])

# ---------------------------------------------------------------- 10 AI
S("Part 3 · Legitimacy", "Artificial insemination", """
<div class="codal">Children conceived as a result of artificial insemination <b>of the wife</b> with the sperm of the <b>husband or that of a donor or both</b> are likewise legitimate children of the husband and his wife, provided, that <b>both of them authorized or ratified</b> such insemination in a <b>written instrument</b> executed and signed by them <b>before the birth</b> of the child. The instrument shall be recorded in the civil registry together with the birth certificate.<span class="src">Art. 164, FC (2nd par.)</span></div>
<div class="row">
 <div class="uribe" data-s="1"><span class="chip blue">URIBE</span><ul><li>Quiz 5: "AI with the husband's sperm → legitimate", with no mention of written consent → <b>False</b></li><li>"<b>Public</b> instrument" → none of the above: "Written lang."</li><li>Embryo carried by another woman: "The FC does not recognize the concept of <b>surrogacy</b>."</li></ul></div>
 <div class="tol" data-s="2"><span class="chip gold">TOLENTINO</span> The writing is only <b>evidence</b> of consent. A 2006 bar answer agrees: a child born in wedlock is presumed legitimate, and lack of consent is just a ground to impugn. <br><b>For Sir, treat the writing as a requirement.</b></div>
</div>""", [
 "The second paragraph of Article one sixty-four covers artificial insemination. A child conceived through insemination of the wife, with the sperm of the husband, a donor, or both, is legitimate, provided both spouses authorized or ratified it in a written instrument signed before the birth.",
 "Sir treats the written instrument as a requirement. In Quiz five, a statement that a child of insemination with the husband's sperm is legitimate, with no mention of written consent, was false. Watch for one changed word: if the item says public instrument instead of written instrument, the answer becomes none of the above. And if the embryo is carried by another woman, that's surrogacy, which the Family Code does not recognize.",
 "Tolentino reads the writing as mere evidence of consent, and a twenty oh six bar answer agrees. But for Sir's class, treat the written instrument as required.",
])

# ---------------------------------------------------------------- 11 illegitimate + rights
S("Part 3 · Legitimacy", "Illegitimate children and their rights", """
<div class="codal small">Children <b>conceived and born outside a valid marriage</b> are illegitimate, unless otherwise provided in this Code.<span class="src">Art. 165, FC</span></div>
<table data-s="1">
 <tr><th></th><th>Legitimate (Art. 174)</th><th>Illegitimate (Art. 176, RA 9255)</th></tr>
 <tr><td>Surname</td><td>Father's <b>and</b> mother's</td><td>Mother's; <b>may</b> use the father's if he expressly recognized the child</td></tr>
 <tr><td>Parental authority</td><td>Joint</td><td><b>Mother</b> alone</td></tr>
 <tr><td>Legitime</td><td>Full</td><td><b>Each</b> = ½ of <b>a</b> legitimate child's</td></tr>
</table>
<div class="row">
 <div class="trap" data-s="2"><span class="chip red">TRAP</span> "conceived <b>or</b> born outside a valid marriage" → <b class="no">False</b> (it's "and"). "½ of the legitime of the legitimate children" → <b class="no">False</b>.</div>
 <div class="card case" data-s="3"><h4>Surname cases</h4><p><b>Osmeña de Valencia:</b> no monopoly over the father's surname. <b>Barcelote</b> (2017): "may" is permissive, and the mother must sign the birth certificate. <b>Moore:</b> no stepfather's surname.</p></div>
</div>""", [
 "Article one sixty-five is the mirror image: children conceived and born outside a valid marriage are illegitimate, unless the Code provides otherwise.",
 "Compare their rights. Legitimate children bear the surnames of the father and mother, are under joint parental authority, and get the full legitime. Illegitimate children use the mother's surname, though under Republic Act ninety-two fifty-five they may use the father's if he expressly recognized them. They are under the mother's sole parental authority, and the legitime of each illegitimate child is one half of the legitime of a legitimate child.",
 "Two traps. Conceived or born outside a valid marriage is false, because the codal says and. And one half of the legitime of the legitimate children is false: it's each illegitimate child getting half of one legitimate child's share.",
 "On surnames: in Osmeña de Valencia, legitimate children have no monopoly over their father's surname. In Barcelote, the word may is permissive, and the mother must sign the birth certificate. And under Moore, a legitimate child can't take the stepfather's surname.",
])

# ---------------------------------------------------------------- 12 impugn grounds
S("Part 3 · Impugning", "Article 166: the only grounds", """
<div class="win">
  <div class="w120" data-s="0">first <b>120</b> days</div><div class="w180" data-s="0">last 180 days (minimum viable gestation)</div>
  <div class="lab"><span>day −300</span><span>day −180</span><span>birth</span></div>
</div>
<div class="row3">
 <div class="card" data-s="1"><h4>(1) Physical impossibility</h4><p>No intercourse possible in the <b>first 120 of the 300 days</b> before birth, because of: (a) the husband's <b>physical incapacity</b> (impotence, not sterility); (b) <b>living separately</b> so intercourse was impossible; or (c) serious illness that <b>absolutely</b> prevented it.</p></div>
 <div class="card" data-s="2"><h4>(2) Biological or scientific reasons</h4><p>Blood tests and DNA. <b>Jao v. CA:</b> blood tests are conclusive of <b>non</b>-paternity only.</p><h4>(3) Vitiated AI consent</h4><p>Mistake, fraud, violence, intimidation, undue influence.</p></div>
 <div class="card case" data-s="3"><h4>Cases</h4><p><b>Andal:</b> severe TB is not impotence. <b>Macadangdang:</b> the spouses lived in the same province, so access was possible; moral impossibility isn't enough. <b>Tan v. Trocio:</b> resemblance is inconclusive.</p></div>
</div>""", [
 "Now, the action to impugn legitimacy. Article one sixty-six says legitimacy may be impugned only on its listed grounds. Look at this timeline: the three hundred days before birth, split into the first one hundred twenty and the last one hundred eighty. Why those numbers? Three hundred days is the longest gestation, and one hundred eighty is the shortest for a viable child. If the husband had no access in the first one hundred twenty days, conception could only have happened in the last one hundred eighty, and a viable child couldn't have been born that soon.",
 "The first ground is physical impossibility of intercourse during that first one hundred twenty days, because of the husband's physical incapacity, meaning impotence and not sterility; because the spouses lived apart so that intercourse was impossible; or because of serious illness that absolutely prevented it.",
 "The second ground is biological or scientific proof, like blood tests or DNA. In Jao versus Court of Appeals, a blood test was conclusive of non-paternity, though not of paternity. The third ground is vitiated consent to artificial insemination.",
 "The cases show how strict this is. In Andal versus Macaraig, a husband with advanced tuberculosis was still capable of intercourse. In Macadangdang, the spouses lived in the same province, so access was possible, and estrangement alone is moral, not physical, impossibility. And in Tan versus Trocio, physical resemblance proved nothing.",
])

# ---------------------------------------------------------------- 13 167-169
S("Part 3 · Impugning", "Arts. 167–169: the mother's word, and remarriage", """
<div class="codal small">The child shall be considered legitimate <b>although the mother may have declared against its legitimacy</b> or may have been <b>sentenced as an adulteress</b>.<span class="src">Art. 167, FC</span></div>
<div class="tl168" data-s="1">
  <div class="axis"></div>
  <div class="m m0">1st marriage ends</div><div class="m m1">2nd wedding (within 300 days)</div><div class="m m2">+180 days</div>
  <div class="z z1">Born ≤ 180 days after the 2nd wedding → <b>1st husband</b><br><small>(only if also within 300 days of the termination)</small></div><div class="z z2">Born after 180 days → <b>2nd husband</b></div>
</div>
<div class="row">
 <div class="uribe" data-s="2"><span class="chip blue">URIBE · QUIZ 5 #13</span> A dies on Jan. 1, 2024. B marries C on Aug. 1, 2024. D is born Nov. 15, 2024: <b>319 days</b> after A's death. → <b>Legitimate child of B and C.</b> "Alangan naman makabuntis pa ang patay."</div>
 <div class="card" data-s="3"><h4>Art. 169</h4><p>Born <b>more than 300 days</b> after the marriage ended, with no remarriage: <b>no presumption</b>. Whoever alleges legitimacy or illegitimacy must prove it.</p></div>
</div>""", [
 "Article one sixty-seven: the child is still legitimate even if the mother declares against its legitimacy, or is convicted of adultery. Her word doesn't decide the child's status.",
 "Article one sixty-eight handles a mother who remarries within three hundred days after her first marriage ends. If the child is born within one hundred eighty days after the second wedding, and also within three hundred days of the termination, the child is presumed the first husband's. If born after one hundred eighty days from the second wedding, the child is presumed the second husband's.",
 "Here's Sir's Quiz five problem. A dies on January first, twenty twenty-four. His widow B marries C on August first. D is born on November fifteenth. That's three hundred nineteen days after A's death, beyond three hundred, so A cannot be the father. The one-eighty rule doesn't even matter. D is the legitimate child of B and C, born during their marriage.",
 "And under Article one sixty-nine, if a child is born more than three hundred days after the marriage ended, there is no presumption either way. Whoever alleges legitimacy or illegitimacy must prove it.",
])

# ---------------------------------------------------------------- 14 170-171
S("Part 3 · Impugning", "Arts. 170–171: when, and who", """
<div class="split">
 <div>
  <div class="bars" data-s="0">
   <div class="bar"><span>Same city or municipality as the birth or recording</span><i style="width:33%"></i><b>1 year</b></div>
   <div class="bar"><span>Elsewhere in the Philippines</span><i style="width:66%"></i><b>2 years</b></div>
   <div class="bar"><span>Abroad</span><i style="width:100%"></i><b>3 years</b></div>
   <p class="note">From knowledge of the birth or its recording; if concealed, from discovery, <b>whichever is earlier</b>.</p>
  </div>
  <div class="card" data-s="1"><h4>Heirs may impugn only if (Art. 171)</h4><ul><li>the husband died before his period expired;</li><li>he died after filing, without desisting; or</li><li>the child was born after his death.</li></ul></div>
 </div>
 <div>
  <div class="conflict" data-s="2"><span class="chip red">CONFLICT</span><p><b>Liyao (2002):</b> only the husband (or his heirs) may impugn; "the child himself cannot choose his own filiation."</p><p><b>Yap v. Yap (2022):</b> the child may establish filiation with the biological father (DNA). <b>Sir agrees:</b> "truth should prevail."</p></div>
  <div class="trap" data-s="3"><span class="chip red">TRAPS</span><ul><li>"resides in the <b>country</b>" → none of the above</li><li>After impugning, the child is <b>not</b> "an illegitimate child of the spouses"; he's simply not the husband's child</li><li>No collateral attack. And <b>Lim v. IAC:</b> "not the child at all" isn't impugning</li></ul></div>
 </div>
</div>""", [
 "How long does the husband have? Under Article one seventy: one year, if he or any heir lives in the city or municipality where the birth took place or was recorded; two years if elsewhere in the Philippines; and three years if abroad. The period runs from knowledge of the birth or its recording, or if the birth was concealed, from discovery, whichever is earlier.",
 "Under Article one seventy-one, the heirs may impugn only in three cases: the husband died before his period expired; he died after filing without desisting; or the child was born after his death.",
 "Who else can impugn? Under Liyao, only the husband or his heirs; the child cannot choose his own filiation. But Yap versus Yap, in twenty twenty-two, allowed a child to establish filiation with his biological father despite the presumption. Sir agrees with Yap: truth over reputation. In recitation, give the rule, then Yap and Sir's view.",
 "Three traps. In Quiz five, Sir changed city or municipality to country, which makes the answer none of the above. A child whose legitimacy is successfully impugned is not an illegitimate child of the spouses; he's simply not the husband's child. And legitimacy can't be attacked collaterally. But under Lim versus Intermediate Appellate Court, a claim that someone is not the child at all is not impugning, so these periods don't apply.",
])

# ---------------------------------------------------------------- 15 proof
S("Part 4 · Proof of Filiation", "Primary and secondary evidence", """
<div class="split">
 <div>
  <div class="card good" data-s="0"><h4>Primary (Art. 172, 1st par.)</h4><ul><li>Record of birth in the civil register, or a <b>final judgment</b></li><li>Admission in a <b>public document</b>, or a <b>private handwritten instrument signed</b> by the parent</li></ul></div>
  <div class="card mid" data-s="1"><h4>Secondary: only <u>in the absence of</u> primary</h4><ul><li><b>Open and continuous possession</b> of status (Mendoza v. CA: treated as his own, directly and not intermittently)</li><li>Any other means under the Rules of Court: testimony, pedigree, DNA</li></ul></div>
 </div>
 <div>
  <div class="card bad" data-s="2"><h4>Not enough by itself</h4><ul><li>A birth certificate the father didn't sign (Reyes). Sir: "You can actually put Gokongwei's name."</li><li>A baptismal certificate; a marriage contract (Lim v. CA)</li><li>Pictures, resemblance, unsigned writings</li></ul></div>
  <div class="conflict" data-s="3"><span class="chip red">ART. 175</span><p>An illegitimate child relying on <b>secondary</b> proof must sue <b>during the alleged parent's lifetime</b> (Ara v. Pizarro).</p><p><b>Sir disagrees</b> ("may"; DNA after death; Aquino, Yap), <b>but his quiz keys follow the codal.</b></p></div>
 </div>
</div>""", [
 "Part four, proof of filiation. Article one seventy-two has primary evidence: the record of birth in the civil register or a final judgment, and an admission of filiation in a public document or a private handwritten instrument signed by the parent.",
 "Secondary evidence is allowed only in the absence of primary evidence: open and continuous possession of the status of a child, or any other means allowed by the Rules of Court, like testimony or DNA. Mendoza versus Court of Appeals says the father must treat the child as his own, directly, spontaneously, and not intermittently.",
 "What's not enough by itself? A birth certificate the father didn't sign, as in Reyes versus Court of Appeals. As Sir put it, you could write anyone's name on it. Baptismal certificates, a marriage contract, photos and resemblance aren't enough either.",
 "Under Article one seventy-five, illegitimate children prove filiation the same way, but if they rely on secondary evidence, they must sue during the alleged parent's lifetime. Sir thinks this is regressive, given DNA, and cites Aquino and Yap. But his quiz keys follow the codal, so answer with the lifetime rule, and add his view if there's room.",
])

# ---------------------------------------------------------------- 16 legitimation
S("Part 4 · Legitimation", "Legitimated children (Arts. 177–182)", """
<div class="codal">Children <b>conceived and born outside of wedlock</b> of parents who, <b>at the time of conception</b> of the former, were <b>not disqualified by any impediment</b> to marry each other, or were so disqualified only because either or both of them were <b>below eighteen (18) years of age</b>, <b>may</b> be legitimated.<span class="src">Art. 177, FC (as amended by RA 9858)</span></div>
<div class="steps3">
  <div data-s="1"><b>1</b>No impediment <u>at conception</u></div>
  <div data-s="1"><b>2</b>Subsequent <u>valid</u> marriage (Art. 178)</div>
  <div data-s="1"><b>3</b>Retroacts to <u>birth</u> (Art. 180)</div>
</div>
<div class="row">
 <div class="uribe" data-s="2"><span class="chip blue">URIBE</span><ul><li>The impediment at <b>birth</b> doesn't matter; only at conception</li><li><b>Age is capacity, not an impediment</b></li><li>"<b>May</b>", not "will"</li><li>Essay: <b>first</b> establish illegitimacy, <b>then</b> legitimation</li></ul></div>
 <div class="card" data-s="3"><h4>Also</h4><p>Annulment of a <b>voidable</b> marriage doesn't affect legitimation, but a <b>void</b> one legitimates no one. A child who died before the marriage benefits his descendants (Art. 181). Impugn only by those <b>prejudiced</b>, within <b>5 years</b> (Art. 182).</p></div>
</div>""", [
 "Last, legitimation. Under Article one seventy-seven, as amended by Republic Act ninety-eight fifty-eight, children conceived and born outside of wedlock may be legitimated if, at the time of conception, their parents were not disqualified by any impediment to marry each other, or were disqualified only because one or both were below eighteen.",
 "So there are three steps. No impediment at conception. A subsequent valid marriage of the parents, under Article one seventy-eight. And then the effect retroacts to the child's birth, under Article one eighty.",
 "Sir's points: what matters is the time of conception. An impediment that arises only by the time of birth doesn't matter. Age is a matter of capacity, not an impediment. The codal says may be legitimated, not will be, because a valid marriage is still needed. And in an essay, first establish that the child is illegitimate, then discuss legitimation.",
 "A few more rules. Annulment of a voidable marriage doesn't undo legitimation, but a void marriage legitimates no one. Legitimation of a child who died before the marriage benefits his descendants. And legitimation may be impugned only by those prejudiced in their rights, within five years.",
])

# ---------------------------------------------------------------- 17 recap
S("Recap", "Ten things to say in recitation", """
<ol class="recap">
 <li data-s="0">Art. 150 lists <b>four</b> relations; in-laws are strangers (Gayon)</li>
 <li data-s="0">Earnest efforts: all family, compromisable, raised on time (Favis)</li>
 <li data-s="1">FH = constituted by <b>occupancy</b>; pre-1988 homes covered prospectively (Modequillo)</li>
 <li data-s="1">Beneficiary = relation + lives there + <b>depends on the head</b> (Patricio)</li>
 <li data-s="1">T-P-M-B; ₱300k / ₱200k <b>at constitution</b>; claim it at the levy (De Mesa)</li>
 <li data-s="2">Conceived <b>or</b> born = legitimate; Art. 54 = <b>only</b> Arts. 36 and 53</li>
 <li data-s="2">AI needs <b>written</b> consent before birth (Sir); surrogacy isn't recognized</li>
 <li data-s="2">First 120 of 300 days; 1 / 2 / 3 years, <b>whichever is earlier</b></li>
 <li data-s="3">Secondary proof needs the parent alive (codal); Sir: DNA after death</li>
 <li data-s="3">Legitimation: impediment tested <b>at conception</b>; age isn't an impediment</li>
</ol>""", [
 "Let's recap. One: Article one fifty lists four relations, and in-laws are strangers. Two: earnest efforts applies only if all parties are family, the subject is compromisable, and the defense is raised on time.",
 "Three: the family home is constituted by occupancy, and homes occupied before nineteen eighty-eight are covered only prospectively. Four: a beneficiary must be related, live there, and depend on the head of the family. Five: remember T, P, M, B, the value limits at constitution, and claim the exemption at the levy.",
 "Six: conceived or born during the marriage means legitimate, and Article fifty-four covers only Articles thirty-six and fifty-three. Seven: for Sir, artificial insemination needs written consent before birth, and surrogacy isn't recognized. Eight: the first one hundred twenty of three hundred days, and one, two or three years to impugn, counted from whichever date is earlier.",
 "Nine: secondary proof of illegitimate filiation needs the parent alive under the codal, though Sir would allow DNA after death. And ten: for legitimation, test the impediment at conception, and remember that age is not an impediment. Good luck in recitation and on Monday's quiz.",
])
