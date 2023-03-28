from peewee import Model, CharField, IntegerField, DateField, PostgresqlDatabase
from db.base_db import BaseDB

class PostgresDB(BaseDB):
    def __init__(self):
        super().__init__()

        self.connect()
        self.create_table()

    def connect(self):
        self.db = PostgresqlDatabase(
            self.cfg.POSTGRES_DATABASE,
            host=self.cfg.POSTGRES_HOST,
            user=self.cfg.POSTGRES_USER,
            password=self.cfg.POSTGRES_PASSWORD,
            port=self.cfg.POSTGRES_PORT,
        )
        
        self.db.connect()
        print("Postgres: Connected successfully")

    def create_table(self):
        class Plane(Model):
            id = IntegerField(primary_key=True)
            name = CharField()
            type_plane = CharField()
            start_date = DateField()
            operation_date = DateField()

            class Meta:
                database = self.db
                table_name = 'planes'
        

        self.plane = Plane
        self.db.create_tables([Plane], safe=True)
        print("Postgres: Table created successfully")

    def select_all(self):
        rows = self.plane.select().tuples()
        return rows

    def insert(self, data):
        self.plane.create(id=data[0], name=data[1], type_plane=data[2], start_date=data[3], operation_date=data[4])
        print("Postgres: Data inserted successfully")

    def update(self, data):
        plane = self.plane.get(self.plane.id == data[0])
        plane.name = data[1]
        plane.type_plane = data[2]
        plane.start_date = data[3]
        plane.operation_date = data[4]
        plane.save()
        print("Postgres: Data updated successfully")

    def delete(self, id):
        plane = self.plane.get(self.plane.id == id)
        plane.delete_instance()
        print("Postgres: Data deleted successfully")

    def get_columns(self):
        return [field.name for field in self.plane._meta.sorted_fields]

    def __del__(self):
        return self
