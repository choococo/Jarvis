from sklearn import preprocessing
import numpy as np

'3. preprocessing.MinMaxScaler(x), 将属性缩放到一个指定的最大和最小值之间(通常是0-1)之间'

"""
使用这种方法的目的包括：
(1) 对于方差非常小的属性可以增强其稳定性
(2) 维持系数矩阵中为0的条目
x_std = (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))
x_scaled = x_std / (max - min) + min
"""

x_train = np.array([[1., -1., 2.],
                    [2., 0., 0.],
                    [0., 1., -1.]])

min_max_scaler = preprocessing.MinMaxScaler()
x_train_minmax = min_max_scaler.fit_transform(x_train)

print(x_train_minmax)
"""
[[0.5        0.         1.        ]
 [1.         0.5        0.33333333]
 [0.         1.         0.        ]]
"""
# 将相同的缩放应用到测试集数据中
x_test = np.array([[-3., -1., 4.]])
x_test_minmax = min_max_scaler.transform(x_test) # [注意]这里是transform不是fit_transform
print(x_test_minmax)
"""
[[-1.5         0.          1.66666667]]
"""

# 缩放因子等属性
print(min_max_scaler.scale_)
"""
[0.5        0.5        0.33333333]
"""
print(min_max_scaler.min_)
"""
[0.         0.5        0.33333333]
"""
print(min_max_scaler.data_max_)
"""
[2. 1. 2.]
"""
print(min_max_scaler.data_min_)
"""
[ 0. -1. -1.]
"""