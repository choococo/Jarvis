import torch
import torch.nn.modules as nn
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import numpy as np
import matplotlib.pyplot as plt


train_dataset = datasets.FashionMNIST(root='./data2', train=True, transform=transforms.ToTensor(), download=True)

test_dataset = datasets.FashionMNIST('./data2', train=False, transform=transforms.ToTensor(), download=False)

# print(len(train_dataset))
# print(len(test_dataset))



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
        x = x.reshape(-1, 784)
        return self.fc_layer(x)


if __name__ == '__main__':
    net = MLPNet().cuda()
    train_loader = DataLoader(train_dataset, batch_size=100, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=100, shuffle=True)

    optimizer = torch.optim.Adam(net.parameters())
    loss_func = nn.CrossEntropyLoss()
    loss_list = []
    count = []
    j = 0
    plt.ion()
    for epoch in range(1):
        for i, (xs, ys) in enumerate(train_loader):
            print(xs)
            exit(0)
            xs, ys = xs.cuda(), ys.long().cuda()
            output = net(xs)

            loss = loss_func(output, ys)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # print(output.shape)
            idx = torch.argmax(output, dim=1).cpu().detach().numpy()

            accuracy = np.mean(np.sum(idx == ys.cpu().detach().numpy()))
            # print(accuracy)
            # print(loss.item())
            loss_list.append(loss.cpu().item())
            count.append(j)
            print(j, loss_list)
            j += 1

        # for test_xs, test_ys in test_loader:
        #     pass
            plt.plot(count, loss_list, ".")
            plt.pause(0.001)
    # plt.show()
    # plt.savefig("4.jpg")
    plt.ioff()
