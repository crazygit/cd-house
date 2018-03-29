# -*- coding: utf-8 -*-
from dash import Dash
from flask import Flask
from werobot.contrib.flask import make_view

import cdhouse.web.settings
from cdhouse.web.extensions import db
from cdhouse.web.werobot import robot


def app_factory():
    app = Flask(__name__)
    config_app(app)
    config_werobot(app)
    config_database(app)
    config_dash(app)
    return app


def config_database(app):
    db.init_app(app)
    db.app = app


def config_app(app):
    app.config.from_object(cdhouse.web.settings)


def config_werobot(app):
    robot.config['TOKEN'] = app.config['WECHAT_TOKEN']
    robot.config['APP_ID'] = app.config['WECHAT_APP_ID']
    robot.config['APP_SECRET'] = app.config['WECHAT_APP_SECRET']

    app.add_url_rule(
        rule='/robot/',
        endpoint='werobot',
        view_func=make_view(robot),
        methods=['GET', 'POST'])


def config_dash(app):
    from cdhouse.web.dash import layout
    dash_app = Dash(server=app)
    # 设置页面标题
    dash_app.title = '成都房协发布房源统计数据'
    # 设置页面布局
    dash_app.layout = layout
