from screener import StockScreener
from optimizer import Optimizer

def main():
    screener = StockScreener()
    optimizer = Optimizer(screener)
    optimizer.run()

if __name__ == "__main__":
    main()
