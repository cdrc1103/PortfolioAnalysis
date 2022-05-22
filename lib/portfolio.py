from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

from parameters import params
from lib import data_sources


class Portfolio:
    def __init__(self):
        """
        Download data from your depot data base table and run analytics.
        """
        engine = create_engine(params.portfolio_db)
        self.con = engine.connect()
        self.depot = pd.read_sql('SELECT * FROM depot', self.con)

    def price_development(self, reference_date: datetime, start_date: datetime = None, end_date: datetime = None,
                          price_type="Close", tickers: list = None, relative=True):
        """
        Calculate the relative or absolute price development relative to the price at a fixed date.
        :param reference_date: Fixed date that is used as reference to calculate price changes of other dates.
        :param start_date: First day to consider for price development.
        :param end_date: Last day to consider for price development.
        :param price_type: Price type. Defaults to "Close". Can be "Close", "Max", "Min" or "Open".
        :param tickers: Defaults to all tickers available in the portfolio. Can take a subset of tickers as list.
        :param relative: Defaults to true. Will calculate the relative changes if set to true. Will calculate the 
            absolute changes if set to false.
        :return: A dataframe where each row refers to a ticker and each column refers to the price change at a certain
            date.
        """

        # Consider a specific list of tickers or all tickers found in the depot
        if tickers is None:
            tickers = self.depot["Ticker"].to_list()

        # Download price development history
        price_data = data_sources.fetch_historical_prices(tickers, start_date, end_date)
        price_data = price_data[price_type].copy()

        # If the reference date is not available in the dataframe take the closest date available
        if reference_date not in price_data.index:
            date_differences = {abs(date.timestamp() - reference_date.timestamp()): date
                                for date in price_data.index.to_list()}
            reference_date = date_differences[min(date_differences.keys())]

        # Calculate price changes relative to reference date
        reference_price = price_data.loc[reference_date]
        price_data = price_data - reference_price
        if relative:
            price_data = price_data / reference_price

        return price_data
