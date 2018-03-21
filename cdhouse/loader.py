# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class FormatTime(object):
    def __call__(self, values):
        return [
            datetime.strptime(value, '%Y-%m-%d %H:%M:%S') for value in values
        ]


class CdHouseItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    start_time_in = FormatTime()
    end_time_in = FormatTime()
