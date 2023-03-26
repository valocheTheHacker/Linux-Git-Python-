import dash
from dash import dcc
from dash import html
import datetime

# Tickers
btc_ticker = "BTC"
xrp_ticker = "XRP"

# Convert to dataframe
import pandas as pd
data_btc = pd.read_csv("data_btc.csv", sep= " ", skipinitialspace=True)
data_xrp = pd.read_csv("data_xrp.csv", sep= " ", skipinitialspace=True)


# Crée une application Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)


# Chaque fois que l'utilisateur modifie la valeur du menu "ticker-dropdown" ou qu'on arrive à 5min, la fonction correspondante sera appelée pour mettre à jour le graphique avec l'ID "ticker-graph"
@app.callback(
    dash.dependencies.Output("ticker-graph", "figure"),
    [dash.dependencies.Input("ticker-dropdown", "value"), dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_ticker_graph(ticker, n):

    if ticker == btc_ticker:
        data = data_btc
    else:
        data = data_xrp
    #new_data = 
    #data = pd.concat([data, new_data])
    
    fig = {
        "data": [{"x": data["Date"], "y": data["Close"], "type": "line", "line": {"color": "red"}}],
        "layout": {"title": f"Graphique du cours du ({ticker})", "fontSize" : 20}
    }
    
    return fig


# Chaque fois que l'intervalle avec l'ID "interval-component" est atteint, la fonction correspondante sera appelée pour mettre à jour le texte de l'élément avec l'ID "update-time"
@app.callback(
    dash.dependencies.Output("update-time", "children"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_time(n):
    return f"Dernière mise à jour : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (MÀJ automatique toutes les 5 min)"


# Ajoute un composant interval pour déclencher la mise à jour automatique
app.layout = html.Div([
    dcc.Interval(id="interval-component", interval=300 * 1000, n_intervals=0),
    html.Div([
        html.H1("Financial Dashboard : Le BTC et le XRP (Sacha Fiereder)", style={'textAlign': 'center', 'color' : 'black', 'fontSize' : 30}),
        
        dcc.Dropdown(
            id="ticker-dropdown",
            options=[
                {"label": "BTC", "value": btc_ticker},
                {"label": "XRP", "value": xrp_ticker}
            ],
            value=btc_ticker,
            style={'color' : 'black'}
        ),
        
        dcc.Graph(
            id="ticker-graph"
        ),
        
        html.Div("ADD DESCRIPTION", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),
        
        html.Div(style={'textAlign': 'right', 'color' : 'red'},
            id="update-time")
    ])
])

# Lance l'application Dash
if __name__ == '__main__':
    app.run_server(debug = True, host='0.0.0.0')

