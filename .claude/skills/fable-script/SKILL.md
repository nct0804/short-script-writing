---
name: fable-script
description: Write a complete Fable script for a faceless animated short (Reels, TikTok, YouTube Shorts) - an invented world with one impossible rule, told by a kid in the first person - as a 2-minute Fable story (warm or eerie) or a 36-second Fable gag, from the user's idea however small, or pitch ideas when they have none. Use for "what if" stories, magic rules, invented worlds, crush gags, or when the user says /fable-script or picks Fable in /short-script. For true stories and real science use fact-script instead.
---

# Fable script writer

**Fable** = an invented world with one impossible rule, told by a kid who doesn't fit it. (Its opposite in this kit is
**Fact**: a real mechanism or true event, told about someone else, in the `fact-script` skill.)

You turn a seed (a word, a "what if", a feeling, a half-plot) into a finished, ready-to-voice script that follows the
patterns measured on the most-viewed animated mini-story reels. The craft is in `references/`. Read it before
writing; don't write from memory.

| File | Read it when |
|---|---|
| `references/patterns.md` | Always, before the first draft: the beats, hook formulas, pacing, picture, endings, titles |
| `references/templates.md` | When drafting: the warm, eerie and gag templates and the exact output format |
| `references/idea-engine.md` | When the user has no idea, or a vague one: seed → rule, the four tests, pitch lenses, idea seeds |
| `references/checklist.md` | Before you show any draft: must-haves + a 100-point score; fix anything below the bar |
| `references/examples.md` | To see the bar: a warm story and two gags, with notes |

## Step 0: Confirm the type and the format (always first)
If the user came through `/short-script`, the type is already chosen: skip to Step 1. Otherwise, before anything else,
ask in one short message:

> "Two kinds of script here. **Fable**: an invented world with one impossible rule, told by a kid ('In my town, if
> you hum, flowers grow where you stand'). **Fact**: a true story or a real piece of science, told as a mini-story
> ('He spun every egg in the diner before he cracked a single one'). Which one?
> And for a Fable: a **2-minute story** or a **36-second gag**?"

If they pick Fact, hand over to the `fact-script` skill. If they're unsure, ask for the idea and recommend one: an
invented rule is a Fable; something that really happens is a Fact.

**Style profiles:** if `style-profiles/` has `fable-*.md` files (made by the `study-references` skill from the user's
own reference videos), name them and ask which one to follow, or the kit defaults. A chosen profile's numbers
(pace, length, sentence length, cut speed, captions) override `references/patterns.md` where they differ.

## Step 1: Ask for the idea
One short question, not a form:

> "Do you have an idea? Anything works: a single word, a weird 'what if', a feeling, a character, a scene you can
> picture. No idea yet? Say 'pitch me' and I'll give you five."

If the first message already has an idea, skip this.

## Step 2a: They have an idea → develop it
1. **Find the rule** with `references/idea-engine.md` ("Turning a seed into a rule"). A good rule is an **everyday
   action**, with a **visible consequence** you can show in frame 1, a **price**, and one **loophole** viewers will argue
   about.
2. **Offer 2-3 rule versions** of their seed in one line each, mark the one you recommend and why, and go ahead with it
   unless they pick another. If they said "just write it", write it with your pick.
3. **Pick the variant** (stories): **warm** (classic 8 beats: funny, warm, bittersweet) or **eerie** (crisis-first:
   eerie, epic, present tense). Gags have one shape.
4. **Pick the heart** (stories): a kid narrator (7-12) who doesn't fit the rule, plus a loved one with a ritual (a
   little sibling, a grandparent, a parent). The misfit trait must become the solution.
5. **Draft the full script** with the matching template in `references/templates.md`, in its output format.
6. **Score it** with `references/checklist.md`. Revise until every must-have passes and the score is 85 or more. Show
   the score card under the script.

Keep the user's idea recognisable. Improve it; don't replace it. If their seed is a romance or a joke, the gag may fit
better: say so and offer both.

## Step 2b: No idea → pitch
1. Generate **5 ideas** with `references/idea-engine.md`: at least 3 stories (one warm, one bittersweet, one eerie) and
   1-2 gags, each from a different lens.
2. For each: a **post title**, the **first line**, the **heart** in one sentence (narrator flaw + loved one), the **turn**
   in one sentence.
3. **Recommend one** in one line (strongest frame-1 image, clearest rule, best twist), and let them pick or combine.

## Step 3: Deliver
Use the output format in `references/templates.md`:
1. Title options (3) and the recommended one
2. Logline
3. The script beat by beat, with timestamps and word counts
4. The world bible (rule, price, loophole, misfit, ritual, plants → payoffs)
5. The hook shot list (first 7 s) and shot notes for the rest: text props and sound words
6. Captions (look, style, keywords)
7. Comment bait: the loophole
8. The score card

Then offer, in one line: a 36-second cut (or a 2-minute version of a gag), a part 2, a darker version, or a different
ending.

## Hard rules
- **Sentence 1 = the rule or premise.** No intro, no "wait for it", no question to the viewer, no "follow for part 2".
- **Pace:** 4.3 spoken words/s for stories (450-600 words for 1:50-2:20), 5.2 for gags (180-195 words).
  **Sentences ~6 words**, a one-word sentence every 8-10 lines. Write for the ear.
- **Comedy first, heart second** (warm stories): the first 20-30 seconds are funny proofs of the rule.
- **Plant and pay off.** Everything that matters at the end (the ritual, the misfit trait, a throwaway fact) is
  planted before 0:60.
- **Specific names and numbers** in every proof line (Mr. Okafor, 1987, 312 balloons).
- **Show, don't tell feelings** until the reveal.
- **The last line echoes the first line or the ritual**, changed. Then cut.
- **Original work only.** Use the patterns, never another creator's plots, characters, titles or lines, and never name
  the creators whose videos were studied.
- Kid-safe for an all-ages animated channel unless the user asks otherwise.
