from abc import ABC, abstractmethod

from src.py_libs.objects.types import AccountPortfolio, TradingRequest


class BasicTrader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_portfolio(self) -> AccountPortfolio:
        pass

    @abstractmethod
    def execute_requests(self, requests: list[TradingRequest]) -> None:
        pass

    @abstractmethod
    def get_orders(self) -> None:
        pass

    @abstractmethod
    def cancel_order(self):
        pass
