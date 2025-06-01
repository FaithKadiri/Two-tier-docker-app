# Two-tier Docker App

A hands-on lab for trying Docker networking using a simple two-tier application (frontend + backend) with Docker Compose.
You’ll build a working app, then break its networking (on purpose) to learn how to debug and fix issues like DNS failures, port conflicts, and misconfigurations.

# Project Overview
This project includes:
A Python Flask backend that returns "Hello from the backend!"
A frontend shell script that uses curl to call the backend
A docker-compose.yml to run both services
Built-in troubleshooting scenarios to simulate real-world network failures

# Directory Structure
Backend, Frontend and docker-compose.yml

Backend:
Dockerfile
app.py

Frontend:
Dockerfile
run.sh

docker-compose.yml
