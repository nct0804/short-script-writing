# Lesson 5 · From script to video

A script from this kit is built to be produced: the timestamps come from a reading pace, the first 7 seconds have a
shot list, the captions are specified. This lesson covers what to keep in mind when it becomes a video, using what
happened when the two samples were animated.

## 1. Voice: the pace is part of the script
| Type | Target pace | 60 s holds |
|---|---|---|
| Fact | 3.7 words/s | ~220 words |
| Fable story | 4.3 words/s | ~260 words a minute |
| Fable gag | 5.2 words/s | ~185 words in 36 s |

- **The voice sets the pace, not the script.** AI voices read at their own speed; most library voices read about 3.2
  words per second. That's fine for a Fact (a small speed-up does it), but far too slow for a gag.
  - In the Fable sample, the only child voice available read slowly. Adding "speak very fast" made it only about 6 %
    faster.
  - Removing the pauses and a 1.25× tempo (pitch kept) got the gag from 55 s to 45 s, but not to 36.
  - **For gags, choose (or design) a naturally fast voice first.**
- **Remove held pauses.** The viral references have almost none: gaps over a quarter of a second add up to about 3 s a
  minute. Trim them in the edit; it does more than speeding up.
- **Get word timings** from a transcription of the final voice. Everything else (cuts, captions, sound effects) lines
  up to them.

## 2. Captions by type
| Type | Style | Position |
|---|---|---|
| Fact | one bold white word at a time, keywords in colour | ~65 % of the height |
| Fable story, bright | 2-4 lowercase words, one keyword in colour | ~75 % |
| Fable story, eerie | one yellow bold word | ~68 % |
| Fable gag | 2-4 word chunks at the top, keyword in green CAPS | ~25 % |

Keep faces and text props out of the caption band. That was the most common fix when the samples were framed.

## 3. The picture follows the script
- **Frame 1 is sentence 1:** the deed (Fact) or the rule happening (Fable). No title card.
- **One shot per narrated noun,** about a second after it's spoken.
- **Cut speed:** a gag or a bright Fable story cuts about every second; an eerie Fable story can open with one continuous move; a
  Fact glides and pushes in, and changes composition every 1-2 s.
- **Text props** from the shot notes (the crate stencil "BOILED + RAW", the calendar "DAY 30") carry information
  without narration.
- **The reveal gets a diagram** (Fact); **the last shot returns to the first place or prop**, changed (Fable).
- **Sound words** in the script ("Pfffft.") are guaranteed sound effects on that word.

## 4. Sound
Mix the voice on top, music about 10 LU under it (ducked a few dB while the voice speaks), master to about −14 LUFS.
Drop the music to silence right before the reveal word or the big gag, and end on a short button.

## 5. The two samples
| | Fact sample | Fable sample |
|---|---|---|
| Script | *The Cook Who Spun Every Egg* (239 words) | *My Crush's Laugh Grows Flowers* (182 words) |
| Voice | adult storyteller, 3.64 words/s, 65.8 s | child voice, 4.07 words/s, 44.9 s |
| Picture | 14 shots, ~40 set-ups, glides and crossfades, a chalkboard reveal | 16 shots, ~36 set-ups, a cut every ~1.3 s, day cards |
| Captions | one word at a time | top-of-frame chunks |
| Folder | `samples/fact-the-cook-who-spun-every-egg/` | `samples/fable-my-crushs-laugh-grows-flowers/` |

Each folder has the script, the finished video and a making-of with the numbers.
