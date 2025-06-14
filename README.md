 Todo_list
todo-list using docker for devops assignment
 Dockerized TODO List App

A simple microservices-based TODO application built using Flask (Backend), PostgreSQL (Database), and a static HTML/JavaScript Frontend. The app is fully Dockerized and uses a custom monitor service to ensure backend health. All services run in isolated containers on a common Docker network.

---

 Project Structure

```
todo-app/
├── Backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── frontend/
│   ├── index.html
│   ├── Dockerfile
├── db/
│   └── init.sql
├── monitor/
│   ├── monitor.sh
│   └── Dockerfile
├── .gitignore
├── .dockerignore
├── README.md
```

---

 Tech Stack

- **Backend:** Flask (Python)
- **Database:** PostgreSQL
- **Frontend:** HTML + Vanilla JavaScript
- **Containerization:** Docker
- **Health Monitor:** Bash + Docker CLI

---

 How to Run the App (Dockerized)

```bash
# Step 1: Create a Docker network
docker network create app-network

# Step 2: Start PostgreSQL container
docker volume create db-data
docker run -d \
  --name db-container \
  --network app-network \
  -v db-data:/var/lib/postgresql/data \
  -v ${PWD}/db/init.sql:/docker-entrypoint-initdb.d/init.sql \
  -e POSTGRES_PASSWORD=secret \
  postgres

# Step 3: Build and run Backend container
docker build -t todo-backend ./Backend
docker run -d \
  --name backend-container \
  --network app-network \
  -p 3000:3000 \
  todo-backend

# Step 4: Build and run Frontend container
docker build -t todo-frontend ./frontend
docker run -d \
  --name frontend-container \
  --network app-network \
  -p 8080:80 \
  todo-frontend

# Step 5: Build and run Monitor container
docker build -t monitor-service ./monitor
docker run -d \
  --name monitor-container \
  --network app-network \
  -v /var/run/docker.sock:/var/run/docker.sock \
  monitor-service
```

Access the app at: **http://localhost:8080**

---

 Monitor Service

This is a creative enhancement. The monitor service is a container running a shell script that pings the backend every 10 seconds using curl. If it fails (i.e., backend is unhealthy), it auto-restarts the backend container using the Docker CLI.

---

.gitignore

```
__pycache__/
*.pyc
*.log
.env
db-data/
```

 .dockerignore

```
__pycache__/
*.pyc
*.log
.env
.git
```

---

 Features

- Add tasks via UI.
- View task list stored in PostgreSQL.
- Backend REST API (`/tasks` GET/POST).
- Monitor container with self-healing behavior.
- All components isolated via Docker containers.

---

 GitHub Integration

All files are tracked in this repository. Each component has its own Dockerfile. All services are tested and can be built/run via commands in this README. No login/auth — this is a minimal Docker-focused app for learning containerized microservices.

---

 Notes

- Tested with Docker Desktop on Windows.
- Simple UI, no frameworks.
- Perfect for learning Docker networking and container lifecycle.
- Screenshots intentionally excluded for brevity.

- Screenshots
- Monitor Screenshots
![image](https://github.com/user-attachments/assets/cbf0a85b-e9b0-4eb9-918d-d0d3a1441a0d)



