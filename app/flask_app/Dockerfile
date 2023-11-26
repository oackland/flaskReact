FROM python:3

WORKDIR /app

COPY requirements.txt .
COPY dev-requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt

COPY . .

COPY entrypoint.sh .

EXPOSE 5000



VOLUME [ "/app" ]

CMD ["flask", "run"]
