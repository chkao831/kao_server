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

import datetime
from pathlib import Path

import pandas as pd
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from src import REPO
from src.private_keys.keys import KEY_ID, SERET_KEY


class AlpacaDataRetriever:
    def __init__(self):
        self.client = StockHistoricalDataClient(KEY_ID, SERET_KEY)
        self.saving_folder_path = REPO / "output/historical_data/"

    def get_historical_data(
        self, symbols: list, start: datetime.datetime, end: datetime.datetime, save_file=False
    ) -> pd.DataFrame:
        request_params = StockBarsRequest(
            symbol_or_symbols=symbols, timeframe=TimeFrame.Day, start=start, end=end
        )
        stock_bars = self.client.get_stock_bars(request_params)
        if save_file:
            st_time_str = start.strftime("%Y%m%d")
            ed_time_str = end.strftime("%Y%m%d")
            symbol_name = "-".join(symbols)
            self.saving_folder_path.mkdir(parents=True, exist_ok=True)
            saving_file_path = (
                self.saving_folder_path / f"{st_time_str}_{ed_time_str}_{symbol_name}.csv"
            )

            stock_bars.df.to_csv(saving_file_path)

        return stock_bars.df

    def update_historical_data(self, csv_file: Path) -> pd.DataFrame:
        data_pd = pd.read_csv(csv_file)
        start, end, symbols = csv_file.stem.split("_")
        # change to from end to yesterday, no permission for free account
        new_start = datetime.datetime.strptime(end, "%Y%m%d")
        new_end = datetime.datetime.today() - datetime.timedelta(hours=1)
        symbols = symbols.split("-")
        request_params = StockBarsRequest(
            symbol_or_symbols=symbols, timeframe=TimeFrame.Day, start=new_start, end=new_end
        )
        stock_bars = self.client.get_stock_bars(request_params)
        new_bars = stock_bars.df.reset_index()
        new_data_pd = pd.concat([data_pd, new_bars]).reset_index(drop=True)

        symbol_name = "-".join(symbols)
        st_time_str = start
        ed_time_str = new_end.strftime("%Y%m%d")
        file_name = f"{st_time_str}_{ed_time_str}_{symbol_name}.csv"
        new_csv_file = csv_file.parent / file_name
        new_data_pd.to_csv(new_csv_file, index=False)
        csv_file.unlink()

        return data_pd

    def update_all_in_data_dir(self):
        for file_path in self.saving_folder_path.iterdir():
            self.update_historical_data(file_path)
