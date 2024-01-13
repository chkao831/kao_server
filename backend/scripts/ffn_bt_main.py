import bt

# import ffn

# fetch some data
data = bt.get("spy,agg", start="2019-01-01")
print(data.head())
