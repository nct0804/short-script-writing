---
name: study-references
description: Learn the patterns of short videos the user admires - measure the reference clips they put in reference-videos/ (length, words per second, sentence length, hooks, beat structure, cut speed, captions, loudness, endings) and turn them into a style profile in style-profiles/ that the fact-script and fable-script skills follow. Patterns only, never copied lines. Use when the user says "study these clips", "analyze my reference videos", "learn this style", "what makes these videos work", "make a style profile", or /study-references.
---

# Study reference videos → a style profile

The writing skills ship with patterns measured on large viral channels. This skill lets the user measure **their own**
references, so the scripts follow the style they want. The output is a **style profile**: numbers and structures in your
own words, never the source's lines.

```
reference-videos/<fact|fable>/<set-name>/*.mp4   the user's clips (private, never committed)
            └── _study/                          the measurements (private: transcripts and frames)
style-profiles/<fact|fable>-<set-name>.md         the result (shareable: patterns only)
```

## Step 1: Ask before measuring (always)
In one short message:
1. **Which type are these clips: Fact or Fable?** Fact = true stories or real science told as mini-stories; Fable =
   invented worlds with one impossible rule, told by a kid. (Mixed folder? Ask to split it into two sets.)
2. **A set name:** a neutral alias like `set-a` or `kitchen-science`. **Never the creator's name or handle**, because the
   profile may be shared or sold.
3. **Where are the clips?** They go in `reference-videos/<type>/<set-name>/`. 10-30 clips is a good set; the most-viewed
   ones teach the most. A transcript with the same name (.srt, .vtt, .json with word timings, or .txt) makes the text
   numbers exact; without one, `--transcribe` runs speech-to-text locally.
4. A one-line reminder: the clips are for **private study** only. Don't re-upload or share them; the folder keeps them
   out of git.

## Step 2: Measure
```bash
python3 .claude/skills/study-references/scripts/study.py reference-videos/<type>/<set-name> [--transcribe]
```
Needs ffmpeg; Pillow for the overview sheets; `pip install faster-whisper` for `--transcribe` (it downloads a speech
model the first time). It prints one line per video and writes `_study/summary.md` (per-video numbers + medians),
`_study/overview/*.jpg` (1 frame per second) and per-video `first.jpg`, `cuts.json`, `transcript.json`,
`sentences.txt`.

## Step 3: Read like an editor
Read `_study/summary.md`, look at every overview sheet and first frame, and read the sentence files. For each video,
note in your working notes (not in the profile):
- **Format** (Fact: story / event / explainer; Fable: story warm / story eerie / gag) and length
- **Hook type**: the shape of sentence 1 (compare with the hook tables in `fact-script` / `fable-script`
  `references/patterns.md`)
- **Beat map**: where the setup, escalation, mystery or turn, reveal or sacrifice, and ending fall (seconds)
- **Ending type**, and whether the video ends on the last word
- **Picture**: frame 1, cut speed in the first 6 s, text props, the look (bright / cinematic), caption style and position
- **What the top performers share** that the others don't (if the user has view counts, rank by them)

## Step 4: Write the style profile
Fill `references/profile-template.md` and save it as `style-profiles/<type>-<set-name>.md`.
- **Numbers** come from the summary medians and ranges.
- **Patterns** are written in your own words: shapes with placeholders ("He [did the strange thing].", "In my town,
  if you [everyday action], [magic result].").
- **Examples must be newly written** by you. Never quote the videos: no line longer than three words, no titles, no
  character names, no plots. Describe the type of thing instead ("a deadpan one-word jab after the run-on sentence").
- **No creator names, handles, links or view counts per video** in the profile. Aggregate numbers are fine ("views
  ranged 1M-9M").
- Add a short **"Different from the kit defaults"** list: where this set's numbers or shapes differ from the writing
  skill's `references/patterns.md`. That list is what the user should know first.

## Step 5: Hand over
Show the user the "Different from the kit defaults" list and three ready-to-use hook shapes from the profile. Say that
`fact-script` / `fable-script` will offer the profile at the start of the next script. Offer to write a first script in
this style now (hand over to `short-script` with the type already chosen).

## Rules
- Patterns, never content: structure, pace, beat timing, hook and ending types, picture habits.
- The clips and `_study/` stay private and out of git (the `reference-videos/.gitignore` handles it). Only
  `style-profiles/` is meant to be kept and shared.
- Never name the studied creators in a profile, a script, a title or a caption.
