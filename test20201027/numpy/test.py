import numpy as np

a = np.arange(12).reshape(2, 2, 3)
print(a)
print(a.ndim)                       # 查看a有几个轴
print(a.size)                       # array中有多少个
print(a.data)                       # 查看ndarray的地址
