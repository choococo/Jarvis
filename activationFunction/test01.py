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


def sigmoid(x):                         # sigmoid 拟合的比较慢
    return 1 / (1 + math.exp(-x))


def simgmoid_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (sigmoid(w * x + b) - sigmoid(y))**2
    dw = 1.0*x*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
    db = 1.0*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
    return loss, dw, db


def mish(x):                            # mish 效果是比较好的，与不加激活的效果差不多
    return x * math.tanh(math.log(1 + math.exp(x)))


def mish_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (mish(w * x + b) - mish(y)) ** 2
    dw = 0.5*(-y*math.tanh(math.log(math.exp(y) + 1)) + (b + w*x)*math.tanh(math.log(math.exp(b + w*x) + 1)))*(2*x*(1 - math.tanh(math.log(math.exp(b + w*x) + 1))**2)*(b + w*x)*math.exp(b + w*x)/(math.exp(b + w*x) + 1) + 2*x*math.tanh(math.log(math.exp(b + w*x) + 1)))
    db = 0.5*(-y*math.tanh(math.log(math.exp(y) + 1)) + (b + w*x)*math.tanh(math.log(math.exp(b + w*x) + 1)))*(2*(1 - math.tanh(math.log(math.exp(b + w*x) + 1))**2)*(b + w*x)*math.exp(b + w*x)/(math.exp(b + w*x) + 1) + 2*math.tanh(math.log(math.exp(b + w*x) + 1)))
    return loss, dw, db


def tanh(x):                            # tanh 拟合的比较慢，效果不好
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


def relu(x):                        # relu
    return max(0, x)


def relu_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (relu(w * x + b) - relu(y)) ** 2
    dw = 1.0 * x * (b + w * x - y)
    db = 1.0 * b + 1.0 * w * x - 1.0 * y
    return loss, dw, db

def leaky_relu(x, alpha=0.01):      # leaky_relu
    return max(alpha*x, x)

def leaky_relu_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (leaky_relu(w * x + b) - leaky_relu(y)) ** 2
    dw = 1.0 * x * (b + w * x - y)
    db = 1.0 * b + 1.0 * w * x - 1.0 * y
    return loss, dw, db

def elu(x, alpha=0.01):             # elu
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

def selu(x, alpha=0.01, lambda_l=0.8):         # selu 给elu乘上系数lambda
    if x > 0:
        return lambda_l * x
    else:
        return lambda_l * alpha * (math.exp(x) - 1)

def selu_loss_dw_db(x, y, w, b):
    if x > 0:
        loss = 1 / 2 * (selu(w * x + b) - selu(y)) ** 2
        dw = 0.64 * x * (b + w * x - y)
        db = 0.64 * b + 0.64 * w * x - 0.64 * y
    else:
        loss = 1 / 2 * (selu(w * x + b) - selu(y)) ** 2
        dw = 6.4e-5 * x * (-math.exp(y) + math.exp(b + w * x)) * math.exp(b + w * x)
        db = 6.4e-5 * (-math.exp(y) + math.exp(b + w * x)) * math.exp(b + w * x)

    return loss, dw, db


def gelu(x):        # Gaussian Error Linerar Units 在bert中应用的比较多——高斯误差线性单元
    return x * 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def gelu_gpt2(x):
    return 0.5 * x * (1 + math.tanh(math.sqrt(2/ math.pi)* (x + 0.044715*math.pow(x, 3))))

def gelu_gpt2_loss_dw_db(x, y, w, b):
    pass


def gelu_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (leaky_relu(w * x + b) - leaky_relu(y)) ** 2
    dw = 0.5 * (-0.5 * y * (math.erf(0.707106781186547 * y) + 1.0) + (0.5 * b + 0.5 * w * x) * (
                math.erf(0.707106781186547 * b + 0.707106781186547 * w * x) + 1.0)) * (
                2.82842712474619 * x * (0.5 * b + 0.5 * w * x) * math.exp(-0.5 * (b + w * x) ** 2) / math.sqrt(math.pi) + x * (
                    math.erf(0.707106781186547 * b + 0.707106781186547 * w * x) + 1.0))
    db = 0.5 * (-0.5 * y * (math.erf(0.707106781186547 * y) + 1.0) + (0.5 * b + 0.5 * w * x) * (
                math.erf(0.707106781186547 * b + 0.707106781186547 * w * x) + 1.0)) * (
                2.82842712474619 * (0.5 * b + 0.5 * w * x) * math.exp(-0.5 * (b + w * x) ** 2) / math.sqrt(math.pi) + math.erf(
            0.707106781186547 * b + 0.707106781186547 * w * x) + 1.0)
    return loss, dw, db


def swish(x, beta=0.1): # beta=1.0/10.0  swish
    return x * sigmoid(beta * x)

def swish_loss_dw_db(x, y, w, b):
    loss = 1 / 2 * (swish(w * x + b) - swish(y)) ** 2
    dw = 0.5 * (-y / (1 + math.exp(-0.1 * y)) + (b + w * x) / (math.exp(-0.1 * b - 0.1 * w * x) + 1)) * (
                0.2 * x * (b + w * x) * math.exp(-0.1 * b - 0.1 * w * x) / (math.exp(-0.1 * b - 0.1 * w * x) + 1) ** 2 + 2 * x / (
                    math.exp(-0.1 * b - 0.1 * w * x) + 1))
    db = 0.5 * (-y / (1 + math.exp(-0.1 * y)) + (b + w * x) / (math.exp(-0.1 * b - 0.1 * w * x) + 1)) * (
                0.2 * (b + w * x) * math.exp(-0.1 * b - 0.1 * w * x) / (math.exp(-0.1 * b - 0.1 * w * x) + 1) ** 2 + 2 / (
                    math.exp(-0.1 * b - 0.1 * w * x) + 1))
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
            loss, dw, db = swish_loss_dw_db(x, y, w, b)
            w = w - 2.3 * dw
            b = b - 0.4 * db

            print("w:{}, b:{}, loss: {}".format(w, b, loss))
            plt.clf()
            plt.plot(_x, _y, 'r')
            v = [w * i + b for i in _x ]
            plt.plot(_x, v, "b")
            plt.pause(0.0001)
        plt.ioff()


