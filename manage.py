# -*- coding: utf-8 -*-
import logging

import click
from flask import Flask
from werobot.contrib.flask import make_view

from cdhouse.web.app import create_menu, robot

logging.basicConfig(
    level=logging.DEBUG,
    format=
    '%(asctime)s %(name)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)


@click.group()
def cli():
    pass


@cli.command()
def create_wechat_menu():
    """创建微信自定义菜单"""

    click.echo(create_menu())


@cli.command()
def run():
    """run web server"""
    app = Flask(__name__)
    app.add_url_rule(
        rule='/robot/',
        endpoint='werobot',
        view_func=make_view(robot),
        methods=['GET', 'POST'])
    app.logger.info('Start server')
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    cli()
