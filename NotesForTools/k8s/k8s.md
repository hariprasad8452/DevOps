--------------------------------------------------------------------------------
                   KUBERNETES (K8S) - THE ORCHESTRATION ENGINE
--------------------------------------------------------------------------------

1. THE "WHY": DRAWBACKS OF STANDALONE DOCKER
   If Docker is so great, why do we need K8S?
   - Manual Labor: If a container crashes at 3 AM in Docker, you have to 
     manually restart it. Docker doesn't "self-heal" easily across multiple hosts.
   - Scalability: Docker is great for 1-10 containers. But if you have 1,000, 
     scaling them manually across 50 servers is impossible.
   - Networking: Managing IP addresses and links between containers on 
     different physical servers (Node A to Node B) is a nightmare in Docker.
   - Storage: Attaching a persistent hard drive to a container that might 
     move from Server 1 to Server 5 is not handled by Docker.
   - Zero Downtime: Doing a "Rolling Update" (updating app version without 
     stopping the service) is manual and risky in Docker.

2. WHAT IS KUBERNETES?
   - Definition: An open-source Container Orchestration platform.
   - Origin: Developed by Google (based on their internal system called 'Borg').
   - Name: "Kubernetes" is Greek for "Helmsman" (the pilot of a ship).
   - Why "K8s"?: There are 8 letters between 'K' and 's'.

3. K8S ARCHITECTURE (THE BRAIN & THE MUSCLE)
   K8s follows a Master-Worker (Control Plane-Node) architecture.

   A. THE CONTROL PLANE (The Master/Brain)
      - API Server: The gateway. Every command (kubectl) goes here first.
      - ETCD: The "Brain's Memory." A key-value store that keeps the cluster state.
      - Scheduler: Decides which Worker Node is healthy enough to run a new Pod.
      - Controller Manager: The "Watchman." If a pod dies, it notices and tells 
        the scheduler to bring it back.

   B. THE WORKER NODES (The Muscle/Server)
      - Kubelet: The "Captain" on the ship. It ensures containers are running 
        in the pods. It talks back to the API Server.
      - Kube-Proxy: The "Traffic Police." Handles networking so pods can talk.
      - Container Runtime: Usually Docker or containerd. The engine that runs 
        the image.



4. KEY K8S COMPONENTS (THE OBJECTS)
   - Pod: The smallest unit in K8s. One Pod usually holds one Container.
   - Deployment: Manages Pods. It handles scaling and rolling updates.
   - Service: Provides a "Permanent IP" or DNS name to a group of Pods.
   - Namespace: Virtual dividers (e.g., 'dev', 'prod') inside one cluster.
   - ConfigMaps/Secrets: Stores config files and passwords separately from code.

5. THE WORKFLOW: GIT PUSH TO K8S (THE MODERN PIPELINE)
   
   STEP 1: Developer pushes code to GitHub.
   STEP 2: Jenkins (via Webhook) triggers a build.
   STEP 3: Jenkins builds a Docker Image and pushes it to Docker Hub/Nexus.
   STEP 4: Jenkins updates the K8s manifest (YAML file) with the new image tag.
   STEP 5: Jenkins runs 'kubectl apply -f deployment.yaml'.
   STEP 6: K8s Control Plane sees the change, pulls the new image, and 
           performs a "Rolling Update" (replaces old pods with new ones).

--------------------------------------------------------------------------------
                  OLD WAY (DOCKER) vs NEW WAY (K8S)
--------------------------------------------------------------------------------

+----------------------+--------------------------+----------------------------+
| Feature              | Traditional Docker       | Kubernetes (K8s)           |
+----------------------+--------------------------+----------------------------+
| Deployment           | Manual (docker run)      | Declarative (YAML files)   |
| Self-Healing         | No (Container stays dead)| Yes (Auto-restarts Pods)   |
| Scaling              | Manual                   | Auto-scaling (HPA)         |
| Load Balancing       | External/Manual          | Built-in (Services)        |
| Updates              | Downtime likely          | Zero-Downtime Updates      |
+----------------------+--------------------------+----------------------------+

6. AN EXAMPLE TO UNDERSTAND (THE RESTAURANT ANALOGY)
   - The App: The Food.
   - The Container (Docker): The Plate holding the food.
   - The Worker Node: The Table where people eat.
   - The Master (K8s): The Restaurant Manager. 
     - If a plate breaks (Pod crash), the Manager (Controller) orders a new one.
     - If the restaurant gets crowded, the Manager adds more tables (Scaling).
     - The Manager ensures the waiter (Kube-proxy) knows which table ordered what.

7. FLOWCHART OF K8S LOGIC
   [User Input: kubectl apply] 
              |
      [API Server] <------> [ETCD (Stores State)]
              |
      [Scheduler] (Finds a Node with CPU/RAM)
              |
      [Kubelet] (Receives instruction on Worker Node)
              |
      [Container Runtime] (Pulls Image & Starts Pod)

