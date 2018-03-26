# -*- coding: utf-8 -*-

from scrapy import signals


class ItemStats(object):
    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.stats)
        crawler.signals.connect(o.item_scraped, signal=signals.item_scraped)
        return o

    def item_scraped(self, item, spider):
        if item['flag'] == 'new':
            self.stats.inc_value('item_new_scraped_count', spider=spider)
        elif item['flag'] == 'update':
            self.stats.inc_value('item_updated_scraped_count', spider=spider)
