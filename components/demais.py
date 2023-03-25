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

# INSTANCIAMENTO DA TABELA
table_header = [
    html.Thead(html.Tr([html.Th("Descrição", style={'width':'80%'}),
                        html.Th("Valor", style={'text-align':'center','width':'35%'}),
                        ]),
                        style={"background-color": "rgb(97, 114, 126)", "color": "white", 'height':'10px'})
]

row1 = html.Tr([html.Td("Água Perfumada pra Tecidos"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgba(49,27,9,255)", "color": "white", "font-weight": "bold", 'height':'7px'})
row2 = html.Tr([html.Td("Água Perfumada - 250 ml",style={"background-color": "rgba(49,27,9,255)", "color": "white"}), html.Td(children='R$ 40,00', style={'text-align':'center'})], style= {'height':'10px'})
row3 = html.Tr([html.Td("Água Perfumada - 500 ml",style={"background-color": "rgba(49,27,9,255)", "color": "white"}), html.Td(children='R$ 60,00', style={'text-align':'center'})], style= {'height':'10px'})

row4 = html.Tr([html.Td("Bandejas Espelhadas"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgb(135,62,35)", "color": "white", "font-weight": "bold", 'height':'4px'})
row5 = html.Tr([html.Td("Bandeja Espelhada - 15 x 12 cm",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 25,00', style={'text-align':'center'})], style= {'height':'4px'})
row6 = html.Tr([html.Td("Bandeja Espelhada - 21 x 15 cm",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 35,00', style={'text-align':'center'})], style= {'height':'6px'})

row7 = html.Tr([html.Td("Velas Aromáticas"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgb(74, 135, 35)", "color": "white", "font-weight": "bold", 'height':'10px'})
row8 = html.Tr([html.Td("Vela Aromática - 90 gr",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 65,00', style={'text-align':'center'})], style= {'height':'10px'})
row9 = html.Tr([html.Td("Vela Aromática - 120 gr",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 85,00', style={'text-align':'center'})], style= {'height':'10px'})

row10 = html.Tr([html.Td("Varetas Decoradas"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgb(27, 69, 1)", "color": "white", "font-weight": "bold", 'height':'10px'})
row11 = html.Tr([html.Td("Varetas - Qualquer modelo",style={"background-color": "rgb(27, 69, 1)", "color": "white"}), html.Td(children='R$ 5,00', style={'text-align':'center'})], style= {'height':'10px'})

table_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7,
                          row8, row9, row10, row11])]

# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([
            html.H1('Difusores Aromáticos e Sabonetes Líquidos', style={'font-weight':'bold'}),
        ]),

# PRIMEIRA LINHA

dbc.Row([
    dbc.Col([
        html.H4('Tabela de Preços', style={'font-weight':'bold'}),
        dbc.Table(table_header + table_body,
        bordered=False,
        dark=False,
        hover=True,
        responsive=True)
    ], md=5),

    dbc.Col([
        dbc.Carousel(
        items=[
                {
                "key": "1",
                "src": "/assets/26.jpeg",
                "header": "Vela Aromática",
                "caption": "90 gr",
                },
                {
                "key": "2",
                "src": "/assets/27.jpeg",
                "header": "Vela Aromática",
                "caption": "120 gr",
                },
                {
                "key": "3",
                "src": "/assets/28.jpeg",
                "header": "Água Perfumada",
                "caption": "250 ml ou 500 ml",
                },
        ]
        )
    ], md=7, style={'margin-top':'30px'})
        
]),

# FINAL DO LAYOUT       
], style={"padding": "7px"})