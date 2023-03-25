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

row1 = html.Tr([html.Td("Kits - Difusores de ambiente + Sabonetes Líquidos"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgba(49,27,9,255)", "color": "white", "font-weight": "bold", 'height':'7px'})
row2 = html.Tr([html.Td("Kit Difusor + Sabonete - 100 ml",style={"background-color": "rgba(49,27,9,255)", "color": "white"}), html.Td(children='R$ 105,00', style={'text-align':'center'})], style= {'height':'10px'})
row3 = html.Tr([html.Td("Kit Difusor + Sabonete - 200 ml",style={"background-color": "rgba(49,27,9,255)", "color": "white"}), html.Td(children='R$ 140,00', style={'text-align':'center'})], style= {'height':'10px'})
row4 = html.Tr([html.Td("Kit Difusor + Sabonete - 250 ml",style={"background-color": "rgba(49,27,9,255)", "color": "white"}), html.Td(children='R$ 155,00', style={'text-align':'center'})], style= {'height':'10px'})
row5 = html.Tr([html.Td("Kit Difusor + Sabonete - 300 ml",style={"background-color": "rgba(49,27,9,255)", "color": "white"}), html.Td(children='R$ 180,00', style={'text-align':'center'})], style= {'height':'10px'})

row6 = html.Tr([html.Td("Difusores de ambiente - Embalagem de vidro com essência e vareta"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgb(135,62,35)", "color": "white", "font-weight": "bold", 'height':'4px'})
row7 = html.Tr([html.Td("Difusor de ambiente - 100 ml",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 60,00', style={'text-align':'center'})], style= {'height':'4px'})
row8 = html.Tr([html.Td("Difusor de ambiente - 200 ml",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 85,00', style={'text-align':'center'})], style= {'height':'6px'})
row9 = html.Tr([html.Td("Difusor de ambiente - 250 ml",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 95,00', style={'text-align':'center'})], style= {'height':'6px'})
row10 = html.Tr([html.Td("Difusor de ambiente - 300 ml",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 115,00', style={'text-align':'center'})], style= {'height':'6px'})
row11 = html.Tr([html.Td("Refil de Difusor de ambiente - 100 ml",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 30,00', style={'text-align':'center'})], style= {'height':'6px'})
row12 = html.Tr([html.Td("Refil de Difusor de ambiente - 250 ml",style={"background-color": "rgb(135,62,35)", "color": "white"}), html.Td(children='R$ 56,00', style={'text-align':'center'})], style= {'height':'6px'})


row13 = html.Tr([html.Td("Sabonetes Líquidos - Embalagem de vidro"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgb(74, 135, 35)", "color": "white", "font-weight": "bold", 'height':'10px'})
row14 = html.Tr([html.Td("Sabonete Líquido - 100 ml",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 55,00', style={'text-align':'center'})], style= {'height':'10px'})
row15 = html.Tr([html.Td("Sabonete Líquido - 200 ml",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 70,00', style={'text-align':'center'})], style= {'height':'10px'})
row16 = html.Tr([html.Td("Sabonete Líquido - 250 ml",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 75,00', style={'text-align':'center'})], style= {'height':'10px'})
row17 = html.Tr([html.Td("Sabonete Líquido - 300 ml",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 85,00', style={'text-align':'center'})], style= {'height':'10px'})
row18 = html.Tr([html.Td("Refil de Sabonete Líquido - 100 ml",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 20,00', style={'text-align':'center'})], style= {'height':'10px'})
row19 = html.Tr([html.Td("Refil de Sabonete Líquido - 250 ml",style={"background-color": "rgb(74, 135, 35)", "color": "white"}), html.Td(children='R$ 35,00', style={'text-align':'center'})], style= {'height':'10px'})

row20 = html.Tr([html.Td("Difusores para carro"), html.Td('', style={'text-align':'center'})], style={"background-color": "rgb(27, 69, 1)", "color": "white", "font-weight": "bold", 'height':'10px'})
row21 = html.Tr([html.Td("Difusor para carro - 10 ml",style={"background-color": "rgb(27, 69, 1)", "color": "white"}), html.Td(children='R$ 20,00', style={'text-align':'center'})], style= {'height':'10px'})
row22 = html.Tr([html.Td("Difusor para carro (10ml) + Refil (20ml)",style={"background-color": "rgb(27, 69, 1)", "color": "white"}), html.Td(children='R$ 30,00', style={'text-align':'center'})], style= {'height':'10px'})
row23 = html.Tr([html.Td("Refil de Difusor para carro - 20 ml",style={"background-color": "rgb(27, 69, 1)", "color": "white"}), html.Td(children='R$ 15,00', style={'text-align':'center'})], style= {'height':'10px'})


table_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7,
                          row8, row9, row10, row11, row12, row13, row14, row15, row16, row17,row18,row19, row20, row21,row22,row23])]

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
    
    ], md=6),

    dbc.Col([
        dbc.Row([
            dbc.Carousel(
                items=[
                        {"key": "1", "src": "/assets/3.jpeg"},
                        {"key": "2", "src": "/assets/8.jpeg"},
                        {"key": "3", "src": "/assets/10.jpeg"},
                        {"key": "4", "src": "/assets/11.jpeg"},
                        {"key": "5", "src": "/assets/12.jpeg"},
                ],
                controls=False,
                indicators=False,
                interval=2000,
                ride="carousel",
            )
        ], style={'margin-top':'38px'}),
    
    ], md=6),
    html.Hr(style={'margin-top':'7px','margin-bottom':'7px'}),

# LINHA DE PRODUTOS
    dbc.Row([
        html.H4('Catálogo de Produtos', style={'font-weight':'bold'})
    ]),
# LINHA 1
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/1.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 001', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/2.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 002', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/5.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 003', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
# LINHA 2
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/6.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 004', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/7.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 005', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/9.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 006', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
# LINHA 3
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/13.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 007', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/14.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 008', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/15.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 009', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
# LINHA 4
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/16.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 010', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/17.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 011', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/18.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 012', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
# LINHA 5
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/19.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 013', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/20.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 014', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/21.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 015', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
# LINHA 6
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/22.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 016', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/23.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 017', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/24.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 018', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
# LINHA 7
    dbc.Row([
        dbc.Col([
            html.A(html.Img(src='/assets/25.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 020', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/30.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 021', style={'margin-bottom':'7px'})
        ], md=4),

        dbc.Col([
            html.A(html.Img(src='/assets/31.jpeg', style={'height':'100%','width':'100%'})),
            html.P('Código do Produto: 022', style={'margin-bottom':'7px'})
        ], md=4),
    ], style={'margin-bottom':'35px'}),
]),

# FINAL DO LAYOUT       
], style={"padding": "7px"})
