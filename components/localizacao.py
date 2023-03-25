import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO

# =========  Layout  =========== #
layout = html.Div([
    dbc.Row([
        html.H1('Localização'),
        html.H3('Endereço:'),
        html.H4('Rua Trajano Lima nº17, Loja 04 - Manhumirim/MG')
    ]),

    dbc.Row([
        html.Div([
            
            html.Iframe(
                src='https://www.google.com/maps/embed/v1/place?key=AIzaSyDHSlCWq_CTfCRozT3ZYQ4qYJkK7AjNq_A&q=-20.357780488149487,-41.959131932697595',
                width='100%',
                height=500
            )
        ])
    ])
    
], style={"padding": "10px"})

# =========  Callbacks  =========== #
