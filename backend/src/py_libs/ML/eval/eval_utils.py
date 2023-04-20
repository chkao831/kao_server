import numpy as np

def get_profit(output, label,):
    label_len = label.shape[1]
    output_len = output.shape[1]

    label_low = label[:, :label_len // 2]
    label_high = label[:, label_len // 2:]

    out_low = output[:, :output_len // 2]
    out_high = output[:, output_len // 2:]
    # Problem, a is not all -1
    a = np.where(label_low < label_high, -1, label_low)
    buy_price = np.where(label_low <= out_low, 0, label_low)
    sell_price = np.where(out_high <= label_high, out_high, buy_price-0.5)


    profit = np.where(buy_price==0, 0, sell_price-buy_price)

    return profit.sum()
