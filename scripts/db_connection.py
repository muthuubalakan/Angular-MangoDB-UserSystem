import pymongo
import asyncio


class DatabaseEngine:
    """
    Database engine process mongo db connection & queries.
    """
    def __init__(self, uri, db_name, collecton, **kwargs):
        self.client = self.connect(uri)
        self.db = self.client[db_name]
        self.connection = self.db[collecton]
    
    async def connect(self, uri):
        """
        Connnect make the connection to the mongodb with uri which suppose to have credentials.

        :param uri: Full mongo db uri with credentials.
        :type uri: string, optional
        returns mongo db connection
        """
        return pymongo.MongoClient(uri)
    
    
    async def query(self, query, **kwargs):
        return None