"""Make the web copies of the explainer videos and their data for the Videos tab.

  python3 video_src/publish_media.py <id> <title> <range> <source.mp4> <source.srt> [<id> ...]

Writes build/media/<id>.mp4 (720p, 5 fps, long keyframe interval, 48 kbps mono AAC:
about 70 kbps in total, so a 25-minute video stays under the 15 MB per-file publish limit),
build/media/<id>.vtt and build/media/<id>.jpg, and data/videos.json (chapters are read
from the source file's chapter markers).
"""
import json, os, re, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(H)
MEDIA = os.path.join(ROOT, "build", "media")
def _sec(t):
    h, m, r = t.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(r)
def _ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"
def srt_to_vtt(srt, maxw=12):
    """WebVTT with long cues split into chunks of about maxw words, timed by word count."""
    out = ["WEBVTT", ""]
    for block in re.split(r"\n\s*\n", srt.strip()):
        lines = block.strip().split("\n")
        a, b = [x.strip() for x in lines[1].split("-->")]
        words = " ".join(lines[2:]).split()
        t0, t1 = _sec(a), _sec(b)
        n = max(1, -(-len(words) // maxw)); size = -(-len(words) // n)
        chunks = [words[k:k + size] for k in range(0, len(words), size)]
        t = t0
        for ch in chunks:
            d = (t1 - t0) * len(ch) / len(words)
            out += [f"{_ts(t)} --> {_ts(t + d)}", " ".join(ch), ""]
            t += d
    return "\n".join(out)

def main(args):
    assert args and len(args) % 5 == 0, __doc__
    os.makedirs(MEDIA, exist_ok=True)
    out = []
    for i in range(0, len(args), 5):
        vid, title, rng, src, srt = args[i:i + 5]
        mp4 = os.path.join(MEDIA, vid + ".mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-map", "0:v", "-map", "0:a", "-map_chapters", "-1",
                        "-vf", "fps=5,scale=1280:720:flags=lanczos", "-c:v", "libx264", "-preset", "veryslow", "-tune", "stillimage",
                        "-crf", "21", "-pix_fmt", "yuv420p", "-g", "600", "-c:a", "aac", "-b:a", "48k", "-ac", "1", "-ar", "24000",
                        "-movflags", "+faststart", mp4], check=True)
        assert os.path.getsize(mp4) < 15_000_000, f"{mp4} is over 15 MB"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "2", "-i", src, "-frames:v", "1", "-vf", "scale=1280:720", "-q:v", "4",
                        os.path.join(MEDIA, vid + ".jpg")], check=True)
        open(os.path.join(MEDIA, vid + ".vtt"), "w").write(srt_to_vtt(open(srt).read()))
        pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_chapters", "-show_format", "-of", "json", src],
                                       capture_output=True, text=True, check=True).stdout)
        chapters = []
        for c in pr["chapters"]:
            name = c["tags"]["title"]
            part, _, t = name.partition(": ") if ": " in name else ("", "", name)
            chapters.append({"t": round(float(c["start_time"]), 2), "part": part, "title": t or name})
        out.append({"id": vid, "title": title, "range": rng, "src": f"media/{vid}.mp4", "vtt": f"media/{vid}.vtt",
                    "poster": f"media/{vid}.jpg", "duration": round(float(pr["format"]["duration"]), 1), "chapters": chapters})
        print(vid, os.path.getsize(mp4), "bytes,", len(chapters), "chapters")
    json.dump(out, open(os.path.join(ROOT, "data", "videos.json"), "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1:])
