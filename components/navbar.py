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
layout = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    dbc.Col(dbc.NavbarBrand("Agnatus", className="ms-2")),
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Difusores", href='difusores')),
                                dbc.NavItem(dbc.NavLink("Demais Produtos", href='demais')),
                                dbc.NavItem(dbc.NavLink("Como Pedir!", href='tabela'), className='me-auto'),
                                dbc.NavItem(dbc.NavLink("Whatsapp(MG)",href='https://api.whatsapp.com/send?phone=5533999991173&text=Ol%C3%A1,%20somos%20a%20Adoratus,%20ser%C3%A1%20um%20prazer%20atend%C3%AA-lo.%0ANo%20que%20poder%C3%ADamos%20ajudar?%20=)', target='_blank')),
                                dbc.NavItem(dbc.NavLink("Whatsapp(RJ)",href='https://api.whatsapp.com/send?phone=5524998324650&text=Ol%C3%A1,%20somos%20a%20Adoratus,%20ser%C3%A1%20um%20prazer%20atend%C3%AA-lo.%0ANo%20que%20poder%C3%ADamos%20ajudar?%20=)', target='_blank')),
                                dbc.NavItem(dbc.NavLink("Facebook",href='https://www.facebook.com/Adoratus-103729810993751', target='_blank')),
                                dbc.NavItem(dbc.NavLink("Instagram",href='https://www.instagram.com/adoratus/', target='_blank')),
                                dbc.NavItem(dbc.NavLink("Localização", href='localizacao')),
                            ],
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
)    

# =========  Callbacks  =========== #
