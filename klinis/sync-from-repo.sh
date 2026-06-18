#!/usr/bin/env bash
# sync-from-repo.sh — Sync skills dari repo ke ~/.hermes/skills/
# Jalankan setelah git pull

set -e
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
HERMES_SKILLS="$HOME/.hermes/skills/clinical"

echo "Sync repo → Hermes skills..."
cp -r "$REPO_DIR/skills/clinical/soap-igd-jantung" "$HERMES_SKILLS/"
cp -r "$REPO_DIR/skills/clinical/echocardiography-igd" "$HERMES_SKILLS/"
echo "✅ Selesai"
