# -*- coding: utf-8 -*-
import logging


class Client(object):

    @property
    def logger(self):
        return logging.getLogger(__class__.__name__)

    @classmethod
    def get_client(cls, crawler):
        """从爬虫获取配置信息"""
        raise NotImplementedError

    def send(self, msg):
        """群发文本消息"""
        raise NotImplementedError


from .slack import SlackClient
from .wechat import WeChatClient
