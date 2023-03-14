# from mysql import connector

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from base_db import BaseDB
from config import Config

cfg = Config()


class MySQLDB(BaseDB):
    def __init__(self):
        super().__init__(cfg.MYSQL_DATABASE)
        self.connect()
        self.create_table()
        self.close()

    def connect(self):
        pass
        # self.conn = connector.connect(
        #     host=cfg.MYSQL_HOST,
        #     user=cfg.MYSQL_USER,
        #     password=cfg.MYSQL_PASSWORD,
        # )
        # self.conn.autocommit = True # self.conn.autocommit(True)
        # self.cursor = self.conn.cursor()
        # self.create_db()
        
    def create_db(self):
        cursor =  self.cnx.cursor()
        DB_NAME = cfg.MYSQL_DATABASE
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        # self.cnx.commit()
        cursor.close()          
                
    def create_table(self):
        cursor =  self.cnx.cursor()
    
        create_table_query = """
        CREATE TABLE {} (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        type_plane VARCHAR(255) NOT NULL,
        start_date DATE NOT NULL,
        operation_date DATE NOT NULL,
        PRIMARY KEY (id)
        )
        """.format('planes')
        cursor.execute(create_table_query)
        # self.cnx.commit()
        cursor.close()
        
    def close(self):
        self.cnx.close()
    