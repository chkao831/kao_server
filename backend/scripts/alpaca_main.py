from pathlib import Path

import hydra
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

    load_historical_data(Path("output/historical_data"))
    simple_strategy = SimpleStrategy()

    print(simple_strategy)
    print(config)


if __name__ == "__main__":
    main()
