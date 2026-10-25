import json, os, subprocess, numpy as np, soundfile as sf
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
meta = json.load(open("audio/meta.json"))
scenes = json.load(open("scenes.json"))
SR = 24000
PAD, SCENE_PAD, LEAD = 0.35, 0.9, 0.6
audio, lines, subs, chapters = [], [], [], []
t = 0.0
def sil(sec): return np.zeros(int(round(sec * SR)), dtype=np.float32)
audio.append(sil(LEAD)); t += LEAD
first_frame = None
for i, m in enumerate(meta):
    last_in_scene = (i + 1 == len(meta)) or meta[i + 1]["scene"] != m["scene"]
    a, sr = sf.read(m["file"], dtype="float32"); assert sr == SR
    pad = SCENE_PAD if last_in_scene else PAD
    seg = len(a) / SR + pad
    if m["step"] == 0:
        sc = scenes[m["scene"]]
        chapters.append((t, (sc["kicker"] + ": " + sc["title"]) if sc["title"] else "Introduction"))
    for s0, s1, txt in m["subs"]:
        subs.append((t + s0, t + s1, txt))
    frame = f"frames/s{m['scene']:02d}_{m['step']}.png"
    if first_frame is None:
        first_frame = frame
        lines.append(f"file '{frame}'\nduration {LEAD + seg:.3f}")
    else:
        lines.append(f"file '{frame}'\nduration {seg:.3f}")
    audio += [a, sil(pad)]; t += seg
lines.append(f"file 'frames/s{meta[-1]['scene']:02d}_{meta[-1]['step']}.png'")
open("list.txt", "w").write("\n".join(lines) + "\n")
full = np.concatenate(audio)
# gentle loudness normalization (peak ~ -1 dBFS)
full = full / max(1e-6, np.abs(full).max()) * 0.89
sf.write("full.wav", full, SR)
total = len(full) / SR

def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
with open("Family_FamilyHome_Paternity_Explainer.srt", "w") as f:
    for k, (a0, a1, txt) in enumerate(subs, 1):
        # wrap long captions into two lines
        words, l1 = txt.split(), []
        f.write(f"{k}\n{ts(a0)} --> {ts(a1)}\n{txt}\n\n")
with open("chapters.txt", "w") as f:
    f.write(";FFMETADATA1\ntitle=The Family, the Family Home, and Paternity & Filiation (FC 149-182)\n")
    for k, (c0, name) in enumerate(chapters):
        c1 = chapters[k + 1][0] if k + 1 < len(chapters) else total
        f.write(f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(c0*1000)}\nEND={int(c1*1000)}\ntitle={name}\n")
out = "Family_FamilyHome_Paternity_Explainer.mp4"
cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "list.txt", "-i", "full.wav",
       "-i", "Family_FamilyHome_Paternity_Explainer.srt", "-i", "chapters.txt",
       "-map", "0:v", "-map", "1:a", "-map", "2:s", "-map_metadata", "3", "-map_chapters", "3",
       "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30",
       "-vf", "fps=30,format=yuv420p", "-c:a", "aac", "-b:a", "160k", "-c:s", "mov_text",
       "-metadata:s:s:0", "language=eng", "-movflags", "+faststart", "-shortest", out]
subprocess.run(cmd, check=True)
print(f"done {total/60:.1f} min, {len(subs)} captions, {len(chapters)} chapters")