1. PODS (The Smallest Unit)
   - A Pod is a wrapper around one or more containers.
   - All containers in a Pod share the same Network IP and Storage (Volume).
   - Key Rule: Pods are ephemeral (they die and are replaced). Never rely on a 
     Pod's IP address.

2. DEPLOYMENTS (The Manager)
   - Manages the lifecycle of Pods.
   - Handles Rolling Updates: If you update version 1 to version 2, it kills 
     old pods one by one and starts new ones to ensure Zero Downtime.
   - Self-Healing: If a worker node crashes, the Deployment notices and 
     re-creates the pods on a healthy node.

3. SERVICES (The Stable Entry Point)
   - Since Pods die and get new IPs, a Service provides a STATIC IP/DNS.
   - Types of Services:
     a) ClusterIP: Internal communication only (default).
     b) NodePort: Exposes the app on a static port of each Node's IP.
     c) LoadBalancer: Integrates with Cloud (AWS/Azure) to give a Public IP.

4. INGRESS (The Smart Router)
   - A Service is layer 4 (IP/Port). Ingress is layer 7 (HTTP/Domain).
   - Allows you to route traffic: 
     - myapp.com/api -> goes to Service A
     - myapp.com/login -> goes to Service B

5. LIVENESS & READINESS PROBES (Self-Healing)
   - Liveness: "Am I alive?" If it fails, K8s restarts the container.
   - Readiness: "Am I ready for traffic?" If it fails, K8s stops sending 
     requests to this pod until it recovers.
   - Example (YAML):
     livenessProbe:
       httpGet:
         path: /healthz
         port: 8080
       initialDelaySeconds: 3

6. RESOURCE QUOTAS & LIMITS (Cost & Stability)
   - Requests: The minimum CPU/RAM a pod is guaranteed.
   - Limits: The maximum CPU/RAM a pod can consume.
   - Critical: Without limits, one "leaky" app can crash your entire server.

7. HPA (HORIZONTAL POD AUTOSCALER)
   - Automatically increases or decreases the number of Pods based on CPU 
     utilization. 
   - Example: During a sale, if CPU hits 70%, K8s scales from 2 pods to 10 pods.

8. TAINTS AND TOLERATIONS
   - Taints: Applied to Nodes. "I don't want pods here unless they are special."
   - Tolerations: Applied to Pods. "I am special and can run on tainted nodes."
   - Use Case: Dedicating a node with a GPU only for Machine Learning pods.

9. CONFIGMAPS & SECRETS
   - Decouples configuration from the image.
   - ConfigMap: For non-sensitive data (database URL).
   - Secret: For sensitive data (passwords) – stored in Base64 encoding.

--------------------------------------------------------------------------------
                     KUBERNETES COMMAND CHEAT SHEET
--------------------------------------------------------------------------------

# VIEWING RESOURCES
kubectl get pods                # List all pods
kubectl get svc                 # List all services
kubectl get nodes               # Check cluster health
kubectl get all                 # See everything in current namespace
kubectl get pods -n <name>      # List pods in a specific namespace

# DEBUGGING (The "DevOps Daily Bread")
kubectl describe pod <name>     # See events (Why is it failing?)
kubectl logs <name>             # See application errors
kubectl logs -f <name>          # Stream logs in real-time
kubectl exec -it <name> -- bash # SSH into a running container

# MANAGING DEPLOYMENTS
kubectl apply -f file.yaml      # Create or Update a resource
kubectl delete -f file.yaml     # Remove a resource
kubectl scale deploy <name> --replicas=5  # Manual scaling
kubectl rollout status deploy/<name>      # Check update progress
kubectl rollout undo deploy/<name>        # ROLLBACK to previous version

# ADVANCED
kubectl top nodes               # Check CPU/RAM usage of nodes
kubectl get events --sort-by='.lastTimestamp' # See what just happened

--------------------------------------------------------------------------------
                      THE FULL CI/CD FLOW (SUMMARY)
--------------------------------------------------------------------------------

1. GIT PUSH: Dev pushes a "bug fix" to Git.
2. JENKINS: Webhook triggers. Jenkins runs Unit Tests.
3. DOCKER: Jenkins builds image: `docker build -t hari/app:v2 .`
4. REGISTRY: Jenkins pushes image to Docker Hub.
5. K8S UPDATE: Jenkins runs: `kubectl set image deployment/my-app app=hari/app:v2`
6. ROLLING UPDATE: K8s creates a "v2 pod," waits for it to pass **Readiness Probe**, 
   then kills a "v1 pod." 
7. VERIFY: If v2 crashes, K8s stops the rollout. Dev runs `kubectl rollout undo`.
