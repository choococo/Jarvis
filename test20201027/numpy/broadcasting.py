import numpy as np

'numpy的广播机制'


a = np.arange(12).reshape(3, 4)
b = np.arange(3).reshape(3, 1)
print(a + b)                            # 后元维度为相同或者为1可以进行广播

a = np.arange(24).reshape(2, 3, 4)
b = np.arange(3).reshape(3, 1)          # 后援维度为1可以进行广播 (3, 4)->(3, 1)
c = np.arange(4).reshape(4, 1)
print(a + b)
print(a + c)                            # (2,3,4) (4,1) 这样就不可以




