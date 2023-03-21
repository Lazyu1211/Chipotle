from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_quantity_list, get_revenue_list

def render(app):
    list_quantity = get_quantity_list()
    top5_quantity = [{'label':i,'value':i} for i in list_quantity]
    @app.callback(
    Output(component_id='quantity_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_top5_quantity(n):
        return list_quantity

    return html.Div(
        children=[
            html.H6("Select Top 5 Quantity Item"),
            dcc.Dropdown(
                options=top5_quantity,
                multi=True,
                id = "quantity_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )

def render1(app):
    list_revenue = get_revenue_list()
    top5_revenue = [{'label':i,'value':i} for i in list_revenue]
    @app.callback(
    Output(component_id='revenue_dropdown', component_property='value'),
    Input(component_id='select_all_button1', component_property='n_clicks')
    )
    def update_top5_revenue(n):
        return list_revenue

    return html.Div(
        children=[
            html.H6("Select Top 5 Revenue Item"),
            dcc.Dropdown(
                options=top5_revenue,
                multi=True,
                id = "revenue_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button1",
                n_clicks=0
            )
        ]
    )