# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("./data/processed_sales_data.csv")
df.head()

fig = px.line(
    df, x="date", 
    y="total_sales", 
    color="region", 
    title="Product Sales Data", 
    labels={"date": "Date", "total_sales": "Total Sales", "region": "Region"}, 
    template="plotly_dark", 
    markers=True, 
    line_shape="linear"
    )

app.layout = html.Div(children=[
    html.H1(children="Sales Data"),
    html.Div(children="""
        A simple dashboard to visualize sales data.
    """),
    dcc.Graph(
        id="sales-graph",
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
