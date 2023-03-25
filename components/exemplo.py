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
            html.H1('Calças', style={'font-weight':'bold'})
        ]),

# PRIMEIRA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/calca_1.webp', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Calça Alfaiataria Sport', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 298,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/calca_2.jpg', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Conjunto Balneário', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 348,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/calca_3.webp', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Conjunto Stella Cropped', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 399,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/calca_4.webp', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Conjunto Blazer e Short Anne', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 379,00', style={'margin':'0px'})
        ], md=3),

    ]),

# SEGUNDA LINHA

        dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/calca_5.webp', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Vestido Básico Midi', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 159,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/calca_6.webp', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Conjunto de Linho Short Box', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 279,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/calca_7.jpg', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Conjunto Saia e Camisa Midi', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 189,00', style={'margin':'0px'})
        ], md=3),

        dbc.Col([
            html.A(html.Img(src='/assets/calca_8.webp', style={'height':'70%','width':'100%'}), href='calcas'),
            html.H4('Conjunto Calça Estilizado', style={'margin-top':'7px', 'font-weight':'bold'}),
            html.H5('R$ 299,00', style={'margin':'0px'})
        ], md=3),

    ])


], style={"padding": "7px"})

# =========  Callbacks  =========== #
