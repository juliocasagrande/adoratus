import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# import from folders
from app import *
from components import inicio, difusores, demais, navbar, localizacao, tabela

# DataFrames and Dcc.Store



# =========  Layout  =========== #

app.layout = dbc.Container(children=[
    
   dbc.Row([
        dbc.Row([
            dcc.Location(id="url"),
            navbar.layout
        ]),

        dbc.Row([
            html.Div(id="page-content")
        ]),
    ])

], fluid=True, className="dbc", style={'width':'100%'})


@app.callback(Output("page-content", "children"),
[Input("url", "pathname")])

def render_page_content(pathname):
    if pathname == "/" or pathname == "/inicio":
        return inicio.layout

    if pathname == "/difusores":
        return difusores.layout

    if pathname == "/demais":
        return demais.layout
        
    if pathname == "/tabela":
        return tabela.layout
    
    if pathname == "/localizacao":
        return localizacao.layout


if __name__ == '__main__':
    app.run_server(debug=False)