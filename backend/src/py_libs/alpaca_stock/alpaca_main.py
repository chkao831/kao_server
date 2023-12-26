# from datetime import datetime
#
# from alpaca.data.historical import StockHistoricalDataClient
# from alpaca.data.requests import StockBarsRequest, StockLatestQuoteRequest
# from alpaca.data.timeframe import TimeFrame
# from alpaca.trading.client import TradingClient
# from alpaca.trading.enums import OrderSide, TimeInForce
# from alpaca.trading.requests import MarketOrderRequest

# Create instance of Alpaca data streaming API

# =============== DataStream


from pathlib import Path

import hydra
from src.py_libs.strategies.simple_strategy import SimpleStrategy
from src.py_libs.utils.data_process import load_historical_data


def main():
    with hydra.initialize(version_base=None, config_path="../../../src/config"):
        config = hydra.compose(config_name="main")

    # data_retriever = AlpacaDataRetriever()
    # data_retriever.get_historical_data(
    #     ["GOOG"], datetime(2021, 12, 1), datetime(2023, 12, 1), save_file=True
    # )
    # data_retriever.update_all_in_data_dir()

    all_historical_data = load_historical_data(Path("output/historical_data"))
    simple_strategy = SimpleStrategy(all_historical_data)

    print(simple_strategy)
    print(config)


if __name__ == "__main__":
    main()
