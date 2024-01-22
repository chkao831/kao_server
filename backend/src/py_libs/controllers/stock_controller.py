import os
from pathlib import Path


class StockController:
    def __init__(self) -> None:
        self.RoleList = []

    def create_role(self, role) -> None:
        self.RoleList.append(role)


IMG_DIR = os.environ.get("IMG_DIR", "data")


class ChapterController:
    def __init__(self) -> None:
        self.img_dir_abs = os.path.abspath(IMG_DIR)

    def get_image(self, chapter_id) -> None:
        img_path = Path(self.img_dir_abs) / f"{chapter_id}.png"
        return img_path

    def get_txt(self, chapter_id) -> None:
        txt_path = Path(self.img_dir_abs) / f"{chapter_id}.txt"
        return txt_path
        
    