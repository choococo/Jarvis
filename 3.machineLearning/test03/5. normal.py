from sklearn import preprocessing
import warnings

import numpy as np
warnings.filterwarnings("ignore")

x = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -3.],
              [0., 1., -3.]])


# 标准化
# 将每一列特征标准化为标准正态分布，注意：标准化是针对每一列而言的
# x_scale = preprocessing.scale(x)
# print(x_scale)
# print(x_scale.mean(axis=0), x_scale.std(axis=0)) # 对列做标准化

# 标准化
scaler = preprocessing.StandardScaler() # 标准化对象，一般深度学习中很少用
x_scaler = scaler.fit_transform(x) # 拟合训练的数据
print(x_scaler)
print(x_scaler.mean(0), x_scaler.std()) # 标准化后的均值为0，标准差为1

# minmax(0-1)
scaler = preprocessing.MinMaxScaler()
x_scaler = scaler.fit_transform(x)
print(x_scaler)
print(x_scaler.mean(), x_scaler.std(0))

# maxAbs(-1,1)
scaler = preprocessing.MaxAbsScaler()
x_scaler = scaler.fit_transform(x)
print(x_scaler)
print(x_scaler.mean(), x_scaler.std(0))

#
scaler = preprocessing.RobustScaler()
x_scaler = scaler.fit_transform(x)
print(x_scaler)
print(x_scaler.mean(), x_scaler.std(0))

# 正则化，均值归一化(-1,1)
scaler = preprocessing.Normalizer(norm="l2")
x_scaler = scaler.fit_transform(x)
print(x_scaler)
print(x_scaler.mean(), x_scaler.std(0))

# 补全缺失数据
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
print(imp)
