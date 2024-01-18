import bt

# import ffn

# fetch some data
data = bt.get("spy,agg", start="2022-01-01")
print(data.head())
s = bt.Strategy(
    "s1",
    [bt.algos.RunMonthly(), bt.algos.SelectAll(), bt.algos.WeighEqually(), bt.algos.Rebalance()],
)

# create a backtest and run it
test = bt.Backtest(s, data)
res = bt.run(test)

# first let's see an equity curve
res.plot()

# ok and what about some stats?
res.display()

# ok and how does the return distribution look like?
res.plot_histogram()
print("OK")
