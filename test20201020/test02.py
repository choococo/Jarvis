import numpy as np
import torch


# numpy 与 torch之间的相互转换
a = np.array([1, 2])                            # array
b = torch.tensor(a, dtype=torch.float64)        # 从numpy转成torch
print(a)
print(b)
c = torch.from_numpy(a)                         # 从numpy转成torch
print(c)

d = c.numpy()                                   # 从torch转换成numpy
print(d)

