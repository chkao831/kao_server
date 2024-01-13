from src.py_libs.objects.basic_strategy import BasicStrategy
from src.py_libs.objects.basic_trader import BasicTrader
from src.py_libs.objects.enum import AssetType, OrderType, RequestType, TimeForce
from src.py_libs.objects.types import StrategyState, TradingRequest


class SimpleStrategy(BasicStrategy):
    def __init__(self, trader: BasicTrader):
        super().__init__()
        self.biases = {}
        self.trader = trader

    def select_action(self, state: StrategyState, asset_type: AssetType) -> list[TradingRequest]:
        if asset_type == AssetType.Crypto:
            raise ValueError(f"Unsupported asset_type: {asset_type}")
            return self._select_action_crypto(state)
        elif asset_type == AssetType.Stock:
            return self._select_action_stock(state)
        else:
            raise ValueError(f"Unsupported asset_type: {asset_type}")

    def _select_action_stock(self, state: StrategyState) -> list[TradingRequest]:
        """Return a MarketOrderRequest according to current price, size and expected price.

        Args:
            state:

        Returns:

        """
        portfolio = self.trader.get_portfolio()
        requests = []
        for symbol in state.symbols:
            latest_quote = state.symbols_latest_quote[symbol]
            hist_data = state.symbols_data[symbol]
            current_price = (latest_quote.ask_price + latest_quote.bid_price) / 2
            current_quote_size = min(latest_quote.ask_size, latest_quote.bid_size)

            expected_price = hist_data.data_np[-50:, 1:4].mean()
            buy_price = expected_price * 0.85
            sell_price = expected_price * 1.15
            if symbol in portfolio.positions and current_price > sell_price:
                sell_qty = min(portfolio.positions[symbol].qty, current_quote_size)
                sell_req = TradingRequest(
                    symbol=symbol,
                    qty=sell_qty,
                    requests_type=RequestType.SELL,
                    order_type=OrderType.MARKET,
                    time_force=TimeForce.IOC,
                )
                requests.append(sell_req)
            buying_power = portfolio.total_market_value
            buying_power_qty = buying_power / buy_price
            buy_qty = min(buying_power_qty, current_quote_size)
            if current_price < buy_price:
                buy_req = TradingRequest(
                    symbol=symbol,
                    qty=buy_qty,
                    requests_type=RequestType.BUY,
                    order_type=OrderType.MARKET,
                    time_force=TimeForce.IOC,
                )
                requests.append(buy_req)
        return requests

    def _select_action_crypto(self, state: StrategyState) -> list[TradingRequest]:
        portfolio = self.trader.get_portfolio()
        requests = []
        for symbol in state.symbols:
            expected_price = state.symbols_data[symbol].data_np[-50:, 1:4].mean()
            buy_price = expected_price * 0.85
            sell_price = expected_price * 1.15
            if symbol in portfolio.positions:
                sell_qty = portfolio.positions[symbol].qty
                sell_req = TradingRequest(
                    symbol=symbol,
                    qty=sell_qty,
                    price=sell_price,
                    requests_type=RequestType.SELL,
                    order_type=OrderType.LIMIT,
                    time_force=TimeForce.IOC,
                )
                requests.append(sell_req)
            buying_power = portfolio.non_marginable_buying_power
            buy_qty = buying_power / buy_price
            buy_req = TradingRequest(
                symbol=symbol,
                qty=buy_qty,
                price=buy_price,
                requests_type=RequestType.BUY,
                order_type=OrderType.LIMIT,
                time_force=TimeForce.IOC,
            )
            requests.append(buy_req)
        return requests
