#!/bin/bash
set -e

# Optional: Execute a command argument or default to the Flask server
cmd="$@"

# You can put other setup commands here

# Example: Wait for Postgres to be ready before starting the Flask app
until PGPASSWORD=$DB_PASS psql -h "$DB_HOST" -U "$DB_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

# Execute the Flask server or whatever command was passed to docker run
exec $cmd
