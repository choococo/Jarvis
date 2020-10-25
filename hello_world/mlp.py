import torch
import torch.nn.modules as nn
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

train_dataset = datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)

test_dataset = datasets.MNIST('./data', train=False, transform=transforms.ToTensor(), download=False)

print(len(train_dataset))
print(len(test_dataset))



class MLPNet(nn.Module):

    def __init__(self):
        super(MLPNet, self).__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(784, 512, bias=True),
            nn.BatchNorm1d(512),
            nn.ReLU(inplace=True),
            nn.Linear(512, 256, bias=True),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 128, bias=True),
            nn.Linear(128, 10),
        )


    def forward(self, x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = MLPNet().cuda()
    train_loader = DataLoader(train_dataset, batch_size=100, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=100, shuffle=True)

    optimizer = torch.optim.Adam(net.parameters())
    loss_func = nn.CrossEntropyLoss()

    for epoch in range(1000):
        for i, (xs, ys) in enumerate(train_loader):
            xs, ys = xs.cuda(), ys.cuda()
            output = net(xs)

            loss = loss_func(output, ys)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        for test_xs, test_ys in test_loader:
            pass

