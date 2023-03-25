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
            html.H1('Acessórios', style={'font-weight':'bold'})
        ]),

# PRIMEIRA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_1.webp', style={'height':'80%','width':'100%'})),
            html.H4('Maxi Necesseaire Caçula', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 59,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_2.webp', style={'height':'80%','width':'100%'})),
            html.H4('Bolsa Anacapri', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 199,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_3.webp', style={'height':'80%','width':'100%'})),
            html.H4('Necessaire Dias de Sol', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 49,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_4.webp', style={'height':'80%','width':'100%'})),
            html.H4('Bolsa Ora Bolas', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 298,00', style={'margin':'0px'})
        ], md=3),

    ]),

# SEGUNDA LINHA

        dbc.Row([
        
        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_5.webp', style={'height':'80%','width':'100%'})),
            html.H4('Bolsa de Alça Clutch', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 78,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_6.webp', style={'height':'80%','width':'100%'})),
            html.H4('Bolsa de Ombro Le Postiche', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 225,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_7.webp', style={'height':'80%','width':'100%'})),
            html.H4('Bolsa Dia e Noite', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 198,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/bolsa_8.webp', style={'height':'80%','width':'100%'})),
            html.H4('Bolsa Noite Le Farm', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 429,00', style={'margin':'0px'})
        ], md=3),

    ])
], style={"padding": "7px"})

# =========  Callbacks  =========== #