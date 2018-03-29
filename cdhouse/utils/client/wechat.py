# -*- coding: utf-8 -*-
import time

from werobot.client import Client as WerobotClient

from cdhouse.utils.client import Client


class WeChatClient(WerobotClient, Client):

    @classmethod
    def get_client(cls, crawler):
        app_id = crawler.settings.get('WECHAT_APP_ID', None)
        app_secret = crawler.settings.get('WECHAT_APP_SECRET', None)
        if app_id and app_secret:
            return cls(config={'APP_ID': app_id, 'APP_SECRET': app_secret})

    def send(self, msg):
        '''
        群发文本消息。

        :param msg: 消息正文
        :return: 返回的 JSON 数据包
        '''
        self.logger.debug(f"> {msg}")
        return self.post(
            url='https://api.weixin.qq.com/cgi-bin/message/mass/sendall',
            data={
                'filter': {
                    'is_to_all': True,
                },
                'text': {
                    'content': msg,
                },
                'msgtype': 'text',
                'clientmsgid': int(time.time() * 1000)
            })
