# -*- coding: utf-8 -*-
import urllib.parse

import click
from flask import current_app, url_for
from flask.cli import FlaskGroup


def create_app(info):
    from cdhouse.web import app_factory
    # todo: 根据部署环境设置启动配置
    return app_factory()


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass


@cli.command()
def create_menu():
    """创建微信自定义菜单"""
    from cdhouse.web.werobot import wx_client

    click.echo(wx_client.create_menu(current_app.config['WECHAT_CUSTOM_MENU']))


@cli.command()
def list():
    """列出当前所有的路由信息"""
    output = []
    with current_app.test_request_context():
        for rule in current_app.url_map.iter_rules():
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            line = urllib.parse.unquote("{:50s} {:20s} {}".format(
                rule.endpoint, methods, url))
            output.append(line)

        for line in sorted(output):
            click.echo(line)


if __name__ == '__main__':
    cli()
