---
name: short-script
description: Start here for any short-video script (Reels, TikTok, YouTube Shorts, faceless animated channels). Asks first which kind of script the user wants - Fact (a true story or real science told as a fast mini-story) or Fiction (an invented world with one impossible rule, told by a kid; a 2-minute story or a 36-second gag) - then hands over to the fact-script or fictional-script skill. Use whenever the user wants to write, improve or brainstorm a short script and hasn't picked a type, says "write me a short", "script for a reel", "pitch me", "help me with a TikTok script", or /short-script.
---

# Short script: start here

This kit writes two kinds of short-video script. They are opposites by design, so they never blur into each other:

| | **Fact** | **Fiction** |
|---|---|---|
| What it is | something real: a mechanism, a trick people use, a true event | something invented: a world with one impossible rule |
| Who tells it | an adult storyteller, about an unnamed "he" | a kid (7-12), in the first person: "In my town …" |
| Sentence 1 | the strange deed: "He spun every egg in the diner before he cracked a single one." | the rule: "In my town, if you hum, flowers grow where you stand." |
| Engine | why would he do that? → the real reason | what does the rule cost? → who it hurts, who saves them |
| Ending | a twist or a visual payoff that shows the mechanism | a callback to the first line or a ritual (warm), a sting (eerie), a flip (gag) |
| Formats | Fact story (~60 s), Fact event, Fact explainer | Fiction story (~2 min, warm or eerie), Fiction gag (36 s) |
| Pace | 3.7 words/s, sentences ~14 words | 4.3 words/s (gag 5.2), sentences ~6 words |
| Truth | every fact sourced; invented framing marked "dramatized" | fully invented, but original |
| Skill | `fact-script` | `fictional-script` |

## Step 1: Ask which kind (always, before anything else)
Even if the user already gave an idea, confirm the type first, in one short message with no form:

> "Which kind of script?
> **Fact**: a true story or a real piece of science, told as a quick mini-story ('He spun every egg in the diner
> before he cracked a single one'). About 60 s.
> **Fiction**: an invented world with one impossible rule, told by a kid ('In my town, if you hum, flowers grow where you
> stand'). A 2-minute story, or a 36-second gag.
> Not sure? Tell me the idea and I'll recommend one."

Skip the question only when the user's own words already chose ("a fact script about …", "a fiction gag about …").

**If they're unsure,** recommend in one line:
- it really happens, or it's science, history, a trick, a "why does X" → **Fact**
- it's a "what if", a magic rule, a feeling turned into a law, a crush joke → **Fiction** (a crush or a joke → the gag;
  anything with a family heart → the story)

**For Fiction, also ask the format** in the same message if it isn't clear: a 2-minute story or a 36-second gag.

**Style profiles:** if `style-profiles/` has profiles for the chosen type (made by `study-references` from the user's own
reference videos), mention them and ask whether to follow one or the kit defaults.

## Step 2: Hand over
- **Fact** → use the `fact-script` skill (start at its Step 1: the type is already chosen).
- **Fiction** → use the `fictional-script` skill with the chosen format (start at its Step 1).

If your setup can't call another skill, read its `SKILL.md` and follow it from Step 1.

## Other things the user may want
- **Learn from reference videos** ("study these clips", "what makes this channel work", "make my style profile") → the
  `study-references` skill. It measures the videos in `reference-videos/` and writes a style profile the two writing
  skills can follow.
- **Turn a finished script into a video** → `course/05-from-script-to-video.md` (voice pace, captions, shot list).

## Rules that apply to both
- Sentence 1 is the premise (Fiction) or the deed (Fact). Nothing before it, no call to action anywhere.
- Every script is scored with its checklist and shipped at 85+.
- Original work only: patterns, never another creator's lines, titles, plots or characters, and never the names of the
  creators whose videos were studied.
