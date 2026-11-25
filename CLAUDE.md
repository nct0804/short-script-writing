# Fact & Fable: instructions for Claude

This folder is a script-writing kit for short videos. Its skills live in `.claude/skills/`.

- **Any request for a short-video script starts with `short-script`**, which asks the user **Fact or Fable** (and, for a
  Fable, a 2-minute story or a 36-second gag) before anything else. Skip the question only when the user's own words
  already chose. Then follow `fact-script` or `fictional-script`.
- **Reference videos** go in `reference-videos/<fact|fable>/<set-name>/` and are studied with `study-references`. They
  are private: never commit, quote or share them, and never write the creator's name anywhere. The only output meant
  to be kept is the style profile in `style-profiles/`.
- **Style profiles:** when one exists for the chosen type, offer it at the start of a script; a chosen profile's numbers
  override the skill's defaults.
- **Original work only:** use the patterns, never another creator's lines, titles, plots or characters.
- **Terms are fixed across the kit:** Fact (Fact story, Fact event, Fact explainer) and Fable (Fable story, warm or eerie;
  Fable gag). Keep them consistent in anything you write here.
- After changing a skill, rebuild the Claude.ai zips with `scripts/package.sh`.
