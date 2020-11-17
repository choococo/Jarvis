import torch
import torch.nn.modules as nn


class LSTMNet(nn.Module):

    def __init__(self):
        super(LSTMNet, self).__init__()
        self.rnn_layer = nn.Sequential(
            nn.LSTM(input_size=784, hidden_size=784, batch_first=True, num_layers=2),
            nn.LSTMCell
        )