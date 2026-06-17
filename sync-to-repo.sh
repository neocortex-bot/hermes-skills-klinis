#!/bin/bash
# Sync clinical skills from ~/.hermes/skills/clinical/ to the repo
# This script copies the skills and prepares them for git commit

REPO_DIR="/tmp/hermes-skills-klinis"
SKILLS_SRC="$HOME/.hermes/skills"

# Copy skills-klinis structure
mkdir -p "$REPO_DIR/skills/clinical"
rsync -a --delete "$SKILLS_SRC/clinical/" "$REPO_DIR/skills/clinical/" 2>/dev/null || true

# Check if there are existing klinis dirs to merge
if [ -d "$SKILLS_SRC/clinical" ]; then
    echo "Synced clinical skills from $SKILLS_SRC/clinical"
else
    echo "No clinical skills dir found at $SKILLS_SRC/clinical"
fi
