# --- GIT ADVANCED BRANCHING & SYNCING (test.py) ---
# 1. git checkout -b test      -> CREATE and SWITCH to a new branch named 'test'
# 2. git branch                -> LIST all local branches (current branch has *)
# 3. git checkout main         -> SWITCH back to the main branch
# 4. git checkout -            -> SHORTCUT to switch back to the previous branch
# 5. git merge test            -> COMBINE 'test' changes into your current branch
# 6. git branch -d test        -> DELETE branch (use after merging)

# --- CHERRY-PICK (Picking the best fruit) ---
# Scenario: You only want ONE specific fix from another branch, not the whole branch.
# History: main (A-B) | feature (C-D-E)
# Goal: Get only 'D' into main.
# Step A: git checkout main
# Step B: git log feature --oneline (Find the hash of D, e.g., 1a2b3c)
# Step C: git cherry-pick 1a2b3c
# Result: main (A-B-D')

# --- REBASE (Cleaning the timeline) ---
# Scenario: You want your 'test' branch to look like it started after the latest 'main'.
# History: main (A-B-C) | test (A-B-D)
# Step A: git checkout test
# Step B: git rebase main
# Result: main (A-B-C) -> test (A-B-C-D')
# 

# --- SQUASH (Cleaning messy commits) ---
# Scenario: You have 3 tiny "typo fix" commits and want them to be 1 clean commit.
# Step A: git rebase -i HEAD~3
# Step B: In the editor, keep 'pick' for the first, change others to 'squash'.

# --- SYNCING FEATURE BRANCH WITH MAIN ---
# Scenario: You are on 'test' branch, but 'main' on GitHub has new updates.
# Step A: git checkout main    -> Move to main
# Step B: git pull origin main -> Get latest from GitHub
# Step C: git checkout test    -> Move back to your work
# Step D: git merge main       -> Bring main's new updates into 'test'

# --- THE BRANCHING GOLDEN RULES ---
# 1. NEVER WORK ON MAIN: Always create a branch for new features or experiments.
# 2. PULL MAIN BEFORE MERGING: Ensure your local main is fresh before joining code.
# 3. REBASE FOR CLEANLINESS: Use rebase for local branches, merge for shared ones.

print("Running test.py on 'test' branch")
print("Branching allows me to experiment without breaking the main code.")
print("Cherry-picking: I just grabbed a specific fix from another branch!")
print("Rebase: My history is now a nice straight line.")
print("Squash: I turned my 5 messy commits into 1 professional one.")
