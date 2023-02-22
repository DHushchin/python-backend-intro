import psycopg2
from mysql import connector

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from config import Config

cfg = Config()

# Connect to PostgreSQL
postgres_conn = psycopg2.connect(
    host=cfg.POSTGRES_HOST,
    user=cfg.POSTGRES_USER,
    password=cfg.POSTGRES_PASSWORD,
    port=cfg.POSTGRES_PORT,
    database=cfg.POSTGRES_DATABASE
)

postgres_cursor = postgres_conn.cursor()

# Connect to MySQL
mysql_conn = connector.connect(
    host=cfg.MYSQL_HOST,
    user=cfg.MYSQL_USER,
    password=cfg.MYSQL_PASSWORD,
    database=cfg.MYSQL_DATABASE,
    port=cfg.MYSQL_PORT
)

mysql_cursor = mysql_conn.cursor()

# Export data from PostgreSQL
postgres_cursor.execute("SELECT * FROM public.planes")
data = postgres_cursor.fetchall()

# Import data into MySQL
for row in data:
    mysql_cursor.execute(
        f"""
            INSERT INTO planes (id, name, type_plane, start_date, operation_date)
            VALUES ({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}')
         """
    )

mysql_conn.commit()

# Close the connections
postgres_cursor.close()
postgres_conn.close()
mysql_cursor.close()
mysql_conn.close()