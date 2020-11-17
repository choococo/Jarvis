import random
import matplotlib.pyplot as plt
import math
import numpy as np

_x = [i / 100 for i in range(100)]  # _x是以0为起点，0.01为差的100个等差数组成的列表
_y = [3 * j ** 2 + 2 * random.random() for j in _x]  # _y是以_x中的数经一定的随机处理生成数的列表
'''
w = random.random()#生成初始系数w
b = random.random()#生成初始系数b
'''
w = 0.5
b = 0.5
plt.ion()


def sigmod(x):  # 定义sigmod函数
    s = 1 / (1 + np.exp(-x))
    return s


def calculate_loss(w, b, _x, _y):  # 将当前系数下的平均损失计算出来
    total_loss = 0
    for x, y in zip(_x, _y):
        total_loss += math.pow(y - w * x ** 2 - b, 2)
        loss = math.sqrt(total_loss / 100)
    return loss


def calculate_dw(w, b, _z, _y, _x):  # 遍历所有的点，计算当前系数时w的平均微分
    dw = 0
    for i in range(100):
        dw = dw - sigmod(w * _x[i] ** 2 + b) * (1 - sigmod(w * _x[i] ** 2 + b)) * (_z[i] - _y[i]) * _x[
            i] ** 2  # 复合函数对w求偏导
    return dw / 100


def calculate_db(w, b, _x, _z, _y):  # 遍历所有的点，计算当前系数时b的平均微分
    db = 0
    for i in range(100):
        db = db - sigmod(w * _x[i] ** 2 + b) * (1 - sigmod(w * _x[i] ** 2 + b)) * (_z[i] - _y[i])  # 复合函数对b求偏导
    return db / 100


plt.ion()
number = 0
loss_list = []  # 记录损失值的列表
for i in range(100):
    # z = w*_x[number]**2+b
    _z = [w * j ** 2 + b for j in _x]  # _z中存储我们计算得到的拟合曲线函数值
    dw = calculate_dw(w, b, _z, _y, _x)
    db = calculate_db(w, b, _x, _z, _y)
    loss = calculate_loss(w, b, _x, _y)

    print("这是第{}次运算,loss = {}".format(number + 1, loss))
    number += 1
    plt.clf()
    plt.plot(_x, _y, '.')  # 画出最开始生成的_x,_y对应的散点图，这是我们需要去拟合的
    plt.plot(_x, _z, "r")  # 画出计算出的函数图像，与散点图进行对比
    w = w + 5 * dw
    b = b + 0.5 * db
    plt.pause(0.1)
    loss_list.append(loss)
plt.ioff()
plt.close()
plt.plot(_x, loss_list, "g")  # 画出损失值的变化图像
plt.show()