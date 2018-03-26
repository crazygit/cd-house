# -*- coding: utf-8 -*-

from scrapy import signals

from cdhouse.misc import render
from cdhouse.sender import SlackSender


class ItemStats(object):
    def __init__(self, stats, web_hook_url):
        self.stats = stats
        self.new_items = []
        self.update_items = []
        self.sender = SlackSender(web_hook_url)

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.stats, crawler.settings['SLACK_WEBHOOK_URL'])
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
            self.sender.send(
                render(
                    'house.tpl',
                    new_items=self.new_items,
                    update_items=self.update_items))
        if self.stats.get_value('log_count/ERROR', 0) > 0:
            self.sender.send('%d ERROR when crawl' % self.stats.get_value(
                'log_count/ERROR', 0))
