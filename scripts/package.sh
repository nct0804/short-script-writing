#!/usr/bin/env bash
# Build one zip per skill in dist/ for Claude.ai (Settings -> Capabilities -> Skills). Each zip holds the skill's folder
# with SKILL.md at its top, as the upload expects. Run after changing anything in .claude/skills/.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for d in .claude/skills/*/; do
  name="$(basename "$d")"
  rm -f "dist/$name.zip"
  (cd .claude/skills && zip -qr -X "../../dist/$name.zip" "$name" -x "*/__pycache__/*" "*.pyc" "*/.DS_Store")
  echo "dist/$name.zip"
done
