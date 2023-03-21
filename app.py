from dash import Dash,html
import dash_bootstrap_components as dbc
import pandas as pd
from layout import create_layout

def main():
    app = Dash(external_stylesheets=[dbc.themes.DARKLY])
    app.title = "Chipotle Analysis"
    app._favicon = "/Users/junyuwu/Chipotle Project/assets/Chipotle.ico" 
    app.layout = create_layout(app)
    app.run_server(debug=True)

if __name__ == "__main__":
   main()