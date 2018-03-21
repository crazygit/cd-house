# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CdhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # 唯一编号
    project_uuid = scrapy.Field()
    # 区域
    region = scrapy.Field()
    # 项目名称
    community_name = scrapy.Field()
    # 预售证号
    sell_no = scrapy.Field()
    # 预售范围
    sell_range = scrapy.Field()
    # 住房套数
    houses = scrapy.Field()
    # 开发商咨询电话
    tel = scrapy.Field()
    # 登记开始时间
    start_time = scrapy.Field()
    # 登记结束时间
    end_time = scrapy.Field()
    # 项目报名状态
    status = scrapy.Field()
