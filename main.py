from dash import Dash, html, dcc
import plotly.express as px
from datetime import datetime

from lib.portfolio import Portfolio


def main():
    """
    Gather portfolio related data.
    Start analytics on the portfolio data.
    Run the dashboard app.
    """

    # Load portfolio data
    portfolio = Portfolio()

    relative_price_development = portfolio.price_development(datetime.strptime("01-01-2022", "%d-%m-%Y"))

    fig = px.line(relative_price_development, x=relative_price_development.index, y=relative_price_development.columns,
                  labels={"value": "Closing Price", "variable": "Stock"}, template="simple_white")
    fig.update_yaxes(showgrid=True)
    fig.update_layout(yaxis_tickformat='.0%')

    app = Dash(__name__)

    """ Dasboard Layout """
    app.layout = html.Div(
        children=[
            html.Label('Stock Prices'),
            dcc.Graph(
                id='Depot Development',
                figure=fig
            )
        ]
    )

    return app


if __name__ == '__main__':
    dashboard = main()
    dashboard.run_server(debug=True)