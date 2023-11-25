# Build stage
FROM node:18 AS build-stage

# Set the working directory in the Docker image
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY my-react-app/package*.json ./

# Install project dependencies
RUN npm install

# Copy project files and folders to the current working directory (i.e. 'app' folder)
COPY my-react-app/ .

# Build the app for production using Vite
RUN npm run build

# Serve stage
FROM node:18

# Set the working directory in the Docker image
WORKDIR /app

# Install serve to serve the static files
RUN npm install -g serve

# Copy the build artifacts from the build stage
COPY --from=build-stage /app/dist /app

# Expose the port that serve uses to serve the application
EXPOSE 5173

# Copy the entrypoint script into the container
COPY ./docker/react-app/entrypoint.sh /entrypoint.sh

# Give execution rights on the entrypoint script
RUN chmod +x /entrypoint.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/entrypoint.sh"]

# Default command to serve the application
CMD ["serve", "-s", "build", "-l", "3000"]
