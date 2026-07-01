from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
df = pd.read_csv("formatted_output.csv")

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date")
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Sales ($)"
    }
)
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),
    dcc.Graph(figure=fig)
])
if __name__ == "__main__":
    app.run(debug=True)