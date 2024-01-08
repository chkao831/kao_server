from datetime import datetime, timedelta
from pathlib import Path

import hydra
from src import REPO
from src.py_libs.alpaca_stock.data_retriever import AlpacaDataRetriever
from src.py_libs.alpaca_stock.trader import AlpacaTrader
from src.py_libs.objects.enum import AssetType
from src.py_libs.objects.types import StrategyState
from src.py_libs.strategies.simple_strategy import SimpleStrategy
from src.py_libs.utils.data_process import load_historical_data


def main():
    with hydra.initialize_config_dir(version_base=None, config_dir=str(REPO / "src/config")):
        config = hydra.compose(config_name="main")

    data_retriever = AlpacaDataRetriever()
    data_retriever.get_historical_data(
        ["BTC/USD", "ETH/USD"],
        datetime(2023, 12, 1),
        datetime(2023, 12, 10),
        interval=timedelta(minutes=10),
        asset_type=AssetType.Crypto,
        save_file=True,
    )
    data_retriever.update_all_in_data_dir(asset_type=AssetType.Crypto)

    historical_data = load_historical_data(Path("output/historical_data"))
    strategy_state = StrategyState(symbols=["BTC/USD", "ETH/USD"], symbols_data=historical_data)
    trader = AlpacaTrader()
    simple_strategy = SimpleStrategy(trader=trader)
    requests = simple_strategy.select_action(strategy_state, asset_type=AssetType.Crypto)
    simple_strategy.trader.execute_requests(requests)
    print(simple_strategy)
    print(config)


if __name__ == "__main__":
    main()