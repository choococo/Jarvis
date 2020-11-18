from sklearn import linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import matplotlib.pyplot as plt
import numpy as np

"""
拟合(回归)模型的评估指标：
    （1）平均均方差（2）平均绝对误
    
    差（3）R2分数 （4）可解释型方差
    其中，最常用的是R2分数，用于后面对于人脸侦测的回归评估指标
"""
# datasets.make_regression 其本质是对一个简单的线性模型进行拟合，然后随机返回某些输入样例和
# 对应的输出样例
x, y = datasets.make_regression(n_samples=1000, n_features=1, n_targets=1, noise=50)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

print(x.shape, y.shape)

# 导入线性回归模型？？？？？？？？？？？？？？？？方程和参数的含义，需要看视频和博客
reg = linear_model.LinearRegression() # y=x 普通线性回归
reg = linear_model.Ridge(alpha=0.5) # 岭回归 加入正则化，使用的是L2正则化
reg = linear_model.Lasso(alpha=0.1) # L1 lasso回归
reg = linear_model.ElasticNet(alpha=0.1, l1_ratio=0.2) # 弹性网络：基于L1和L2的综合考虑
reg = linear_model.LogisticRegression() # sigmoid, 逻辑斯蒂回归，这个虽然是回归，但是其实是分类的，这里会报错
reg = linear_model.BayesianRidge() # 贝叶斯岭回归
reg = linear_model.ElasticNet()

# 进行拟合
reg.fit(x_train, y_train)
# intercept：代表w0
print(reg.coef_, reg.intercept_)

# 拟合之后进行预测
y_pred = reg.predict(x_test)

# 通过回归的评估指标对模型进行评估
# (1)平均绝对误差
print("平均绝对误差:", mean_absolute_error(y_test, y_pred))

# (2) 均方误差
print("均方误差:", mean_squared_error(y_test, y_pred))

# (3) R2评分
print("R2评分:", r2_score(y_test, y_pred))

# (4) 可解释型方差
print("可解释型方差:", explained_variance_score(y_test, y_pred))

# print(y_test)
# print(y_pred)

_x = np.array([-2.5, 2.5])
_y = reg.predict(_x[:, None]) # 对其进行升维 输入到模型中的x需要是 [n, 1]维度的

print((_x[:, None]).shape)
print(_x.shape)

plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred)
plt.show()




