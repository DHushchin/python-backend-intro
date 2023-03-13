import sqlite3

class SQLLite:
    def __init__(self, db_name):
        self.db_name = db_name
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
            
    def close(self):
        self.conn.close()
        