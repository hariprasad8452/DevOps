# --- MANUAL DEPLOYMENT CHEAT SHEET (deploy.py) ---
# 1. THE GOAL    -> Turn your HTML files into a live website URL.
# 2. THE FILE    -> Your main file MUST be named 'index.html'.
# 3. THE HOST    -> GitHub Pages (Free hosting for your repo).

# --- STEP-BY-STEP: MANUAL DEPLOY (NO CI/CD) ---
# Step A: Create your 'index.html' file in the root folder.
# Step B: Push your code to GitHub (git add -> commit -> push).
# Step C: Go to your Repository on GitHub.com.
# Step D: Click on 'Settings' (top tab).
# Step E: Click on 'Pages' (left sidebar).
# Step F: Under 'Build and deployment' > 'Branch', select 'main'.
# Step G: Click 'Save'.

# --- WHAT HAPPENS NEXT? ---
# 1. Wait 1-2 minutes.
# 2. Refresh the 'Pages' settings page.
# 3. You will see a bar saying: "Your site is live at https://username.github.io/repo-name/"
# 4. Click the link to see your website!

# --- UPDATING THE SITE ---
# 1. Edit your index.html locally.
# 2. git add . -> git commit -m "update site" -> git push.
# 3. GitHub will automatically update the live link in a few seconds.

# --- THE DEPLOYMENT GOLDEN RULES ---
# 1. INDEX IS KING: If you don't name it 'index.html', the site will show a 404 error.
# 2. CASE SENSITIVE: In HTML, 'Image.jpg' is NOT the same as 'image.jpg' on Linux servers.
# 3. RELATIVE PATHS: Use <img src="logo.png"> not <img src="C:/Users/Desktop/logo.png">.

print("Preparing for Manual Deployment...")
print("Step 1: Ensure index.html exists in the root.")
print("Step 2: Push to GitHub.")
print("Step 3: Enable 'Pages' in Repository Settings.")
print("Result: Your HTML is now a live website accessible by anyone!")
