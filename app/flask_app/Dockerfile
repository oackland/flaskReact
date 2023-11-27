FROM python:3

WORKDIR /app

COPY requirements.txt .
COPY dev-requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt

COPY . .

EXPOSE 5000

# Set environment variables
# FLASK_APP should point to the Python file that creates your app instance
# FLASK_RUN_HOST is set to 0.0.0.0 to make the server externally visible
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


#ENV FLASK_APP=app.py \
#    FLASK_RUN_HOST=0.0.0.0

#CMD ["flask", "run"]
