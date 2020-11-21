import numpy as np
import sklearn
import os
from sklearn.datasets import load_iris, load_wine

iris = load_iris()
# with open("./data/wine.data", 'r') as f:
#     # wine = f.readlines()
#     x = []
#     y = []
#     for line in f.readlines():
#         strs = line.strip().split(",")
#         # print(strs)
#         _x = np.float64(strs[0])
#         _y = np.float64(strs[1])
#         print(_x, _y)
#         x.append(_x)
#         y.append(_y)
#     print(x)
#     print(y)
wine_file = open("data/wine.data")
wine = wine_file.readlines()
# print(wine)
x = []
y = []
for L in wine:
    str = L.strip().split(",")
    print(str)
    _x = np.float64(str[0])
    _y = np.float64(str[1])
    print(_x)
    print(_y)
    x.append(_x)
    y.append(_y)
x = np.stack(x)
y = np.stack(y)
# print(x)
# print(y)

house = np.loadtxt("./data/wine.data", delimiter=",")
print(house)