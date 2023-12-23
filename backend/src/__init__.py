import datetime

from omegaconf import OmegaConf

REPO = __file__[: __file__.find("src")]


def datetime_resolver(time):
    datetime_format = "%Y-%m-%d %H:%M:%S"
    return datetime.datetime.strptime(time, datetime_format)


OmegaConf.register_new_resolver("time", datetime_resolver())
