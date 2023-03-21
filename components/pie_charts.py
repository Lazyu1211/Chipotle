from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output,Input
from utill import get_quantity

def render(app):
    df = get_quantity()

    @app.callback(
    Output("pie_volume", component_property='children'),
    Input("quantity_dropdown",component_property='value')
    )

    def update_pie_chart(dropdown):
        filtered_data = df.query("item in @dropdown")
        fig = px.pie(filtered_data, values = 'quantity', names = "item", title = 'Top 5 Quantity')
        return html.Div(dcc.Graph(figure=fig),id="pie_volume")
    return html.Div(id="pie_volume")