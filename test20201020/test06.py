import torch


# 一些特殊的矩阵
a = torch.diag(torch.tensor([1, 2, 3]))         # 对角矩阵
print(a)

a = torch.eye(4, 4)                             # 单位矩阵，中间是形状
print(a)
print(a.shape)

a = torch.zeros(3, 3)                           # 0 矩阵
print(a)

a = torch.ones(3, 3)                            # 1 矩阵
print(a)

a = torch.tril(torch.ones(3, 3))                # 下三角矩阵
a = torch.tril(torch.arange(9).reshape(3, 3))   # 同上
print(a)