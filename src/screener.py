import os
import pandas as pd
from data_fetcher import DataFetcher

class StockScreener:
    def __init__(self):
        self.tickers = self.load_tickers()
        self.filters = {}

    def load_tickers(self):
        tickers = []
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        for file in os.listdir(data_dir):
            if file.endswith('.txt'):
                df = pd.read_csv(os.path.join(data_dir, file), delimiter='\t')
                tickers.extend(df['Symbol'].tolist())
        return tickers

    def fetch_data(self):
        data_fetcher = DataFetcher()
        return data_fetcher.fetch_data(self.tickers)

    def apply_filters(self, data):
        filtered_data = {ticker: df for ticker, df in data.items() if self.passes_filters(ticker, df)}
        return filtered_data

    def passes_filters(self, ticker, df):
        if 'price' in self.filters:
            if not (self.filters['price'][0] <= df['Close'].iloc[-1] <= self.filters['price'][1]):
                return False
        if 'market_cap' in self.filters:
            if not self.market_cap_in_range(df['marketCap'].iloc[-1]):
                return False
        if 'dividend_yield' in self.filters:
            if not (self.filters['dividend_yield'][0] <= df['dividendYield'].iloc[-1] <= self.filters['dividend_yield'][1]):
                return False
        if 'average_volume' in self.filters:
            if not (self.filters['average_volume'][0] <= df['Volume'].mean() <= self.filters['average_volume'][1]):
                return False
        return True

    def market_cap_in_range(self, market_cap):
        if self.filters['market_cap'] == 'small' and market_cap >= 2e9:
            return False
        if self.filters['market_cap'] == 'mid' and (market_cap < 2e9 or market_cap > 10e9):
            return False
        if self.filters['market_cap'] == 'large' and market_cap <= 10e9:
            return False
        return True

    def set_filter(self, filter_name, filter_value):
        self.filters[filter_name] = filter_value