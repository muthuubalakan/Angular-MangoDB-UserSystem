#!/usr/bin/python3
from pymongo import errors, MongoClient
import asyncio


class Connection(MongoClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'Connection({self._repr_helper()}'
    
    def connect(self, db, collection):
        try:
            client = self
            db = client[db]
            return db[collection]
        except errors.ConnectionError:
            print("error")
            
    async def exit(self):
        """abrupt exit"""
        return self.close()
    


class DatabaseEngine:
    """
    Database engine process mongo db connection & queries.
    """
    def __init__(self, uri, db_name, collection, **kwargs):
        self.client = Connection(uri)
        self.loop = asyncio.get_event_loop()
        self.connection = self.client.connect(db_name, collection)
    
    def find_user(self, username, password=None):
        return self.connection.find_one({'username': username}, {'_id':0})
    
    def delete_user(self, username):
        try:
            self.connection.delete_one({'username':username})
            return True
        except Exception:
            return False
    
    def update_user(self, oldvalue, newvalue):
        self.connection.update_one(oldvalue, newvalue)
    
    def create_user(self, doc):
        assert isinstance(doc, dict), (
            f'{type(self).__name__} Error: Expected dict. '
        )
        return self.connection.insert_one(doc).inserted_id