import torch.optim as optim
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch
from tqdm import tqdm
from src.py_libs.ML.model.model import Net
from src.py_libs.ML.dataset.dataset import StockDataset
from src.py_libs.ML.eval.eval_utils import get_profit
from src.py_libs.ML.utils.utils import undo_normaliztion
import matplotlib.pyplot as plt

# Create a DataLoader object to manage your data
stock_data_path = "./stock_raw_data"

dataset = StockDataset(stock_data_path)
train_size = int(0.8 * len(dataset))  # 80% for training
test_size = len(dataset) - train_size  # Remaining 20% for testing
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=True)

# Create an instance of your neural network and choose an optimizer
net = Net(in_dim=5 * 3000, out_dim=1000)
optimizer = optim.Adam(net.parameters(), lr=1e-4)

losses = []
eval_losses = []
profits=[]
# Train your neural network
for epoch in range(10):  # Replace 10 with the number of epochs you want to train for
    net.train()
    for batch in tqdm(train_dataloader):
        inputs, labels = torch.tensor(batch["data"]).to(torch.float32), torch.tensor(batch["label"]).to(torch.float32)
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = nn.functional.mse_loss(outputs, labels)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())

    net.eval()
    for batch in tqdm(test_dataloader):
        inputs, labels = torch.tensor(batch["data"]).to(torch.float32), torch.tensor(batch["label"]).to(torch.float32)
        outputs = net(inputs)
        loss = nn.functional.mse_loss(outputs, labels)
        real_outputs, real_labels = undo_normaliztion(outputs, labels, [dataset.means, dataset.stds])
        profit = get_profit(real_outputs, real_labels)
        eval_losses.append(loss.item())
        profits.append(profit)

plt.plot(losses)
plt.title('Training Loss')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

plt.plot(eval_losses)
plt.title('Test Loss')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

plt.plot(profits)
plt.title('Test Profit')
plt.xlabel('Iteration')
plt.ylabel('Profit')
plt.show()
