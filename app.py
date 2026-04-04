# --- GIT CHEAT SHEET FOR THIS FILE ---
# 1. git init                -> Start a new local repository
# 2. git add app.py          -> Stage changes (prepare for commit)
# 3. git commit -m "msg"     -> Save staged changes with a descriptive message
# 4. git remote add origin <url> -> Connect local repo to your GitHub repository
# 5. git branch -M main      -> Rename your default branch to "main"
# 6. git push -u origin main -> Upload local commits to GitHub for the first time
# 7. git pull origin main    -> Download/Sync changes from GitHub to local computer
# 8. git status              -> Check which files are changed or staged
# 9. git log --oneline       -> View a compact history of all your commits
# 10. git merge <branch>     -> Combine changes from different branches

# --- CONFLICT SCENARIO: Local & GitHub both have different new commits ---
# Scenario: You committed locally, but someone (or you) changed the same line on GitHub.
# Step A: git pull origin main -> This will fail and show "CONFLICT (content)"
# Step B: Open app.py          -> Look for <<<<<<< HEAD, =======, and >>>>>>> markers
# Step C: Manually edit file   -> Delete the markers and keep the code you want
# Step D: git add app.py       -> Mark the conflict as resolved
# Step E: git commit -m "Fix merge conflict" -> Finalize the resolution


print("Hello, Harry")
print("Hello, Harry Potter")
print("Hello, Git!")
print("This is my very first commit.")
print("I am practicing the version control workflow.")
print("Now I am adding remote push commands to my cheat sheet.")
print("Adding a line to practice pulling changes from GitHub back to my local machine.")
print("Learning to resolve merge conflicts: Edit file -> Remove markers -> Add -> Commit.")
print("Conflict Resolution: I manually picked the best code and removed Git's markers!")
