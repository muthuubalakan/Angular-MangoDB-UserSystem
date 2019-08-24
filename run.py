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
from settings import PATH, STATIC, CONFIG_FILE
from scripts import Handler, DatabaseEngine, AppView


log = logging.getLogger()


def setup_routes(app):
    view = app["view"]
    app.router.add_route("GET", "/", view.home)
    app.router.add_route("POST", "/log", view.login)
    app.router.add_static("/static/", STATIC, name="static")
    app.router.add_route("POST", "/sign", view.sign_up)


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
    app["view"] = AppView()
    conf = load_configuration_file(filename)
    init_logging(conf)
    app['db'] = DatabaseEngine(uri=conf.db.uri,
                  db_name=conf.db.db_name,
                  collecton="users")
    setup_routes(app)
    web.run_app(app, host=conf.common.host, port=conf.common.port)


if __name__ == '__main__':
    sys.stdout.write("Starting the App....\n")
    assert os.path.isfile(CONFIG_FILE),(
        'Configuration file required.'
    )
    main(CONFIG_FILE)
