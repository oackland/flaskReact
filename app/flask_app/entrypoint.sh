#!/bin/bash

# Sleep for a short time to ensure that dependent services are up
sleep 5
echo "Waiting for PostgreSQL to be ready..."

# Set error flag
set -e

# Wait for Postgres to be ready before starting the Flask app
python wait_for_postgres.py

>&2 echo "PostgreSQL is up - continuing"

# Debug: print the current directory and list files
echo "Current directory: $(pwd)"
ls -la

# Set the FLASK_APP environment variable
export FLASK_APP=app.py

# Debug: Verify that Flask is installed
flask --version

# Execute the Flask server
exec flask run --host=0.0.0.0
