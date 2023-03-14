class BaseDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = None
        self.cursor = None

    def connect(self):
        pass

    def disconnect(self):
        pass

    def create_table(self):
        pass

