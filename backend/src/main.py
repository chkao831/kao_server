import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.routers import stock_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    stock_router.router,
    prefix="/Stock",
    tags=["Stock"],
    responses={404: {"description": "Not found"}},
)
app.mount("/", StaticFiles(directory="./static/my_html", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=5000, host="0.0.0.0", log_level="info")
