import datetime
from pathlib import Path

import pandas as pd
from src import REPO, START_TIMESTAMP


def load_historical_data(folder_path: Path):
    all_data = {}
    needed_col = ["timestamp_int", "open", "high", "low", "close", "volume", "trade_count", "vwap"]
    for path in (REPO / folder_path).iterdir():
        data = pd.read_csv(path)
        symbol_name = data["symbol"].loc[0]
        data["timestamp_int"] = data["timestamp"].apply(
            lambda x: (
                datetime.datetime.strptime(x.split(" ")[0], "%Y-%m-%d") - START_TIMESTAMP
            ).days
        )
        needed_data_np = data[needed_col].to_numpy()
        all_data[symbol_name] = needed_data_np
    return all_data
