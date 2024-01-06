import datetime
from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd
from src.py_libs.objects.enum import AssetType


class BasicDataRetriever(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_historical_data(
        self,
        symbols: list,
        start: datetime.datetime,
        end: datetime.datetime,
        asset_type: AssetType,
        save_file=False,
    ) -> dict[str, pd.DataFrame]:
        pass

    @abstractmethod
    def update_historical_data(self, csv_file: Path, asset_type: AssetType) -> pd.DataFrame:
        pass

    @abstractmethod
    def update_all_in_data_dir(self, asset_type: AssetType):
        pass
