from sympy import *

def mish(x):
    return x * tanh(log(1 + exp(x)))

def tanh(x):
    return (exp(x)-exp(-x)) / (exp(x) + exp(-x))

def elu(x, alpha=0.01):
    return alpha * (exp(x) - 1)

x, y, w, b = symbols("x y w b")
y = elu(y)
z = elu(w * x + b)
loss = 1 / 2 * (z - y) **2
print(diff(loss, w, 1))
print(diff(loss, b, 1))

