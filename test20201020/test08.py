import math
import random
import torch
import matplotlib.pyplot as plt

"""
各个激活函数拟合曲线的能力
"""


def y_eq_x(x):                          # 不激活 y=x
    return x


def y_eq_x_loss_dw_b(x, y, w, b):
    loss = 1 / 2 * (w * x + b - y) ** 2
    dw = 1.0 * x * (b + w * x - y)
    db = 1.0 * b + 1.0 * w * x - 1.0 * y
    return loss, dw, db


def sigmoid(x):                         # 拟合的比较慢
    return 1 / (1 + math.exp(-x))


def simgmoid_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (sigmoid(w * x + b) - sigmoid(y))**2
    dw = 1.0*x*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
    db = 1.0*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
    return loss, dw, db


def mish(x):                            # 效果是比较好的，与不加激活的效果差不多
    return x * math.tanh(math.log(1 + math.exp(x)))


def mish_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (mish(w * x + b) - mish(y)) ** 2
    dw = 0.5*(-y*math.tanh(math.log(math.exp(y) + 1)) + (b + w*x)*math.tanh(math.log(math.exp(b + w*x) + 1)))*(2*x*(1 - math.tanh(math.log(math.exp(b + w*x) + 1))**2)*(b + w*x)*math.exp(b + w*x)/(math.exp(b + w*x) + 1) + 2*x*math.tanh(math.log(math.exp(b + w*x) + 1)))
    db = 0.5*(-y*math.tanh(math.log(math.exp(y) + 1)) + (b + w*x)*math.tanh(math.log(math.exp(b + w*x) + 1)))*(2*(1 - math.tanh(math.log(math.exp(b + w*x) + 1))**2)*(b + w*x)*math.exp(b + w*x)/(math.exp(b + w*x) + 1) + 2*math.tanh(math.log(math.exp(b + w*x) + 1)))
    return loss, dw, db


def tanh(x):                            # 拟合的比较慢，效果不好
    return (math.exp(x)-math.exp(-x)) / (math.exp(x) + math.exp(-x))


def tanh_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (tanh(w * x + b) - tanh(y))**2
    dw = 0.5 * (-(math.exp(y) - math.exp(-y)) / (math.exp(y) + math.exp(-y)) + (
                -math.exp(-b - w * x) + math.exp(b + w * x)) / (math.exp(-b - w * x) + math.exp(b + w * x))) * (
                     2 * (x * math.exp(-b - w * x) - x * math.exp(b + w * x)) * (
                         -math.exp(-b - w * x) + math.exp(b + w * x)) / (
                                 math.exp(-b - w * x) + math.exp(b + w * x)) ** 2 + 2 * (
                                 x * math.exp(-b - w * x) + x * math.exp(b + w * x)) / (
                                 math.exp(-b - w * x) + math.exp(b + w * x)))
    db = 0.5 * (-(math.exp(y) - math.exp(-y)) / (math.exp(y) + math.exp(-y)) + (
                -math.exp(-b - w * x) + math.exp(b + w * x)) / (math.exp(-b - w * x) + math.exp(b + w * x))) * (
                     2 * (-math.exp(-b - w * x) + math.exp(b + w * x)) * (
                         math.exp(-b - w * x) - math.exp(b + w * x)) / (
                                 math.exp(-b - w * x) + math.exp(b + w * x)) ** 2 + 2)
    return loss, dw, db


def relu(x):
    return max(0, x)


def relu_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (relu(w * x + b) - relu(y)) ** 2
    dw = 1.0 * x * (b + w * x - y)
    db = 1.0 * b + 1.0 * w * x - 1.0 * y
    return loss, dw, db

def leaky_relu(x, alpha=0.01):
    return max(alpha*x, x)

def leaky_relu_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (leaky_relu(w * x + b) - leaky_relu(y)) ** 2
    dw = 1.0 * x * (b + w * x - y)
    db = 1.0 * b + 1.0 * w * x - 1.0 * y
    return loss, dw, db

def elu(x, alpha=0.01):
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)

def elu_loss_dw_db(x, y, w, b):
    if x > 0:
        loss = 1 / 2 * (elu(w * x + b) - elu(y)) ** 2
        dw = 1.0 * x * (b + w * x - y)
        db = 1.0 * b + 1.0 * w * x - 1.0 * y
    else:
        loss = 1 / 2 * (elu(w * x + b) - elu(y)) ** 2
        dw = 0.0001 * x * (-math.exp(y) + math.exp(b + w * x)) * math.exp(b + w * x)
        db = 0.0001 * (-math.exp(y) + math.exp(b + w * x)) * math.exp(b + w * x)
    return loss, dw, db

if __name__ == '__main__':
    _x = [i / 100 for i in range(100)]
    _y = [4 * j + 3 for j in _x]
    print(_x)
    print(_y)

    w = random.random()
    b = random.random()
    plt.ion()
    for epoch in range(100000):
        for x, y in zip(_x, _y):
            # y = mish(y)
            # z = mish(w * x + b)

            # loss = 1 / 2 * (mish(w * x + b) - mish(y))**2
            # loss = 1 / 2 * (tanh(w * x + b) - tanh(y))**2

            # dw = 1.0*x*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
            # db = 1.0*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
            # dw = 0.5*(-y*math.tanh(math.log(math.exp(y) + 1)) + (b + w*x)*math.tanh(math.log(math.exp(b + w*x) + 1)))*(2*x*(1 - math.tanh(math.log(math.exp(b + w*x) + 1))**2)*(b + w*x)*math.exp(b + w*x)/(math.exp(b + w*x) + 1) + 2*x*math.tanh(math.log(math.exp(b + w*x) + 1)))
            # db = 0.5*(-y*math.tanh(math.log(math.exp(y) + 1)) + (b + w*x)*math.tanh(math.log(math.exp(b + w*x) + 1)))*(2*(1 - math.tanh(math.log(math.exp(b + w*x) + 1))**2)*(b + w*x)*math.exp(b + w*x)/(math.exp(b + w*x) + 1) + 2*math.tanh(math.log(math.exp(b + w*x) + 1)))
            # dw = 0.5*(-(math.exp(y) - math.exp(-y))/(math.exp(y) + math.exp(-y)) + (-math.exp(-b - w*x) + math.exp(b + w*x))/(math.exp(-b - w*x) + math.exp(b + w*x)))*(2*(x*math.exp(-b - w*x) - x*math.exp(b + w*x))*(-math.exp(-b - w*x) + math.exp(b + w*x))/(math.exp(-b - w*x) + math.exp(b + w*x))**2 + 2*(x*math.exp(-b - w*x) + x*math.exp(b + w*x))/(math.exp(-b - w*x) + math.exp(b + w*x)))
            # db = 0.5*(-(math.exp(y) - math.exp(-y))/(math.exp(y) + math.exp(-y)) + (-math.exp(-b - w*x) + math.exp(b + w*x))/(math.exp(-b - w*x) + math.exp(b + w*x)))*(2*(-math.exp(-b - w*x) + math.exp(b + w*x))*(math.exp(-b - w*x) - math.exp(b + w*x))/(math.exp(-b - w*x) + math.exp(b + w*x))**2 + 2)
            loss, dw, db = elu_loss_dw_db(x, y, w, b)
            w = w - 2.3 * dw
            b = b - 0.4 * db

            print("w:{}, b:{}, loss: {}".format(w, b, loss))
            plt.clf()
            plt.plot(_x, _y, 'r')
            v = [w * i + b for i in _x ]
            plt.plot(_x, v, "b")
            plt.pause(0.0001)
        plt.ioff()


