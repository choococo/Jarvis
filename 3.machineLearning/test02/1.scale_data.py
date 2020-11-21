from sklearn import preprocessing
import numpy as np

# 数据处理
'1. preprocessing.scale(x) 可以直接将给定的数据进行标准化'
# 将每一列的特征标准化，每一列表示同一特征，类似于图片每个通道上的对应点
x = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
x_scled = preprocessing.scale(x)
print(x_scled)
"""
[[ 0.         -1.22474487  1.33630621]
 [ 1.22474487  0.         -0.26726124]
 [-1.22474487  1.22474487 -1.06904497]]
"""

'2. 处理后数据的均值和方差'
print(x_scled.mean(axis=0)) # 消除第一个维度，保留第二个维度
"""
[0. 0. 0.]
"""
print(x_scled.std(axis=0))
"""
[0. 0. 0.]
"""

'2.preprocessing.StandardScaler() 保存训练集中的参数(均值和方差), 直接使用对象标准化转换测试集的数据'
scaler = preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True).fit(x)
print(scaler)
"""
StandardScaler(copy=True, with_mean=True, with_std=True)
"""
print(scaler.transform([[-1., 1., 0.]]))
"""
[[-2.44948974  1.22474487 -0.26726124]]
"""
print(scaler.mean_)
print(scaler.var_)
print(np.array([1., 2, 0]).mean())
print(np.array([1., 2, 0]).var())
print(np.array([-1., 0, 1]).mean())
print(np.array([-1., 0, 1]).var())
print(np.array([2., 0, -1]).mean())
print(np.array([2., 0, -1]).var())
