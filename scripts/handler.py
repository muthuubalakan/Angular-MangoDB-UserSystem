from collections import namedtuple


class Handler:
    """
    Handles incoming request

    :param request: HTTP request object
    :methods : `create_user(db, form)`
    """
    def __init__(self, request=None):
        self.request = request
        self.__response = namedtuple("Response", "status data")
        self.post_data = {}
    
    def check_user(self, db, form):
        username = form.get("username")
        if not username: return False
        password = form.get("password")
        if not password: return False
        user = db.find_user(username)
        if not user:
            return False
        pwd = user.get('password', None)
        if pwd != password:
            return False
        return True
    
    def create_user(self, db, form):
        self.post_data['firstname'] = form.get("firstname")
        self.post_data['lastname'] = form.get("lastname")
        self.post_data['email'] = form.get("email")
        username = form.get("username", None)
        password = form.get("password")
        if not username and not password:
            return False
        self.post_data['username'] = username
        self.post_data['password'] = password
        mongo_id = db.create_user(self.validate(self.post_data))
        if not mongo_id:
            return False
        return True
    
    def validate(self, doc):
        return doc