from enum import Enum


class RequestType(Enum):
    Sell = "Sell"
    Buy = "Buy"


class OrderType(Enum):
    Limit = "Limit"
    Market = "Market"


class TimeForce(Enum):
    DAY = "DAY"
    IOC = "IOC"
    FOK = "FOK"
