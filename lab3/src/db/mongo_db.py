from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import ObjectId
from db.base_db import BaseDB

class MongoDB(BaseDB):
    def __init__(self):
        super().__init__()

        self.connect()
        self.create_collection()

    def connect(self):
        try:
            self.client = MongoClient(self.cfg.MONGO_URI)
            self.db = self.client[self.cfg.MONGO_DATABASE]
            print("MongoDB: Connected successfully")
        except ConnectionFailure as e:
            print(f"MongoDB: Could not connect to server: {e}")

    def create_collection(self):
        self.collection = self.db["planes"]
        print("MongoDB: Collection created successfully")

    def select_by_id(self, id):
        row = self.collection.find_one({"_id": ObjectId(id)})
        if row:
            row["id"] = str(row["_id"])  # Convert ObjectId to string
            del row["_id"]  # Remove ObjectId field
        return row

    def select_all(self):
        rows = list(self.collection.find())

        result = []
        for idx, row in enumerate(rows):
            result.insert(idx, {'_id': str(row['_id']), 'name': row['name'], 'type_plane': row['type_plane'], 'start_date': row['start_date'], 'operation_date': row['operation_date']})
        converted_list = [(str(d['_id']), d['name'], d['type_plane'], d['start_date'], d['operation_date']) for d in result]

        return converted_list

    def insert(self, data):
        self.collection.insert_one({"name": data[0], "type_plane": data[1], "start_date": data[2], "operation_date": data[3]})
        print("MongoDB: Data inserted successfully")

    def update(self, data):
        self.collection.update_one({"_id": ObjectId(data[0])}, {"$set": {"name": data[1], "type_plane": data[2], "start_date": data[3], "operation_date": data[4]}})
        print("MongoDB: Data updated successfully")

    def delete(self, id):
        print(id)
        self.collection.delete_one({"_id": ObjectId(id)})
        print("MongoDB: Data deleted successfully")

    def get_columns(self):
        return ["_id", "name", "type_plane", "start_date", "operation_date"]

    def get_columns_fields(self):
        return ["name", "type_plane", "start_date", "operation_date"]

    def __del__(self):
        self.client.close()
