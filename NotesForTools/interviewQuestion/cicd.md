# ==============================================================================
# HARI'S DEVOPS & JENKINS CASE STUDIES
# ==============================================================================

# ------------------------------------------------------------------------------
# Q1: Application works locally but fails in CI with "Permission Denied".
# ------------------------------------------------------------------------------
# ROOT CAUSES:
# 1. Script lacks execute permission (+x) in Git metadata.
# 2. Jenkins user (UID 1000) lacks write access to the target directory.
#
# SOLUTIONS:
# - git update-index --chmod=+x deploy.sh (Permanent Git Fix)
# - sh "chmod +x script.sh" (Temporary Pipeline Workaround)
#I’d check file permissions (ls -l), user context (whoami), and mount type. In CI, permission issues often come from containerized agents where UID/GID mismatch or volume mounts override permissions.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q2: Difference between > vs >> (Real Pipeline Impact)
# ------------------------------------------------------------------------------
# LOGIC:
# >  (Overwrite): Clears file and writes new content.
# >> (Append): Keeps existing content and adds new content to the end.
#
# CI/CD IMPACT:
# - Use [ > ] for VERSIONING/STATUS where only the latest value matters.
# - Use [ >> ] for LOGGING/AUDIT where you need history across steps.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q3: Disk is full on Jenkins Agent (Identify, Fix, Prevent)
# ------------------------------------------------------------------------------
# 1. IDENTIFY:
# - Command: 'df -h' (Check disk usage percentage).
# - Command: 'du -sh * | sort -hr' (Find the heaviest folders in the workspace).
# - Jenkins UI: Manage Jenkins -> Nodes -> (Node Name) -> Disk Space Monitoring.
#
# 2. FIX IMMEDIATELY:
# - Wipe Workspace: In Jenkins Job UI, click "Wipe Out Current Workspace".
# - Docker Clean: 'docker system prune -af' (Removes unused images/containers/networks).
# - Manual Delete: 'find /var/lib/jenkins/workspace -type f -mtime +7 -delete' 
#   (Deletes files older than 7 days).
#
# 3. PREVENT:
# - Discard Old Builds: In Job Config, check "Discard old builds" (Keep max 10-20).
# - Pipeline Cleanup: Always use 'cleanWs()' in the 'post' block of your Jenkinsfile.
# - Log Rotation: Ensure /var/log/jenkins is rotated so logs don't grow to 50GB.
# - Tooling: Use the "Workspace Cleanup Plugin" to automate deletions.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q4: Production broke after a PR merge. Revert, Reset, or Hotfix?
# ------------------------------------------------------------------------------
# DECISION PROCESS (PRIORITY = STABILITY):
# 1. REVERT (Best Practice):
#    - Command: 'git revert <commit_id>'
#    - Why: Safe, creates a new commit, does not rewrite history. 
#    - Rule: If you can't fix it in 5 mins, REVERT to restore service immediately.
#
# 2. HOTFIX (The "Roll Forward"):
#    - Why: Use ONLY for 1-line trivial fixes (typos, env variables).
#    - Danger: High risk of "fixing a bug with another bug" under pressure.
#
# 3. RESET (Forbidden on Main):
#    - Command: 'git reset --hard <old_commit_id>'
#    - Why: Rewrites history. It will break the local repos of everyone else on 
#      the team. ONLY use on private/local feature branches.
#
# INTERVIEW ANSWER:
# "I would REVERT the commit immediately to minimize downtime (MTTR). 
# Stability is more important than 'fixing it live'. Once production is stable, 
# I will investigate the bug in a dev environment and prepare a proper PR."
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q5: git merge vs. git rebase (CI/CD Impact)
# ------------------------------------------------------------------------------
# LOGIC:
# - MERGE: Joins branches and creates a merge commit. Non-destructive.
# - REBASE: Moves the entire feature branch to begin on the tip of the main 
#   branch. Rewrites history.
#
# CI/CD IMPACT:
# - Use [ MERGE ] when moving code from 'Feature' -> 'Main'. It preserves the 
#   history of how and when the feature was built.
# - Use [ REBASE ] locally to keep your feature branch clean and linear. 
#   Makes 'git log' much easier to read in production.
#
# DANGER ZONE (The Golden Rule):
# "Never rebase a branch that has already been pushed to a remote/shared repo."
# REASON: Rebase changes commit IDs. If you 'force push' a rebased shared 
# branch, you will break the local repositories of every other team member 
# and potentially cause the CI/CD pipeline to lose its reference point.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q6: Pipeline triggered on every push -> Too many builds. How to control?
# ------------------------------------------------------------------------------
# 1. COMMIT MESSAGE KEYWORDS:
#    - Use '[ci skip]' or '[skip ci]' in the commit message. Jenkins plugins 
#      can detect this and cancel the build automatically.
#
# 2. PATH FILTERING (Changeset):
#    - logic: Only trigger stages if specific files change.
#    - when { 
#        not { changeset "docs/**" } // Don't build for documentation updates
#      }
#
# 3. QUIET PERIOD:
#    - Config: In Job Settings -> "Quiet Period" (e.g., 60 seconds).
#    - Result: If a dev pushes 3 times in 1 minute, Jenkins combines them 
#      into a single build instead of three.
#
# 4. BRANCH FILTERING:
#    - Restrict "Push Triggers" to main or staging branches. Use "Pull Request" 
#      triggers for feature branches so code is only tested when ready for review.
#
# 5. DEBOUNCING / GENERIC WEBHOOK FILTER:
#    - If using Webhooks, use the "Generic Webhook Trigger" plugin to filter 
#      by JSON path (e.g., only trigger if 'ref' == 'refs/heads/main').
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q7: Why does CI exist? (The "Real" Problem)
# ------------------------------------------------------------------------------
# PROBLEM: "Integration Hell"
# 1. LATENT BUGS: Conflicts stay hidden for weeks, making them 10x harder to fix.
# 2. ENVIRONMENTAL DRIFT: "Works on my machine" syndrome due to lack of a 
#    neutral, standardized testing ground.
# 3. LONG FEEDBACK LOOPS: Developers lose context of their code before 
#    bugs are discovered.
#
# CI SOLUTION:
# CI forces "Continuous Pain." By merging and testing 10 times a day, conflicts 
# are tiny and caught in minutes. It standardizes the build environment so 
# "it works on the CI agent" becomes the only truth.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q8: Build -> Test -> Deploy. Where to apply caching and why?
# ------------------------------------------------------------------------------
# PRIMARY LOCATION: The BUILD / INSTALL Stage.
# TARGETS: External dependencies (node_modules, venv, .m2, pip-cache).
#
# WHY APPLY IT:
# 1. SPEED: Dependencies take 80% of build time but change <5% of the time.
# 2. COST: Reduces data transfer costs between GitHub/Registry and Jenkins.
# 3. RELIABILITY: Protects against external downtime (e.g., if PyPI is down, 
#    your build still works because you have the cache).
#
# PIPELINE IMPACT:
# Without caching: Build takes 10 mins (Downloading world).
# With caching: Build takes 2 mins (Using local copy).
#
# DANGER:
# "Stale Cache." If you update a version in requirements.txt but Jenkins 
# uses the old cache, your build might pass but fail in production. 
# FIX: Use a 'Cache Key' based on the hash of your requirements file.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q9: Pipeline takes 15 mins. Optimization Strategy (Beyond Parallelism).
# ------------------------------------------------------------------------------
# 1. GIT OPTIMIZATION (THE "FETCH" PHASE):
#    - Use 'Shallow Clone' with depth 1 to avoid pulling GBs of history.
#    - Use 'Sparse Checkout' if you only need a specific sub-folder (Monorepo).
#
# 2. DEPENDENCY CACHING (THE "BUILD" PHASE):
#    - Map the agent's package manager cache (e.g., ~/.cache/pip) to a 
#      persistent volume so it survives between builds.
#
# 3. DOCKER LAYER CACHING:
#    - Order Dockerfile commands from 'least likely to change' to 'most likely'.
#    - Use '--cache-from' to pull existing layers from your registry.
#
# 4. TEST IMPACT ANALYSIS (THE "TEST" PHASE):
#    - Only run tests for the modified service (Changeset logic).
#    - Separate "Fast" Unit tests from "Slow" Integration tests. Fail the 
#      pipeline immediately if Unit tests fail (Fail-Fast).
#
# 5. AGENT WARMING:
#    - Keep a set of "Hot" agents with pre-installed tools (Python, Docker) 
#    - so Jenkins doesn't waste time downloading runtimes during the build.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q10: Job vs. Step (Why is a file from Job A missing in Job B?)
# ------------------------------------------------------------------------------
# THE CONCEPTS:
# - STEP: An atomic action (sh 'make'). All steps in one Job share one workspace.
# - JOB: A high-level process. Each Job gets its own ISOLATED workspace folder.
#
# THE "MISSING FILE" REALITY:
# Job A creates 'app.zip' in /var/jenkins_home/workspace/Job_A.
# Job B starts in /var/jenkins_home/workspace/Job_B.
# Job B fails because it cannot access Job A's private folder.
#
# THE SOLUTION (How to share files between Jobs):
# 1. ARTIFACTS: Job A uses 'archiveArtifacts'. Job B uses 'copyArtifacts' plugin.
# 2. EXTERNAL STORAGE: Job A pushes to S3/Nexus; Job B pulls from there.
# 3. STASH/UNSTASH: Used only *within* a single pipeline to move files between 
#    different agents (nodes).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q11: Cache is active, but dependencies still install every time. Why?
# ------------------------------------------------------------------------------
# REASON 1: DYNAMIC CACHE KEYS
# - If the cache key is based on $BUILD_NUMBER or $TIMESTAMP, it is unique 
#   every run. Jenkins treats it as a "Cache Miss" and downloads from scratch.
# - FIX: Base the key on a file hash: checksum("requirements.txt").
#
# REASON 2: PATH MISMATCH
# - If your 'pip' is looking in /home/jenkins/.cache but you cached the 
#   local ./venv/ folder, the tool won't see the saved data.
# - FIX: Ensure the 'PATH' inside the cache config matches the tool's 
#   default download location.
#
# REASON 3: FILE PERMISSIONS/TIMESTAMPS
# - If restored files have 'Read-Only' permissions or older timestamps than 
#   the manifest, some managers force a "Fresh Install" to ensure integrity.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q12: Pipeline fails on Jenkins but works locally. (3 Causes)
# ------------------------------------------------------------------------------
# 1. ENV VARS: Missing credentials or config in Jenkins 'Credentials Store'.
# 2. DEPENDENCY DRIFT: Manual global installs on local PC vs fresh Jenkins venv.
# 3. NETWORK: Jenkins Agent lacks firewall clearance to reach DBs or Registries.
# Python version mismatch
# OS differences
# missing system packages
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q13: Why is running everything on Jenkins Controller a bad idea?
# ------------------------------------------------------------------------------
# 1. STABILITY: A single heavy build can crash the Jenkins UI for everyone.
# 2. SECURITY: Build scripts gain access to Jenkins 'master' config and secrets.
# 3. BOTTLENECK: No parallel scaling; you are limited to one machine's hardware.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q14: Artifact in Build stage missing in Next stage. Why? Fix?
# ------------------------------------------------------------------------------
# THE WHY:
# Stages are running on DIFFERENT AGENTS/NODES. Workspace is not shared 
# across physical/virtual server boundaries.
#
# THE FIX (Internal to Pipeline):
# THE FIX (STASH & UNSTASH):
# Use 'stash' to save files temporarily and 'unstash' to retrieve them on 
# a different agent within the same pipeline execution.
# stage('Build') {
#    steps { 
#        sh 'zip app.zip .'
#        stash name: 'my-app', includes: 'app.zip' 
#    }
# }
# stage('Deploy') {
#    agent { label 'production' }
#    steps { 
#        unstash 'my-app'
#        sh 'unzip app.zip'
#    }
# }
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q15: Developer changes 'chat-service', but all services build. Why? Fix?
# ------------------------------------------------------------------------------
# THE PROBLEM:
# The pipeline lacks "Path Awareness". It treats the whole repository as a 
# single unit. This leads to wasted CPU, slow feedback, and "Version Bloat".
#
# THE FIX (Selective CI / Changeset Logic):
# Use the 'when' block with 'changeset' in your Declarative Pipeline.
#
# EXAMPLE JENKINSFILE LOGIC:
# stage('Build Chat Service') {
#     when { 
#         changeset "chat-service/**" 
#     }
#     steps {
#         dir('chat-service') { sh './build.sh' }
#     }
# }
# stage('Build Media Service') {
#     when { 
#         changeset "media-service/**" 
#     }
#     steps {
#         dir('media-service') { sh './build.sh' }
#     }
# }
#
# INTERVIEW PRO-TIP:
# "To prevent redundant builds in a Monorepo, I use 'Changeset' patterns. 
# I also ensure that shared library changes (e.g., /common-utils/**) trigger 
# ALL service builds to ensure compatibility."
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q16: Flaky Pipeline (Random Test Failures)
# ------------------------------------------------------------------------------
# ROOT CAUSES:
# 1. RESOURCE CLASH: Parallel stages fighting for the same Port or DB record.
# 2. NETWORK FLAKINESS: Calling real external APIs instead of using Mocks.
#
# FIXES:
# 1. ISOLATION: Use Docker-compose to spin up a fresh, private DB for every test.
# 2. RETRY STRATEGY: 
#    retry(3) {
#        sh 'pytest tests/integration'
#    }
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q17: Security - API Key leaked in code.
# ------------------------------------------------------------------------------
# IMMEDIATE ACTION:
# 1. ROTATE: Invalidate the key immediately. It is now public property.
# 2. PURGE: Use 'git filter-repo' to delete the secret from all history.
#
# LONG-TERM PREVENT (THE "RIGHT" WAY):
# 1. JENKINS CREDENTIALS: Use 'withCredentials' block in Jenkinsfile.
#    withCredentials([string(credentialsId: 'my-api-key', variable: 'SECRET')]) {
#        sh "curl -H 'Auth: $SECRET' https://api.service.com"
#    }
# 2. SCANNING: Integrate 'Gitleaks' in the 'Source' stage to "Fail-Fast" 
#    if a secret is detected.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q18: Design CI Pipeline for 3 Microservices (User, Chat, Notification)
# ------------------------------------------------------------------------------
# 1. TRIGGERS:
#    - Webhook: GitHub 'push' event.
#    - Filter: 'when { changeset "serviceName/**" }' to avoid redundant builds.
#
# 2. STAGES (Executed in Parallel):
#    - Init: Install dependencies (shared cache for venv).
#    - Test: Linting (Flake8) + Unit Tests (Pytest).
#    - Build: Create versioned Artifact (zip) or Docker Image.
#    - Security: Scan image for vulnerabilities (Trivy/Snyk).
#
# 3. OPTIMIZATION:
#    - Parallelism: Run all 3 services at once using the 'parallel' block.
#    - Shallow Clone: Fetch only the latest commit (depth 1).
#    - Docker Caching: Reuse layers for dependencies that haven't changed.
#
# 4. FAILURE HANDLING:
#    - Fail-Fast: If 'User' fails, decide whether to stop 'Chat' (usually NOT).
#    - Post-Actions:
#      post {
#          failure { 
#              mail to: 'dev-team@company.com', subject: "Service ${SERVICE} Failed" 
#          }
#          always { cleanWs() } // Disk hygiene
#      }
#
# INTERVIEW ANSWER:
# "In a microservice CI, I implement a 'Fan-out' strategy. I use parallel stages 
# wrapped in 'when' conditions. This ensures independent scaling, where one 
# team's failing tests don't block another team's deployment (Isolation)."
I design separate pipelines for PR validation and main branch builds, with fail-fast checks early and artifact reuse to avoid rebuilding.
# ------------------------------------------------------------------------------

