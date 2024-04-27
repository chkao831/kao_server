import datetime
from pathlib import Path

REPO = Path(__file__[: __file__.find("src")])
START_TIMESTAMP = datetime.datetime(2000, 1, 1)
HISTORICAL_DATA_FEATURES = [
    "timestamp_int",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "trade_count",
    "vwap",
]
REAL_TIME_DATA_FEATURES = ["price"]


