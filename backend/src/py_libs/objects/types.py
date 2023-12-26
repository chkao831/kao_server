import numpy as np


class HistoricalData:
    def __init__(self, data: np.ndarray):
        self.data: np.ndarray = data
        self.extra = {}


class RealTimeData:
    def __init__(self, data: np.ndarray):
        self.data: np.ndarray = data
        self.extra = {}
