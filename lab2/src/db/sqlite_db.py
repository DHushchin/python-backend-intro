from peewee import *
from db.base_db import BaseDB


class SQLiteDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()

    def connect(self):
        self.db = SqliteDatabase(self.cfg.SQLITE_DATABASE)
        self.db.connect()
        print("SQLite: Connected successfully")

    def create_table(self):
        class PlaneModel(Model):
            id = IntegerField(primary_key=True)
            name = CharField(max_length=255)
            type_plane = CharField(max_length=255)

            class Meta:
                table_name = "planes"
                database = self.db

        self.plane = PlaneModel
        self.db.create_tables([PlaneModel])
        print("SQLite: Table created successfully")

    def insert(self, data):
        plane = self.plane.create(id=data[0], name=data[1], type_plane=data[2])
        print(f"SQLite: Data inserted successfully: {plane.id}")

    def truncate(self):
        self.plane.delete().execute()
        print("SQLite: Table truncated successfully")

    def select_all(self):
        rows = list(self.plane.select().tuples())
        return rows

    def get_columns(self):
        return [field.name for field in self.plane._meta.sorted_fields]

    def __del__(self):
        self.db.close()
