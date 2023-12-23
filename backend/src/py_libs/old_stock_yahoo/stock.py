import logging
from datetime import datetime
from pathlib import Path

import pandas as pd
from src.py_libs.old_stock_yahoo.data_preprocess import DataPreprocessor

# from src.py_libs.old_stock_yahoo.stock_data import StockDataHandler
from tqdm import tqdm

api = [
    "C2V30XU2UCBFGIAT",
    "QV3LU4DT8MRXH5KA",
    "T5SGMB43G0HDYRZV",
    "TM2Q8WNAPM96UR10",
    "10BPTI39DXMDXBL4",
    "WUTQYDO6CNMMZEOG",
    "440PJWGZ5H4BF4KN",
    "5CWPWQ1HH58QT1AT",
    "SHC7F820VSO911Z2",
    "Q3ZOVCAQKSEZE168",
    "SWCF6RGAH0HL32KH",
    "Q0QN86T6K9K5NOXM",
]
FORMAT = " %(name)s :: %(levelname)-8s :: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__file__)


def refill_unfetchable_data(cur_date: str = "2088/8/28"):
    root_folder = Path("./stock_raw_data")
    cur_date = datetime.strptime(cur_date, "%Y/%m/%d")

    for file in tqdm(root_folder.iterdir()):
        df = pd.read_csv(file)
        last_date = df.iloc[:, 1].iloc[-1]
        last_date = datetime.strptime(last_date, "%Y/%m/%d")
        if cur_date >= last_date:
            continue


if __name__ == "__main__":
    # tool = StockDataHandler()
    # tool.fetch_history()
    tool = DataPreprocessor()
    tool.check_na()
