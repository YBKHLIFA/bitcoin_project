import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from datetime import datetime

app = dash.Dash(__name__)
app.title = "Bitcoin Dashboard"

def load_data():
    try:
        df = pd.read_csv("btc_data.csv", names=["timestamp", "value"])
        df = df[df["value"] != "ERROR"]
        df["value"] = pd.to_numeric(df["value"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")
        return df
    except Exception:
        return pd.DataFrame(columns=["timestamp", "value"])

app.layout = html.Div(children=[
    html.H1("BTC/USD Live Rate", style={"textAlign": "center"}),
    html.H3(id="latest", style={"textAlign": "center", "color": "green"}),
    dcc.Graph(id="graph"),
    html.H4("Daily Report (20:00)", style={"padding": "20px"}),
    html.Pre(id="report"),
    dcc.Interval(id="interval", interval=5 * 60 * 1000, n_intervals=0)  # every 5 minutes
])

@app.callback(
    dash.dependencies.Output("graph", "figure"),
    dash.dependencies.Output("latest", "children"),
    dash.dependencies.Output("report", "children"),
    dash.dependencies.Input("interval", "n_intervals")
)
def update_dashboard(n):
    df = load_data()
    if df.empty:
        fig = px.line(title="No data available")
        latest = "No data"
    else:
        fig = px.line(df, x="timestamp", y="value", title="BTC/USD Exchange Rate")
        latest = f"Latest Value: {df['value'].iloc[-1]}"

    try:
        with open("daily_report.txt", "r") as f:
            report = f.read()
    except FileNotFoundError:
        report = "Report not available yet."

    return fig, latest, report

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
