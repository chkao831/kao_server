from abc import ABC, abstractmethod

import pandas as pd


class BasicStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def select_action(self, state):
        pass


class SimpleStrategy(BasicStrategy):
    def __init__(self, historical_data: pd.DataFrame):
        super().__init__()
        self.historical_data = historical_data
        self.biases = {}

    def select_action(self, state):
        pass
