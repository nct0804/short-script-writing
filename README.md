# Fact & Fable · Short-video script kit for Claude

Write short-video scripts (Reels, TikTok, YouTube Shorts) the way the most-viewed faceless animated story channels do,
with Claude. Built by measuring what those channels actually do: how fast they talk, how long their sentences are,
what sentence 1 looks like, where the twist lands, how often they cut.

**Two script types, built as opposites:**

| | **Fact** | **Fable** |
|---|---|---|
| The idea | something real: a mechanism, a trick people use, a true event | something invented: a world with one impossible rule |
| Sentence 1 | the strange deed: *"He spun every egg in the diner before he cracked a single one."* | the rule: *"In my town, if you hum, flowers grow where you stand."* |
| Told by | an adult storyteller, about an unnamed "he" | a kid, in the first person |
| The hook asks | why would he do that? | what does this rule cost? |
| Ending | the real reason pays off on screen | the first line or a ritual returns, changed |
| Formats | Fact story (~60 s) · Fact event · Fact explainer | Fable story (~2 min, warm or eerie) · Fable gag (36 s) · moral Fables |
| Pace | 3.7 words/s | 4.3 words/s (gag 5.2) |

## What's inside
```
.claude/skills/
  short-script/         START HERE: asks Fact or Fable (and the format), then hands over
  fact-script/          writes Fact scripts: research, facts table, deed hooks, the reveal, a score card
  fictional-script/     writes Fable scripts: rule design, misfit + loved one, the turn, the callback; gags; moral stories
  study-references/     learns YOUR reference videos → a style profile the two writers follow
course/                 7 lessons: Fact vs Fable, writing each, learning from references, script → video, cheat sheets
samples/                one Fact and one Fable script, each animated into a finished vertical video
reference-videos/       drop your reference clips here (private: kept out of git automatically)
style-profiles/         what study-references learned (patterns only, safe to keep and share)
dist/                   one zip per skill, for Claude.ai
```

## Quick start
**Claude Code (everything, including the reference-video study):** open this folder in Claude Code and say
**"Write me a short script."** Claude asks *Fact or Fable?* first, then for your idea (or say *"pitch me"*).

**Claude.ai / the Claude app:** upload `dist/short-script.zip`, `dist/fact-script.zip` and `dist/fictional-script.zip` under
Settings → Capabilities → Skills, then ask for a short script.

**Every script comes with:** title options, the script beat by beat with timestamps and word counts, a shot list for
the first 7 seconds, shot notes, caption style and keywords, comment bait, and a score card. It's scored against the
type's checklist and shipped at 85/100 or more. Fact scripts add a facts-and-sources table, Fable scripts a world bible.

## Learn your own style
1. Put 10-30 clips you admire in `reference-videos/fact/<set-name>/` or `reference-videos/fable/<set-name>/`.
2. Say **"Study my reference videos."** You get their numbers (pace, sentence length, cut speed, hook and ending
   types, loudness) and a style profile in `style-profiles/`.
3. Next script: Claude offers to follow your profile instead of the kit defaults.

Reference clips stay private. The folder's own `.gitignore` keeps every video and every measurement out of git. Profiles
hold patterns in their own words, never quotes, titles or creator names.

## Samples
| | Script | Video |
|---|---|---|
| Fact story | *The Cook Who Spun Every Egg* (239 words, 92/100) | `samples/fact-the-cook-who-spun-every-egg/final.mp4` (66 s) |
| Fable gag | *My Crush's Laugh Grows Flowers* (182 words, 89/100) | `samples/fable-my-crushs-laugh-grows-flowers/final.mp4` (46 s) |

## The course
Start with [`course/00-start-here.md`](course/00-start-here.md):
1. Fact vs Fable
2. Writing a Fact script
3. Writing a Fable script (including moral Fables)
4. Learning from reference videos
5. From script to video
6. Cheat sheets

## Principles
- **Sentence 1 is the whole hook.** The deed (Fact) or the rule (Fable). No intro, no "did you know", no call to action.
- **Measured, not guessed.** Every number comes from measured viral videos, or from your own references.
- **Original work only.** The kit learns patterns, never lines. It never copies another creator's lines, titles, plots
  or characters, and never names the creators whose videos were studied.
- **True means sourced.** Fact scripts carry a source for every claim and mark invented framing as "dramatized".

## Upgrading from `viral-short-script`
The earlier single skill is now `fictional-script` (same craft, re-measured numbers, an eerie variant, original examples
throughout). Remove `viral-short-script` from your skills and install the four skills above.
