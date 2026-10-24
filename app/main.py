
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Ansible FastAPI Deployment",
    description="A FastAPI application deployed using Docker and Ansible.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "FastAPI application is running!",
        "deployment": "Docker Compose + Ansible",
        "status": "success",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
