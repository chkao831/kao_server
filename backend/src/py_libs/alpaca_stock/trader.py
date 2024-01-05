# ============ Stock trading

# from alpaca.trading.client import TradingClient
# trading_client = TradingClient(keys, url_override="https://api.alpaca.markets")
# account = trading_client.get_account()
#
# market_order_data = MarketOrderRequest(
#                     symbol="AMZN",
#                     qty=0.01,
#                     side=OrderSide.SELL,
#                     time_in_force=TimeInForce.DAY
#                     )
#
# market_order = trading_client.submit_order(
#                 order_data=market_order_data
#                )
# print(market_order_data)
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest
from src.private_keys.keys import KEY_ID, SERET_KEY
from src.py_libs.objects.basic_trader import BasicTrader
from src.py_libs.objects.enum import OrderType, RequestType
from src.py_libs.objects.types import AccountPortfolio, EquityPosition, TradingRequest


class AlpacaTrader(BasicTrader):
    def __init__(self):
        self.trading_client = TradingClient(
            KEY_ID, SERET_KEY, url_override="https://api.alpaca.markets"
        )

    def get_portfolio(self) -> AccountPortfolio:
        alpaca_positions = self.trading_client.get_all_positions()
        account = self.trading_client.get_account()

        positions = {
            pos.symbol: EquityPosition(
                symbol=pos.symbol, qty=float(pos.qty), market_value=float(pos.market_value)
            )
            for pos in alpaca_positions
        }

        portfolio = AccountPortfolio(
            total_market_value=float(account.portfolio_value), positions=positions
        )

        return portfolio

    def execute_requests(self, requests: list[TradingRequest]) -> None:
        for request in requests:
            if request.order_type == OrderType.Limit:
                market_order_data = LimitOrderRequest(
                    symbol=request.symbol,
                    qty=request.qty,
                    limit_price=request.price,
                    side=OrderSide.SELL
                    if request.requests_type == RequestType.Sell
                    else OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                )

            elif request.order_type == OrderType.Market:
                market_order_data = MarketOrderRequest(
                    symbol=request.symbol,
                    qty=request.qty,
                    side=OrderSide.SELL
                    if request.requests_type == RequestType.Sell
                    else OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                )
            else:
                raise ValueError(f"Unsupported order_type: {request.order_type}")
            market_order = self.trading_client.submit_order(order_data=market_order_data)
            print(f"Executed {market_order}")

    def get_orders(self):
        pass

    def cancel_order(self):
        pass
