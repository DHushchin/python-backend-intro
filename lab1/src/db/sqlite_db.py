import sqlite3
from base_db import BaseDB

class SQLiteDB(BaseDB):
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_table()
        self.disconnect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        with  self.conn:
             self.conn.execute(
                '''CREATE TABLE IF NOT EXISTS planes (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type_plane TEXT NOT NULL,
                    start_date DATE NOT NULL,
                    operation_date DATE NOT NULL
                )'''
            )
            
    def insert_data(self, data):
        with self.conn:
            self.conn.execute(
                '''INSERT INTO planes (id, name, type_plane, start_date, operation_date) VALUES (?, ?, ?, ?, ?)''', data
            )
            
    def disconnect(self):
        self.conn.close()
        