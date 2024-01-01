from abc import ABC, abstractmethod


class BasicStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def select_action(self, state) -> None:
        pass
