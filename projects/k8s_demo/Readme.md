# Local Kubernetes Frontend Project

## 🎯 Goal
To deploy a scalable, self-healing frontend application on a local Kubernetes cluster 
(Docker Desktop) using Git Bash.

## 📂 File Structure
- `index.html`: The application source code (UI).
- `Dockerfile`: The blueprint for building the container image.
- `k8s.yaml`: The orchestration manifest containing Deployment and Service definitions.

## 🛠 Prerequisites
- Docker Desktop (Kubernetes enabled in settings)
- Git Bash
- Docker Hub Account (for advanced image syncing)

## 🚀 Execution Steps
1. **Build the image:** `docker build -t hari-frontend:v1 .`
2. **Apply K8s config:** `kubectl apply -f k8s.yaml`
3. **Access:** http://localhost:30005

---

## 🔄 The Evolution of Deployment: V1/V2 vs. Latest

### 1. The Manual Versioning Process (V1 & V2)
In the beginning, we used specific version tags. This is known as **Immutable Tagging**.

**The Process:**
1. Update `index.html`.
2. Build with a new tag: `docker build -t hari-frontend:v2 .`
3. **Manual Step:** You must open `k8s.yaml` and manually change `image: hari-frontend:v1` to `image: hari-frontend:v2`.
4. Run `kubectl apply -f k8s.yaml`.

**Pros & Cons:**
* ✅ **Pro:** Very safe. You know exactly which version is running. Easy to "Roll Back" by just changing the YAML back to `v1`.
* ❌ **Con:** Slow. Every small CSS change requires you to edit your YAML file and re-apply.

---

### 2. The Advanced "Latest" Process (Continuous Deployment)
To speed up development, we switched to the `latest` tag combined with a remote registry.

**The Process:**
1. Update `index.html`.
2. Build/Push: `docker push username/hari-frontend:latest`.
3. **Automated Step:** Since `k8s.yaml` already says `image: username/hari-frontend:latest`, you **don't** need to edit the file.
4. Run `kubectl rollout restart deployment/hari-deploy`.

**How it works:**
By setting `imagePullPolicy: Always`, Kubernetes ignores its local cache. The `rollout restart` command acts as the "trigger" that tells K8s: *"Go check Docker Hub; there is a new 'latest' waiting for you."*

---

## ⚠️ Lessons Learned & Troubleshooting

### 1. The "NotFound" Naming Trap
* **Error:** `Error from server (NotFound): deployments.apps "hari-deployment" not found`
* **Lesson:** Resource names are defined in the `metadata` of the YAML. We used `hari-deploy`.

### 2. The Image Visibility Issue (ErrImagePull)
* **Error:** `ErrImagePull` or `ImagePullBackOff`
* **Lesson:** Kubernetes defaults to looking at public registries. If your image is just `hari-frontend`, it fails. It **must** be prefixed with your registry username (e.g., `hari123/hari-frontend`).

### 3. The "Waiting to Start" Log Error
* **Error:** `Error from server (BadRequest): container is waiting to start`
* **Lesson:** You cannot check `kubectl logs` if the image hasn't finished downloading. Use `kubectl describe pod <name>` to see the "Events" log for pull errors.

### 4. Browser Cache "Ghosting"
* **Issue:** K8s shows the pod is updated, but the browser shows the old UI.
* **Fix:** Static files are cached heavily. Use **Ctrl + F5** to force the browser to fetch the new `index.html`.
