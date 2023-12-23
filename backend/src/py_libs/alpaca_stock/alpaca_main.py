# from datetime import datetime
#
# from alpaca.data.historical import StockHistoricalDataClient
# from alpaca.data.requests import StockBarsRequest, StockLatestQuoteRequest
# from alpaca.data.timeframe import TimeFrame
# from alpaca.trading.client import TradingClient
# from alpaca.trading.enums import OrderSide, TimeInForce
# from alpaca.trading.requests import MarketOrderRequest

# Create instance of Alpaca data streaming API

# =============== DataStream


# ===== websocket
# import websocket, json
#
# def on_open(ws):
#     print("opened")
#     auth_data = {
#         "action": "auth",
#         "data": {"key_id":'}
#     }
#
#     ws.send(json.dumps(auth_data))
#
#     listen_message = {"action":"subscribe", "quotes":["AMD"]}
#
#     ws.send(json.dumps(listen_message))
#
#
# def on_message(ws, message):
#     print("received a message")
#     print(message)
#
#
# def on_close(ws):
#     print("closed connection")
#
#
# socket = 'wss://stream.data.sandbox.alpaca.markets/v2/iex'
#
# ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
# ws.run_forever()
