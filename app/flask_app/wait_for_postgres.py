import os
import time

import psycopg2

host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
dbname = os.environ["POSTGRES_DB"]

connected = False
while not connected:
    try:
        conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        conn.close()
        connected = True
    except psycopg2.OperationalError:
        print("PostgreSQL is unavailable - sleeping")
        time.sleep(1)

print("PostgreSQL is up - continuing")
