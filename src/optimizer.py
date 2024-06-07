from backtester import backtest

class Optimizer:
    def __init__(self, screener):
        self.screener = screener

    def run(self):
        # Define filter ranges
        filter_ranges = {
            'price': [(10, 50), (50, 100), (100, 200)],
            'market_cap': ['small', 'mid', 'large'],
            'dividend_yield': [(0, 2), (2, 4), (4, 6)],
            'average_volume': [(0, 100000), (100000, 500000), (500000, 1000000)],
            # Add other filters as needed
        }

        # Fetch data
        data = self.screener.fetch_data()

        # Optimization loop
        best_value = 0
        best_filters = {}

        for price_range in filter_ranges['price']:
            for market_cap in filter_ranges['market_cap']:
                for dividend_yield in filter_ranges['dividend_yield']:
                    for average_volume in filter_ranges['average_volume']:
                        # Set filters
                        self.screener.set_filter('price', price_range)
                        self.screener.set_filter('market_cap', market_cap)
                        self.screener.set_filter('dividend_yield', dividend_yield)
                        self.screener.set_filter('average_volume', average_volume)

                        # Apply filters
                        filtered_data = self.screener.apply_filters(data)
                        if not filtered_data:
                            continue

                        # Backtest filtered data
                        backtest_value = backtest(filtered_data)

                        # Check if this is the best combination
                        if backtest_value > best_value:
                            best_value = backtest_value
                            best_filters = {
                                'price': price_range,
                                'market_cap': market_cap,
                                'dividend_yield': dividend_yield,
                                'average_volume': average_volume
                            }

        print(f"Best backtested portfolio value: {best_value}")
        print(f"Optimal filters: {best_filters}")