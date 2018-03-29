# -*- coding: utf-8 -*-
from cdhouse.web.app import render_projects


def test_query_by_region():
    print(render_projects('天府新区'))
