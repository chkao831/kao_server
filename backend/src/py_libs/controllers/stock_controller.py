import os
from pathlib import Path


class StockController:
    def __init__(self) -> None:
        self.RoleList = []

DATA_DIR = os.environ.get("DATA_DIR", "data")

class ChapterController:
    def __init__(self) -> None:
        self.data_dir_abs = os.path.abspath(DATA_DIR)

    def get_txt(self, chapter_id) -> None:
        txt_path = Path(self.data_dir_abs) / f"{chapter_id}.txt"
        return txt_path
