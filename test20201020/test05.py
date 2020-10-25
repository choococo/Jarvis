import torch
import numpy as np

# 最小二乘法
x = torch.tensor([[2.], [4.]])
# x = np.array([[2], [4]])
w = 4
y = w * x

w = x.T@y@((x.T@x).inverse())       # inverse() 求矩阵的逆
# w = x.T@y@(np.linalg.inv(x.T@x))  # 同上
print(w)
