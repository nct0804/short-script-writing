# Reference videos (private)

Put the short videos you want to learn from here, one folder per set:

```
reference-videos/
  fact/<set-name>/     true stories, real science, tricks people use (Fact)
  fable/<set-name>/    invented worlds with one impossible rule, crush gags (Fable)
```

- **Set names are aliases** (`set-a`, `kitchen-science`, `bedtime-eerie`), never the creator's name or handle.
- **10-30 clips per set** is a good size. The most-viewed ones teach the most.
- **Transcripts help:** a `.srt`, `.vtt`, `.json` (word timings) or `.txt` with the same name as the video makes the
  text numbers exact. Without one, the study can transcribe locally (`--transcribe`).
- Then ask Claude: **"study my reference videos"** (the `study-references` skill). It writes the measurements into
  `<set>/_study/` here and a **style profile** into `../style-profiles/`.

**Private by design.** These are other people's videos: use them for your own study, don't re-upload or share them.
This folder's `.gitignore` keeps every clip and every `_study/` folder out of git, so you can't publish them by
accident. Only the style profiles (patterns in your own words) are meant to be kept and shared.
