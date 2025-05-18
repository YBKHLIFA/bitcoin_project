import pandas as pd
from datetime import datetime

df = pd.read_csv("btc_data.csv", names=["timestamp", "value"])
df = df[pd.to_numeric(df["value"], errors="coerce").notna()]
df["value"] = df["value"].astype(float)
df["timestamp"] = pd.to_datetime(df["timestamp"])

today = datetime.now().date()
df = df[df["timestamp"].dt.date == today]

if not df.empty:
    open_price = df.iloc[0]["value"]
    close_price = df.iloc[-1]["value"]
    high = df["value"].max()
    low = df["value"].min()
    volatility = df["value"].std()

    report = f"""
    🗓️ Date: {today}
    🔓 Open: {open_price}
    🔒 Close: {close_price}
    📈 High: {high}
    📉 Low: {low}
    🔁 Volatility: {volatility:.4f}
    """
else:
    report = "Aucune donnée pour aujourd’hui."

with open("daily_report.txt", "w") as f:
    f.write(report)
