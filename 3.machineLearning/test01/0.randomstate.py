import numpy as np
import time

a = np.random.RandomState(0) # 生成固定的种子，保持和上一次随机的结果是一样的
b = a.randn(10)
print(b)

for i in range(3):
    a = np.random.RandomState(0)
    print(type(a), np.shape(a))
    print(a.randn(1, 10))