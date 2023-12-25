import pickle
from abc import ABC, abstractmethod

import numpy as np
import src


class BasicStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def select_action(self, state):
        pass


class SimpleStrategy(BasicStrategy):
    def __init__(self, historical_data: dict[str, np.ndarray]):
        super().__init__()
        self.historical_data = historical_data
        self.biases = {symbol: 0 for symbol in historical_data.keys()}
        with open(
            src.REPO / "tests/test_data/test_historical_data/test_two_historical_data.pkl", "wb"
        ) as f:
            pickle.dump(historical_data, f)

    def select_action(self, state):
        pass
