import datetime
from datetime import timedelta
from pathlib import Path

import pandas as pd
from src import HISTORICAL_DATA_FEATURES, REPO, START_TIMESTAMP
from src.py_libs.objects.enum import AssetType
from src.py_libs.objects.types import HistoricalData


def load_historical_data(folder_path: Path, interval_minutes: int):
    all_data = {}
    for path in (REPO / folder_path).iterdir():
        data = pd.read_csv(path)
        symbol_name = data["symbol"].loc[0]
        # Convert seconds from start_timestamp and convert into interval_minutes
        data["timestamp_int"] = data["timestamp"].apply(
            lambda x: int(
                (
                    datetime.datetime.strptime(x.split("+")[0], "%Y-%m-%d %H:%M:%S")
                    - START_TIMESTAMP
                ).total_seconds()
            )
            // 60
            // interval_minutes
        )
        all_data[symbol_name] = HistoricalData(data[HISTORICAL_DATA_FEATURES])
    return all_data


def get_historical_data_file_name(
    st_time_str: str, ed_time_str: str, symbol_name: str, interval: timedelta, asset_type: AssetType
) -> str:
    # Deal symbols with "/"
    symbol_name = symbol_name.replace("/", "-")
    interval_min = interval.seconds // 60

    file_path = f"{st_time_str}_{ed_time_str}_{interval_min}m_{symbol_name}_{asset_type.value}.csv"
    return file_path


def get_symbols_from_file_name(symbol_name: str) -> str:
    # Revert symbols with "/"
    symbol_name = symbol_name.replace("-", "/")
    return symbol_name
