import torch
import torch.nn as nn

loss_alpha=0.001
def MSE_save(outputs, labels):
    labels_len = labels.shape[1]
    outputs_len = outputs.shape[1]

    labels_low = labels[:, :labels_len // 2]
    labels_high = labels[:, labels_len // 2:]

    out_low = outputs[:, :outputs_len // 2]
    out_high = outputs[:, outputs_len // 2:]

    low_loss = torch.clamp(out_low-labels_low, min=0).sum()
    high_loss = torch.clamp(out_high - labels_high, min=0).sum()

    loss = nn.functional.mse_loss(outputs, labels) + (low_loss + high_loss)*loss_alpha

    return loss