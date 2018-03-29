# -*- coding: utf-8 -*-
import pytest

from cdhouse.crawler.settings import DATABASE_URL
from cdhouse.models import CdHouseModel, get_session
from cdhouse.utils.misc import render


@pytest.fixture(scope='function')
def projects():
    db_session = get_session(url=DATABASE_URL)
    return db_session.query(CdHouseModel).limit(3).all()


def test_render(projects):
    print(render('open_house.tpl', projects=projects, region='所有区域'))
