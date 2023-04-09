from db.mongo_db import MongoDB


class DBFactory:
    def __init__(self):
        self.db = None

    def get_db(self, db_name):
        if db_name == 'mongodb':
            self.db = MongoDB()
        return self.db
        