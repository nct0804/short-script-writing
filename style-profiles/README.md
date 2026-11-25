# Style profiles

A style profile is what the `study-references` skill learned from one set of your reference videos: numbers (length,
words per second, sentence length, cut speed), hook and ending shapes, the beat map, picture habits, and a short list
of how the set differs from the kit's defaults. Patterns in its own words only: no quotes, titles, plots or creator
names, so a profile is safe to keep, share and reuse.

```
style-profiles/fact-<set-name>.md
style-profiles/fable-<set-name>.md
```

When you start a script, `fact-script` and `fable-script` list the profiles for that type and ask whether to follow one
or the kit defaults. A chosen profile's numbers win where they differ. The empty template is
`.claude/skills/study-references/references/profile-template.md`.
