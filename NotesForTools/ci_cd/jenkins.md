⚙️ JENKINS COMPLETE NOTES (HARI'S EDITION)

🔹 WHAT IS JENKINS?
Jenkins = Automation Server
Runs pipelines, Automates builds, Orchestrates workflows.

🔹 JENKINS ARCHITECTURE
Controller (Brain) → Schedules jobs
Agent (Muscle)     → Executes jobs (e.g., your harry-container)

🔹 PIPELINE AS CODE (✅ Jenkinsfile)
Declarative Syntax: Structured and readable.
Scripted Syntax: More flexible but complex.
1. Declarative Pipeline (Recommended)

Pros: Easy to read, strict structure, integrates with Blue Ocean.

Example:

pipeline {

    agent any

    stages {

        stage('Hello') {

            steps { echo 'Declarative Mode' }

        }

    }

}



2. Scripted Pipeline (Legacy/Advanced)

Pros: Full Groovy power, logic-heavy, no structure limits.

Example:

node {

    stage('Build') {

        if (env.BRANCH_NAME == 'main') {

            echo 'Running on main'

        }

        sh 'echo Scripted Mode'

    }

}
🔹 CORE CONCEPTS & TRICKS
-----------------------------------
1. DIRECTORY CONTEXT (CRITICAL)
If your project is in a subfolder, use 'dir'.
dir('projects/sample_jenkins') {
    sh 'pip install -r requirements.txt'
}

2. SELECTIVE TRIGGERING (MONOREPO)
Only run stages if specific folders change.
when {
    changeset "userService/**"
}

3. PARALLEL EXECUTION
Run multiple service builds at the SAME TIME.
parallel {
    stage('User') { steps { ... } }
    stage('Chat') { steps { ... } }
}

4. ARTIFACT VERSIONING
Never overwrite builds. Use unique names.
environment {
    VERSION = "1.0.${env.BUILD_NUMBER}"
}
archiveArtifacts artifacts: "app-${VERSION}.zip"

5. PARAMETERS
Build with custom options.
parameters {
    choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Target Env')
}

6. CREDENTIALS (SECURITY)
Never hardcode passwords.
withCredentials([string(credentialsId: 'api-key', variable: 'KEY')]) {
    sh 'echo $KEY'
}

7. SHARED LIBRARIES (Reusable Code)
Instead of copying code to every Jenkinsfile, store it in a central Git repo.
Usage:
@Library('my-shared-library') _
buildTools.helperMethod()

🔹 TRIGGERING BUILDS (THE HEARTBEAT)

How does Jenkins know when to run? There are 4 main ways:

1. POLL SCM (The "Pinger")
Jenkins checks Git at a set interval (e.g., every minute) to see if there are new commits.
✅ Pros: Works behind firewalls/local machines (no public IP needed).
❌ Cons: Delay in starting (up to the interval time), puts load on Git server.
Schedule: * * * * * (Every minute)

2. WEBHOOKS (The "Push" - Best Practice)
GitHub sends a notification TO Jenkins the second a "Push" happens.
✅ Pros: Instant triggering, zero wasted resources.
❌ Cons: Requires Jenkins to have a Public IP or a tool like Ngrok/Smee.io.
Setup: GitHub Repo -> Settings -> Webhooks -> Payload URL: http://your-jenkins/github-webhook/

3. BUILD PERIODICALLY (The "Timer")
Runs on a schedule regardless of code changes.
✅ Pros: Great for nightly security scans or cleaning up old logs.
❌ Cons: Wasteful if code hasn't changed.
Schedule: H H(0-2) * * * (Runs daily between midnight and 2 AM)

4. BUILD AFTER OTHER PROJECTS (The "Chain")
Trigger a build once another job finishes successfully.
Use: Build "Backend" after "Shared-Library" is updated.

🔹 SCHEDULE SYNTAX (CRON)
Format: MINUTE HOUR DOM MONTH DOW
* * * * * -> Every minute
H/15 * * * * -> Every 15 minutes
0 0 * * * -> Every day at midnight
H H(0-5) * * 1-5 -> Once a night on weekdays

🔹 THE "5 STAR" (CRON) SYNTAX DEFINED

Jenkins uses a 5-field Cron expression to determine timing.
Format: MINUTE HOUR DOM MONTH DOW

  * * * * *
  ^     ^     ^     ^     ^
  |     |     |     |     |
  |     |     |     |     +----- Day of Week (0-7, where 0 and 7 are Sunday)
  |     |     |     +----------- Month (1-12)
  |     |     +----------------- Day of Month (1-31)
  |     +----------------------- Hour (0-23)
  +----------------------------- Minute (0-59)

🔹 COMMON CRON SYMBOLS
* -> "Every" (e.g., Every minute, Every hour)
H   -> "Hash" (The Jenkins way to spread the load; prevents all jobs from starting at once)
/   -> "Interval" (e.g., H/15 means every 15 minutes)
-   -> "Range" (e.g., 1-5 for Monday through Friday)
,   -> "List" (e.g., 0,12 for midnight and noon)

🔹 EXAMPLES FOR HARI
* * * * * -> Trigger every single minute (Standard for fast Polling).
H/5 * * * * -> Trigger every 5 minutes (H distributes the load).
H 21 * * * -> Trigger once a day between 9 PM and 10 PM.
H H(0-4) * * 1-5  -> Trigger once a night between midnight and 4 AM, only on weekdays.
H H 1,15 * * -> Trigger on the 1st and 15th of every month.

🔹 THE "H" FACTOR (JENKINS SPECIAL)
In standard Linux Cron, "0 0 * * *" starts every job at exactly midnight, which can CRASH your server if you have 100 jobs.
In Jenkins, "H H * * *" tells Jenkins to pick a random time (e.g., 12:07 AM) to balance the CPU usage.

🔹 UPSTREAM vs DOWNSTREAM
Upstream: The project that triggers the next one.
Downstream: The project that gets triggered.

🔹 GITHUB HOOK TRIGGER FOR GITSCRIPT
A specific checkbox in Jenkins Job configuration that enables Jenkins to "listen" for GitHub Webhooks.

🔹 TRIGGERED BY CAUSE
In your Jenkinsfile, you can check HOW the build started:
when {
    triggeredBy 'TimerTrigger' // Ran via Build Periodically
}
when {
    triggeredBy 'SCMTrigger'   // Ran via Webhook or Polling
}

🔹 QUIET PERIOD
A delay (in seconds) Jenkins waits before starting a job after a trigger.
Use: To wait for multiple small commits to finish before starting the build.

🔹 FULL MONOREPO PIPELINE EXAMPLE
-----------------------------------
pipeline {
    agent any
    
    environment {
        PROJECT_ROOT = "projects/sample_jenkins"
    }

    stages {
        stage('Init') {
            steps {
                dir("${env.PROJECT_ROOT}") {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Parallel Build') {
            parallel {
                stage('User Service') {
                    when { changeset "${env.PROJECT_ROOT}/userService/**" }
                    steps {
                        dir("${env.PROJECT_ROOT}") {
                            sh 'zip -r user-v${env.BUILD_NUMBER}.zip userService/'
                        }
                    }
                }
                stage('Chat Service') {
                    when { changeset "${env.PROJECT_ROOT}/chatService/**" }
                    steps {
                        dir("${env.PROJECT_ROOT}") {
                            sh 'zip -r chat-v${env.BUILD_NUMBER}.zip chatService/'
                        }
                    }
                }
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: "${env.PROJECT_ROOT}/*.zip", allowEmptyArchive: true
            }
        }
    }

    post {
        success { echo 'Pipeline Success!' }
        failure { echo 'Build Failed - check console logs.' }
    }
}

🔹 COMMON ERRORS & FIXES
-----------------------------------
❌ ERROR: "zip: not found" or "python3: not found"
✅ FIX: Tool missing in container. Use: docker exec -u 0 -it <id> apt install zip

❌ ERROR: "Bad substitution"
✅ FIX: Conflict between Groovy and Shell. Use double quotes "sh ..." for variables.

❌ ERROR: Stages skipped when they shouldn't be
✅ FIX: Shallow Clone issue. Uncheck 'Shallow Clone' in Git settings.

❌ ERROR: "ModuleNotFoundError" in Tests
✅ FIX: Missing __init__.py or wrong PYTHONPATH. Use: export PYTHONPATH=.

🔹 DEBUGGING PRO-TIP
Always check the "Console Output" and look for:
1. "Checking evaluation of when condition" -> Tells you why a stage skipped.
2. "Running in /var/jenkins_home/workspace/..." -> Tells you where Jenkins is looking for files.
