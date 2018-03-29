# -*- coding: utf-8 -*-
import pytest

from cdhouse.web import app_factory


@pytest.fixture
def app():
    app = app_factory()
    return app
