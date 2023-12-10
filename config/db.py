from pymongo import MongoClient
import os


class MongoDBSingleton:
    _instance = None
    db: MongoClient

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoDBSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.db = MongoClient()
            cls._instance.connect_to_mongodb()
        return cls._instance

    def connect_to_mongodb(self):
        print('Starting connection')
        user = os.getenv('MONGO_USER','admin')
        password = os.getenv('MONGO_PASS','adminpassword')
        host = os.getenv('MONGO_HOST','localhost')
        port = os.getenv('MONGO_PORT','27017')
        
        uri = f"mongodb://{user}:{password}@{host}:{port}"
        self.db = MongoClient(uri)
        
    def close_connection(self):
        print('closing connection')
        if self.db:
            self.db.close()

    def get_database(self):
        return self.db