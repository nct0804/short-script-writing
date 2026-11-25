# Short script writing

A Claude skill that writes viral short-video story scripts (Reels, TikTok, YouTube Shorts) for faceless animated channels. It's built from a study of the top 25 reels of an animated mini-story account (1.8M to 8.9M views).

## What it does

1. Asks for your idea. Anything works: one word, a "what if", a feeling, a character.
2. Turns it into an impossible world rule, picks a misfit narrator and a loved one, and writes the full script in 8 beats with timestamps and word counts.
3. Adds a shot list for the first 7 seconds, shot notes for the rest, caption style and a comment-bait loophole.
4. Scores the draft against a viral checklist and fixes weak spots before showing it.
5. No idea? Say "pitch me" and it gives 5 ideas with a recommendation.

Two formats: the long world-rule story (about 2 minutes, the format behind every top-5 hit) and the 36-second gag.

## Files

```
viral-short-script/
  SKILL.md                      the workflow Claude follows
  references/
    patterns.md                 8 beats, hook formulas, pacing, visuals, endings, titles
    templates.md                fill-in templates and the output format
    idea-engine.md              seed-to-rule method, pitch lenses, original idea seeds
    viral-checklist.md          must-haves and a 100-point score
    examples.md                 two original worked scripts (long + gag)
    source-clips.md             the 25 studied reels, paraphrased
```

## Install

- **Claude.ai / Claude app:** upload `viral-short-script.zip` (in this repo) under Settings → Capabilities → Skills, or save it from the proposal card in the project thread.
- **Claude Code:** copy `viral-short-script/` into `~/.claude/skills/` (or `.claude/skills/` in a project).

Then say something like "write me a short script" or "pitch me ideas for a short".

## Key numbers

- First sentence states the rule. Strangest image in frame 1.
- About 4.3 spoken words per second for long stories (450 to 600 words), 5.2 for gags (about 185 words).
- Comedy for the first 20 to 30 seconds, heart after.
- The last line echoes the first line or a ritual planted early.
