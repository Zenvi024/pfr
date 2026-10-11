"""Helpers for authoring the property-relations quiz bank.

Each bank_*.py file builds a list of items with these helpers and writes
data/quiz_bank/NN_<topic>.json in the schema documented in HANDOFF.md §4.3.
"""
import json, os

PAIR = ["Both are true", "Both are false", "No. 1 is true, No. 2 is false", "No. 1 is false, No. 2 is true"]
TF = ["True", "False"]
ABS = "Consider the statement true only when it is absolutely true."
ABS_MID = "If not absolutely true, the statement is false."
NOSHUFFLE = {"M-49", "M-50", "M-63", "A-25", "A-34", "C-19", "S-9", "S-13", "U-2", "U-32"}


def pair_index(s1, s2):
    return {(True, True): 0, (False, False): 1, (True, False): 2, (False, True): 3}[(s1, s2)]


class Bank:
    def __init__(self, topic, prefix):
        self.topic, self.prefix, self.items = topic, prefix, []

    def _add(self, origin, src, typ, stem, choices, answer, expl, key=None, statements=None, topic=None):
        it = {"id": f"{self.prefix}-{len(self.items) + 1}", "topic": topic or self.topic, "origin": origin,
              "src": src, "type": typ, "stem": stem}
        if statements:
            it["statements"] = statements
        it.update({"choices": choices, "answer": answer, "explanation": expl, "key_note": key})
        assert 0 <= answer < len(choices), it["id"]
        self.items.append(it)
        return it

    def tf(self, origin, src, stem, ans, expl, key=None, topic=None):
        return self._add(origin, src, "tf", stem, TF, 0 if ans else 1, expl, key, topic=topic)

    def pair(self, origin, src, s1, s2, a1, a2, expl, key=None, stem=ABS, topic=None):
        return self._add(origin, src, "pair", stem, PAIR, pair_index(a1, a2), expl, key,
                         statements=["1. " + s1, "2. " + s2], topic=topic)

    def mcq(self, origin, src, stem, choices, ans, expl, key=None, topic=None):
        if isinstance(ans, str):
            ans = "abcdefgh".index(ans.lower())
        return self._add(origin, src, "mcq", stem, choices, ans, expl, key, topic=topic)

    def shuffle_choices(self):
        # Rotate choices of authored/adapted MCQs so answers are not all "c".
        # Verbatim samplex and UP BOC items keep the professor's lettering.
        import random
        for it in self.items:
            if it["type"] != "mcq":
                continue
            if it["origin"] == "samplex" or (it["origin"] == "bar" and "adapted" not in it["src"]):
                continue
            if any(k in c.lower() for c in it["choices"] for k in ("above", "a and b", "all of the", "none of")):
                continue
            if it["id"] in NOSHUFFLE:  # explanation refers to options by letter
                continue
            rnd = random.Random(it["id"] + "pr2026")
            order = list(range(len(it["choices"])))
            rnd.shuffle(order)
            ans_text = it["choices"][it["answer"]]
            it["choices"] = [it["choices"][i] for i in order]
            it["answer"] = it["choices"].index(ans_text)

    def write(self, fname):
        self.shuffle_choices()
        out = os.path.join(os.path.dirname(__file__), "..", "data", "quiz_bank", fname)
        ids = [x["id"] for x in self.items]
        assert len(ids) == len(set(ids))
        with open(out, "w") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=1)
        print(f"wrote {fname}: {len(self.items)} items")
