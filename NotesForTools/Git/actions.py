# --- GITHUB ACTIONS CHEAT SHEET (actions.py) ---
# 1. WHAT IS IT? -> Automation! It runs scripts when you push code.
# 2. THE LOCATION -> Must be in: .github/workflows/main.yml
# 3. THE TRIGGER  -> 'on: [push]' means run every time you upload code.
# 4. THE RUNNER   -> 'runs-on: ubuntu-latest' means use a Linux cloud server.

# --- STEP-BY-STEP: HOW TO CREATE A PIPELINE ---
# Step A: In your project root, create a hidden folder: .github
# Step B: Inside .github, create another folder: workflows
# Step C: Inside workflows, create a file: main.yml (The configuration file)

# --- EXAMPLE WORKFLOW (A-B-C FLOW) ---
# A: Trigger -> B: Environment -> C: Steps (Commands)

# --- COPY THIS INTO YOUR .github/workflows/main.yml ---
"""
name: Python Basic Pipeline
on: [push]  # Trigger: Runs on every push to any branch

jobs:
  build:
    runs-on: ubuntu-latest  # The cloud machine type
    steps:
      - name: Checkout code
        uses: actions/checkout@v4  # Step 1: Copy your code to the cloud

      - name: Set up Python
        uses: actions/setup-python@v5  # Step 2: Install Python in the cloud
        with:
          python-version: '3.10'

      - name: Run my script
        run: python actions.py  # Step 3: Actually execute your code
"""

# --- DEBUGGING ACTIONS ---
# 1. Push your code to GitHub.
# 2. Click the 'Actions' tab on your GitHub repository page.
# 3. Click on the latest "Run" to see the logs and check for errors.

# --- THE ACTIONS GOLDEN RULES ---
# 1. INDENTATION MATTERS: YAML files use spaces (not tabs). One wrong space breaks it.
# 2. USE ACTIONS/CHECKOUT: Always start with this so the runner can see your files.
# 3. SECRETS: Never put passwords in YAML. Use 'GitHub Secrets' settings instead.

print("Running actions.py...")
print("This file is being executed by a GitHub Actions runner!")
print("Workflow: Push -> GitHub detects .yml -> Ubuntu Server starts -> Python runs this.")
print("Automation complete: Code validated on every push.")
