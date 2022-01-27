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

app = dash.Dash(__name__)


markdown_text = '''
### Markdown w Dashu
To jest prosty Markdown napisany w Markdown

- lista
- elemntow
- z Markdown

## Markdown!!! 
'''
app.layout = html.Div(
    [
        dcc.Markdown(markdown_text),
        html.Label('Dropdowny'),
        dcc.Graph(id='example-graph',
              figure=fig),
        dcc.Dropdown(
                options=[
                        {'label':'New York City', 'value': 'NYC'},
                        {'label':'Warszawa', 'value':'Waw'},
                        {'label':'Krakow', 'value':'Krk'}
                        ],
                value= 'NYC',

        ),
        html.Label('Dropdowny'),
        dcc.Dropdown(
                options=[
                        {'label':'New York City', 'value': 'NYC'},
                        {'label':'Warszawa', 'value':'Waw'},
                        {'label':'Krakow', 'value':'Krk'}
                        ],
                value= ['Waw','NYC'],
                multi=True
        ),
        html.Label('Radiobutton'),
        dcc.RadioItems(
                options=[
                        {'label':'New York City', 'value': 'NYC'},
                        {'label':'Warszawa', 'value':'Waw'},
                        {'label':'Krakow', 'value':'Krk'}
                        ],
                value= 'NYC',

        )
]
)
if __name__ == '__main__':
    app.run_server(debug=True)
