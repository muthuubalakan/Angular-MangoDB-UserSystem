import pymongo
import asyncio


class DatabaseEngine:
    """
    Database engine process mongo db connection & queries.
    """
    def __init__(self, uri, db_name, collecton, **kwargs):
        self.client = self.connect(uri)
        self.db = self.client[db_name]
        self.loop = asyncio.get_event_loop()
        self.connection = await self.db[collecton]
    
    async def connect(self, uri):
        """
        Connnect make the connection to the mongodb with uri which suppose to have credentials.

        :param uri: Full mongo db uri with credentials.
        :type uri: string, optional
        returns mongo db connection
        """
        return pymongo.MongoClient(uri)
    
    async def query(self, query, **kwargs):
        user = query.pop("username", None)
        if not user: return None, None
        password = user.get("password", None)
        return user, password
    
    def insert_doc(self, doc):
        assert isinstance(doc, dict), (
            f'{type(self).__name__} Error: Expected dict. '
        )
        return self.connection.insert_one(doc)