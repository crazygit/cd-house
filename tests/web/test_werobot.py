# -*- coding: utf-8 -*-
from cdhouse.web.werobot import render_projects


def test_query_by_region(client):
    print(render_projects('天府新区'))
