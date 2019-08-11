from collections import namedtuple
from .db_connection import DatabaseEngine


class Handler:
    def __init__(self, request):
        self.request = request
        self.__response = namedtuple("Response", "status data")
        self.post_data = {}
    
    async def _request_validation(self):
        return self.request
    
    async def insert_post_data(self):
        assert self.request.method == 'POST', (
            'Method not allowed.'
        )
        form = await self.request.post()
        self.post_data['firstname'] = form.get("firstname")
        self.post_data['lastname'] = form.get("lastname")
        self.post_data['email'] = form.get("email")
        self.post_data['username'] = form.get("username")
        self.post_data['password'] = form.get("password")
        mongo_id = (self.post_data)
        if not mongo_id:
            raise SystemError
        return self.__response(201, "created")
    
    @property
    def response(self):
        return self.__response(200, "OK")
