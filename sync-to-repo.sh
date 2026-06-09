#!/usr/bin/env bash
# sync-to-repo.sh — Sync skills dari ~/.hermes/skills/ ke repo
# Jalankan setelah update skill dari Hermes

set -e
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
HERMES_SKILLS="$HOME/.hermes/skills/clinical"

echo "Sync Hermes skills → repo..."
cp -r "$HERMES_SKILLS/soap-igd-jantung/SKILL.md" "$REPO_DIR/skills/clinical/soap-igd-jantung/"
cp -r "$HERMES_SKILLS/soap-igd-jantung/references/"* "$REPO_DIR/skills/clinical/soap-igd-jantung/references/" 2>/dev/null
cp -r "$HERMES_SKILLS/echocardiography-igd/SKILL.md" "$REPO_DIR/skills/clinical/echocardiography-igd/"
cp -r "$HERMES_SKILLS/echocardiography-igd/scripts/"* "$REPO_DIR/skills/clinical/echocardiography-igd/scripts/" 2>/dev/null
echo "✅ Selesai — jangan lupa git add, commit, push"
