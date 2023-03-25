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
layout = dbc.Col([
    dbc.Row([
            html.H1('Sapatos', style={'font-weight':'bold'})
        ]),

# PRIMEIRA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/tenis_1.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Moleca - Recortes Femininos', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 119,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/tenis_2.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Via Marte Flatform', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 219,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/tenis_3.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Moleca Amar', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 119,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/tenis_4.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Adidas Swift Run', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 599,00', style={'margin':'0px'})
        ], md=3),

    ]),

# SEGUNDA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/tenis_5.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Vizzano Casual', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 149,00', style={'margin':'0px'})
        ], md=3),
        
        dbc.Col([
            html.A(html.Img(src='/assets/tenis_6.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Vizzano Cano Médio', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 159,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/tenis_7.webp', style={'height':'80%','width':'100%'})),
            html.H4('Tênis Sketchers', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 129,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/tenis_8.webp', style={'height':'80%','width':'100%'})),
            html.H4('Slip On Via Marte', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 179,00', style={'margin':'0px'})
        ], md=3),

    ])
], style={"padding": "7px"})

# =========  Callbacks  =========== #
