import numpy as np


'True 和 False'
a = np.array([1, 2, 4, 7, 3, 9])
print(True + False + True)
b = np.array([True, False, False, True, False, True])

b = np.array([1, 0, 0, 1, 0, 1])                                # 0, 1可以做布尔值，也可以做索引，使用的时候一定要指明
print(a[b])                                                     # 取出为True的值
print(a[b == True])
print(a[b == False])

a = np.array([1, 2, 3, 4, 5, 6])
print(a > 3)
print(a[a > 3])
print((a == 3 | (a == 5)))                                  # 或
print((a == 3) & (a == 5))                                  # 并


a = np.array([True, False, True, True, False])              # 布尔值是可以进行运算的
print(a + 1)



