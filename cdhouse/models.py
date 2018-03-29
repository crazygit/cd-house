# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class ModelMixin(object):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci',
    }
    id = Column(Integer, primary_key=True)

    def get_identity(self):
        raise NotImplementedError

    @staticmethod
    def get_unique_column():
        raise NotImplementedError

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    def parse_item(self, item):
        for column in self.columns:
            if column in item:
                setattr(self, column, item[column])


def get_session(url, echo=False):
    engine = create_engine(url, echo=echo)
    Session = sessionmaker(bind=engine)
    # create table
    Base.metadata.create_all(engine)
    return Session()


class CdHouseModel(Base, ModelMixin):
    __tablename__ = 'house'
    # 唯一编号
    project_uuid = Column(String(100), doc='唯一编号', unique=True, nullable=False)
    community_name = Column(String(100), doc='项目名称', nullable=False)
    region = Column(String(100), doc='区域', nullable=False)
    sell_no = Column(String(100), doc='预售证号', nullable=False)
    sell_range = Column(String(255), doc='预售范围', nullable=False)
    houses = Column(Integer, doc='住房套数', nullable=False)
    tel = Column(String(100), doc='开发商咨询电话', nullable=False)
    start_time = Column(DateTime(), doc='登记开始时间', nullable=False)
    end_time = Column(DateTime(), doc='登记结束时间', nullable=False)
    status = Column(String(64), doc='项目报名状态', nullable=False)
    created_on = Column(
        DateTime, nullable=False, default=datetime.now, doc='爬取时间')
    update_on = Column(
        DateTime, nullable=True, onupdate=datetime.now, doc='更新时间')

    def __init__(self, item):
        self.init_or_update(item)

    def init_or_update(self, item):
        self.parse_item(item)

    def get_identity(self):
        return self.project_uuid

    @staticmethod
    def get_unique_column():
        return 'project_uuid'

    def is_updated(self, item):
        updated_columns = []
        for column in self.columns:
            if column in item and getattr(self, column) != item[column]:
                updated_columns.append({
                    "column_name": column,
                    "updated_from": getattr(self, column),
                    "updated_to": item[column],
                    "project_uuid": self.project_uuid
                })
        return updated_columns


class UpdateHistoryModel(Base, ModelMixin):
    __tablename__ = 'update_history'

    project_uuid = Column(String(100), ForeignKey('house.project_uuid'))
    column_name = Column(String(100), doc='改变的字段', nullable=False)
    updated_from = Column(String(255), doc='字段的原始值', nullable=True)
    updated_to = Column(String(255), doc='字段新的值', nullable=True)
    updated_on = Column(
        DateTime, nullable=False, default=datetime.now, doc='更新时间')
