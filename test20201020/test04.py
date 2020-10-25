import torch
import numpy as np


# 向量的加减法
a = np.array([1, 2])            # array
b = np.array([3, 4])            # array
print(a + b)                    # +
print(a - b)                    # -
print(a * b)                    # 数乘
print(a / b)                    # /
print(a.dot(b))                 # 点乘,是一个标量
print(np.dot(a, b))             # 同上
print(a@b)                      # 向量的内积,一个标量


# 矩阵的计算
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.dot(b))                 # 是矩阵，则为矩阵乘法
print(np.dot(a, b))
print(a@b)
print(np.linalg.det(a))         # 求行列式的，这里精度有点问题
print(np.linalg.inv(a))         # 求矩阵的逆
