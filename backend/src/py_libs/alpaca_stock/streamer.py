from alpaca.data.live.stock import StockDataStream
from src.private_keys.keys import KEY_ID, SERET_KEY

# keys are required for live data
wss_client = StockDataStream(KEY_ID, SERET_KEY)


async def quote_data_handler(data):
    # quote data will arrive here
    print("Received")
    print(data)


wss_client.subscribe_quotes(quote_data_handler, "GOOG")
wss_client.subscribe_quotes(quote_data_handler, "AMZN")

wss_client.run()
