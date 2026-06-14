#!/bin/bash

# Stage Passed - Auto Commit & Push
# Internal skill: automatically triggered when Claude judges a stage as passed

set -e

# Get stage name from first argument (required)
STAGE_NAME="${1}"

if [ -z "$STAGE_NAME" ]; then
    echo "Error: Stage name required"
    exit 1
fi

# Already in the project root when skill is called
echo "📝 Staging all changes..."
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit"
    exit 0
fi

echo "💾 Creating commit..."
git commit -m "chore(learning): pass stage ${STAGE_NAME} - auto commit"

echo "🚀 Pushing to remote..."
git push

echo "✅ Successfully committed and pushed stage: ${STAGE_NAME}"
