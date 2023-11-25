#!/bin/bash
set -e

# Example: Check if the static files directory exists
if [ ! -d "/app" ]; then
  echo "Error: The directory containing the built app does not exist."
  exit 1
fi

# You can place other pre-serve commands here.

# Start the serve command with the options you want
exec "$@"
