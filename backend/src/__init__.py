import datetime
from pathlib import Path

from omegaconf import OmegaConf

REPO = Path(__file__[: __file__.find("src")])
START_TIMESTAMP = datetime.datetime(2000, 1, 1)


def datetime_resolver(time):
    datetime_format = "%Y-%m-%d %H:%M:%S"
    return datetime.datetime.strptime(time, datetime_format)


OmegaConf.register_new_resolver("time", datetime_resolver)
