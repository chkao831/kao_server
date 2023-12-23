from fastapi import APIRouter

router = APIRouter()


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
