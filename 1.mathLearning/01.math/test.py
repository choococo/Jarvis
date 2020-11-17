import math
import random
import torch
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def mish(x):
    return x * math.tanh(math.log(1 + math.exp(x)))


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
            y = sigmoid(y)
            z = sigmoid(w * x + b)

            loss = 1 / 2 * (z - y)**2

            # dw = 1.0*x*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
            # db = 1.0*(1/(math.exp(-b - w*x) + 1) - 1/(1 + math.exp(-y)))*math.exp(-b - w*x)/(math.exp(-b - w*x) + 1)**2
            dw = (z-y)*z*(1-z)*x
            db = (z-y)*z*(1-z)
            w = w - 2.3 * dw
            b = b - 0.4 * db

            print("w:{}, b:{}, loss: {}".format(w, b, loss))
            plt.clf()
            plt.plot(_x, _y, 'r')
            v = [w * i + b for i in _x ]
            plt.plot(_x, v, "b")
            plt.pause(0.0001)
        plt.ioff()


