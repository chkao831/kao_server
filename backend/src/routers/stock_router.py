from fastapi import APIRouter, Response
from src.py_libs.controllers.stock_controller import ChapterController

router = APIRouter()
chapter_controller = ChapterController()

@router.get("/get_ch_txt/{chapter_id}")
async def get_chapter_txt(chapter_id: str):
    txt_path = chapter_controller.get_txt(chapter_id)
    return Response(content=txt_path.read_text(), media_type="text/plain")
