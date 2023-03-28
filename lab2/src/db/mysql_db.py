from peewee import *
from db.base_db import BaseDB


class MySQLDB(BaseDB):
    def __init__(self):
        super().__init__()
        self.connect()
        self.create_table()

    def connect(self):
        self.db = MySQLDatabase(
            self.cfg.MYSQL_DATABASE,
            host=self.cfg.MYSQL_HOST,
            user=self.cfg.MYSQL_USER,
            password=self.cfg.MYSQL_PASSWORD,
            port=int(self.cfg.MYSQL_PORT),
        )
        self.db.connect()
        print("MySQL: Connected successfully")

    def create_table(self):
        class PlaneModel(Model):
            id = IntegerField(primary_key=True)
            name = CharField(max_length=255)
            type_plane = CharField(max_length=255)
            start_date = DateField()
            operation_date = DateField()

            class Meta:
                database = self.db
                table_name = "planes"
        
        self.plane = PlaneModel
        self.db.create_tables([PlaneModel], safe=True)
        print("MySQL: Table created successfully")

    def select_all(self):
        rows = list(self.plane.select().dicts())
        return [(row["id"], row["name"], row["type_plane"], row["start_date"], row["operation_date"]) for row in rows]

    def insert(self, data):
        plane = self.plane.create(
            id=data[0], name=data[1], type_plane=data[2], start_date=data[3], operation_date=data[4]
        )
        print(f"MySQL: Data inserted successfully: {plane.id}")

    def truncate(self):
        self.plane.delete().execute()
        print("MySQL: Table truncated successfully")

    def export_query(self):
        rows = self.plane.select(self.plane.id + 1, fn.upper(self.plane.name), fn.upper(self.plane.type_plane)).tuples()
        return rows

    def get_columns(self):
        return [field.name for field in self.plane._meta.sorted_fields]

    def __del__(self):
        self.db.close()
