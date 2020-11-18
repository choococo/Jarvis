import numpy as np
import matplotlib.pyplot as plt


def Normalization0(x):
    """
    归一化(0~1) x = (x - x_min) / (x_max - x_min)
    :param x: 是一组数据
    :return: 归一化后的一组数据
    """
    return [(float(i) - min(x)) / float(max(x) - min(x)) for i in x]


def Normalization1(x):
    """
    最值归一化 (-1, 1)  x = (x - x_min) / (x_max -x_min)
    :param x:
    :return:
    """
    return [float(i) / np.max(np.abs(x)) for i in x]  # #[-1,1)||(-1,1]


def Normalization2(x):
    """
    均值归一化(-1~1) x = (x - x_mean) / (x_max - x_min)
    :param x:
    :return:
    """
    return [(float(i) - np.mean(x)) / (max(x) - min(x)) for i in x]


def Normalization3(x):
    """
    标准化（μ=0，σ=1） x =(x−μ)/σ
    :param x:
    :return:
    """
    x_mean = np.mean(x)  # 均值
    s2 = np.mean([(i - x_mean) ** 2 for i in x])  # 方差
    std = np.sqrt(s2)  # 标准差

    return [(i - x_mean) / (s2 + 1e-10) for i in x]  # 减均值，除以方差


def Normalization4(x):
    """
    归一化：只有全是非负数的情况下使用，[-1, 1] x = ((x - x_max) - 0.5) / 0.5
    :param x:
    :return:
    """
    x_mean = [((float(i)) / max(x) - 0.5) / 0.5 for i in x]
    return x_mean


s = [21312313, 0, 76, 223, 12, -1341656]
l = [3, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11,
     12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]
cs = []
for i in l:
    c = l.count(i)
    cs.append(c)
# print(cs)

n0 = Normalization0(l)
n1 = Normalization1(l)
n2 = Normalization2(l)
n3 = Normalization3(l)
n4 = Normalization4(l)

# print(n0)
# print(n1)
print(n2)
# print(n3)
# plt.plot(l,cs)
# plt.plot(n0, cs, c="r")
# plt.plot(n1, cs, c="blue")
# # plt.plot(n2,cs,c="g")
# plt.plot(n3, cs, c="y")
# plt.plot(n4, cs, c="k")
#
# plt.show()
