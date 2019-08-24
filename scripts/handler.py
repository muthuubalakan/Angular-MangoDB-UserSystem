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
        password = form.get("password")
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
        self.post_data['username'] = form.get("username")
        self.post_data['password'] = form.get("password")
        mongo_id = db.create_user(self.post_data)
        if not mongo_id:
            return False
        return True