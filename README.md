# Flask and Redis App with Docker Compose and GitHub Actions

This is a Flask application that uses Redis to count visits and have a healthcheck. It includes:

- A main page (`/`)
- A health check endpoint (`/health`)
- A visits counter endpoint (`/visits`)
- Dockerized services using Docker Compose
- CI pipeline via GitHub Actions with Docker healthcheck integration

## Features

- **Flask** for web serving
- **Redis** to store a persistent visit counter
- **Docker Compose** to orchestrate services
- **Health checks** for both Redis and Flask
- **GitHub Actions** CI pipeline that uses container health status

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

## How to build and run the application locally
In bash:  
docker-compose up --build

Visit in browser:  
http://localhost:8000 → Main page  
http://localhost:8000/health → Health check  
http://localhost:8000/visits → Visit counter (stored in Redis)  

To stop (in bash):  
docker-compose down

## Health Checks & GitHub Actions pipeline Testing

### Health Checks

Both the **Redis** and **Flask** services are configured with health checks to ensure reliable startup and operation:

- **Redis**: Uses the command `redis-cli ping` to confirm the Redis server is responsive.
- **Flask App**: Periodically checks the `/health` endpoint to verify that the application is running and accessible.

The Flask service will only start after Redis passes its health check, ensuring service dependencies are met before proceeding.

### GitHub Actions CI Workflow

This project includes a GitHub Actions workflow that automatically tests the application on each push or pull request to the `main` branch.

The CI pipeline performs the following steps:

1. **Checkout Code**: Pulls the latest version of the repository.
2. **Build & Start Services**: Uses Docker Compose to build and run the Flask and Redis containers in detached mode.
3. **Wait for Service Availability**: Repeatedly checks the `/healthz` endpoint to ensure the Flask service is up and responsive.
4. **Validate Health Endpoint**: Verifies that the `/health` endpoint returns HTTP status `200`, confirming the app is healthy.
5. **Cleanup**: Shuts down and removes the Docker containers after the tests complete.
