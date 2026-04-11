🚀 CI/CD COMPLETE NOTES (HARI'S MASTER EDITION)

🔹 WHAT IS CI? (Continuous Integration)
Definition: The practice of merging all developer working copies to a shared mainline several times a day.
Focus: "Build & Test".
Goal: Detect "Integration Hell" early.

🔹 WHAT IS CD? (The Two Versions)
1. Continuous Delivery: Automated testing/packaging, but MANUAL "push to prod."
2. Continuous Deployment: Every change that passes tests goes to PROD AUTOMATICALLY.

🔹 THE MONOREPO CI STRATEGY (CRITICAL)
Problem: Building 10 services when only 1 changed is a waste of time.
Solution: Selective CI (Changeset Logic).
Logic: 
  IF change in /userService -> Run User-CI.
  ELSE -> Skip.

🔹 PIPELINE STAGES (DETAILED)
1. Source: Git Checkout (Full vs. Shallow).
2. Build: Dependency installation + Static Analysis (Linting).
3. Test: 
   - Unit Tests (Logic)
   - Integration Tests (Database/API)
   - Smoke Tests (Does it even start?)
4. Package (Artifact Management):
   - Versioning: service-v1.0.X.zip
   - Storage: Jenkins Archive or Nexus/JFrog.
5. Deploy: Moving to Staging/Prod.

🔹 DEPLOYMENT STRATEGIES (MODERN CD)
1. Blue/Green: Two identical environments. Switch traffic from Blue (Old) to Green (New).
2. Canary: Deploy to 5% of users first. If no bugs, roll out to 100%.
3. Rolling: Update one server at a time.

🔹 PERFORMANCE OPTIMIZATION (THE "PRO" WAY)
1. Parallel Execution: Run tests for 10 services at once.
2. Caching: Cache 'venv' or 'node_modules' folders to save download time.
3. Fail-Fast: Stop the entire pipeline the second the first test fails.

🔹 ARTIFACT vs IMAGE vs CONTAINER
Concept      | Definition                 | Example
-------------|----------------------------|------------------
Artifact     | The raw output             | app.zip / app.jar
Image        | Artifact + OS + Runtime    | Docker Image
Container    | The running Image          | Running Instance

🔹 RELIABILITY & SECURITY
- Secrets: NEVER in Git. Use 'withCredentials' or HashiCorp Vault.
- Flaky Tests: Tests that pass sometimes and fail others. Use 'Retry' logic.
- Idempotency: Running the deploy twice should NOT break the system.

🔹 INTERVIEW KEY POINTS (ADVANCED)
- Explain "Time to Recovery" (TTR): How fast can you fix a broken prod?
- Explain "Build Lead Time": Time from code push to prod deploy.
- Explain "Triggers": Why Webhooks are better than Polling for CI.

🔹 FINAL UNDERSTANDING
CI/CD is NOT: Just making a Jenkinsfile turn green.
CI/CD IS: Ensuring that code can move from a dev's brain to a user's screen with zero manual errors.
