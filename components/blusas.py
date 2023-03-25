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
            html.H1('Blusas', style={'font-weight':'bold'})
        ]),
        

# PRIMEIRA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/blusa_1.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa We Are The Basic', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 49,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/blusa_2.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa Ayaka Borboleta', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 69,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/blusa_3.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa Ayaka Poá', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 79,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/blusa_4.webp', style={'height':'80%','width':'100%'})),
            html.H4('Kimono Aisthy', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 119,00', style={'margin':'0px'})
        ], md=3),        

    ]),

# SEGUNDA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/blusa_5.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa Sal Rosa', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 69,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/blusa_6.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa Bolas Brancas', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 79,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/blusa_7.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa Paw Bola', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 39,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/blusa_8.webp', style={'height':'80%','width':'100%'})),
            html.H4('Blusa KAgawa Listras', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 89,00', style={'margin':'0px'})
        ], md=3),

    ])
], style={"padding": "7px"})

# =========  Callbacks  =========== #
