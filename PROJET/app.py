
eth_ticker = "ETH"
xrp_ticker = "XRP"

# Convert to dataframe
import pandas as pd
data_eth = pd.read_csv("data_eth.csv", sep= " ", skipinitialspace=True)
data_xrp = pd.read_csv("data_xrp.csv", sep= " ", skipinitialspace=True)


# Create and open Dash application
import dash
from dash import dcc
from dash import html
import datetime
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Manage drop down menu
@app.callback(
    dash.dependencies.Output("ticker-graph", "figure"),
    [dash.dependencies.Input("ticker-dropdown", "value"), dash.dependencies.Input("interval-component", "n_intervals")]
)


# Function to update graph
def change_graph(ticker, n):

    if ticker == eth_ticker:
        data = data_eth
    else:
        data = data_xrp
    
    fig = {
        "data": [{"x": data["Date"], "y": data["Close"], "type": "line", "line": {"color": "red"}}],
        "layout": {"title": f"Graphic for ({ticker})", "fontSize" : 20}
    }
    
    return fig

# Manage time interval between updates
@app.callback(
    dash.dependencies.Output("update-time", "children"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_time(n):
    return f"Updated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Manage automatic updates
app.layout = html.Div([
    dcc.Interval(id="interval-component", interval=300 * 1000, n_intervals=0),
    html.Div([
        html.H1("Dashboard", style={'textAlign': 'center', 'color' : 'green', 'fontSize' : 25}),
        
        dcc.Dropdown(
            id="ticker-dropdown",
            options=[
                {"label": "BTC", "value": eth_ticker},
                {"label": "XRP", "value": xrp_ticker}
            ],
            value=eth_ticker,
            style={'color' : 'black'}
        ),
        
        dcc.Graph(
            id="ticker-graph"
        ),
        
        html.Div("At its core, Ethereum is a decentralized global software platform powered by blockchain technology. It is most commonly known for its native cryptocurrency, ether (ETH).", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),

        html.Div("", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),

        html.Div("Ripple is a real-time, cryptocurrency gross-settlement system, currency exchange and remittance network created by Ripple Labs Inc, a US-based technology company. The company then created the XRP cryptocurrency, which it describes as a “digital asset built for global payments”.", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),
        
        html.Div(style={'textAlign': 'right', 'color' : 'red'},
            id="update-time")
    ])
])

# Launch dash application
if __name__ == '__main__':
    app.run_server(debug = True, host='0.0.0.0')

