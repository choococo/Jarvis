import numpy as np


'交换轴'
a = np.arange(24).reshape(2, 3, 4)
print(a)
b = a.T                                         # a的转置
print(b.shape)
# print(b)

c = np.transpose(a, [1, 2, 0])                  # 换轴
print(c.shape)
# print(c)

d = a.transpose(1, 0, 2)                        # 同上也是对a换轴
print(d)

e = np.swapaxes(a, 0, 2)                        # 0与2轴进行交换
print(e)

f = a.swapaxes(0, 2)                            # 同上
print(f)

print("--------------------------------------------------------------")
'numpy 中的函数对轴的操作'
a = np.arange(8).reshape(2, 4)
print(a)

print(np.add(a, a))

print(np.sum(a))                                # 对每个轴的对应元素求和

print(np.sum(a, axis=0))                        # 对0轴求和，就会消除0轴
print(np.sum(a, axis=1))                        # 对1轴求和，就会消除1轴


print("--------------------------------------------------------------")
a = np.array([[1, 10], [5, 9]])
b = np.array([[8, 3],[6, 7]])
print(a[0])                                     # 取第一轴的第0索引位置的值
print(a[1])                                     # 取第一轴的第1索引位置的值
print(a[0][1])                                  # 取第一轴的第0个位置索引的第一个值
print(np.max(a, 0))                             # 求在0轴的最大值，消除掉第一个轴，只剩下第二个轴
print(np.argmax(a, 0))                          # 求0轴最大值得索引 值为5 10 索引为 1 0

print(np.maximum(a, b))                          # 两个数组对应元素取最大，组成新的数组
print(np.minimum(a, b))                          # 两个数组对应元素取最小，组成新的数组

print("--------------------------------------------------------------")
m = np.array([1, 2, 5, 3, 4, 1, 2, 8 , 3, 5])
n = np.where(m > 3)                               # 得到的是True和False的值得索引
print(n)
print(m > 3)                                      # 得到对应位置是否大于3的True和False


p = np.where(m>3, 1, 0)                           # 表示合格的使用一个数代替，不合格的使用另一个数代替，用来分类
print(n)
print(p)

print(np.sum(p))
print(np.sum(p) / len(m))                          # 求精度
print(np.mean(np.sum(p)))


