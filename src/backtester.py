import backtrader as bt

class BacktestStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if not self.position:
            self.buy()

def backtest(data):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(BacktestStrategy)
    for ticker, df in data.items():
        df_bt = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(df_bt)
    cerebro.broker.set_cash(100000)
    cerebro.run()
    return cerebro.broker.getvalue()