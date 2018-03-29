# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, PackageLoader, select_autoescape


def render(filename, *args, **kwargs):
    package_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
    package_loader = PackageLoader(package_name, 'templates')
    jinjia_env = Environment(
        loader=package_loader,
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return jinjia_env.get_template(filename).render(*args, **kwargs)
