# Lesson 4 · Learning from reference videos

The kit's defaults come from measuring big viral channels. Your niche may move differently: kitchen science shorts may
run 45 s, bedtime Fables may whisper at 3.5 words per second. The `study-references` skill measures the videos **you**
admire and turns them into a **style profile** the writing skills follow.

## The idea: measure, don't copy
Copying a creator's lines gets you nothing but a worse copy and a takedown. What transfers is **structure**: how long,
how fast, how short the sentences, what sentence 1 does, where the turn lands, how often the picture cuts, how it ends.
Those are numbers and shapes, and they're yours to use.

## 1. Collect a set
- Pick **10-30 shorts of one type** (Fact or Fable) that you'd love to have made. The most-viewed teach the most.
- Save them in `reference-videos/<fact|fable>/<set-name>/`. Use an alias for the set (`set-a`, `kitchen-science`),
  never the creator's name.
- If you can, add a transcript with the same file name (`.srt`, `.vtt`, `.txt`, or a `.json` with word timings): the
  text numbers become exact. Without one, the study transcribes locally.
- These clips are for your private study. The folder's `.gitignore` keeps them, and every measurement made from them,
  out of git, so they're never published by accident.

## 2. Run the study
Say: **"Study my reference videos."** Claude asks the type and the set name, then runs:
```bash
python3 .claude/skills/study-references/scripts/study.py reference-videos/fable/set-a --transcribe
```
(Requirements: ffmpeg; `pip install pillow` for the overview sheets; `pip install faster-whisper` for `--transcribe`.)

You get, per video: length, cuts and cuts in the first 6 s, median shot length, loudness, words per second, sentence
lengths, one-word sentences, how many sentences start with So/But/And/Then, where "you see" falls, I/you/he per 100
words, questions, plus a 1-frame-per-second overview sheet and frame 1. All of it private, in `_study/`.

## 3. Read the profile
Claude reads the numbers, the sheets and the sentences like an editor (format, hook type, beat map, ending, picture)
and writes `style-profiles/<type>-<set-name>.md`:
- **"Different from the kit defaults"**: the list to read first.
- Numbers next to the kit's defaults.
- Hook shapes with **newly written** examples, the beat map, language, picture, endings.

A profile never quotes the videos (no line over three words, no titles, no plots, no names), so it's safe to keep and
share.

## 4. Write with it
Next time you start a script, the writing skill lists your profiles: "Follow *fable-set-a* or the kit defaults?" Pick
the profile, and its pace, length, sentence length and picture notes override the defaults.

## Exercise
Make two sets of the same type from two channels you like, study both, and ask Claude: "Compare fable-set-a and
fable-set-b. What should I take from each?"
