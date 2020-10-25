import numpy as np
import torch

a = np.array([1., 2.], dtype=np.float32)        # 转成float32
a = a.astype(np.float64)                        # 转成float64

a = torch.tensor([1., 2.], dtype=torch.float32) # 转成float32
print(a.shape)

# torch与numpy之间的转换
