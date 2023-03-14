from mysql_db import MySQLDB
from postgres_db import PostgresDB
from sqlite_db import SQLiteDB

class DBFactory:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_db(self):
        if self.db_name == "sqlite":
            return SQLiteDB(self.db_name)
        elif self.db_name == "postgres":
            return PostgresDB(self.db_name)
        elif self.db_name == "mysql":
            return MySQLDB(self.db_name)