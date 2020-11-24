import torch
import torch.nn as nn
from torch.utils.data import DataLoader


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

    def forward(self, x):
        return x


