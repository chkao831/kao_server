from pathlib import Path

import hydra
from src.py_libs.alpaca_stock.trader import AlpacaTrader
from src.py_libs.objects.types import StrategyState
from src.py_libs.strategies.simple_strategy import SimpleStrategy
from src.py_libs.utils.data_process import load_historical_data


def main():
    with hydra.initialize(version_base=None, config_path="../src/config"):
        config = hydra.compose(config_name="main")

    # data_retriever = AlpacaDataRetriever()
    # data_retriever.get_historical_data(
    #     ["GOOG"], datetime(2021, 12, 1), datetime(2023, 12, 1), save_file=True
    # )
    # data_retriever.update_all_in_data_dir()

    historical_data = load_historical_data(Path("output/historical_data"))
    strategy_state = StrategyState(symbols=["AAPL"], symbols_data=historical_data)
    trader = AlpacaTrader()
    simple_strategy = SimpleStrategy(trader=trader)
    requests = simple_strategy.select_action(strategy_state)
    simple_strategy.trader.execute_requests(requests)
    print(simple_strategy)
    print(config)


if __name__ == "__main__":
    main()
