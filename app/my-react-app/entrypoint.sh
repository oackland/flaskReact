#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status.

# Check if the static files directory exists
if [ ! -d "/app" ]; then
  echo "Error: The directory containing the built app does not exist."
  exit 1
fi

# Start the serve command with the options you want
exec serve -s . -l 5173
