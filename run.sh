#!/bin/bash

set -e

# Load environment variables
if [ ! -f .env ]; then
  echo "Environment file (.env) not found!"
  exit 1
fi

export $(grep -v '^#' .env | xargs)

echo "Starting Docker Compose..."
docker-compose up --build
