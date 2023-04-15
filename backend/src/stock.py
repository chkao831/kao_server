from src.py_libs.objects.stock_data import StockDataHandler
import logging
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from datetime import datetime

api = ['C2V30XU2UCBFGIAT',
       'QV3LU4DT8MRXH5KA',
       'T5SGMB43G0HDYRZV',
       'TM2Q8WNAPM96UR10',
       '10BPTI39DXMDXBL4',
       'WUTQYDO6CNMMZEOG',
       '440PJWGZ5H4BF4KN',
       '5CWPWQ1HH58QT1AT',
       'SHC7F820VSO911Z2',
       'Q3ZOVCAQKSEZE168',
       'SWCF6RGAH0HL32KH',
       'Q0QN86T6K9K5NOXM',
       ]
FORMAT = ' %(name)s :: %(levelname)-8s :: %(message)s'
logging.basicConfig(format=FORMAT, level = logging.INFO)
logger = logging.getLogger(__file__)

def refill_unfetchable_data(cur_date: str="2088/8/28"):
    root_folder = Path('./stock_raw_data')
    tmp_path = root_folder / 'tmp_file.csv'
    cur_date = datetime.strptime(cur_date, '%Y/%m/%d')

    for file in tqdm(root_folder.iterdir()):
        df = pd.read_csv(file)
        last_date = df.iloc[:, 1].iloc[-1]
        last_date = datetime.strptime(last_date, '%Y/%m/%d')
        if cur_date>= last_date:
            continue




if __name__ == '__main__':
    tool = StockDataHandler()
    tool.fetch_until_today()
