import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sqlalchemy import func

from cdhouse.web.extensions import db
from cdhouse.web.models import CdHouseModel


def get_region_projects():
    rows = db.session.query(CdHouseModel.region, func.count(
        CdHouseModel.region)).group_by(CdHouseModel.region).all()
    regions = []
    projects_number = []
    for row in rows:
        regions.append(row[0])
        projects_number.append(row[1])
    return (regions, projects_number)


def get_layout():
    return html.Div(children=[
        html.H1(children='成都房协发布房源统计数据', id='pie-title'),
        dcc.Graph(id='region-pie')
    ])


def config_dash(dash_app):
    # 设置页面标题
    dash_app.title = '成都房协发布房源统计数据'
    # 设置页面布局
    dash_app.layout = get_layout()

    @dash_app.callback(
        Output('region-pie', 'figure'), [Input('pie-title', 'id')])
    def update_figure(input_value):
        regions, projects_number = get_region_projects()
        return go.Figure(
            data=[
                go.Pie(
                    labels=regions,
                    values=projects_number,
                    hole=0.3,
                    hoverinfo='label+percent+name',
                    textinfo='value',
                )
            ],
            layout={
                "title": "各市县房源数",
            })
