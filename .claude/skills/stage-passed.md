---
name: stage-passed
description: Internal skill - auto commit and push when stage assessment passed
trigger: internal
---

# Stage Passed - Auto Commit & Push

**Internal skill** - Called automatically by Claude when judging a learning stage as passed.

## Behavior

When Claude determines a stage assessment has passed:
1. Stage all changes (`git add -A`)
2. Commit with: `chore(learning): pass stage {name} - auto commit`
3. Push to remote

## Not user-invocable

This skill is triggered by Claude's judgment, not by the user typing `/stage-passed`.
