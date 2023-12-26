from abc import ABC, abstractmethod

import numpy as np


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

    def select_action(self, state):
        pass
