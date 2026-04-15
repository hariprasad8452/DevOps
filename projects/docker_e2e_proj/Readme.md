# 🚀 DevOps Full-Stack Docker Project

---

# 📌 Project Overview

This project demonstrates a **complete DevOps workflow** using:

* Frontend (HTML + JS)
* Backend (Python Flask API)
* Docker (multi-stage builds)
* Docker Networking
* Docker Volumes
* Jenkins CI Pipeline

---

# 🧠 Architecture

```
Frontend (Nginx)
     ↓ HTTP call
Backend (Flask API)
     ↓
Docker Network (devops-net)
```

---

# 📁 Project Structure

```
frontend/
backend/
docker/
Jenkinsfile
README.md
```

---

# ⚙️ How It Works

1. Jenkins pulls code from Git
2. Builds Docker images (frontend + backend)
3. Creates Docker network
4. Runs backend container
5. Runs frontend container
6. Frontend calls backend using container name
7. UI is exposed on browser

---

# 🌐 Output

Open:

```
http://localhost:8085
```

Click button → calls backend API

---

# 🐳 Docker Concepts Used

## 1. Multi-Stage Build

* Separates build and runtime
* Reduces image size

## 2. Networking

* Containers communicate using names
* Example: `http://backend:5000`

## 3. Volumes

* Used for persistence (optional)

---

# 🛠️ Commands & Explanation

---

## 🔹 Build Backend Image

```
docker build -t backend-app:1 -f docker/Dockerfile.backend .
```

### Why?

* Creates Docker image from backend code

---

## 🔹 Build Frontend Image

```
docker build -t frontend-app:1 -f docker/Dockerfile.frontend .
```

### Why?

* Packages frontend into Nginx server

---

## 🔹 Create Network

```
docker network create devops-net
```

### Why?

* Allows containers to communicate

---

## 🔹 Run Backend

```
docker run -d --name backend --network devops-net backend-app:1
```

### Why?

* Starts backend container
* Attaches to network

---

## 🔹 Run Frontend

```
docker run -d -p 8085:80 --name frontend --network devops-net frontend-app:1
```

### Why?

* Exposes UI to browser

---

## 🔹 Test Application

```
curl http://localhost:8085
```

### Why?

* Validates deployment

---

# 🔁 CI/CD Flow

```
Git Push
   ↓
Jenkins
   ↓
Build Docker Images
   ↓
Run Containers
   ↓
Test Application
```

---

# ⚠️ Common Issues

## ❌ Backend not reachable

* Check network:

```
docker network inspect devops-net
```

## ❌ Container not running

```
docker logs backend
```

## ❌ Port already used

* Change port 8085 → 8086

---

# 🎯 Key Learnings

* Docker images as artifacts
* Container networking
* Multi-stage optimization
* CI pipeline automation

---

# 🚀 Future Improvements

* Push images to DockerHub
* Deploy using Kubernetes
* Add monitoring (Prometheus/Grafana)

---

# 📌 Summary

This project demonstrates:

* End-to-end containerized application
* CI pipeline using Jenkins
* Real-world DevOps practices

---

# 👨‍💻 Author

Built as part of DevOps learning journey 🚀

