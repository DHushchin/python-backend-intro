from mysql import connector

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from config import Config

cfg = Config()

# Connect to MySQL
cnx = connector.connect(
    host=cfg.MYSQL_HOST,
    user=cfg.MYSQL_USER,
    password=cfg.MYSQL_PASSWORD,
)

# Create a cursor object
cursor = cnx.cursor()

# Create a new database
DB_NAME = cfg.MYSQL_DATABASE
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

# Clean up
cursor.close()
cnx.close()
