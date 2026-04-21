
# Full-Stack DevOps Portfolio: Automated Jenkins to Kubernetes Pipeline

## 📌 Project Overview & Problem Statement
Deploying modern applications manually is inefficient and prone to configuration drift. This project demonstrates a **Production-Ready CI/CD Pipeline** that automates the lifecycle of a multi-tier application. It moves code from a local Git repository, through a Jenkins build server, into containerized Docker images, and finally orchestrates them using a Kubernetes cluster.

---

## 🏗️ Environmental Architecture & Ports
The entire ecosystem runs locally using Docker Desktop and Git Bash.

| Component | Service | Port | Description |
| :--- | :--- | :--- | :--- |
| **Jenkins** | CI/CD Server | `8081` | Manages the build, push, and deploy automation. |
| **Kubernetes API** | Control Plane | `6443` | The entry point for `kubectl` commands. |
| **Frontend UI** | Web App | `80` | External access for users to view the app. |
| **Backend API** | Node.js API | `5000` | Internal/External data service. |

---

## 🛠️ Step-by-Step Execution Flow

### 1. Initialize Local Infrastructure
First, run Jenkins as a container with access to the host's Docker socket so it can build images.
```bash
# Run Jenkins in Git Bash
docker run -d -p 8081:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins-local jenkins/jenkins:lts
```

### 2. Configure Jenkins Container
Install the Kubernetes CLI (`kubectl`) inside the running Jenkins container so it can talk to your cluster.
```bash
# Enter Jenkins container as root
docker exec -u 0 -it jenkins-local bash

# Install kubectl
curl -LO "[https://dl.k8s.io/release/$](https://dl.k8s.io/release/$)(curl -L -s [https://dl.k8s.io/release/stable.txt](https://dl.k8s.io/release/stable.txt))/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
exit
```

### 3. Establish Kubernetes Credentials
To solve "Authentication Required" errors, Jenkins needs your K8s config file.
1. Run `cat ~/.kube/config` in Git Bash.
2. In Jenkins: **Manage Jenkins > Credentials > Global > Add Credentials**.
3. Select **Secret File**, paste your config, and name the ID `k8s-config`.

---

## 📂 Project Structure & Component Roles

### 📁 Root Directory
* `Jenkinsfile`: Defines the automated stages (Build, Push, Deploy).
* `k8s-spec.yaml`: The Kubernetes manifest defining Deployments (replicas, images) and Services (LoadBalancer, ClusterIP).

### 📁 /backend
* `server.js`: Node.js logic providing a JSON API.
* `package.json`: Manages backend dependencies (Express, CORS).
* `Dockerfile`: Instructions to containerize the Node.js API.

### 📁 /frontend
* `index.html`: The User Interface that fetches data from the backend service.
* `Dockerfile`: Uses Nginx to serve the static HTML file.

---

## 🚀 The Automation Lifecycle (CI/CD)

The following sequence is triggered automatically upon every code change:

1. **Git Push:** Developer pushes code to the repository.
2. **Build Stage:** Jenkins triggers `docker build` for both Frontend and Backend folders.
3. **Push Stage:** Jenkins logs into Docker Hub and pushes the `:latest` images.
4. **Deploy Stage:** - `kubectl apply`: Updates the cluster configuration.
   - `imagePullPolicy: Always`: Ensures the cluster checks for new image layers.
   - `kubectl rollout restart`: Forces the Pods to terminate and restart to pull the fresh code from Docker Hub.

---

## 🔍 Verification & Troubleshooting Commands

### Check Deployment Health
```bash
# Verify pods are 'Running'
kubectl get pods

# Verify 'frontend-service' shows 'localhost' under External-IP
kubectl get svc

# Check logs if the Backend isn't responding
kubectl logs -l app=backend
```

### Common Resolution Strategies
* **InvalidImageName:** Ensure image names in `k8s-spec.yaml` are strictly lowercase.
* **Auth Errors:** Ensure the `KUBECONFIG` environment variable is correctly mapped in the Jenkins Pipeline stage using `withCredentials`.
* **Port Conflicts:** If port 80 is taken on your Windows machine, change the `frontend-service` nodePort or use a different mapping in Docker Desktop.

---

## 🎯 Final Output Access
* **View App:** `http://localhost:80`
* **View API:** `http://localhost:5000`
* **Manage Pipeline:** `http://localhost:8081`
