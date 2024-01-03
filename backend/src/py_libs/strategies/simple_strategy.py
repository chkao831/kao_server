from src.py_libs.objects.basic_strategy import BasicStrategy
from src.py_libs.objects.basic_trader import BasicTrader
from src.py_libs.objects.types import StrategyState, TradingRequest


class SimpleStrategy(BasicStrategy):
    def __init__(self, trader: BasicTrader):
        super().__init__()
        self.biases = {}
        self.trader = trader

    def select_action(self, state: StrategyState) -> list[TradingRequest]:
        portfolio = self.trader.get_portfolio()
        requests = []
        for symbol in state.symbols:
            expected_price = state.symbols_data[symbol].data_np[:, 1:4].mean()
            buy_price = expected_price * 0.85
            sell_price = expected_price * 1.15
            if symbol in portfolio.positions:
                sell_qty = portfolio.positions[symbol].qty
                sell_req = TradingRequest(qty=sell_qty, price=sell_price, requests_type="sell")
                requests.append(sell_req)
            buy_qty = portfolio.total_market_value / buy_price
            buy_req = TradingRequest(qty=buy_qty, price=buy_price, requests_type="buy")
            requests.append(buy_req)
        return requests
