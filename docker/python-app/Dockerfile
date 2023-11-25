# Dockerfile in the docker/python-app directory

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/flaskapi

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements files into the container
COPY requirements.txt dev-requirements.txt ./

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir -r dev-requirements.txt

# Copy the application source code into the container
COPY . .

# Copy the entrypoint script into the container
COPY entrypoint.sh /usr/src/flaskapi/entrypoint.sh

# Give execution rights on the entrypoint script
RUN chmod +x /usr/src/flaskapi/entrypoint.sh

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0

# Set the entrypoint script to be executed
ENTRYPOINT ["/usr/src/flaskapi/entrypoint.sh"]

# Run app.py when the container launches
CMD ["flask", "run"]
