import torch
import torch.nn.modules as nn
from torchvision import transforms, datasets
from torch.utils.data import DataLoader


class CNNNet(nn.Module):

    def __init__(self):
        super(CNNNet, self).__init__()
        self.cnn_layer = nn.Sequential(
            nn.Conv2d(in_channels=1)
        )
        self.fc_layer = nn.Sequential(

        )

    def forward(self, x):
        return x


if __name__ == '__main__':
    # net = CNNNet().cuda()
    train_dataset = datasets.FashionMNIST(root="./data2", train=True, transform=transforms.ToTensor(), download=True)
    test_dataset = datasets.FashionMNIST(root="./data2", train=False, transform=transforms.ToTensor(), download=False)

    # train_loader = DataLoader(dataset=train_dataset, batch_size=100, shuffle=True)
    # test_loader = DataLoader(dataset=test_dataset, batch_size=100, shuffle=True)
    #
    # optimizer = torch.optim.Adam(net.parameters())
    # loss_func = nn.CrossEntropyLoss()
    #
    # for eopc in range(1000):
    #     for i, (xs, ys) in enumerate(train_loader):
    #         xs, ys = xs.cuda(), ys.cuda()
    #         output = net(xs)
    #         loss = loss_func(output, ys)
    #
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()
    #
    #         idx = torch.argmax(output, dim=1)
    #         accuracy = torch.sum(idx == ys)




