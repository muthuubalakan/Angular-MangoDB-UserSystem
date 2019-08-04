#!/usr/bin/python
# coding: utf-8

import os
import addict
import json
import sys
import logging
import asyncio
import pymongo
from aiohttp import web
from collections import OrderedDict
from settings import *
from scripts import Handler


log = logging.getLogger()

    
def check_file(filename):
    if not os.path.isfile(filename):
        return False
    return open(filename).read()

async def home(request):
    if not check_file(INDEX_HTML):
        return web.Response(text="<h6>Server Error</h6>")
    return web.Response(text=check_file(INDEX_HTML), content_type="text/html")

async def check_credentials(db, username, password):
    check_user = db.find_one({"username": username})
    if not check_user:
        return False
    pass_check = check_user["password"]
    if pass_check != password:
        return False
    return True

async def sign_up(self, request):
    handler = Handler(request)
    status, response = handler.response
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
    app.router.add_route("POST", "/sign", sign_up)


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
    # client = {} #pymongo.MongoClient(conf.db.uri)
    # db = client[conf.db.db_name]
    # customer_db = db['new_users']
    app['db'] = {} #customer_db
    setup_routes(app)
    web.run_app(app, host=conf.common.host, port=conf.common.port)


if __name__ == '__main__':
    sys.stdout.write("Starting the App....\n")
    if not check_file(CONFIG_FILE):
        sys.stderr.write("configuration file is mising\n")
    main(CONFIG_FILE)