import sqlite3
from mysql import connector

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from config import Config

cfg = Config()

# Connect to MySQL
mysql_conn = connector.connect(
    host=cfg.MYSQL_HOST,
    user=cfg.MYSQL_USER,
    password=cfg.MYSQL_PASSWORD,
    database=cfg.MYSQL_DATABASE,
    port=cfg.MYSQL_PORT
)

table_name = "planes"

# Retrieve data from MySQL
with mysql_conn.cursor() as mysql_cursor:
    mysql_cursor.execute(f'SELECT * FROM {table_name}')
    data = mysql_cursor.fetchall()

# Connect to SQLite
sqlite_conn = sqlite3.connect('db_planes.db')

with sqlite_conn:
    sqlite_conn.execute(
        '''CREATE TABLE IF NOT EXISTS planes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type_plane TEXT NOT NULL,
            start_date DATE NOT NULL,
            operation_date DATE NOT NULL
        )'''
    )

# Insert data into SQLite
with sqlite_conn:
    sqlite_conn.executemany(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)', data)

sqlite_conn.commit()

sqlite_cursor = sqlite_conn.cursor()
sqlite_cursor.execute(f"SELECT * from {table_name}")

# Display data to show that exports done correctly
print(sqlite_cursor.fetchall())

mysql_cursor.close()
mysql_conn.close()
sqlite_cursor.close()
sqlite_conn.close()