import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

weather_df = pd.read_csv('data/WeatherAusReady.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

indicators = weather_df['Location'].unique()

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1(children="Australia Weather Forecast")
        ], className = "row")
    ]),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value':i} for i in indicators],
                value = 'Sydney'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle = {'disaply': 'inline-block'}
            )
        ],
        style = {'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value':i} for i in indicators],
                value = 'Canberra'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle = {'disaply': 'inline-block'}
            )
        ], style = {'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    html.Div([
        html.Div([
            dcc.Graph(id='graph-one'),
            dcc.Slider(
                id='Year--slider',
                min=weather_df['Year'].min(),
                max=weather_df['Year'].max(),
                value=weather_df['Year'].max(),
                marks={str(Year): str(Year) for Year in weather_df['Year'].unique()},
                step=None
            )
        ]),
        html.Div([
            dcc.Graph(id='graph-two'),
            dcc.Slider(
                id='Year--slider',
                min=weather_df['Year'].min(),
                max=weather_df['Year'].max(),
                value=weather_df['Year'].max(),
                marks={str(Year): str(Year) for Year in weather_df['Year'].unique()},
                step=None
            )
        ])
    ], className = "row")
])

@app.callback(
    Output('graph-one', 'figure'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('Year--slider', 'value'),
    ]
)

def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value):
    Year_weather_df = weather_df[weather_df['Year'] == year_value]

    return {
        'data': [go.Scatter(
            x=Year_weather_df[Year_weather_df['Location'] == xaxis_column_name]['MaxTemp'],
            y=Year_weather_df[Year_weather_df['Location'] == yaxis_column_name]['MaxTemp'],
            text= Year_weather_df[Year_weather_df['Location'] == yaxis_column_name]['Location'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color':'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
