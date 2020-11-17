import math
import numpy as np
import matplotlib.pyplot as plt


def mish(x):
    return x * math.tanh(math.log(1 + math.exp(x)))

def ln_e(x):
    return math.log(1 + math.exp(x))

x = np.linspace(-10, 10, 100)
y = [mish(i) for i in x]
z = [ln_e(i) for i in x]

plt.plot(x, y)

plt.plot(x, z)
plt.legend(['Mish', "ln_e"])

plt.grid()
plt.show()