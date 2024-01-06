import datetime
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from alpaca.common.rest import RESTClient
from alpaca.data.historical import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import BaseBarsRequest, CryptoBarsRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from src import REPO
from src.private_keys.keys import KEY_ID, SERET_KEY
from src.py_libs.objects.basic_data_retriever import BasicDataRetriever
from src.py_libs.objects.enum import AssetType
from src.py_libs.utils.data_process import (
    get_historical_data_file_name,
    get_symbols_from_file_name,
)


@dataclass
class ClientComponents:
    client: RESTClient
    get_bars: Callable
    request_type: BaseBarsRequest


class AlpacaDataRetriever(BasicDataRetriever):
    def __init__(self):
        self.stock_client = StockHistoricalDataClient(KEY_ID, SERET_KEY)
        self.crypto_client = CryptoHistoricalDataClient(KEY_ID, SERET_KEY)
        self.saving_folder_path = REPO / "output/historical_data/"
        self.client_switcher = {
            AssetType.Stock: ClientComponents(
                client=self.stock_client,
                get_bars=self.stock_client.get_stock_bars,
                request_type=StockBarsRequest,
            ),
            AssetType.Crypto: ClientComponents(
                client=self.crypto_client,
                get_bars=self.crypto_client.get_crypto_bars,
                request_type=CryptoBarsRequest,
            ),
        }

    def get_historical_data(
        self,
        symbols: list,
        start: datetime.datetime,
        end: datetime.datetime,
        asset_type: AssetType,
        save_file=False,
    ) -> dict[str, pd.DataFrame]:
        """Get data of symbols one by one separately within given period.

        Args:
            symbols: list of symbols to get data
            start: start date
            end: end date
            asset_type: Crypto or Stock
            save_file: if save as a csv file

        Returns:
            a dict containing dataframe of symbols
        """
        symbols_dict = {}
        for symbol in symbols:
            client_component = self.client_switcher[asset_type]
            request_params = client_component.request_type(
                symbol_or_symbols=[symbol], timeframe=TimeFrame.Day, start=start, end=end
            )
            data_bars = client_component.get_bars(request_params)
            symbols_dict[symbol] = data_bars
            if save_file:
                st_time_str = start.strftime("%Y%m%d")
                ed_time_str = end.strftime("%Y%m%d")

                self.saving_folder_path.mkdir(parents=True, exist_ok=True)

                saving_file_path = self.saving_folder_path / get_historical_data_file_name(
                    st_time_str, ed_time_str, symbol, asset_type
                )

                data_bars.df.to_csv(saving_file_path)

        return symbols_dict

    def update_historical_data(self, csv_file: Path, asset_type: AssetType) -> pd.DataFrame:
        client_component = self.client_switcher[asset_type]
        data_delay_hours = 1 if asset_type == AssetType.Stock else 0
        data_pd = pd.read_csv(csv_file)
        start, end, symbol_name, file_asset_type = csv_file.stem.split("_")
        # change to from end to yesterday, no permission for free account
        new_start = datetime.datetime.strptime(end, "%Y%m%d")
        new_end = datetime.datetime.today() - datetime.timedelta(hours=data_delay_hours)

        symbols = get_symbols_from_file_name(symbol_name)
        request_params = client_component.request_type(
            symbol_or_symbols=symbols, timeframe=TimeFrame.Day, start=new_start, end=new_end
        )
        data_bars = client_component.get_bars(request_params)
        if len(data_bars.data) == 0:
            new_data_pd = data_pd
        else:
            new_bars = data_bars.df.reset_index()
            new_data_pd = pd.concat([data_pd, new_bars]).reset_index(drop=True)

        st_time_str = start
        ed_time_str = new_end.strftime("%Y%m%d")
        file_name = get_historical_data_file_name(st_time_str, ed_time_str, symbols, asset_type)
        new_csv_file = csv_file.parent / file_name
        new_data_pd.to_csv(new_csv_file, index=False)
        if new_csv_file != csv_file:
            csv_file.unlink()

        return data_pd

    def update_all_in_data_dir(self, asset_type: AssetType):
        for file_path in self.saving_folder_path.iterdir():
            start, end, symbols, file_asset_type = file_path.stem.split("_")
            self.update_historical_data(file_path, AssetType(file_asset_type))
