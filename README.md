# Flask and Redis App with Docker Compose and GitHub Actions

This is a Flask application that uses Redis to count visits. It includes:

- A main page (`/`)
- A health check endpoint (`/health`)
- A visits counter endpoint (`/visits`)
- Dockerized services using Docker Compose
- CI pipeline via GitHub Actions with Docker healthcheck integrationrk-Assignment

## Features

- **Flask** for web serving
- **Redis** to store a persistent visit counter
- **Docker Compose** to orchestrate services
- **Health checks** for both Redis and Flask
- **GitHub Actions** CI pipeline that uses container health status (no curl needed externally)

## Project Structure

flask_redis_app/
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── docker-compose.yml
├── requirements.txt
└── .github/
└── workflows/

To run it locally (bash):
docker-compose up --build

Visit in browser:
http://localhost:5000 → Main page
http://localhost:5000/health → Health check
http://localhost:5000/visits → Visit counter (stored in Redis)

To stop (bash):
docker-compose down

- Docker Compose Overview
Redis:
Use redis:alpine

Healthcheck via redis-cli ping

Flask App
Built from the local Dockerfile

Connects to Redis via service name (redis)

Healthcheck using Python's urllib to call /health inside the container

- GitHub Actions CI Pipeline

The workflow automatically:

Checks out code

Builds Docker services

Starts services using docker-compose up

Waits for the Flask app to become healthy via internal Docker healthcheck

Optionally runs tests (you can add pytest, etc.)

Shuts down containers

- Health Check Logic
The workflow uses this logic to wait for readiness (no curl involved externally):

in bash

docker inspect --format='{{json .State.Health.Status}}' flask_app

- Environment Variables

REDIS_HOST=redis
REDIS_PORT=6379

- Endpoints
Route	Method	Description
/	GET	Welcome page
/health	GET	Returns OK if app is healthy
/visits	GET	Increments and returns visit count (Redis)
