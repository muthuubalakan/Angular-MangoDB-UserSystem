from aiohttp import web
import os
import addict
import json
import sys
import logging
import asyncio
import pymongo


log = logging.getLogger()

PATH = os.path.dirname(os.path.realpath(__file__))

STATIC = PATH + "/static"
INDEX_HTML = "index.html"
CONFIG_FILE = "assets/conf.json"


async def check_credentials(db, username, password):
    check_user = db.find_one({"username": username})
    if not check_user:
        return False
    pass_check = check_user["password"]
    if pass_check != password:
        return False
    return True


def check_file(filename):
    if not os.path.isfile(filename):
        return False
    f = open(filename).read()
    return f


async def home(request):
    filename = check_file(INDEX_HTML)
    return web.Response(text=filename, content_type="text/html")


async def sign(request):
    db = {}
    form = await request.post()
    db['first_name'] = form.get("firstname")
    db['last_name'] = form.get("lastname")
    db['email'] = form.get("email")
    db['username'] = form.get("username")
    db['password'] = form.get("password")
    users = request.app['db'].insert_one(db)
    print(db)
    return web.HTTPFound('/')


async def login(request):
    form = await request.post()
    username = form.get("username")
    password = form.get("password")
    db = request.app['db']
    if not check_credentials(db, username, password):
        return web.Response(text="<h1>Wrong password or username</h1>")   
    return web.HTTPFound('/')


def setup_routes(app):
    app.router.add_route("GET", "/", home)
    app.router.add_route("POST", "/log", login)
    app.router.add_static("/static/", STATIC, name="static")
    app.router.add_route("POST", "/sign", sign)


def init_logging(conf):
    log_level_conf = "warning"
    if conf.common.logging:
        log_level_conf = conf.common.logging
    numeric_level = getattr(logging, log_level_conf.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: {}'.format(numeric_level))
    logging.basicConfig(level=numeric_level, format='%(message)s')
    log.error("Log level configuration: {}".format(log_level_conf))


def load_configuration_file(filename):
    with open(filename) as f:
        return addict.Dict(json.load(f))


def main(filename):
    app = web.Application()
    conf = load_configuration_file(filename)
    init_logging(conf)
    client = pymongo.MongoClient(conf.db.uri)
    db = client[conf.db.db_name]
    customer_db = db['new_users']
    app['db'] = customer_db
    setup_routes(app)
    web.run_app(app, host=conf.common.host, port=conf.common.port)


if __name__ == '__main__':
    sys.stdout.write("Starting the App....\n")
    if not check_file(CONFIG_FILE):
        sys.stderr.write("configuration file is mising\n")
    main(CONFIG_FILE)