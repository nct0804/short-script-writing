#!/usr/bin/env python3
"""Measure a set of reference videos the same way every time, for private style study.

    python3 study.py reference-videos/<fact|fable>/<set-name> [--transcribe] [--model small.en] [--scene 0.35]

Reads every video in the set folder (.mp4 .mov .webm .mkv .m4v). For words it uses, in this order:
  1. a transcript you put next to the video with the same name: .json (word timings), .srt, .vtt or .txt
  2. --transcribe: local speech-to-text with faster-whisper (pip install faster-whisper; downloads a model once)
  3. nothing: picture and sound numbers only

Writes everything into <set>/_study/ (PRIVATE: it holds transcripts and frames of someone else's videos; the
reference-videos folder keeps it out of git):
  summary.md / summary.json    per-video numbers + medians (what the style profile is built from)
  videos/<name>/first.jpg      frame 1 (the hook image)
  videos/<name>/cuts.json      hard-cut times
  videos/<name>/transcript.json, sentences.txt   when words were available
  overview/<name>.jpg          1 frame per second, 12 per row, with timestamps (needs Pillow: pip install pillow)

Needs ffmpeg + ffprobe on the PATH. Standard library otherwise.
"""
import argparse
import json
import math
import os
import re
import statistics as st
import subprocess
import sys
import tempfile

VID_EXT = (".mp4", ".mov", ".webm", ".mkv", ".m4v")
CONNECTORS = ("so", "but", "and", "then", "well")


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(path):
    r = run("ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
            "stream=width,height,r_frame_rate:format=duration", "-of", "json", path)
    d = json.loads(r.stdout or "{}")
    s = (d.get("streams") or [{}])[0]
    num, den = (s.get("r_frame_rate") or "30/1").split("/")
    return float(d["format"]["duration"]), s.get("width"), s.get("height"), float(num) / max(float(den), 1)


def hard_cuts(path, thr):
    r = run("ffmpeg", "-hide_banner", "-i", path, "-vf", f"select='gt(scene,{thr})',showinfo", "-an", "-f", "null", "-")
    return [round(float(t), 3) for t in re.findall(r"pts_time:([0-9.]+)", r.stderr)]


def loudness(path):
    r = run("ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128", "-f", "null", "-")
    i = re.findall(r"I:\s+(-?[0-9.]+) LUFS", r.stderr)
    lra = re.findall(r"LRA:\s+([0-9.]+) LU", r.stderr)
    return (float(i[-1]) if i else None), (float(lra[-1]) if lra else None)


def first_frame(path, out_dir):
    run("ffmpeg", "-v", "error", "-y", "-i", path, "-frames:v", "1", os.path.join(out_dir, "first.jpg"))


