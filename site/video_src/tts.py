import json, re, os, numpy as np, soundfile as sf, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import SCENES
from kokoro_onnx import Kokoro
k = Kokoro("voice/kokoro-v1.0.int8.onnx", "voice/voices-v1.0.bin")
os.makedirs("audio", exist_ok=True)
SR = 24000
meta = []
def sents(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", t) if x.strip()]
for si, sc in enumerate(SCENES):
    for st, text in enumerate(sc["steps"]):
        fn = f"audio/s{si:02d}_{st}.wav"
        parts, subs, t = [], [], 0.0
        for s in sents(text):
            a, sr = k.create(s, voice="af_heart", speed=1.02, lang="en-us")
            gap = np.zeros(int(SR * 0.18), dtype=np.float32)
            subs.append([round(t, 3), round(t + len(a) / SR, 3), s])
            parts += [a.astype(np.float32), gap]
            t += (len(a) + len(gap)) / SR
        audio = np.concatenate(parts)
        sf.write(fn, audio, SR)
        meta.append({"scene": si, "step": st, "file": fn, "dur": len(audio) / SR, "subs": subs})
        print(si, st, round(len(audio) / SR, 1), flush=True)
json.dump(meta, open("audio/meta.json", "w"), indent=1)
print("DONE")
