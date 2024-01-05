from enum import Enum


class RequestType(Enum):
    Sell = "Sell"
    Buy = "Buy"


class OrderType(Enum):
    Limit = "Limit"
    Market = "Market"
