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
        html.Img(src='/assets/inicio.webp', style={'height':'100%','width':'100%'}),
        html.Hr(style={'margin-top':'10px'}),
    ]),

    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/1.jpeg', style={'height':'90%','width':'100%'}), href='difusores'),
            html.H3('Difusores', style={'margin-top':'7px', 'font-weight':'bold'})
        ], md=6),

        dbc.Col([
            html.A(html.Img(src='/assets/26.jpeg', style={'height':'90%','width':'100%'}), href='demais'),
            html.H3('Demais Produtos!', style={'margin-top':'7px', 'font-weight':'bold'})
        ], md=6),

    ])
        
], style={"padding": "10px"})

# =========  Callbacks  =========== #
