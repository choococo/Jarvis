import numpy as np

'生成随机数的用法'
x = np.random.randint(0, 10, 100)       # 随机生成0-10之间的额100个整数
print(x)                                # 输出
print(x.sum())                          # 求和操作

x = np.random.random(100).reshape(2, 50)    # 生成0-1之间的指定个数的小树
print(x)                                    # 生成的是“连续均匀分布”

x = np.random.rand(10)                      # 随机生成0-1之间指定个数的小数，是均匀分布
print(x)

x = np.random.rand(2, 2, 2, 2)              # 也可以指定形状
print(x)

x = np.random.rand(8).reshape(2, 4)         # 指定形状
print(x)

x = np.random.randn(10, 10)                 # 随机生成指定个数的标准的正态分布
print(x)

x = np.random.randn(100).reshape(10, 10)    # 给随机生成的正态分布指定相对应的形状
print(x)

x = np.random.ranf(10)                      # 随机生成0-1指定个数的小数
print(x)

x = np.random.random_sample(10)             # 随机生成0-1之间指定个数的小树
print(x)

x = np.random.uniform(-1, 1, 100)           # 随机生成-1-1之间的指定个数的小数
print(x)

x = np.random.normal(2, 5, 100)             # 生成指定均匀方差的分布
print(x)



