from fastapi import APIRouter, Response
from src.py_libs.controllers.stock_controller import ChapterController

router = APIRouter()

chapter_controller = ChapterController()


@router.post("/createRole")
def create_role(role: dict):
    print(role)
    return {"CreatedRole": role}


@router.get("/startTrade")
def fetch_plot():
    print("fetch_plot: ")
    return {"isReady": True}


@router.get("/stopTrade")
def stop_trade():
    print("fetch_plot: ")
    return {"isReady": True}


@router.get("/fetchTransaction")
def fetch_transaction():
    print("fetch_plot: ")
    return {"isReady": True}


@router.get("/fetchPrediction")
def fetch_prediction():
    print("fetch_plot: ")
    return {"isReady": True}


@router.get("/fetchHistorical/{days}")
def fetch_historical(days: int):
    print("fetch_plot: ", days)
    return {"isReady": True}


@router.get("/get_ch/{chapter_id}")
def get_chapter(chapter_id: str):
    img_path = chapter_controller.get_image(chapter_id)
    return Response(content=img_path.read_bytes(), media_type="image/png")
