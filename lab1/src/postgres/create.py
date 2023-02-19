import psycopg2

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from config import Config

cfg = Config()

conn = psycopg2.connect(
    host=cfg.POSTGRES_HOST, 
    user=cfg.POSTGRES_USER, 
    password=cfg.POSTGRES_PASSWORD,
    port=cfg.POSTGRES_PORT
)
conn.autocommit = True

DB_NAME = cfg.POSTGRES_DATABASE
    
with conn.cursor() as cur:
    cur.execute(f"CREATE DATABASE {DB_NAME}")

cur.close()
conn.close()
