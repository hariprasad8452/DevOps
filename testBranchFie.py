# --- GIT BRANCHING CHEAT SHEET (test.py) ---
# 1. git checkout -b test      -> CREATE and SWITCH to a new branch named 'test'
# 2. git branch                -> LIST all local branches (current branch has *)
# 3. git checkout main         -> SWITCH back to the main branch
# 4. git checkout -            -> SHORTCUT to switch back to the previous branch
# 5. git merge test            -> COMBINE 'test' changes into your current branch
# 6. git branch -d test        -> DELETE branch (use after merging)

# --- SYNCING FEATURE BRANCH WITH MAIN ---
# Scenario: You are on 'test' branch, but 'main' on GitHub has new updates.
# Step A: git checkout main    -> Move to main
# Step B: git pull origin main -> Get latest from GitHub
# Step C: git checkout test    -> Move back to your work
# Step D: git merge main       -> Bring main's new updates into 'test'

# --- THE BRANCHING GOLDEN RULES ---
# 1. NEVER WORK ON MAIN: Always create a branch for new features or experiments.
# 2. PULL MAIN BEFORE MERGING: Ensure your local main is fresh before joining code.
# 3. CLEAN UP: Delete the feature branch once the code is safely in main.

print("Running test.py on 'test' branch")
print("Branching allows me to experiment without breaking the main code.")
print("I can switch between 'main' and 'test' using 'git checkout'.")
print("Once my tests pass, I will merge this into the main branch.")
print("Branching is the best way to keep production code stable!")
