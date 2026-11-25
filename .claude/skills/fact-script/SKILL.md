---
name: fact-script
description: Write a complete ~60-second Fact script for a faceless animated short (Reels, TikTok, YouTube Shorts) - a real mechanism, practice or true event told hook-first as a fast mini-story about an unnamed "he" - with the strange deed in sentence 1, So/But/Then escalation, a mystery question, the real mechanism ("Well," / "You see,") and a twist or visual payoff, every fact sourced. Also doctors drafts and pitches true-story topics. Use for true stories, science, history, "why does X happen", tricks people really use, weird laws, accidental inventions, or when the user says /fact-script or picks Fact in /short-script. For invented worlds and gags use fictional-script instead.
---

# Fact script writer

**Fact** = a real mechanism, practice or true event, told as a fast mini-story about someone else. (Its opposite in this
kit is **Fable**: an invented world with one impossible rule, told by a kid, in the `fictional-script` skill.)

You turn a true story or a real phenomenon into a ready-to-voice ~60 s script that follows the patterns measured on 53
viral animated explainer-story shorts. The craft is in `references/`. Read it before writing; don't write from memory.

| File | Read it when |
|---|---|
| `references/patterns.md` | Always, before the first draft: the beat shape, the three formats, hooks, truth rules, pace |
| `references/templates.md` | When drafting: the Fact story / event / explainer templates and the exact output format |
| `references/idea-engine.md` | When the user has no topic or a vague one: what travels, where to dig, deed hooks, pitch format |
| `references/checklist.md` | Before you show any draft: must-haves + a 100-point score; fix anything below the bar |
| `references/examples.md` | To see the bar: a worked Fact story with beat notes and sources |

## Step 0: Confirm the type (always first)
If the user came through `/short-script`, the type is already chosen: skip to Step 1. Otherwise, before anything else,
ask in one short message:

> "Two kinds of script here. **Fact**: a true story or a real piece of science, told as a mini-story ('He spun every egg
> in the diner before he cracked a single one'). **Fable**: an invented world with one impossible rule, told by a kid
> ('In my town, if you hum, flowers grow where you stand'). Which one?"

If they pick Fable, hand over to the `fictional-script` skill. If they're unsure, ask for the idea and recommend one:
something that really happens is a Fact; an invented rule is a Fable.

**Style profiles:** if `style-profiles/` has `fact-*.md` files (made by the `study-references` skill from the user's own
reference videos), name them and ask which one to follow, or the kit defaults. A chosen profile's numbers override
`references/patterns.md` where they differ.

## Step 1: Ask for the topic
One short question, not a form:

> "What's the story? A true event, a weird fact, a trick people really use, a 'why does X happen'. One line is enough.
> Or say 'pitch me' and I'll find a few."

If the first message already has a topic or a draft, skip this.

## Step 2a: They have a topic or a draft
1. **Research before writing.** List every claim in a facts table with a source and a confidence (high / medium / low),
   and mark every line **fact** or **dramatized** (`references/patterns.md`, "Truth"). Use web search when available. A
   fact short that gets a fact wrong gets corrected in the comments and loses trust. Unverifiable → flag it or cut it.
   **Jokes must be true details too.**
2. **Pick the format** (`references/templates.md`): **Fact story** by default (an unnamed "he" acts out the
   mechanism); **Fact event** for a documented event with a date and a place; **Fact explainer** ("If you …") for
   science with no person in it.
3. **Find the deed:** the one strange, dumb or mean-looking thing he did that the mechanism explains. That's sentence 1.
   Offer 3 hook versions, mark the one you recommend, and go ahead with it unless they pick another.
4. **Find the one mechanism** for the reveal, or let the payoff show it. An everyday analogy helps when it's abstract.
   If it needs three ideas, narrow the story.
5. **Draft** with the template, in its output format.
6. **Score** with `references/checklist.md`. Revise until every must-have passes and the score is 85 or more. Show the
   score card under the script.

For a draft: keep the user's idea and phrasing where they work. Diagnose with line numbers (late hook, setup before the
deed, narrating what's on screen, no "why", no payoff, too long), then give the tightened version.

## Step 2b: No topic → pitch
Up to 5 quick questions in one message (interests, audience, tone, no-go topics, a short they loved), or skip them if
the user just says "pitch me". Then give **6 pitches** with `references/idea-engine.md`, mixing veins (a trick people
really use, a body or science "why", an accident, a weird law, an invention, an "If you …" thought experiment). Score
each and recommend one.

## Step 3: Deliver
Use the output format in `references/templates.md`:
- title options and hook options
- logline
- the script by beat, with timestamps and word counts
- the facts and sources table (fact or dramatized per line)
- the hook shot list and shot notes (text props, the reveal insert, the big visual payoff)
- captions
- comment bait
- the score card

Then offer, in one line: a 35-45 s cut, 3 more hooks, an "Imagine you're …" second-person version, or a different
payoff.

## Hard rules
- **Sentence 1 = the deed or the paradox as plain fact.** No "did you know", no greeting, no "in this video", no
  question to the viewer, no call to action anywhere. The video ends on the last word.
- **True.** Every claim is sourced. Dramatize the *telling* (present tense, an unnamed everyman, short in-character
  lines), never the facts. A generic invented parable around a real mechanism is allowed when the reveal says what is
  real and the facts table marks those lines "dramatized".
- **Pace: 3.4-4.1 words/s (aim 3.7)**, Fact story 55-65 s / 200-245 words. Median sentence ~14 words with a long-short
  rhythm, no held pauses.
- **One mechanism**, revealed after a mystery question or shown by the payoff.
- **Never narrate what the viewer sees.** The picture shows the egg spinning; the voice says why it's strange.
- **Every sentence can be shown literally,** and props carry the jokes.
- **Original telling only.** Never reuse another creator's script, structure-for-structure retelling, titles or lines,
  and never name the creators whose videos were studied.
