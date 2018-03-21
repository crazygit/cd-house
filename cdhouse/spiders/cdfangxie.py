# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import FormRequest

from cdhouse.items import CdhouseItem
from cdhouse.loader import CdHouseItemLoader


class CdfangxieSpider(scrapy.Spider):
    name = 'cdfangxie'
    allowed_domains = ['171.221.172.13']
    url = 'http://171.221.172.13:8888/lottery/accept/projectList'
    start_urls = [url]

    def parse(self, response):
        pages = response.css(
            'div.pages-box a:last-child::attr(onclick)').extract_first()
        pages = self.parse_page_number(pages)
        for page in range(1, pages + 1):
            yield FormRequest(
                url=self.url,
                method='POST',
                dont_filter=True,
                callback=self.parse_page,
                formdata={
                    'pageNo': str(page),
                    'regioncode': '00',
                })

    def parse_page_number(self, str):
        m = re.search('(\d+)', str)
        if m:
            return int(m.groups()[0])

    def parse_page(self, response):
        for selector in response.css('table.nav-table tbody tr'):
            l = CdHouseItemLoader(item=CdhouseItem(), selector=selector)
            l.add_xpath('project_uuid', './td[1]/text()')
            l.add_xpath('region', './td[3]/text()')
            l.add_xpath('community_name', './td[4]/text()')
            l.add_xpath('sell_no', './td[5]/text()')
            l.add_xpath('sell_range', './td[6]/text()')
            l.add_xpath('houses', './td[7]/text()')
            l.add_xpath('tel', './td[8]/text()')
            l.add_xpath('start_time', './td[9]/text()')
            l.add_xpath('end_time', './td[10]/text()')
            l.add_xpath('status', './td[11]/text()')
            yield l.load_item()
