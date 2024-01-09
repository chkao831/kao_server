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
            return self._select_action_crypto(state)
        elif asset_type == AssetType.Stock:
            return self._select_action_stock(state)
        else:
            raise ValueError(f"Unsupported asset_type: {asset_type}")

    def _select_action_stock(self, state: StrategyState) -> list[TradingRequest]:
        portfolio = self.trader.get_portfolio()
        requests = []
        for symbol in state.symbols:
            # current_price = self.trader.get_latest_quote([symbol])
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
            buying_power = portfolio.total_market_value
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
