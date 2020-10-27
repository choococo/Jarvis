import torch
import torch.nn.modules as nn
from torch.utils.data import DataLoader
from torchvision import transforms, datasets


class RNNNet(nn.Module):

    def __init__(self):
        super(RNNNet, self).__init__()
        self.rnn_layer = nn.RNN(input_size=28, hidden_size=28, num_layers=1, batch_first=True)
        self.fc_layer = nn.Linear(28, 10)

    def forward(self, x):       # [N 1 28 28]
        x = x.reshape(x.size(0), -1, 28)    # [N 28 28]
        x = self.rnn_layer(x)
        print(x)
        x = x[:,-1,:]
        return x


if __name__ == '__main__':
    x = torch.randn(2, 1, 28, 28)
    net = RNNNet()
    y = net(x)
    print(y)
    # train_dataset = datasets.MNIST('./data', train=True, transform=transforms.ToTensor(), download=True)
    # train_loader = DataLoader(dataset=train_dataset, batch_size=1000, shuffle=True)
    #
    # test_dataset = datasets.MNIST('./data', train=False, transform=transforms.ToTensor(), download=False)
    # test_loader = DataLoader(dataset=test_dataset, batch_size=1000, shuffle=True)
    #
    # net = RNNNet().cuda()
    # optimizer = torch.optim.Adam(net.parameters())
    # loss_fn = nn.CrossEntropyLoss()
    #
    # for epoch in range(1000):
    #     for xs, ys in train_loader:
    #         xs, ys = xs.cuda(), ys.cuda()
    #         output = net(xs)
    #         loss = loss_fn(output, ys)
    #
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()
    #
    #     for test_xs, test_ys in test_loader:
    #         test_xs, test_ys = test_xs.cuda(), test_ys.cuda()
    #         test_out = net(test_xs)
    #
    #         test_idx = torch.argmax(torch.log_softmax(test_out, dim=1), dim=1)
    #         accuracy = torch.mean(torch.sum(torch.eq(test_idx, test_ys)))
    #         print(accuracy)
    #         break
