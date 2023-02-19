import psycopg2

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from config import Config


def create_table():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS planes
                   (id INT PRIMARY KEY NOT NULL,
                   name TEXT NOT NULL,
                   type_plane TEXT NOT NULL,
                   start_date DATE NOT NULL,
                   operation_date DATE NOT NULL);''')
    conn.commit()
    print("Table created successfully")
    cur.close()


def insert_data(id, name, type_plane, start_date, operation_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO planes (ID, NAME, TYPE_PLANE, START_DATE, OPERATION_DATE) VALUES (%s, %s, %s, %s, %s)", (id, name, type_plane, start_date, operation_date))
    conn.commit()
    print("Data inserted successfully")
    cur.close()


def select_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM planes")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("TYPE_PLANE = ", row[2])
        print("START_DATE = ", row[3],)
        print("OPERATION_DATE = ", row[4], "\n")
    cur.close()


def update_data(id, name, type_plane, start_date, operation_date):
    cur = conn.cursor()
    cur.execute("UPDATE planes SET NAME = %s, TYPE_PLANE = %s, START_DATE = %s, OPERATION_DATE = %s WHERE ID = %s", (name, type_plane, start_date, operation_date, id))
    conn.commit()
    print("Data updated successfully")
    cur.close()


def delete_data(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM planes WHERE ID = %s", (id,))
    conn.commit()
    print("Data deleted successfully")
    cur.close()
    
     
cfg = Config()

conn = psycopg2.connect(
    host=cfg.POSTGRES_HOST,
    user=cfg.POSTGRES_USER,
    password=cfg.POSTGRES_PASSWORD,
    database=cfg.POSTGRES_DATABASE,
    port=cfg.POSTGRES_PORT
)

cur = conn.cursor()
    
create_table()

conn.close()