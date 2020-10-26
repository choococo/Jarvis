from sympy import *


def sigmoid(x):                         # 拟合的比较慢
    return 1 / (1 + exp(-x))
def mish(x):
    return x * tanh(log(1 + exp(x)))

def tanh(x):
    return (exp(x)-exp(-x)) / (exp(x) + exp(-x))

def elu(x, alpha=0.01):
    return alpha * (exp(x) - 1)

def selu(x, alpha=0.01, lambda_l=0.8):         # 给elu乘上系数lambda
    # if x > 0:
    #     return lambda_l * x
    # else:
        return lambda_l * alpha * (exp(x) - 1)

def gelu(x):
    return x * 0.5 * (1.0 + erf(x / sqrt(2.0)))

def gelu_gpt2(x):
    return 0.5 * x * (1 + tanh(sqrt(2/ pi)* (x + 0.044715*pow(x, 3))))

def swish(x, beta=0.1): # beta=1.0/10.0
    return x * sigmoid(beta * x)

x, y, w, b = symbols("x y w b")
y = gelu_gpt2(y)
z = gelu_gpt2(w * x + b)
loss = 1 / 2 * (z - y) **2
print(diff(loss, w, 1))
print(diff(loss, b, 1))