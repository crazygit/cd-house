# -*- coding: utf-8 -*-
import werobot

from cdhouse.models import CdHouseModel, get_session
from cdhouse.utils.misc import render
from cdhouse.web.settings import (DATABASE_URL, ECHO_SQL, REGIONS_PATTERN,
                                  WECHAT_APP_ID, WECHAT_APP_SECRET,
                                  WECHAT_CUSTOM_MENU, WECHAT_TOKEN)

robot = werobot.WeRoBot(
    token=WECHAT_TOKEN, app_id=WECHAT_APP_ID, app_secret=WECHAT_APP_SECRET)
client = robot.client
db_session = get_session(DATABASE_URL, echo=ECHO_SQL)


def create_menu():
    return client.create_menu(WECHAT_CUSTOM_MENU)


def render_projects(region):
    projects = db_session.query(CdHouseModel).filter(
        CdHouseModel.region == region, CdHouseModel.status != '报名结束').all()
    return render(
        'open_house.tpl',
        projects=projects,
        region=region,
    )


@robot.click
def region_click_handle(message):
    if message.key in ["天府新区", '高新南区', '双流区']:
        return render_projects(message.key)
    return f'不支持的区域: {message.key}'


@robot.text
def text_region(message):
    regions = REGIONS_PATTERN.findall(message.content)
    if regions:
        return '\n'.join([render_projects(region) for region in regions])
    return f"找不到支持的区域: {message.content}"


@robot.subscribe
def subscribe():
    return '感谢您的关注！在这里你能及时获取成都房协发布的预售楼盘信息。更多实用功能正在开发中，敬请期待！🎉🎉🎉'


@robot.error_page
def error_page(url):
    return '<h1>Building ...</h1>'
