from sklearn import preprocessing
import numpy as np

"""
6. Normalizer()
norm：可以为l1、l2或max，默认为l2
若为l1时：样本各个特征值除以各个特征值的绝对值之和
若为l2时：样本各个特征值除以各个特征值的平方之和
若为max时：样本各个特征值除以样本中特征值最大的值
"""
x = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

scaler = preprocessing.Normalizer(norm="max")
x_scaler = scaler.fit_transform(x)
print(x_scaler)
print(x_scaler.mean(0), x_scaler.std(0))

# 数据二值化
scaler = preprocessing.Binarizer(threshold=0)
x_scaler = scaler.fit_transform(x)
print(x_scaler)