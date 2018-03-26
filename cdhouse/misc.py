# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, PackageLoader, select_autoescape


def render(filename, *args, **kwargs):
    return Environment(
        loader=PackageLoader(
            os.path.basename(os.path.dirname(__file__)), 'templates'),
        autoescape=select_autoescape(['html',
                                      'xml'])).get_template(filename).render(
                                          *args, **kwargs)
