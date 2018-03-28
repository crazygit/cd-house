# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from cdhouse.items import CdhouseItem
from cdhouse.models import CdHouseModel, UpdateHistoryModel, get_session
from scrapy.exceptions import DropItem, NotConfigured
from sqlalchemy.exc import IntegrityError


class SQLAlchemyPipeline(object):

    def __init__(self, url):
        self.session = get_session(url)

    def close_spider(self, spider):
        self.session.close()

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings['DATABASE_URL']:
            raise NotConfigured
        return cls(crawler.settings['DATABASE_URL'])

    def process_item(self, item, spider):
        model_class = None
        if isinstance(item, CdhouseItem):
            model_class = CdHouseModel
        if model_class:
            self.save_item(item, spider, model_class)
        else:
            spider.logger.warning('Unhandled Item %s' % item)

        return item

    def save_item(self, item, spider, model_class):
        unique_column = model_class.get_unique_column()
        unique_condition = {unique_column: item[unique_column]}
        model = self.session.query(model_class).filter_by(
            **unique_condition).first()
        if model:
            update_info = model.is_updated(item)
            if not update_info:
                raise DropItem(f"Duplicate item: {item}")
            self.session.bulk_insert_mappings(UpdateHistoryModel, update_info)
            item['flag'] = 'update'
            model.init_or_update(item)
        else:
            item['flag'] = 'new'
            model = model_class(item)
            self.session.add(model)
        try:
            self.session.commit()
        except IntegrityError as e:
            spider.logger.error("Save %s failed, %s" % (item, e))
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            spider.logger.error("Add %s failed, %s" % (item, e))
