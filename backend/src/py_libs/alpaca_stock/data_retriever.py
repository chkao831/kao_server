# ============ Stock historical data
# # keys required for stock historical data client
#
# # multi symbol request - single symbol is similar
# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])
#
# request_params = StockBarsRequest(
#                         symbol_or_symbols=["AAPL", "GOOG"],
#                         timeframe=TimeFrame.Day,
#                         start=datetime(2021, 7, 1),
#                         end=datetime(2022, 9, 1)
#                  )
#
# latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)
# stock_bars = client.get_stock_bars(request_params)
#
# gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price
#
# print(gld_latest_ask_price)

from alpaca.data.historical import StockHistoricalDataClient
from src.private_keys.keys import KEY_ID, SERET_KEY


class AlpacaDataRetriever:
    def __init__(self):
        self.client = StockHistoricalDataClient(KEY_ID, SERET_KEY)

    def get_historical_data(self, symbols, start, end, timeframe, save_path=None):
        pass

    def get_stream_data(self, symbols):
        pass
