import numpy as np

a = np.random.uniform(0, 100, 20)
# print(a)
# print(a.shape)
a = a[a.argsort(axis=0)]
print(a)