#!/bin/bash
# Sync clinical skills from ~/.hermes/skills/clinical/ to the repo
# This script copies the skills and prepares them for git commit

REPO_DIR="/tmp/hermes-skills-klinis"
SKILLS_SRC="$HOME/.hermes/skills/clinical"

# Sync clinical skills from ~/.hermes/skills/clinical/ to repo's klinis/ dir
if [ -d "$SKILLS_SRC" ]; then
    rsync -a --delete "$SKILLS_SRC/" "$REPO_DIR/klinis/"
    echo "Synced clinical skills → repo klinis/"
else
    echo "No clinical skills dir found at $SKILLS_SRC"
fi
