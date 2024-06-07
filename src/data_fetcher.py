import yfinance as yf
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    def __init__(self):
        self.periods = ['1y', '6mo', '3mo', '1mo', '1d']

    def fetch_data_for_ticker(self, ticker):
        for period in self.periods:
            try:
                df = yf.Ticker(ticker).history(period=period)
                if not df.empty:
                    logger.info(f"Fetched data for {ticker} with period {period}")
                    return ticker, df
            except Exception as e:
                logger.warning(f"Error fetching data for {ticker} with period {period}: {e}")
                continue
        logger.warning(f"{ticker}: No valid data found for any period")
        return ticker, None

    def fetch_data(self, tickers):
        data = {}
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_ticker = {executor.submit(self.fetch_data_for_ticker, ticker): ticker for ticker in tickers}
            for future in as_completed(future_to_ticker):
                ticker, df = future.result()
                if df is not None:
                    data[ticker] = df
        logger.info("Data fetching process completed")
        return data