from dataclasses import dataclass

import numpy as np
import pandas as pd
from src import HISTORICAL_DATA_FEATURES


class HistoricalData:
    """HistoricalData need  all HISTORICAL_DATA_FEATURES and keep a numpy cache of
    HISTORICAL_DATA_FEATURES for quick access"""

    def __init__(self, data_pd: pd.DataFrame):
        for feat in HISTORICAL_DATA_FEATURES:
            if feat not in data_pd.columns:
                raise ValueError(
                    f"HistoricalData need all HISTORICAL_DATA_FEATURES but '{feat}' is missing."
                )
        self.data_pandas: pd.DataFrame = data_pd
        self.data_numpy: np.ndarray | None = None

    @property
    def data_np(self) -> np.ndarray:
        if self.data_numpy is None:
            self.data_numpy = self.data_pandas[HISTORICAL_DATA_FEATURES].to_numpy()
        return self.data_numpy

    @property
    def data_pd(self) -> pd.DataFrame:
        return self.data_pandas


@dataclass
class TradingRequest:
    price: float
    quantity: float
    requests_type: str
