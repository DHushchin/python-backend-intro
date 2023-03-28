from db.mysql_db import MySQLDB
from db.postgres_db import PostgresDB
from db.sqlite_db import SQLiteDB


class DBFactory:
    def __init__(self):
        self.db = None

    def get_db(self, db_name):
        if db_name == 'sqlite':
            self.db = SQLiteDB()
        elif db_name == 'mysql':
            self.db = MySQLDB()
        elif db_name == 'postgres':
            self.db = PostgresDB()
        return self.db
        