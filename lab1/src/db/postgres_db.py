# import psycopg2

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from base_db import BaseDB
from config import Config

cfg = Config()


class PostgresDB(BaseDB):
    def __init__(self):
        super().__init__(cfg.POSTGRES_DATABASE)
        self.connect()
        self.create_table()
        self.close()

    def connect(self):
        pass
        # self.conn = psycopg2.connect(
        #     host=cfg.POSTGRES_HOST, 
        #     user=cfg.POSTGRES_USER, 
        #     password=cfg.POSTGRES_PASSWORD,
        #     port=cfg.POSTGRES_PORT
        # )
        # self.conn.autocommit = True
        # self.cursor = self.conn.cursor()
        # self.create_db()
             
    def create_db(self):
        with self.conn.cursor() as cur:
            if cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{self.DB_NAME}'") == 0:
                cur.execute(f"CREATE DATABASE {self.DB_NAME}")
                            
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS planes
                    (id INT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    type_plane TEXT NOT NULL,
                    start_date DATE NOT NULL,
                    operation_date DATE NOT NULL);''')
        
        # self.conn.commit()
        print("Table created successfully")
        cur.close()

    def insert_data(self, id, name, type_plane, start_date, operation_date):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO planes (ID, NAME, TYPE_PLANE, START_DATE, OPERATION_DATE) VALUES {(id, name, type_plane, start_date, operation_date)}")
        # self.conn.commit()
        print("Data inserted successfully")
        cur.close()

    def select_data(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes")
        rows = cur.fetchall()
        for row in rows:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TYPE_PLANE = ", row[2])
            print("START_DATE = ", row[3],)
            print("OPERATION_DATE = ", row[4], "\n")
            
        cur.close()

    def update_data(self, id, name, type_plane, start_date, operation_date):
        cur = self.conn.cursor()
        cur.execute(f"UPDATE planes SET NAME = {name}, TYPE_PLANE = {type_plane}, START_DATE = {start_date}, OPERATION_DATE = {operation_date} WHERE ID = {id}")
        # self.conn.commit()
        print("Data updated successfully")
        cur.close()

    def delete_data(self, id):
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM planes WHERE ID = {id}")
        # self.conn.commit()
        print("Data deleted successfully")
        cur.close() 
        
    def disconnect(self):
        return super().disconnect()
    