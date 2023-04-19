import torch
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import torch.nn as nn
from tqdm import tqdm
from src.py_libs.model.model import Net
from src.py_libs.dataset.dataset import StockDataset
import matplotlib.pyplot as plt


# Create a DataLoader object to manage your data
stock_data_path="./stock_raw_data"
train_dataset = StockDataset(stock_data_path)
train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)

# Create an instance of your neural network and choose an optimizer
net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Train your neural network
for epoch in range(10):  # Replace 10 with the number of epochs you want to train for
    for batch in tqdm(train_dataloader):
        inputs, labels = batch["data"], batch["label"]
        # optimizer.zero_grad()
        # outputs = net(inputs)
        # loss = nn.functional.cross_entropy(outputs, labels.long())
        # loss.backward()
        # optimizer.step()

