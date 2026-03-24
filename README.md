# 🚀 flask-redis-worker-docker-compose

> Multi-service Python backend with Flask API and Redis Worker, containerized and orchestrated using Docker Compose.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey?logo=flask)
![Redis](https://img.shields.io/badge/Redis-Cache-red?logo=redis)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker--Compose-Multi--Service-2496ED?logo=docker)

---

## 📌 Project Architecture

```
User Request
      ↓
  API Service (Microservice 1)    ← Flask app.py
      ↓
  Redis Cache                     ← Shared memory
      ↓
  Worker Service (Microservice 2) ← worker.py
      ↓
  Database (future layer)
```

### DevOps Infrastructure View
```
        Internet
            |
       Load Balancer
            |
      Kubernetes Service
            |
          API Pods
            |
        Redis Cache
            |
        Worker Pods
            |
         Database
```

---

## 🗂️ Project Structure

```
flask-redis-worker-docker-compose/
├── api/
│   ├── app.py               # Flask REST API (Microservice 1)
│   └── Dockerfile           # API container config
├── worker/
│   ├── worker.py            # Background Worker (Microservice 2)
│   └── Dockerfile           # Worker container config
├── docker-compose.yml       # Multi-service orchestration
└── requirements.txt         # Python dependencies
```

---

## 🔵 Layer 1 — Microservices Overview

| Component | Purpose |
|-----------|---------|
| **API Service** | Handles HTTP requests from users |
| **Redis Cache** | Fast in-memory data storage |
| **Worker Service** | Background processing tasks |

### Technology Mapping

| Layer | Tool Used |
|-------|-----------|
| API | Python + Flask |
| Cache | Redis |
| Worker | Python background service |
| Container | Docker |
| Orchestration | Docker Compose |

---

## 🔴 Layer 2 — Backend Code

### API Service — `api/app.py`

Flask app connects to Redis and tracks page visit count.

**Endpoint:**
```
GET /
```

**Response:**
```
Hello! This page has been visited 3 times.
```

### Worker Service — `worker/worker.py`

Runs continuously in the background, sets `worker_status` in Redis every 5 seconds.

---

## 🐳 Layer 3 — Docker Compose Setup

Three services defined in `docker-compose.yml`:

| Service | Build | Port |
|---------|-------|------|
| `redis` | Official Redis image | Internal |
| `api` | `./api` Dockerfile | `5001:5000` |
| `worker` | `./worker` Dockerfile | Internal |

---

## ▶️ Layer 4 — Run the Project

### Start all services
```bash
docker compose up --build
```

### Stop all services
```bash
docker compose down
```

### Rebuild after code changes
```bash
docker compose down
docker compose up --build
```

---

## ✅ Layer 5 — Test the Output

### 1. Test the API
Open browser or use curl:
```
http://localhost:5001
```

Expected output:
```
Hello! This page has been visited 1 times.
```
Refresh the page — the count increases each time ✅

### 2. Check Worker Logs
```bash
docker compose logs worker
```

Expected output:
```
Worker is running...
Worker is running...
```

### 3. Check Redis Directly
```bash
docker exec -it <project-redis-container> redis-cli
```

```bash
127.0.0.1:6379> GET worker_status
"running"

127.0.0.1:6379> GET hits
"5"
```

---

## 🌐 Service Communication

```
api    ──→ redis   (stores hit count)
worker ──→ redis   (sets worker_status every 5 seconds)
```

| From | To | Data |
|------|----|------|
| API | Redis | `hits` counter |
| Worker | Redis | `worker_status = running` |

---

## 💡 Project Outcomes

| Outcome | Description |
|---------|-------------|
| **Multi-service architecture** | API + Worker as separate microservices |
| **Container orchestration** | All services managed via Docker Compose |
| **Service communication** | Both services communicate through Redis |

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 + Flask | API microservice |
| Python + Redis client | Worker microservice |
| Redis | In-memory cache and message store |
| Docker | Containerization |
| Docker Compose | Multi-service orchestration |
