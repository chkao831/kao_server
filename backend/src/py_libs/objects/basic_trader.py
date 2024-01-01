from abc import ABC, abstractmethod


class BasicTrader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def buy_stock(self, symbol, qty) -> None:
        pass

    @abstractmethod
    def sell_stock(self, symbol, qty) -> None:
        pass

    @abstractmethod
    def get_orders(self) -> None:
        pass

    @abstractmethod
    def cancel_order(self):
        pass
