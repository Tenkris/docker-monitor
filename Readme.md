# Performance Monitoring and Testing Suite

This project provides a comprehensive solution for monitoring container performance and running network tests using Prometheus, cAdvisor, Grafana, and custom testing tools.

## Components

- **Prometheus**: Time series database for metrics collection
- **cAdvisor**: Container monitoring tool
- **Grafana**: Visualization and analytics platform
- **Custom Network Testing**: Network performance testing script
- **Load Testing Script**: Python-based concurrent request testing

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- Bash shell

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create environment variables file (optional):

   ```bash
   cp .env.example .env
   # Edit .env file with your preferred Grafana credentials
   ```

3. Start the monitoring stack:
   ```bash
   docker-compose up -d
   ```

## Monitoring Stack Access

- **Prometheus**: http://localhost:9090
- **cAdvisor**: http://localhost:8080
- **Grafana**: http://localhost:3000
  - Default credentials: admin/admin (unless modified in .env)

## Running Tests

### Load Testing

The `main.py` script performs concurrent HTTP requests to test endpoint performance:
