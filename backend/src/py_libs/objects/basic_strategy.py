from abc import ABC, abstractmethod

from src.py_libs.objects.types import StrategyState


class BasicStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def select_action(self, state: StrategyState) -> None:
        pass
