import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from sqlalchemy import func
from flask import current_app

from cdhouse.web.extensions import db
from cdhouse.web.models import CdHouseModel


def get_region_projects():
    labels = []
    values = []
    rows = db.session.query(CdHouseModel.region, func.count(
        CdHouseModel.region)).group_by(CdHouseModel.region).all()
    for row in rows:
        labels.append(row[0])
        values.append(rows[1])
    return (labels, values)


def get_region_projects_pie():
    # current_app.logger.debug('get_region_projects_pie')
    # todo: fixme
    # labels, values = get_region_projects()
    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]

    # current_app.logger.debug(f'labels: {labels}')
    # current_app.logger.debug(f'values: {values}')
    return dcc.Graph(
        id='region_pie',
        figure=go.Figure(data=[go.Pie(labels=labels, values=values)]))


layout = html.Div(children=[
    html.H1(children='各区市房源数量'),
    get_region_projects_pie(),
])
