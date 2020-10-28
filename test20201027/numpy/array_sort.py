import numpy as np

a = np.array([8, 2, 4, 5, 1, 6])
print(a)

b = np.sort(a)                          # 从小到大排序
print(b)

c = -np.sort(-a)                        # 先把a转换成负数进行排序，然后再转回正数
print(c)                                # 从大到小排序

d = np.sort(a)[::-1]                    # 先从小到大正着排序，然后反向索引逆序
print(d)

e = a[::-1]                             # 列表中值的逆序
print(e)

print("----------------------------------------------")

a = np.array([[2, 9, 3], [3, 8, 2]])
print(a)

b = np.sort(a)                          # 如果不指定维度，就是在最后一个维度内部进行排序
print(b)

b = np.sort(a, axis=-1)                 # 将指定的维度写了出来
print(b)

c = np.sort(a, axis=0)                  # 按照0轴进行排序，但是这个会打乱原始数组的数字位置
print(c)

d = -np.sort(-a)
print(d)

e = a[::-1]                             # 这里是对第一个维度进行逆序，把a[0]与a[1]位置转换
print(e)
