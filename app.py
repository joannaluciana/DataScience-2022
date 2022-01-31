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
gdp_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
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
        html.H6('Wpisz cos w polu zeby zobaczyc jak dziala callback'),
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value='dummy', type='text')
        ]),
        html.Br(),
        html.Div(id='my-output'),

]
)
@app.callback(
    Output('my-output', 'children'),
    Input('my-input', 'value')

)

def update_output_div (input_value):
    return f'Jak dziala callback? wpisales: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
