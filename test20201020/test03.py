import torch


# 矩阵形状变换
a = torch.arange(12).reshape(3, 4)       # 生成0-11的数据，并进行形状变换
b = torch.arange(12).view(3, 4)          # 同上
print(a)
# print(b)

c = a.T                                 # 矩阵的转置
d = a.t()                               # 同上
print(c)
print(d)

