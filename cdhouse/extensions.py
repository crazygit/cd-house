# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from cdhouse.misc import render
from cdhouse.utils.client import SlackClient, WeChatClient
from scrapy import signals

logger = logging.getLogger(__name__)


class ItemStats(object):

    def __init__(self, stats, clients=None):
        self.stats = stats
        self.new_items = []
        self.update_items = []
        self.clients = clients or []

    def send(self, msg):
        for client in self.clients:
            if client:
                try:
                    client.send(msg)
                except Exception as e:
                    logger.error(e)

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(
            crawler.stats,
            clients=[
                SlackClient.get_client(crawler),
                WeChatClient.get_client(crawler)
            ])
        crawler.signals.connect(o.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def item_scraped(self, item, spider):
        if item['flag'] == 'new':
            self.stats.inc_value('item_new_scraped_count', spider=spider)
            self.new_items.append(item)
        elif item['flag'] == 'update':
            self.stats.inc_value('item_updated_scraped_count', spider=spider)
            self.update_items.append(item)

    def spider_closed(self, spider, reason):
        if self.new_items or self.update_items:
            msg = render(
                'house.tpl',
                new_items=self.new_items,
                update_items=self.update_items,
                update_time=datetime.strftime(datetime.now(),
                                              '%Y-%m-%d %H:%M:%S'))
            self.send(msg)
        if self.stats.get_value('log_count/ERROR', 0) > 0:
            self.send('%d ERROR when crawl' % self.stats.get_value(
                'log_count/ERROR', 0))
