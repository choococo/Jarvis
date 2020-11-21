from sklearn import preprocessing
import numpy as np

"""
4. MaxAbsScaler 最大绝对值，它不移动数据的中心的数据
这样不会破坏任何稀疏性
x = max(abs(x))
"""

x = np.array([[1., -1., -2.],
              [2., 0., 0.],
              [0., 1., -1.]])
sclaer = preprocessing.MaxAbsScaler()
x_scale = sclaer.fit_transform(x)
print(x_scale)

# 与上面的效果是一眼的
out = x / np.max(np.abs(x))
print(out)

