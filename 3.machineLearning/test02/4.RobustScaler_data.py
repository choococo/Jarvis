from sklearn import preprocessing
import numpy as np

"""
5. RobustScaler(), robust_scaler()
机器学习估计，通常是通过去除平均值来实现的
然后缩放到单位方差。然而，异常值往往会影响样本均值/方差。在这种情况下，中位数和四分位范围
(RobustScaler)通常会得到更好的结果。该缩放器删除中位数，并根据百分位数范围(默认值为IQR：四分位间距)缩放数据
IQR是第一个四分位数(25%)和第三个四分位数(75%)之间的范围
"""
x = np.array([[1., -1., 2.],
              [2., 1000., 0.],
              [0., 1., -1.]])

scaler = preprocessing.RobustScaler()
x_scaler = preprocessing.robust_scale(x)
print(x_scaler)
print(x_scaler.mean(0), x_scaler.std(0))


