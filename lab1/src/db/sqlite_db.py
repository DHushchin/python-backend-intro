import sqlite3
from db.base_db import BaseDB


class SQLiteDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()
        

    def connect(self):
        self.conn = sqlite3.connect(self.cfg.SQLITE_DATABASE)
        self.cursor = self.conn.cursor()


    def create_table(self):
        with self.conn:
             self.conn.execute(
                '''CREATE TABLE IF NOT EXISTS planes (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type_plane TEXT NOT NULL
                )''')  
             
        print("SQLite: Table created successfully")   
        
            
    def insert(self, data):
        with self.conn:
            self.conn.execute('INSERT INTO planes (id, name, type_plane) VALUES (?, ?, ?)', data)  
        
        
    def truncate(self):
        with self.conn:
            self.conn.execute('DELETE FROM planes')
           
            
    def select_all(self):
        with self.conn:
            rows = self.conn.execute("SELECT * FROM planes").fetchall() 
              
        return rows
                   
        
    def get_columns(self):
        with self.conn:
            cursor = self.conn.execute(f"SELECT * FROM planes")
            names = [description[0] for description in cursor.description]
            
        return names
        
        
    def __del__(self):
        self.conn.close() 
        