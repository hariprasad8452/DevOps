# --- GIT CHEAT SHEET  ---
# 1. git init                -> Start a new local repository
# 2. git add app.py          -> Stage changes (prepare for commit)
# 3. git commit -m "msg"     -> Save staged changes with a descriptive message
# 4. git remote add origin <url> -> Connect local repo to your GitHub repository
# 5. git branch -M main      -> Rename your default branch to "main"
# 6. git push -u origin main -> Upload local commits to GitHub for the first time
# 7. git pull origin main    -> Download/Sync changes from GitHub to local computer
# 8. git status              -> Check which files are changed or staged
# 9. git log --oneline       -> View a compact history of all your commits

# --- UNDOING & RESTORING (The A-B-C Scenario) ---
# OPTION 1: git restore app.py -> DISCARD unsaved changes. Use when you messed up current typing.
# OPTION 2: git restore --staged app.py -> UN-STAGE. Use if you added a file by mistake but aren't ready to commit.

# --- RESET VS REVERT (When to use what) ---
# OPTION 3: git reset --soft B -> UNDO COMMIT, KEEP WORK. Use if you forgot to add a file to the last commit.
# OPTION 4: git reset --hard B -> TOTAL WIPE. Use only if you want to destroy everything after commit B.
# OPTION 5: git revert C       -> SAFE UNDO. Use if you already PUSHED to GitHub. It creates a new "undo" commit.

# --- STASHING (The "Pause" Button) ---
# 1. git stash               -> Saves uncommitted changes to a secret "shelf"
# 2. git stash pop           -> Brings those changes back

# --- CONFLICT SCENARIO: Local & GitHub both have different new commits ---
# Scenario: You committed locally, but someone changed the same line on GitHub.
# Step A: git pull origin main -> This will fail and show "CONFLICT (content)"
# Step B: Open app.py          -> Look for <<<<<<< HEAD, =======, and >>>>>>> markers
# Step C: Manually edit file   -> Delete the markers and keep the code you want
# Step D: git add app.py       -> Mark the conflict as resolved
# Step E: git commit -m "Fix merge conflict" -> Finalize the resolution

# --- THE GOLDEN RULES ---
# 1. COMMIT OFTEN: Small, frequent commits make conflicts easier to solve.
# 2. PULL BEFORE PUSH: Always 'git pull' before you 'git push' to catch conflicts early.
# 3. NEVER RESET --HARD ON SHARED CODE: If others have your code, use 'revert' instead.
# 4. READ THE TERMINAL: Git usually tells you exactly how to fix the problem in the error message.

print("Hello, Harry")
print("Hello, Git!")
print("This is my very first commit.")
print("I am practicing the version control workflow.")
print("Now I am adding remote push commands to my cheat sheet.")
print("Adding a line to practice pulling changes from GitHub back to my local machine.")
print("Learning to resolve merge conflicts: Edit file -> Remove markers -> Add -> Commit.")
print("Reset Soft: I kept my work but moved the 'pointer' back.")
print("Reset Hard: I wiped the slate clean back to a stable version.")
print("Revert: I added a 'fix' commit to undo a mistake safely.")
print("Stash: I tucked my messy code away to handle an emergency pull.")
print("Restore: I discarded my unsaved mistakes to get back to the last clean version.")
print("Golden Rule: Always pull before you push!")
