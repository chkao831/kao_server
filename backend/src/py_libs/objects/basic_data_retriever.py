import datetime
from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class BasicDataRetriever(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_historical_data(
        self, symbols: list, start: datetime.datetime, end: datetime.datetime, save_file=False
    ) -> pd.DataFrame:
        pass

    @abstractmethod
    def update_historical_data(self, csv_file: Path) -> pd.DataFrame:
        pass

    @abstractmethod
    def update_all_in_data_dir(self):
        pass
