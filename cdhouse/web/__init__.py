# -*- coding: utf-8 -*-
from dash import Dash
from flask import Flask
from werobot.contrib.flask import make_view

from cdhouse.web import settings
from cdhouse.web.extensions import db
from cdhouse.web.werobot import robot
from cdhouse.web.dash import config_dash


def app_factory():
    app = Flask(__name__)
    config_app(app)
    config_werobot(app)
    config_database(app)
    dash_factory(app)
    return app


def config_database(app):
    db.init_app(app)
    db.app = app


def config_app(app):
    app.config.from_object(settings)


def config_werobot(app):
    robot.config['TOKEN'] = app.config['WECHAT_TOKEN']
    robot.config['APP_ID'] = app.config['WECHAT_APP_ID']
    robot.config['APP_SECRET'] = app.config['WECHAT_APP_SECRET']

    app.add_url_rule(
        rule='/robot/',
        endpoint='werobot',
        view_func=make_view(robot),
        methods=['GET', 'POST'])


def dash_factory(app):
    dash_app = Dash(server=app)
    config_dash(dash_app)
