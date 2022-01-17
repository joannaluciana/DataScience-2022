colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df,
             x='Fruit', y='Amount', color='City',
             barmode='group')
# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )



markdown_text = 'Markdown text'

# app.layout = html.Div([
#     dcc.Markdown(markdown_text),
#     dcc.Dropdown(
#         options=[{'label': 'New York City', 'value': 'NYC'},
#                  {'label': 'Warsaw', 'value': 'WAW'},
#                  {'label': 'Krakow', 'value': 'KRK'}],
#         value= ['NYC','WAW'],
#         multi= True
#     ),
#     dcc.RadioItems(
#         options=[{'label': 'New York City', 'value': 'NYC'},
#                  {'label': 'Warsaw', 'value': 'WAW'},
#                  {'label': 'Krakow', 'value': 'KRK'}],
#         value= 'NYC'
#
#     )
#     ,
#     dcc.Checklist(
#         options=[{'label': 'New York City', 'value': 'NYC'},
#                  {'label': 'Warsaw', 'value': 'WAW'},
#                  {'label': 'Krakow', 'value': 'KRK'}],
#         value= ['NYC','WAW'],
#
#     ),
#     dcc.Input(value='Dummy', type='text')
#     ,
#     dcc.Slider(
#         min=0,
#         max=9,
#         marks={i: f'Label {i}' for i in range(10)},
#         value=5
#     )
#     ,
#     dcc.Graph(id='example',
#               figure=fig)
# ])
gdp_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

countries_df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': indicator, 'value': indicator}
                         for indicator in countries_df['Indicator Name'].unique()],
                value=countries_df['Indicator Name'].unique()[0]
            )
        ],
            style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': indicator, 'value': indicator}
                         for indicator in countries_df['Indicator Name'].unique()],
                value=countries_df['Indicator Name'].unique()[0]
            )
        ],
            style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='indicator-graph'),
        dcc.Slider(
            id='year-slider-2',
            min=countries_df['year'].min(),
            max=countries_df['year'].max(),
            value=countries_df['year'].min(),
            marks={
                str(year): str(year) for year in gdp_df['year'].unique()
            },
            step=None
        ),
    ])
])


@app.callback(
    Output('indicator-graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('year-slider-2', 'value'),
)
def update_indicator_graph(xaxis_col, yaxis_col, year):
    fig = px.scatter(x=countries_df['Indicator Name'] == xaxis_col,
                     y=countries_df['Indicator Name'] == yaxis_col)
    return fig


def update_gdp_graph(selected_year):
    filtered_df = gdp_df[gdp_df['year'] == selected_year]

    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',
                     size='pop', color='continent',
                     hover_name='country',
                     log_x=True, size_max=55)

    return fig


def update_output_div(input_value):
    return f'Wpisales:  {input_value}'


