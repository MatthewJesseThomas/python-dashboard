import dash
import dash_core_components as dcc  # Optional in Dash v2+, but kept for compatibility
import dash_html_components as html  # Optional in Dash v2+, but kept for compatibility

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the Dashboard
app.layout = html.Div(
    children=[
        html.H1("My Dashboard"),
        dcc.Graph(
            id='my-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Line chart'}
                ],
                'layout': {
                    'title': 'Graph Title',
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                }
            }
        )
    ]
)

# Run the Application
if __name__ == '__main__':
    app.run_server(debug=True)
