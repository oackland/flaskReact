# Step 1: Use an official Node.js runtime as a parent image
FROM node:latest

# Step 2: Set the working directory inside the container
WORKDIR /usr/src/app

# Step 3: Copy package.json and package-lock.json (or yarn.lock if using Yarn)
COPY package*.json ./

# Step 4: Install dependencies
# This will install both production and development dependencies
RUN npm install

# Step 5: Copy the rest of your app's source code
COPY . .

# Step 6: Build the app
# This will transpile TSX files and build your React app
RUN npm run build

# Step 7: Expose the port the app runs on
EXPOSE 3000

# Step 8: Define the command to run your app
CMD [ "npm", "run", "dev" ]
