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
