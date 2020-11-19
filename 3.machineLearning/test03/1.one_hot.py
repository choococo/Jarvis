import numpy as np
import torch

'numpy创建one_hot'
# # 构建单位矩阵
# num_classes = 10
# arr = [1, 3, 4, 5]
# one_hots = np.eye(num_classes)[arr]
# print(one_hots)
#
# # 返回原始数据
# data = [np.argmax(one_hot) for one_hot in one_hots]
# print(data)

from torch.nn.functional import one_hot
'pytorch创造one_hot'
num_classes = 10
y = torch.tensor([1, 3, 4, 5])
one_hot = torch.zeros(y.shape[0], num_classes).scatter_(1, y.reshape(-1, 1), 1)
# one_hot = one_hot.scatter_(1, )

print(one_hot)