from collections import namedtuple


class Handler:
    def __init__(self, request):
        self.request = request
        self.__response = namedtuple("Response", "status data")
    
    async def _request_validation(self):
        return self.request
    
    async def get_post_data(self):
        return None
    
    @property
    def response(self):
    #     db = {}
    # form = await request.post()
    # db['first_name'] = form.get("firstname")
    # db['last_name'] = form.get("lastname")
    # db['email'] = form.get("email")
    # db['username'] = form.get("username")
    # db['password'] = form.get("password")
    # users = request.app['db'].insert_one(db)
        return self.__response("Response", 200, "OK")
