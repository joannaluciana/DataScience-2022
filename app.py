import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame( {"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
                    "Amount": [4, 1, 2, 2, 4, 5],
                    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
                    })
fig = px.bar( df, x = "Fruit",
              y="Amount", color="City",
              barmode="group")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app = dash.Dash(__name__)

app.layout = html.Div(

    [
        html.H1('Hallo!!!',
                style={'color': colors['text']}),
        html.Div('Moj pierwszy dashb',
             style={'color': colors['text']}),
        dcc.Graph(id='example-graph',
              figure= fig,
                  style={'color': colors['background']})
    ],
    style={
        'backgroundColor': colors['background']
    }
)
if __name__ == '__main__':
    app.run_server(debug=True)
