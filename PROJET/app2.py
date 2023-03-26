import yfinance as yf
import dash
from dash import dcc
from dash import html
import datetime
import time


# Tickers
btc_ticker = "BTC"
eth_ticker = "ETH"

# Convert to dataframe
import pandas as pd
data_btc = pd.read_csv("data_btc.csv", sep= " ")
data_eth = pd.read_csv("data_eth.csv", sep= " ")
print (data_btc)

# Crée une application Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)


# Définit la mise à jour automatique des données toutes les minutes
@app.callback(
    dash.dependencies.Output("ticker-graph", "figure"),
    [dash.dependencies.Input("ticker-dropdown", "value"), dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_ticker_graph(ticker, n):
    # Récupère les données les plus récentes
    if ticker == btc_ticker:
        data = data_btc
    else:
        data = data_eth
    #new_data = yf.download(ticker, start=data.index[-1], end=datetime.date.today(), interval="1d")
    #data = pd.concat([data, new_data])
    # Crée la figure pour le graphique
    fig = {
        "data": [{"x": data["Date"], "y": data["Close"], "type": "line", "line": {"color": "red"}}],
        "layout": {"title": f"Price Chart ({ticker})"}
    }
    # Retourne la figure
    return fig


# Définit l'affichage de l'heure de la dernière mise à jour
@app.callback(
    dash.dependencies.Output("update-time", "children"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_time(n):
    return f"Last update : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (every 5 min)"


# Ajoute un composant interval pour déclencher la mise à jour automatique
app.layout = html.Div([
    dcc.Interval(id="interval-component", interval=300 * 1000, n_intervals=0),
    html.Div([
        html.H1("Final Project : Financial Project (created by Sacha FIEREDER)", style={'textAlign': 'center', 'color' : 'black'}),
        
        dcc.Dropdown(
            id="ticker-dropdown",
            options=[
                {"label": "BTC", "value": btc_ticker},
                {"label": "ETH", "value": eth_ticker}
            ],
            value=btc_ticker,
            style={'color' : 'black'}
        ),
        
        html.Div("BTC and ETH Description balabalabalaba", style={'textAlign': 'justify', 'color' : 'black'}
        ),
        
        dcc.Graph(
            id="ticker-graph"
        ),
        
        html.Div(style={'textAlign': 'right', 'color' : 'red'},
            id="update-time")
    ])
])

# Lance l'application Dash
if __name__ == '__main__':
    app.run_server(debug = True)

