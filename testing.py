import yfinance as yf

def fetch_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    calendar = stock.calendar

    earnings_date = 'N/A'
    if isinstance(calendar, dict) and 'Earnings Date' in calendar:
        earnings_date = calendar['Earnings Date']

    attributes = {
        "Exchange": info.get("exchange", "N/A"),
        "Sector": info.get("sector", "N/A"),
        "Industry": info.get("industry", "N/A"),
        "Country": info.get("country", "N/A"),
        "Market Cap": info.get("marketCap", "N/A"),
        "Dividend Yield": info.get("dividendYield", "N/A"),
        "Float Short": info.get("shortPercentOfFloat", "N/A"),
        "Analyst Recommendation": info.get("recommendationMean", "N/A"),
        "Option Short": info.get("shortName", "N/A"),
        "Earnings Date": earnings_date,
        "Average Volume": info.get("averageVolume", "N/A"),
        "Current Volume": stock.history(period="1d")['Volume'].iloc[-1] if not stock.history(period="1d").empty else 'N/A',
        "Price": stock.history(period="1d")['Close'].iloc[-1] if not stock.history(period="1d").empty else 'N/A',
        "Target Price": info.get("targetMeanPrice", "N/A"),
        "IPO Date": info.get("ipoDate", "N/A"),
        "Shares Outstanding": info.get("sharesOutstanding", "N/A"),
        "Float": info.get("floatShares", "N/A")
    }

    for attr, value in attributes.items():
        print(f"{attr}: {value}")

# Example usage
fetch_stock_info("AAPL")
