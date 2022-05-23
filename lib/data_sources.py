import pandas as pd
import yfinance as yf
from datetime import datetime

from parameters import params


def fetch_historical_prices(tickers: list, start_date: datetime = None, end_date: datetime = None, interval="1d"):
    """
    Fetch historical prices for a given list of stock tickers.
    :param tickers: List of tickers to fetch.
    :param start_date: First day to fetch prices.
    :param end_date: Last day to fetch prices.
    :param interval: Frequency of data points (see yfinance documentation).
    :return: A dataframe with all price types on the first header level and all requested tickers on the second header
        level.
    """
    # Join ticker name list to a single string to make the format applicable to the YFinance API
    tickers = " ".join(tickers)

    # Set reference_date values if not defined
    if start_date is None:
        start_date = params.start_date.strftime("%Y-%m-%d")
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    # Fetch the prices from Yahoo
    price_data = yf.download(tickers, start_date, end_date, interval=interval)

    # Transform reference_date index to Python datetime object
    price_data.index = pd.to_datetime(price_data.index)

    return price_data
