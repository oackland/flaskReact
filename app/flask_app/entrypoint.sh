#!/bin/bash

# Sleep for a short time to ensure that dependent services are up
sleep 5

# Set error flag
set -e

# Optional: Execute a command argument or default to the Flask server
cmd="${1:-flask run}"

# Wait for Postgres to be ready before starting the Flask app
until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

# Execute the Flask server or whatever command was passed to docker run
exec $cmd
