#!/bin/bash
# Sync clinical skills from ~/.hermes/skills/clinical/ to the repo
# This script copies the skills and prepares them for git commit

REPO_DIR="/home/linuxmint/hermes-skills-klinis"
SKILLS_SRC="$HOME/.hermes/skills/clinical"

# Sync clinical skills (excluding .git and recursive klinis/ subdirectory)
if [ -d "$SKILLS_SRC" ]; then
    rsync -a --delete --exclude=.git --exclude=klinis --exclude=skills "$SKILLS_SRC/" "$REPO_DIR/klinis/"
    echo "Synced clinical skills → repo klinis/"
else
    echo "No clinical skills dir found at $SKILLS_SRC"
fi
