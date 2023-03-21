from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_revenue

def render(app):
    df = get_revenue()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("revenue_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("item in @dropdown")
        fig = px.bar(
                filtered_data,
                x="item",
                y="ip",
                color="ip",
                title="Total Revenue")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume")
    return html.Div(id="bar_volume")