# Q19: Jenkins vs. GitHub Actions - Why choose Jenkins TODAY?
# ------------------------------------------------------------------------------
# 1. FULL CONTROL/PRIVACY: Essential for Air-Gapped environments or highly 
#    regulated industries (Banking/Gov) where code cannot leave the network.
#
# 2. LEGACY INTEGRATION: 1,800+ plugins allow Jenkins to connect to old 
#    hardware, mainframes, or niche enterprise tools that GHA doesn't support.
#
# 3. COST FOR MASSIVE SCALE: No "per-minute" billing. You pay for the server 
#    resources, not the execution time, which is cheaper for heavy 24/7 builds.
#
# 4. CUSTOM LOGIC: Jenkins Shared Libraries (Groovy) provide deeper 
#    orchestration power than YAML-based GHA workflows for complex pipelines.
#
# INTERVIEW ANSWER:
# "I choose GitHub Actions for speed and 'Standard' web projects. I choose 
# Jenkins for 'Enterprise' projects that require high security, complex 
# private-cloud infrastructure, or massive build volumes where GHA costs 
# would be prohibitive."
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Q20: How do you design reliable and scalable CI pipelines? (The Framework)
# ------------------------------------------------------------------------------
# 1. SECURITY (Gatekeeping):
#    - Implement 'Fail-Fast' logic: Run Linting and Secret Scans first.
#    - Protect 'main' branch via mandatory PR status checks.
#
# 2. ISOLATION (Execution):
#    - Use Dockerized Agents: Ensure a sterile, reproducible environment.
#    - Parallelism: Use 'parallel' blocks to reduce 'Lead Time to Feedback'.
#
# 3. SCALABILITY (Infrastructure):
#    - Dynamic Provisioning: Use K8s/Docker clouds to spin up agents on-demand.
#    - Shared Libraries: Centralize reusable Groovy code to manage 100+ repos.
#
# 4. PERFORMANCE (Reliability):
#    - Caching: Hash-based cache keys (checksum 'requirements.txt') for speed.
#    - Hygiene: Automate workspace cleanup (cleanWs()) to prevent disk failures.
#
# INTERVIEW SUMMARY:
# "Reliable pipelines come from isolation (Docker), fail-fast validation, and clear feedback. Scalable pipelines use distributed agents and parallel execution. Maintainability comes from reusable logic and clean design."
# ------------------------------------------------------------------------------
