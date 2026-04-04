# GIT (Goabal Information Tracker
- Working Directory → where you write code  
- Staging → prepare changes (`git add`)  
- Local Repo → commits (`git commit`)  
- Remote → GitHub (`git push`)  
# 📊 2. Commit Graph (VERY IMPORTANT)
A → B → C
- A = first commit  
- B = change  
- C = latest  
👉 Git = history of commits
# 🧱 3. Daily Workflow (Single Branch)
git status                  # check changes
git add .                   # stage changes
git commit -m "message"     # commit
git pull origin main        # sync latest
git push origin main        # push
# 📊 Example Flow
A → B → C
# 🌐 4. Remote Setup
git remote add origin <repo-url>
git push -u origin maiN
# ⚔️ 5. Merge Conflict (Most Important Skill)
## Why it happens
Same file changed in:
* local
* remote
## Conflict Example
```
<<<<<<< HEAD
your code
=======
remote code
>>>>>>> main
## Fix Steps
# edit file manually
git add .
git commit -m "resolved conflict"

# 🔁 6. Undo Operations (CRITICAL)
## 1. Undo file changes
git restore file.txt
👉 Removes local changes
## 2. Undo last commit (keep code)
git reset --soft HEAD~1
A → B → C
↓
A → B
👉 Code still exists
## 3. Undo last commit (delete everything)
git reset --hard HEAD~1
👉 Removes commit + code
⚠️ Dangerous
## 4. Safe undo (after push)
git revert <commit-id>
A → B → C → R(C)
👉 Adds new commit that cancels old one
# 🚨 GOLDEN RULE
If pushed → use revert
If not pushed → use reset
# 📦 7. Stash (Temporary Save)
git stash
git stash pop
👉 Use when switching work temporarily
git diff
git log --oneline --graph
👉 Helps understand what changed
# 🔥 9. REAL SCENARIO — Buggy Commit (IMPORTANT)
A → B → C
* B = buggy commit
* C = your work
## Now B is reverted
A → B → C → R(B)
## Problem
👉 C still depends on B
👉 Bug still affects your code
## ✅ Correct Solution (SAFE)
### Step 1: Revert your commit C
git revert <commit-C>
### Step 2: Reapply clean changes
* Fix code manually
* Commit again
git commit -m "Clean version without bug from B"
git push
## Final Graph
A → B → C → R(B) → R(C) → C'
👉 Clean + safe
👉 No history rewrite
# ⚠️ What NOT to do

❌ git reset --hard + push -f
❌ rewriting main history
❌ ignoring conflicts
# 🏆 10. Golden Rules

1. Pull before push
2. Never rewrite main history
3. Use revert for shared code
4. Understand commit graph

# 🎯 11. Interview Summary

Git tracks code changes using commits. In a single-branch workflow, changes are synchronized using pull and push. Conflicts are resolved manually, and undo operations are handled using reset for local changes and revert for shared changes.
