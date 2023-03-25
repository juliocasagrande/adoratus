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

# COMO MONTAR O KIT
layout = dbc.Row([
    dbc.Row([
        dbc.Col([
                dbc.Row([
                        html.H1('Como montar seu kit', style={'font-weight':'bold'}),
                        html.H4('- Comece escolhendo a essência de acordo com sua preferência;'),
                        html.H4('- Escolha o modelo do recipiente;'),
                        html.H4('- Escolha a cor da tampa/válvula (dourada ou prata);'),
                        html.H4('- O laço decorativo é feito de forma única e artesanal. As fotos do catálogo representam alguns modelos, podendo variar o tom das fitas e modelo das pedras utilizadas;'),
                        html.H4('- Itens opcionais: bandeja, vareta decorada e adornos.'),
                ]),
        ], md=8),

# IMAGENS RODANDO
        dbc.Col([
                dbc.Carousel(
                items=[
                        {"key": "1", "src": "/assets/13.jpeg"},
                        {"key": "2", "src": "/assets/28.jpeg"},
                        {"key": "3", "src": "/assets/26.jpeg"},
                ],
                controls=False,
                indicators=False,
                interval=2000,
                ride="carousel",
                )
        ], md=4),
    ], style={'margin-bottom':'10px'}),

# SEGUNDA LINHA - ESSÊNCIAS

dbc.Row([
    html.Hr(),
    html.H2('Nossas essências', className='text-primary', style={'margin-top':'2px'}),
    html.H4('Trousseau', className='text-success', style={'margin-bottom':'1px'}),
    html.P('Uma essência muito agradável, com notas cítricas e amadeiradas com um toque de sofisticação, proporcionando sensação de prazer e satisfação.', style={'margin-top':'0px'}),

    html.H4('Bamboo', className='text-success', style={'margin-bottom':'1px','margin-top':'2px'}),
    html.P('Essência com notas florais e muita personalidade, que possui aroma moderno e proporciona sensação de bem estar, serenidade e harmonia', style={'margin-top':'0px'}),

    html.H4('Pimenta Rosa', className='text-success', style={'margin-bottom':'1px','margin-top':'2px'}),
    html.P('Levemente adocicada, é uma fragância sensual e profunda, em que a mistura das características rústicas e picantes porporcionam sensação de encantamento.', style={'margin-top':'0px'}),

    html.H4('Chá Branco', className='text-success', style={'margin-bottom':'1px','margin-top':'2px'}),
    html.P('Aroma floral cítrico, refrescante e suave, transmite tranquilidade e paz interior. Ótimo para criar atmosfera relaxante, proporcionando sensação de beme estar para a mente e corpo.', style={'margin-top':'0px'}),

    html.H4('Figo', className='text-success', style={'margin-bottom':'1px','margin-top':'2px'}),
    html.P('Uma fragância frutada com toque amadeirado e aroma vagamente doce, reconfortante e marcante. Um aroma inconfundível e sofisticado.', style={'margin-top':'0px'}),

    html.H4('Vento', className='text-success', style={'margin-bottom':'1px','margin-top':'2px'}),
    html.P('Inspirado na fragância da Osklen, é um aroma leve e suave, com notas cítricas, proporcionando uma sensação de frescor, suavidade e aconchego.', style={'margin-top':'0px'}),

    html.H4('Baby', className='text-success', style={'margin-bottom':'1px','margin-top':'2px'}),
    html.P('Sabe aquele cheirinho gostoso de bebê? Essa é a sensação transmitida por esse aroma, composto por notas cítricas, florais e um toque amadeirado. Uma essência que nos remete afeto, carinho e aconchego.', style={'margin-top':'0px'}),   
]),

# LINHA FORMA DE PAGAMENTO
dbc.Row([
    html.Hr(style={'margin-top':'2px'}),
    html.H2('Formas de Pagamento:'),
    html.H4('- PIX (5% de desconto)'),
    html.H4('- Cartão - Parcelamento em até 3 vezes'),
    html.H4('- Os pedidos são feitos sob encomenda e serão preparados após confirmação do pagamento, enviado pelo cliente'),
    html.H4('- A entrega será combinada no ato da venda e poderá ser cobrada'),
])

# FINAL DO LAYOUT       
], style={"padding": "7px"})

# =========  Callbacks  =========== #