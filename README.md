# Automated FastAPI Deployment Using Ansible and Docker Compose

## 1. Project Overview

This project demonstrates the deployment of a FastAPI web application using Docker, Docker Compose, and Ansible. Ansible automates application deployment and configuration on remote Linux servers.

## 2. Objectives

- Develop a REST API using FastAPI.
- Containerize the application using Docker.
- Define the application service using Docker Compose.
- Automate remote deployment using an Ansible playbook.
- Verify application availability through a health-check endpoint.

## 3. Technologies Used

- Python and FastAPI
- Docker
- Docker Compose
- Ansible
- Ubuntu/Debian Linux (for the target-server configuration)
- Git and GitHub

## 4. Project Structure

```text
ansible-fastapi-docker-deployment/
├── app/
│   ├── main.py
│   └── requirements.txt
├── ansible/
│   ├── inventory.ini
│   └── deploy.yml
├── Dockerfile
├── compose.yaml
├── ansible.cfg
├── .gitignore
└── README.md
```

## 5. Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Displays the application welcome message |
| `/health` | Returns application health status |
| `/docs` | Interactive API documentation |

## 6. Local Setup and Testing

Start the application using Docker Compose:

```bash
docker compose up --build -d
```

Check the container status:

```bash
docker compose ps
```

Test the health endpoint:

```bash
curl http://localhost:8000/health
```

Expected response includes:

```json
{
  "status": "healthy"
}
```

The actual health response also includes a timestamp.

## 7. Ansible Deployment

The `ansible/inventory.ini` file defines the target servers. The `ansible/deploy.yml` playbook installs the required packages on supported Ubuntu/Debian hosts, copies the application files, and deploys the application with Docker Compose.

Install the Docker collection:

```bash
ansible-galaxy collection install community.docker
```

Validate the playbook syntax:

```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --syntax-check
```

Before deployment, replace the placeholder server addresses in the inventory with real, reachable target hosts. Configure SSH access and ensure the required privileges and network access are available.

Run the deployment after configuring the inventory:

```bash
ansible-playbook ansible/deploy.yml
```

## 8. Verification Results

The following checks have been completed in GitHub Codespaces:

- Docker image built successfully.
- FastAPI container started successfully.
- Docker reported the container as healthy.
- The `/health` endpoint returned a healthy status.
- Ansible playbook syntax validation passed.

**Remote deployment status:** Deployment to multiple remote servers must be verified separately after the target servers and SSH access are configured.

## 9. Conclusion

This project demonstrates FastAPI development, Docker containerization, health checking, and Ansible playbook preparation. It provides a foundation for repeatable deployment to multiple Linux servers.

## 10. Author

Created as part of a practical exercise on automated application deployment using Ansible and Docker Compose.