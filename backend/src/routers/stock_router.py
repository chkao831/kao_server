from fastapi import APIRouter, Response, HTTPException
from src.py_libs.controllers.stock_controller import ChapterController


router = APIRouter()
chapter_controller = ChapterController()

@router.get("/get_ch_txt/{chapter_id}")
async def get_chapter_txt(chapter_id: str):
    try:
        html_content = chapter_controller.get_txt(chapter_id)
        return Response(content=html_content, media_type="text/html")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))