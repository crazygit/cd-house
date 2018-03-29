# -*- coding: utf-8 -*-
import werobot
from flask import current_app

from cdhouse.utils.misc import render
from cdhouse.web.models import CdHouseModel

robot = werobot.WeRoBot()
wx_client = robot.client


def render_projects(region):
    projects = CdHouseModel.query.filter(CdHouseModel.region == region,
                                         CdHouseModel.status != '报名结束').all()
    current_app.logger.debug(f'{region} has {len(projects)} projects')
    return render(
        'open_house.tpl',
        projects=projects,
        region=region,
    )


@robot.click
def region_click_handle(message):
    current_app.logger.debug(f'Receive click {message.key}')
    if message.key in ["天府新区", '高新南区', '双流区']:
        return render_projects(message.key)
    return f'不支持的区域: {message.key}'


@robot.text
def text_region(message):
    regions = current_app.config['REGIONS_PATTERN'].findall(message.content)
    if regions:
        return '\n'.join([render_projects(region) for region in regions])
    return f"找不到支持的区域: {message.content}"


@robot.subscribe
def subscribe():
    return '感谢您的关注！在这里你能及时获取成都房协发布的预售楼盘信息。更多实用功能正在开发中，敬请期待！🎉🎉🎉'


@robot.error_page
def error_page(url):
    return '<h1>Building ...</h1>'
