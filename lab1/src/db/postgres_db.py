import psycopg2
from db.base_db import BaseDB


class PostgresDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()


    def connect(self):
        self.conn = psycopg2.connect(
            host=self.cfg.POSTGRES_HOST, 
            user=self.cfg.POSTGRES_USER, 
            password=self.cfg.POSTGRES_PASSWORD,
            port=self.cfg.POSTGRES_PORT
        )
        self.conn.autocommit = True
        self.create_db()
            
                    
    def create_db(self):
        with self.conn.cursor() as cur:
            if cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{self.cfg.POSTGRES_DATABASE}'") == 0:
                cur.execute(f"CREATE DATABASE {self.cfg.POSTGRES_DATABASE}") 
        print("Postgres: Database created successfully")      
          
                            
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS planes
                    (id serial PRIMARY KEY,
                    name TEXT NOT NULL,
                    type_plane TEXT NOT NULL,
                    start_date DATE NOT NULL,
                    operation_date DATE NOT NULL);''')
        cur.close()
        print("Postgres: Table created successfully")   
        
        
    def select_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes")
        rows = cur.fetchall()
        cur.close()
        return rows


    def insert(self, data):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO planes (id, NAME, TYPE_PLANE, START_DATE, OPERATION_DATE) VALUES (DEFAULT, %s, %s, %s, %s)", data)
        cur.close()
        print("Postgres: Data inserted successfully")


    def update(self, data):
        cur = self.conn.cursor()
        data = (data[1], data[2], data[3], data[4], data[0])
        cur.execute("UPDATE planes SET NAME = %s, TYPE_PLANE = %s, START_DATE = %s, OPERATION_DATE = %s WHERE ID = %s", data)
        cur.close()
        print("Postgres: Data updated successfully")


    def delete(self, id):
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM planes WHERE ID = {id}")
        print("Data deleted successfully")
        cur.close() 
             
    
    def get_columns(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM planes")
        return [description[0] for description in cur.description]
    
    
    def __del__(self):
        return self.conn.close()
    