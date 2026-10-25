"""Samplex quiz videos for property relations: plan → tts → render → assemble.

  python3 video_src/quiz_video.py plan|tts|render|assemble <workdir>

plan      frames.json (HTML per frame) and segs.json (timeline) per video, from the quiz bank
          (origin "samplex") and video_src/quiz_property.py
tts       Kokoro narration per segment (cached by text), with per-sentence caption timings
render    PNG per frame (video_src/render_frames.js)
assemble  <file>.mp4 (1080p, chapters, soft subtitles), <file>.srt and <file>.quiz.json
          (the reveal points the Videos tab uses for its answer-along mode)
Needs <workdir>/voice/kokoro-v1.0.int8.onnx and voices-v1.0.bin.
"""
import hashlib, html, json, os, re, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(H)
sys.path.insert(0, H)
from quiz_property import VIDEOS, PARTS, Q

SR = 24000
COUNT = 5                       # seconds to answer
L = "ABCDEFGH"
PAIR_SAY = "A: both are true. B: both are false. C: No. 1 is true, No. 2 is false. D: No. 1 is false, No. 2 is true."
NAMEVERBS = {"inherited", "owned", "died", "saved", "married", "was", "has"}

# ------------------------------------------------------------------ spoken text
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def words(n):
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
    if n < 1000: return ONES[n // 100] + " hundred" + (" " + words(n % 100) if n % 100 else "")
    return words(n // 1000) + " thousand" + (" " + words(n % 1000) if n % 1000 else "")
def ordinal(n):
    w = words(n); irregular = {"one": "first", "two": "second", "three": "third", "five": "fifth", "eight": "eighth", "nine": "ninth", "twelve": "twelfth"}
    head, _, last = w.rpartition("-")
    last = irregular.get(last, (last[:-1] + "ieth") if last.endswith("y") else last + "th")
    return (head + "-" if head else "") + last
def year(n):
    if 2000 <= n < 2010: return "two thousand" + (" " + ONES[n % 10] if n % 10 else "")
    hi, lo = divmod(n, 100)
    return words(hi) + " " + ("hundred" if lo == 0 else ("oh " + ONES[lo] if lo < 10 else words(lo)))
SUBS = [("₱5,000", "five thousand pesos"), ("1/5", "one-fifth"), ("20%", "twenty percent"), ("5PM", "five p.m."), ("10AM", "ten a.m."),
        ("June 1, 2019", "June first, twenty nineteen"), ("No. 1", "number one"), ("No. 2", "number two"), ("PH laws", "Philippine laws"),
        ("CPG", "conjugal partnership of gains"), ("ACP", "absolute community of property"), (" prop ", " property "), ("A & B", "A and B"),
        ("Article 41", "Article forty-one"), ("Niñal", "Neenyal"), ("Uribe", "Oo-ree-beh")]
def speak(s):
    """Text for the TTS engine: numbers and abbreviations spelled out, and the letter A said as a letter when it names a party."""
    for a, b in SUBS: s = s.replace(a, b)
    s = re.sub(r"\b(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2})\b",
               lambda m: m.group(1) + " " + ordinal(int(m.group(2))), s)
    s = re.sub(r"\b(19\d\d|20\d\d)\b", lambda m: year(int(m.group())), s)
    s = re.sub(r"\b\d+\b", lambda m: words(int(m.group())), s)
    def fix(m):
        i = m.start(); before = s[:i].rstrip()
        start = not before or before[-1] in ".!?:"
        nxt = re.match(r"(\S+)", s[m.end():].lstrip())
        nxt = nxt.group(1) if nxt else ""
        if start and s[m.end():m.end() + 1] == " " and nxt[:1].islower() and nxt.strip(",.") not in NAMEVERBS:
            return "A"                     # the article "A parcel …"
        return "Eigh"
    s = re.sub(r"\bA\b(?!')", fix, s)
    s = re.sub(r"\bA's\b", "Eigh's", s)
    return s
def sents(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'“])", t) if x.strip()]

# ------------------------------------------------------------------ data
def bank():
    out = {}
    for f in sorted(os.listdir(os.path.join(ROOT, "data", "quiz_bank"))):
        for q in json.load(open(os.path.join(ROOT, "data", "quiz_bank", f))):
            if q["origin"] == "samplex": out[q["id"]] = q
    return out
def short_src(s):
    s = s.split(";")[0]
    s = re.sub(r"\s*\((scanned[^)]*|Studocu)\)", "", s)
    return s.replace("Uribe CivRev 2025 Quiz 4 (Sep 25, 2025)", "Uribe CivRev Quiz 4 (2025)").strip()
def esc(s): return html.escape(s, quote=False)
def apply_ops(text, ops):
    t = esc(text)
    for op in ops:
        k = op[0]
        if k == "x":
            w = esc(op[1]); assert w in t, (text, op); t = t.replace(w, f"<del>{w}</del> <ins>{esc(op[2])}</ins>", 1)
        elif k == "+":
            ins = f"<ins>{esc(op[2]).strip()}</ins>"
            if op[1] == "^": t = ins + " " + t[0].lower() + t[1:] if not t.startswith(("X", "A ")) else ins + " " + t
            elif op[1] == "$": t = t.rstrip(".") + " " + ins + "."
            else:
                a = esc(op[1]); assert a in t, (text, op); lead = "" if op[2].startswith(",") else " "
                t = t.replace(a, a + lead + ins, 1)
        elif k in ("ok", "hl"):
            w = esc(op[1]); assert w in t, (text, op); t = t.replace(w, f'<mark class="{k}">{w}</mark>', 1)
    return t

# ------------------------------------------------------------------ frames
def top(part, n, total):
    return (f'<div class="qtop"><div class="brand">Property Relations · Samplex Quiz</div><div class="part">{esc(part)}</div>'
            f'<div class="qn">Question <b>{n}</b> of {total}</div></div><div class="bar"><i style="width:{100 * n / total:.1f}%"></i></div>')
def timer(k):
    r, c = 108, 2 * 3.14159 * 108
    return (f'<div class="timer"><svg viewBox="0 0 250 250"><circle cx="125" cy="125" r="{r}" fill="#fff" stroke="#efe4e6" stroke-width="22"/>'
            f'<circle cx="125" cy="125" r="{r}" fill="none" stroke="#7a1f2b" stroke-width="22" stroke-linecap="round" '
            f'stroke-dasharray="{c * k / COUNT:.1f} {c:.1f}"/></svg><div class="n">{k}</div></div>'
            f'<div class="lab">Your answer?<small>Pause if you need more time</small></div>')
def qframe(q, n, total, part, hi=None, mode="read", k=0):
    typ = q["type"]; ans = q["answer"]
    def chcls(i):
        if mode == "reveal": return " right" if i == ans else " dim"
        return " on" if hi == ("c", i) else ""
    body = ""
    if typ == "tf":
        body += f'<div class="stem">{esc(q["stem"])}</div><div class="tfrow">'
        body += "".join(f'<div class="ch{chcls(i)}">{c.upper()}</div>' for i, c in enumerate(q["choices"])) + "</div>"
    elif typ == "pair":
        body += f'<div class="stem small">{esc(q["stem"])}</div>'
        for i, s in enumerate(q["statements"]):
            body += f'<div class="st{" on" if hi == ("s", i) else ""}"><b>{i + 1}</b><span>{esc(re.sub(r"^\d\.\s*", "", s))}</span></div>'
        body += '<div class="chs grid">' + "".join(
            f'<div class="ch{chcls(i)}{" on" if hi == ("all",) and mode == "read" else ""}"><b>{L[i]}</b><span>{esc(c)}</span></div>'
            for i, c in enumerate(q["choices"])) + "</div>"
    else:
        body += f'<div class="stem">{esc(q["stem"])}</div><div class="chs">'
        body += "".join(f'<div class="ch{chcls(i)}"><b>{L[i]}</b><span>{esc(c)}</span></div>' for i, c in enumerate(q["choices"])) + "</div>"
    if mode == "count": side = timer(k)
    elif mode == "reveal":
        a = q["choices"][ans]
        side = f'<div class="stamp"><div><small>ANSWER</small><b class="{"w" if typ == "tf" else ""}">{esc(a.upper() if typ == "tf" else L[ans])}</b></div></div>'
    else: side = '<div class="ear">🎧</div><div class="lab">Listen<small>{} seconds after the choices</small></div>'.format(COUNT)
    label = {"tf": "True or False", "pair": "Pair · absolutely true?", "mcq": "Multiple choice"}[typ]
    return (f'<div class="frame">{top(part, n, total)}<div class="qbody"><div class="qmeta"><span class="type {typ}">{label}</span>'
            f'<span>{esc(short_src(q["src"]))}</span></div><div class="qmain"><div class="fit">{body}</div><div class="side">{side}</div></div></div></div>')
def xframe(q, a, n, total, part):
    typ = q["type"]; ans = q["answer"]
    if typ == "tf": head = f'The answer is <b>{q["choices"][ans].upper()}</b>'
    else: head = f'<b>{L[ans]}</b> · {esc(q["choices"][ans])}'
    body = f'<div class="ansbar"><i>✓</i><span>{head}</span></div>'
    if typ in ("tf", "pair"):
        sts = [q["stem"]] if typ == "tf" else [re.sub(r"^\d\.\s*", "", s) for s in q["statements"]]
        truth = [ans == 0] if typ == "tf" else [[True, True], [False, False], [True, False], [False, True]][ans]
        body += '<div class="vcs">'
        for i, (s, ok) in enumerate(zip(sts, truth)):
            spec = a["s"][i]
            lab = "The statement" if typ == "tf" else f"Statement {i + 1}"
            note = f'<div class="vn">{esc(spec["n"])}</div>' if spec.get("n") else ""
            body += (f'<div class="vc {"T" if ok else "F"}"><div class="vh"><span>{lab}</span><b>{"TRUE" if ok else "FALSE"}</b>'
                     f'<em>{esc(spec.get("c", ""))}</em></div><div class="vt">{apply_ops(s, spec["o"])}</div>{note}</div>')
        body += "</div>"
    else:
        assert len(a["w"]) == len(q["choices"]), q["id"]
        body += '<div class="ws">' + "".join(
            f'<div class="wr{" right" if i == ans else ""}"><b>{L[i]}</b><span>{esc(c)}</span><span class="wv">{esc(a["w"][i])}</span></div>'
            for i, c in enumerate(q["choices"])) + "</div>"
    if a.get("tip"): body += f'<div class="tip"><span>URIBE</span>{esc(a["tip"])}</div>'
    return f'<div class="frame">{top(part, n, total)}<div class="xbody"><div class="fit">{body}</div></div></div>'
def title_frame(v, n):
    return (f'<div class="titlecard"><div class="tk">Persons and Family Relations · Atty. Uribe · Samplex Quiz</div><h1>{esc(v["title"].split(": ", 1)[1])}</h1>'
            f'<div class="tsub">{n} questions from Sir\'s past quizzes · {esc(v["range"].split(" · ")[0])}</div><div class="how">'
            f'<div><b>🎧</b>Listen<small>Question and choices, read aloud</small></div><div><b>{COUNT}</b>Answer<small>A {COUNT}-second countdown</small></div>'
            f'<div><b>✓</b>Reveal<small>The answer, highlighted</small></div><div><b>?</b>Why<small>The planted word or the rule</small></div></div></div>')
def divider_frame(part, n):
    p, name = part.split(" · ")
    return f'<div class="divider"><div class="tk">{esc(p)}</div><h1>{esc(name)}</h1><div class="rule"></div><p>{n} samplex question{"s" if n > 1 else ""}</p></div>'
def end_frame(v, n):
    return (f'<div class="divider"><div class="tk">That\'s all {n}</div><h1>How did you do?</h1><div class="rule"></div>'
            f'<p>Missed one? Find it in the Quiz bank (Samplex filter) and in the Reviewer.</p></div>')

def plan(work):
    B = bank()
    for v in VIDEOS:
        qs = [q for t in v["topics"] for q in B.values() if q["topic"] == t]
        qs.sort(key=lambda q: (v["topics"].index(q["topic"]), int(q["id"].split("-")[1])))
        total = len(qs); frames, segs = {}, []
        def F(fid, h): frames[fid] = h; return fid
        segs.append(dict(f=F("title", title_frame(v, total)), say=v["intro"], pad=0.8, ch="Introduction"))
        last = None
        for n, q in enumerate(qs, 1):
            a = Q[q["id"]]; part = PARTS[q["topic"]]
            if len(v["topics"]) > 1 and q["topic"] != last:
                cnt = sum(1 for x in qs if x["topic"] == q["topic"])
                p, name = part.split(" · ")
                segs.append(dict(f=F(f"div_{q['topic']}", divider_frame(part, cnt)), say=f"{p}: {name}.", pad=0.6, ch=f"{part}: Q{n} · {a['t']}"))
                ch = None
            else:
                ch = f"{part}: Q{n} · {a['t']}"
            last = q["topic"]
            pre = f"q{n:02d}"
            typ = q["type"]
            if typ == "tf":
                segs.append(dict(f=F(pre + "_r", qframe(q, n, total, part)), say=f"Question {n}. True or false? {q['stem']}", pad=0.4, ch=ch))
            elif typ == "pair":
                segs.append(dict(f=F(pre + "_r", qframe(q, n, total, part)), say=f"Question {n}. {q['stem']}", pad=0.3, ch=ch))
                for i, s in enumerate(q["statements"]):
                    segs.append(dict(f=F(f"{pre}_s{i}", qframe(q, n, total, part, ("s", i))),
                                     say=f"Statement {'one' if i == 0 else 'two'}. {re.sub(r'^\d\.\s*', '', s)}", pad=0.3))
                segs.append(dict(f=F(pre + "_c", qframe(q, n, total, part, ("all",))), say=PAIR_SAY, pad=0.4))
            else:
                segs.append(dict(f=F(pre + "_r", qframe(q, n, total, part)), say=f"Question {n}. {q['stem']}", pad=0.3, ch=ch))
                for i, c in enumerate(q["choices"]):
                    segs.append(dict(f=F(f"{pre}_c{i}", qframe(q, n, total, part, ("c", i))), say=f"{L[i]}: {c.rstrip('.:')}.", pad=0.25 if i + 1 < len(q["choices"]) else 0.4))
            for k in range(COUNT, 0, -1):
                segs.append(dict(f=F(f"{pre}_t{k}", qframe(q, n, total, part, mode="count", k=k)), sil=1.0, sfx="tick",
                                 stop=dict(q=n, n=len(q["choices"]), answer=q["answer"], labels=q["choices"] if typ == "tf" else list(L[:len(q["choices"])])) if k == COUNT else None))
            ansl = q["choices"][q["answer"]]
            say = (f"The answer is {ansl.lower()}." if typ == "tf" else
                   f"The answer is {L[q['answer']]}: {ansl[0].lower() + ansl[1:]}" + ("" if ansl.endswith(".") else ".") if typ == "pair" or len(ansl) < 70 else
                   f"The answer is {L[q['answer']]}.")
            segs.append(dict(f=F(pre + "_a", qframe(q, n, total, part, mode="reveal")), say=say, sfx="ding", pad=0.5))
            segs.append(dict(f=F(pre + "_x", xframe(q, a, n, total, part)), say=a["x"], pad=1.2))
        segs.append(dict(f=F("end", end_frame(v, total)), say=f"That's all {words(total)} questions. Count your score, and look up anything you missed in the quiz bank and the reviewer. Good luck in Sir's quiz.", pad=1.5, ch="End"))
        d = os.path.join(work, v["id"]); os.makedirs(d, exist_ok=True)
        json.dump([{"id": k, "html": h} for k, h in frames.items()], open(os.path.join(d, "frames.json"), "w"), ensure_ascii=False)
        json.dump(segs, open(os.path.join(d, "segs.json"), "w"), ensure_ascii=False, indent=0)
        print(v["id"], total, "questions,", len(frames), "frames,", len(segs), "segments")

def tts(work):
    import numpy as np, soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(work, "voice", "kokoro-v1.0.int8.onnx"), os.path.join(work, "voice", "voices-v1.0.bin"))
    cache = os.path.join(work, "audio"); os.makedirs(cache, exist_ok=True)
    for v in (VIDEOS[::-1] if os.environ.get("TTS_REVERSE") else VIDEOS):   # a second worker can start from the other end
        segs = json.load(open(os.path.join(work, v["id"], "segs.json")))
        for s in segs:
            if not s.get("say"): continue
            h = hashlib.sha1(s["say"].encode()).hexdigest()[:16]
            fn = os.path.join(cache, h + ".wav"); meta = fn[:-4] + ".json"
            if os.path.exists(meta): continue
            parts, subs, t = [], [], 0.0
            for disp in sents(s["say"]):
                a, sr = k.create(speak(disp), voice="af_heart", speed=1.02, lang="en-us")
                gap = np.zeros(int(SR * 0.16), dtype=np.float32)
                subs.append([round(t, 3), round(t + len(a) / SR, 3), disp])
                parts += [a.astype(np.float32), gap]; t += (len(a) + len(gap)) / SR
            sf.write(fn, np.concatenate(parts), SR)
            json.dump(subs, open(meta, "w"))
            print(v["id"], h, round(t, 1), flush=True)
    print("TTS DONE")

def render(work):
    for v in VIDEOS:
        subprocess.run(["node", os.path.join(H, "render_frames.js"), os.path.join(work, v["id"]), os.path.join(H, "quiz.css")], check=True)

def sfx(kind):
    import numpy as np
    t = np.arange(int(SR * (0.06 if kind == "tick" else 0.7))) / SR
    if kind == "tick": return (0.22 * np.sin(2 * np.pi * 1250 * t) * np.exp(-t * 70)).astype(np.float32)
    w = np.sin(2 * np.pi * 880 * t) * np.exp(-t * 6) + 0.7 * np.sin(2 * np.pi * 1320 * t) * np.exp(-np.maximum(0, t - 0.09) * 6) * (t > 0.09)
    return (0.28 * w).astype(np.float32)

def assemble(work):
    import numpy as np, soundfile as sf
    def ts(x):
        h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
        return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
    for v in VIDEOS:
        d = os.path.join(work, v["id"]); segs = json.load(open(os.path.join(d, "segs.json")))
        audio, lines, subs, chapters, stops, t = [], [], [], [], [], 0.0
        for s in segs:
            parts = []
            if s.get("sfx") == "ding": parts += [sfx("ding")[:int(SR * 0.45)]]
            if s.get("sfx") == "tick": parts += [sfx("tick")]
            lead = sum(len(p) for p in parts) / SR
            if s.get("say"):
                h = hashlib.sha1(s["say"].encode()).hexdigest()[:16]
                a, sr = sf.read(os.path.join(work, "audio", h + ".wav"), dtype="float32"); assert sr == SR
                for s0, s1, txt in json.load(open(os.path.join(work, "audio", h + ".json"))): subs.append((t + lead + s0, t + lead + s1, txt))
                parts += [a, np.zeros(int(SR * s.get("pad", 0.3)), dtype=np.float32)]
            else:
                parts += [np.zeros(int(SR * s["sil"]) - sum(len(p) for p in parts), dtype=np.float32)]
            seg = np.concatenate(parts); dur = len(seg) / SR
            if s.get("ch"): chapters.append((t, s["ch"]))
            if s.get("stop"): stops.append(dict(t=round(t, 2), **s["stop"]))
            lines.append(f"file 'frames/{s['f']}.png'\nduration {dur:.4f}")
            audio.append(seg); t += dur
        lines.append(f"file 'frames/{segs[-1]['f']}.png'")
        open(os.path.join(d, "list.txt"), "w").write("\n".join(lines) + "\n")
        full = np.concatenate(audio); full = full / max(1e-6, np.abs(full).max()) * 0.89
        sf.write(os.path.join(d, "full.wav"), full, SR)
        base = os.path.join(work, v["file"])
        with open(base + ".srt", "w") as f:
            for i, (a0, a1, txt) in enumerate(subs, 1): f.write(f"{i}\n{ts(a0)} --> {ts(a1)}\n{txt}\n\n")
        meta = lambda x: re.sub(r"([=;#\\])", r"\\\1", x)
        with open(os.path.join(d, "chapters.txt"), "w") as f:
            f.write(f";FFMETADATA1\ntitle={meta(v['title'])}\n")
            for i, (c0, name) in enumerate(chapters):
                c1 = chapters[i + 1][0] if i + 1 < len(chapters) else t
                f.write(f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(c0 * 1000)}\nEND={int(c1 * 1000)}\ntitle={meta(name)}\n")
        json.dump(stops, open(base + ".quiz.json", "w"), ensure_ascii=False)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "list.txt", "-i", "full.wav",
                        "-i", base + ".srt", "-i", "chapters.txt", "-map", "0:v", "-map", "1:a", "-map", "2:s", "-map_metadata", "3",
                        "-map_chapters", "3", "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "20",
                        "-pix_fmt", "yuv420p", "-vf", "fps=30,format=yuv420p", "-c:a", "aac", "-b:a", "128k", "-c:s", "mov_text",
                        "-metadata:s:s:0", "language=eng", "-movflags", "+faststart", "-shortest", base + ".mp4"], check=True, cwd=d)
        print(v["id"], f"{t / 60:.1f} min,", len(subs), "captions,", len(chapters), "chapters,", len(stops), "stops")

if __name__ == "__main__":
    {"plan": plan, "tts": tts, "render": render, "assemble": assemble}[sys.argv[1]](sys.argv[2])
