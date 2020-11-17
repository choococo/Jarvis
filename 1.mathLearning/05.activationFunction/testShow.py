import math
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):                         # 拟合的比较慢
    return 1 / (1 + math.exp(-x))

def mish(x):
    return x * math.tanh(math.log(1 + math.exp(x)))

def ln_e(x):
    return math.log(1 + math.exp(x))

def tanh(x):                            # 拟合的比较慢，效果不好
    return (math.exp(x)-math.exp(-x)) / (math.exp(x) + math.exp(-x))

def relu(x):
    return max(0, x)

def leaky_relu(x, alpha=0.01):
    return max(alpha*x, x)

def elu(x, alpha=0.01):
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)

def selu(x, alpha=0.01, lambda_l=0.8):         # 给elu乘上系数lambda
    if x > 0:
        return lambda_l * x
    else:
        return lambda_l * alpha * (math.exp(x) - 1)

def swish(x, beta=0.1): # beta=1.0/10.0
    return x * sigmoid(beta * x)

def gelu(x):
    return x * 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def gelu_gpt2(x):
    return 0.5 * x * (1 + math.tanh(math.sqrt(2/ math.pi)* (x + 0.044715*math.pow(x, 3))))

x = np.linspace(-10, 10, 100)
y = [mish(i) for i in x]
z1 = [ln_e(i) for i in x]
z2 = [tanh(i) for i in x]
z3 = [relu(i) for i in x]
z4 = [leaky_relu(i) for i in x]
z5 = [elu(i) for i in x]
z6 = [selu(i) for i in x]
z7 = [swish(i) for i in x]
z8 = [gelu(i) for i in x]
z9 = [gelu_gpt2(i) for i in x]

plt.plot(x, y)

plt.plot(x, z1)
plt.plot(x, z2)
plt.plot(x, z3)
plt.plot(x, z4)
plt.plot(x, z5)
plt.plot(x, z6)
plt.plot(x, z7)
plt.plot(x, z8)
plt.plot(x, z9)
plt.legend(['Mish', "ln_e", "tanh", "relu", "leakyRelu", "elu", "selu", "swish", "gelu","gelu_gpt2"])
# plt.legend([ "gelu","gelu_gpt2"])
# plt.legend([ "gelu"])

plt.grid()
plt.savefig("./pic/01.png")
plt.show()
