# -*- coding: utf-8 -*-
from cdhouse.web.dash import get_region_projects


def test_get_region_projects(client):
    print(get_region_projects())