def overview(path, out_jpg, tile_w=110, cols=12):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return False
    with tempfile.TemporaryDirectory() as td:
        run("ffmpeg", "-v", "error", "-y", "-i", path, "-vf", f"fps=1,scale={tile_w}:-2", "-q:v", "4",
            os.path.join(td, "f_%04d.jpg"))
        frames = sorted(os.listdir(td))
        if not frames:
            return False
        th = Image.open(os.path.join(td, frames[0])).size[1]
        sheet = Image.new("RGB", (cols * tile_w, math.ceil(len(frames) / cols) * th), "black")
        d = ImageDraw.Draw(sheet)
        for i, f in enumerate(frames):
            x, y = (i % cols) * tile_w, (i // cols) * th
            sheet.paste(Image.open(os.path.join(td, f)), (x, y))
            d.rectangle((x, y, x + 30, y + 12), fill="black")
            d.text((x + 2, y), f"{i // 60}:{i % 60:02d}", fill="white")
        os.makedirs(os.path.dirname(out_jpg), exist_ok=True)
        sheet.save(out_jpg, quality=80)
    return True


# ---------------------------------------------------------------- words
def _ts(t):
    h, m, s = t.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def load_sidecar(video_path):
    """word list [{w, s, e}] from a transcript next to the video; (words, has_timings)"""
    base = os.path.splitext(video_path)[0]
    if os.path.exists(base + ".json"):
        d = json.load(open(base + ".json", encoding="utf-8"))
        items = d.get("words", d) if isinstance(d, dict) else d
        out = []
        for it in items:
            if it.get("type") in ("spacing", "audio_event"):
                continue
            w = (it.get("w") or it.get("word") or it.get("text") or "").strip()
            if w:
                out.append({"w": w, "s": float(it.get("s", it.get("start", 0))), "e": float(it.get("e", it.get("end", 0)))})
        return out, True
    for ext in (".srt", ".vtt"):
        if os.path.exists(base + ext):
            txt = open(base + ext, encoding="utf-8").read()
            out = []
            for a, b, body in re.findall(r"(\d+:\d+:\d+[.,]\d+)\s+-->\s+(\d+:\d+:\d+[.,]\d+)[^\n]*\n(.*?)(?:\n\s*\n|\Z)", txt, re.S):
                s, e = _ts(a), _ts(b)
                ws = re.sub(r"<[^>]+>", "", body).split()
                for k, w in enumerate(ws):  # spread the cue's words evenly over its time
                    out.append({"w": w, "s": round(s + (e - s) * k / len(ws), 3), "e": round(s + (e - s) * (k + 1) / len(ws), 3)})
            return out, True
    if os.path.exists(base + ".txt"):
        return [{"w": w, "s": None, "e": None} for w in open(base + ".txt", encoding="utf-8").read().split()], False
    return [], False


def transcribe(path, model_name):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("--transcribe needs faster-whisper: pip install faster-whisper (or put a .srt/.vtt/.json/.txt next to each video)")
    model = WhisperModel(model_name, compute_type="int8")
    segs, _ = model.transcribe(path, word_timestamps=True, vad_filter=True)
    return [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for s in segs for w in (s.words or [])]


def text_stats(words, dur, timed):
    if not words:
        return {}
    text = " ".join(w["w"] for w in words)
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    lens = [len(s.split()) for s in sents]
    toks = re.findall(r"[a-z']+", text.lower())
    n = max(1, len(toks))
    cnt = lambda *ws: sum(toks.count(w) for w in ws)
    starts = [re.sub(r"[^a-z]", "", s.split()[0].lower()) for s in sents if s.split()]
    span = (words[-1]["e"] - words[0]["s"]) if timed else dur
    gaps = [b["s"] - a["e"] for a, b in zip(words, words[1:])] if timed else []
    you_see = None
    for i in range(len(words) - 1):
        if re.sub(r"[^a-z]", "", words[i]["w"].lower()) == "you" and re.sub(r"[^a-z]", "", words[i + 1]["w"].lower()) == "see":
            you_see = round((words[i]["s"] - words[0]["s"]) / span, 2) if timed else round(i / len(words), 2)
            break
    return {
        "words": len(words),
        "wps": round(len(words) / span, 2) if span else None,
        "sentences": len(sents),
        "median_sentence_words": st.median(lens) if lens else None,
        "one_word_sentences": sum(1 for x in lens if x <= 2),
        "sentences_20plus": sum(1 for x in lens if x >= 20),
        "first_sentence_words": lens[0] if lens else None,
        "connector_starts_pct": round(100 * sum(1 for s in starts if s in CONNECTORS) / max(1, len(starts))),
        "you_see_at": you_see,
        "I_per100": round(100 * cnt("i", "my", "me", "i'm", "i've", "i'd") / n, 1),
        "you_per100": round(100 * cnt("you", "your", "you're", "you'd", "you'll") / n, 1),
        "he_she_per100": round(100 * cnt("he", "she", "his", "her", "he's", "she's", "they", "their") / n, 1),
        "questions": text.count("?"),
        "pauses_over_0.25s": round(sum(g for g in gaps if g > 0.25), 2) if gaps else None,
        "_first_sentence": sents[0] if sents else "",
        "_last_sentence": sents[-1] if sents else "",
        "_sentences": sents,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("set_dir", help="reference-videos/<fact|fable>/<set-name>")
    ap.add_argument("--transcribe", action="store_true", help="local speech-to-text (faster-whisper) when no transcript sits next to a video")
    ap.add_argument("--model", default="small.en", help="faster-whisper model (default small.en)")
    ap.add_argument("--scene", type=float, default=0.35, help="scene-change threshold for hard cuts (default 0.35)")
    ap.add_argument("--no-sheets", action="store_true", help="skip the 1-fps overview sheets")
    a = ap.parse_args()

    vids = sorted(f for f in os.listdir(a.set_dir) if f.lower().endswith(VID_EXT)) if os.path.isdir(a.set_dir) else []
    if not vids:
        sys.exit(f"no videos in {a.set_dir} (supported: {', '.join(VID_EXT)})")
    study = os.path.join(a.set_dir, "_study")
    rows = []
    for f in vids:
        path, name = os.path.join(a.set_dir, f), os.path.splitext(f)[0]
        out = os.path.join(study, "videos", name)
        os.makedirs(out, exist_ok=True)
        dur, w, h, fps = probe(path)
        cuts = hard_cuts(path, a.scene)
        json.dump(cuts, open(os.path.join(out, "cuts.json"), "w"))
        shots = [b - x for x, b in zip([0.0] + cuts, cuts + [dur])]
        lufs, lra = loudness(path)
        first_frame(path, out)
        if not a.no_sheets:
            overview(path, os.path.join(study, "overview", name + ".jpg"))
        words, timed = load_sidecar(path)
        src = "sidecar" if words else None
        if not words and a.transcribe:
            words, timed, src = transcribe(path, a.model), True, "whisper"
        row = {"video": f, "duration": round(dur, 2), "size": f"{w}x{h}", "fps": round(fps, 2), "cuts": len(cuts),
               "cuts_per_10s": round(10 * len(cuts) / dur, 2), "cuts_first_6s": sum(1 for t in cuts if t < 6),
               "median_shot_s": round(st.median(shots), 2), "lufs": lufs, "lra": lra, "words_from": src or "none"}
        ts = text_stats(words, dur, timed)
        if words:
            json.dump(words, open(os.path.join(out, "transcript.json"), "w"), indent=1)
            open(os.path.join(out, "sentences.txt"), "w").write("\n".join(ts.pop("_sentences")) + "\n")
        row.update(ts)
        rows.append(row)
        print(f"{f}: {row['duration']} s, {row['cuts']} cuts ({row['cuts_first_6s']} in the first 6 s), {lufs} LUFS"
              + (f", {row.get('words')} words, {row.get('wps')} w/s" if words else ", no words"))

    json.dump(rows, open(os.path.join(study, "summary.json"), "w"), indent=1)
    cols = ["video", "duration", "cuts", "cuts_per_10s", "cuts_first_6s", "median_shot_s", "lufs", "lra"]
    tcols = ["words", "wps", "sentences", "median_sentence_words", "one_word_sentences", "sentences_20plus",
             "first_sentence_words", "connector_starts_pct", "you_see_at", "I_per100", "you_per100", "he_she_per100",
             "questions", "pauses_over_0.25s"]
    has_text = any(r.get("words") for r in rows)
    show = cols + (tcols if has_text else [])
    num = lambda k: [r[k] for r in rows if isinstance(r.get(k), (int, float))]
    L = [f"# Study: {os.path.normpath(a.set_dir)} ({len(rows)} videos)", "",
         "Private working file (it names the videos). The shareable result is the style profile in style-profiles/.", "",
         "| " + " | ".join(show) + " |", "|" + "---|" * len(show)]
    L += ["| " + " | ".join(str(r.get(k, "")) for k in show) + " |" for r in rows]
    L += ["", "## Medians", ""] + [f"- {k}: {st.median(num(k))}" for k in show[1:] if num(k)]
    if has_text:
        L += ["", "## First and last sentences (private: for spotting hook and ending TYPES, never to copy)", ""]
        L += [f"- {r['video']}: first “{r.get('_first_sentence', '')}” · last “{r.get('_last_sentence', '')}”" for r in rows if r.get("words")]
    open(os.path.join(study, "summary.md"), "w").write("\n".join(L) + "\n")
    print("wrote", os.path.join(study, "summary.md"))


if __name__ == "__main__":
    main()
