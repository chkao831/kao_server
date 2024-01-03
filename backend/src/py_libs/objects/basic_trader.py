from abc import ABC, abstractmethod

from src.py_libs.objects.types import AccountPortfolio


class BasicTrader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_portfolio(self) -> AccountPortfolio:
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
