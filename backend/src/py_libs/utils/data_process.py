import datetime
from pathlib import Path

import pandas as pd
from src import HISTORICAL_DATA_FEATURES, REPO, START_TIMESTAMP
from src.py_libs.objects.types import HistoricalData


def load_historical_data(folder_path: Path):
    all_data = {}
    for path in (REPO / folder_path).iterdir():
        data = pd.read_csv(path)
        symbol_name = data["symbol"].loc[0]
        data["timestamp_int"] = data["timestamp"].apply(
            lambda x: (
                datetime.datetime.strptime(x.split(" ")[0], "%Y-%m-%d") - START_TIMESTAMP
            ).days
        )
        all_data[symbol_name] = HistoricalData(data[HISTORICAL_DATA_FEATURES])
    return all_data
