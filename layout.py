from dash import Dash,html, dcc
import os   
import dash_bootstrap_components as dbc
from components import bar_charts, pie_charts, dropdown

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMLV5z_b4GXBTKZSq-RJVS_mAIfGvR6y2R2EirmvUBltYYAzEbhcF-jK9DTCL8ObpLzK4&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqlOmzbeR8-_1GG695vwHoC4wup7sLaTuW_xnxxrYH6xdtPF6dR21FfRc5lai-H6QmrnA&usqp=CAU"
def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.H1(
                "Chipotle Analysis", className="header-title", style={'margin-top': '10px', 'text-align': 'center'}
              ),
        html.P(
                "Base on the dataset we can analysis The Chipotle!!!🔥🔥🔥",
                className="header-description", style={'margin-top': '10px', 'text-align': 'center'}
                ),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'})
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(dropdown.render(app),lg=6,style={'margin-top': '30px', 'text-align': 'left'}),
            dbc.Col(dropdown.render1(app),lg=6,style={'margin-top': '30px', 'text-align': 'left'}),
            dcc.Slider(2000, 7400, step=None, marks={2201.04:'Chips and Guacamole', 2260.19:'Steak Bowl', 3851.43:'Steak Burrito', 5575.82:'Chicken Burrito', 7342.73:'Chicken Bowl'}, value=5,id='my-slider'),html.Div(id='slider-output-container'),
            dbc.Col(pie_charts.render(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'})
        ],className="mt-4"),
    ])



