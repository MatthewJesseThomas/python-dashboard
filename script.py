import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import os

port = int(os.getenv("port", 8050))

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the Dashboard
app.layout = html.Div(
    style={
        'backgroundColor': '#1a1a1a',
        'color': '#ffffff',
        'fontFamily': 'Arial, sans-serif',
        'padding': '20px',
    },
    children=[
        html.H1(
            "Caffeine Consumption Dashboard",
            style={'textAlign': 'center', 'color': '#00ccff'}
        ),
        html.P(
            "Analyzing caffeine consumption across age demographics. "
            "Data reflects average consumption in mg per day.",
            style={'textAlign': 'center', 'color': '#cccccc'}
        ),
        dcc.Graph(
            id='caffeine-age-graph',
            figure={
                'data': [
                    go.Bar(
                        x=['18-25', '26-35', '36-45', '46-60', '60+'],
                        y=[200, 250, 300, 220, 150],
                        name='Caffeine Consumption (mg/day)',
                        marker=dict(color='rgb(26, 118, 255)'),
                    ),
                    go.Scatter(
                        x=['18-25', '26-35', '36-45', '46-60', '60+'],
                        y=[20, 22, 30, 27, 15],
                        name='Energy Drink Usage (%)',
                        mode='lines+markers',
                        line=dict(color='rgb(255, 65, 54)', width=2),
                        marker=dict(size=8),
                    )
                ],
                'layout': {
                    'title': {
                        'text': 'Caffeine vs. Age Demographics',
                        'font': {'size': 24, 'color': '#00ccff'},
                    },
                    'xaxis': {
                        'title': 'Age Groups',
                        'titlefont': {'size': 18, 'color': '#cccccc'},
                        'tickfont': {'color': '#cccccc'},
                    },
                    'yaxis': {
                        'title': 'Caffeine Consumption (mg/day) & Usage (%)',
                        'titlefont': {'size': 18, 'color': '#cccccc'},
                        'tickfont': {'color': '#cccccc'},
                    },
                    'plot_bgcolor': '#2a2a2a',
                    'paper_bgcolor': '#1a1a1a',
                    'legend': {
                        'font': {'color': '#cccccc'}
                    }
                }
            }
        )
    ]
)

# Run the Application
if __name__ == '__main__':
    app.run_server(debug=True, host="127.0.0.1", port=port)
