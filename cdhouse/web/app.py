# -*- coding: utf-8 -*-
import werobot

from cdhouse.web.settings import WECHAT_TOKEN

robot = werobot.WeRoBot(token=WECHAT_TOKEN)


@robot.subscribe
def subscribe(message):
    return '感谢您的关注，在这里你能及时获取成都房协发布的预售楼盘信息。更多实用功能正在开发中，尽请期待！🎉🎉🎉'
