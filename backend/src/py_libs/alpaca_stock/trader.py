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
from src.private_keys.keys import KEY_ID, SERET_KEY
from src.py_libs.objects.basic_trader import BasicTrader
from src.py_libs.objects.types import AccountPortfolio, EquityPosition


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

    def buy_stock(self, symbol, qty):
        pass

    def sell_stock(self, symbol, qty):
        pass

    def get_orders(self):
        pass

    def cancel_order(self):
        pass
