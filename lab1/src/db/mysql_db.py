from mysql import connector
from db.base_db import BaseDB


class MySQLDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()


    def connect(self):
        self.conn = connector.connect(
            host=self.cfg.MYSQL_HOST,
            user=self.cfg.MYSQL_USER,
            password=self.cfg.MYSQL_PASSWORD,
            port = self.cfg.MYSQL_PORT
        )
        self.conn.autocommit = True
        self.conn._buffered = True
        self.create_db()
              
              
    def create_db(self):
        cursor = self.conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.cfg.MYSQL_DATABASE}")
        cursor.close()   
        print("MySQL: Database created successfully")       
            
                        
    def create_table(self):
        cursor = self.conn.cursor()
    
        create_table_query = """
        CREATE TABLE IF NOT EXISTS {} 
        (
            id INT PRIMARY KEY NOT NULL,
            name VARCHAR(255) NOT NULL,
            type_plane VARCHAR(255) NOT NULL,
            start_date DATE NOT NULL,
            operation_date DATE NOT NULL
        )
        """.format(f'{self.cfg.MYSQL_DATABASE}.planes')
        cursor.execute(create_table_query)
        cursor.close()       
        print("MySQL: Table created successfully")
        
        
    def select_all(self):
        select_all_query =  """
                                SELECT * FROM {}
                            """.format(f'{self.cfg.MYSQL_DATABASE}.planes')
        cursor = self.conn.cursor()
        cursor.execute(select_all_query)
        rows = cursor.fetchall() 
        cursor.close()    
        return rows
        
        
    def insert(self, data):
        cursor = self.conn.cursor()
        insert_query =  """
                            INSERT INTO {} (ID, NAME, TYPE_PLANE, START_DATE, OPERATION_DATE) VALUES (%s, %s, %s, %s, %s)
                        """.format(f'{self.cfg.MYSQL_DATABASE}.planes')
        cursor.execute(insert_query, data)
        cursor.close()
        print("MySQL: Data inserted successfully")
       
        
    def truncate(self):
        cursor = self.conn.cursor()
        truncate_query = """
                             TRUNCATE TABLE {}
                         """.format(f'{self.cfg.MYSQL_DATABASE}.planes')
        cursor.execute(truncate_query)
        cursor.close()
        print("MySQL: Table truncated successfully")
        
        
    def export_query(self):
        cursor = self.conn.cursor()
        query = """
                    SELECT id + 1, upper(name), upper(type_plane) FROM {}
                """.format(f'{self.cfg.MYSQL_DATABASE}.planes')
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
                   
        
    def get_columns(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.cfg.MYSQL_DATABASE}.planes")
        return [description[0] for description in cursor.description]
        
        
    def __del__(self):
        self.conn.close() 
    