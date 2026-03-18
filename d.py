# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, Input, Output, html, dcc
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
        figure=fig,
    ),
    html.Div(children=[
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All Regions", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            labelStyle={"display": "flex", "margin-right": "10px", "font-size": "32px", "color": "#333"},
            style={"display": "flex", "justify-content": "center", "margin-top": "20px"}
        )
    ], style={"margin-top": "20px", "display": "flex", "flex-direction": "row", "justify-content": "center"})
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)

def filter_data(region):
    if region == "all":
        return px.line(
            df, x="date", 
            y="total_sales", 
            color="region", 
            title="Product Sales Data", 
            labels={"date": "Date", "total_sales": "Total Sales", "region": "Region"}, 
            template="plotly_dark", 
            markers=True, 
            line_shape="linear"
    )
    else:
        filtered_df = df[df["region"] == region]
        return px.line(
            filtered_df, x="date", 
            y="total_sales", 
            color="region", 
            title="Product Sales Data", 
            labels={"date": "Date", "total_sales": "Total Sales", "region": "Region"}, 
            template="plotly_dark", 
            markers=True, 
            line_shape="linear"
        )

if __name__ == '__main__':
    app.run(debug=True)
