# -*- coding: utf-8 -*-
from datetime import datetime

from cdhouse.crawler.models import ModelMixin
from cdhouse.web.extensions import db


class CdHouseModel(db.Model, ModelMixin):
    __tablename__ = 'house'

    project_uuid = db.Column(
        db.String(100), doc='唯一编号', unique=True, nullable=False)
    community_name = db.Column(db.String(100), doc='项目名称', nullable=False)
    region = db.Column(db.String(100), doc='区域', nullable=False)
    sell_no = db.Column(db.String(100), doc='预售证号', nullable=False)
    sell_range = db.Column(db.String(255), doc='预售范围', nullable=False)
    houses = db.Column(db.Integer, doc='住房套数', nullable=False)
    tel = db.Column(db.String(100), doc='开发商咨询电话', nullable=False)
    start_time = db.Column(db.DateTime(), doc='登记开始时间', nullable=False)
    end_time = db.Column(db.DateTime(), doc='登记结束时间', nullable=False)
    status = db.Column(db.String(64), doc='项目报名状态', nullable=False)
    created_on = db.Column(
        db.DateTime, nullable=False, default=datetime.now, doc='爬取时间')
    update_on = db.Column(
        db.DateTime, nullable=True, onupdate=datetime.now, doc='更新时间')
