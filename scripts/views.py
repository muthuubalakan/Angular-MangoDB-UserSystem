import os
import asyncio
from aiohttp import web
from .handler import Handler
from settings import PATH


INDEX_HTML = os.path.join(PATH, "app","index.html")


class AppView(Handler):

    def check_file(self, filename):
        if not os.path.isfile(filename):
            return False
        return open(filename).read()

    async def home(self, request):
        if not self.check_file(INDEX_HTML):
            return web.Response(text="<h6>Server Error</h6>")
        return web.Response(text=self.check_file(INDEX_HTML), content_type="text/html")

    async def sign_up(self, request):
        cookie = request.get('coin', None)
        if cookie:
            return web.HTTPFound('/')
        
        signup_form = await request.post()
        db = request.app['db']
        user_created = self.create_user(signup_form, db)
        if not user_created:
            return web.HTTPBadRequest()
        return web.HTTPFound('/login')

    async def login(self, request):
        cookie = request.get('coin', None)
        if cookie:
            return web.HTTPFound('/')
        
        form = await request.post()
        db = request.app['db']

        if not self.check_user(db, form):
            return web.Response(text="<h1>Wrong password or username</h1>")   
        return web.HTTPFound('/')