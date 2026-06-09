#!/usr/bin/env bash
# sync-to-repo.sh — Sync skills dari ~/.hermes/skills/ ke repo + auto commit & push

set -e
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
HERMES_SKILLS="$HOME/.hermes/skills/clinical"

echo "Sync Hermes skills → repo..."
cp "$HERMES_SKILLS/soap-igd-jantung/SKILL.md" "$REPO_DIR/skills/clinical/soap-igd-jantung/"
cp -r "$HERMES_SKILLS/soap-igd-jantung/references/"* "$REPO_DIR/skills/clinical/soap-igd-jantung/references/" 2>/dev/null
cp "$HERMES_SKILLS/echocardiography-igd/SKILL.md" "$REPO_DIR/skills/clinical/echocardiography-igd/"
cp -r "$HERMES_SKILLS/echocardiography-igd/scripts/"* "$REPO_DIR/skills/clinical/echocardiography-igd/scripts/" 2>/dev/null

cd "$REPO_DIR"
git add -A
if ! git diff --cached --quiet; then
    git commit -m "auto-sync $(TZ=Asia/Makassar date '+%Y-%m-%d %H:%M')"
    git push
    echo "Committed & pushed"
else
    echo "No changes"
fi
