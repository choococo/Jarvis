from sklearn import linear_model

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import matplotlib.pyplot as plt
import numpy as np

# 多任务岭回归
x, y = datasets.make_regression(n_samples=1000, n_features=1, n_targets=10, noise=10, random_state=0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# 弹性网络
reg = linear_model.MultiTaskElasticNet(0.1) # 多任务弹性网络回归
reg = linear_model.MultiTaskLasso(0.1) # 多任务lasso回归
reg = linear_model.MultiTaskLassoCV(0.1) # 多任务lasso回归
reg = linear_model.MultiTaskElasticNetCV(0.1) # 多任务弹性网络回归


reg.fit(x_train, y_train)

print(reg.coef_, reg.intercept_)

y_pred = reg.predict(x_test)

# 平均绝对误差
print(mean_absolute_error(y_test, y_pred))

# 均方误差
print(mean_squared_error(y_test, y_pred))

# R2评分
print(r2_score(y_test, y_pred))

# 可解释型方差
print(explained_variance_score(y_test, y_pred))

# 模拟数据
_x = np.array([-2.5, 2.5])
_y = reg.predict(_x[:, None]) # 给数据升维，使数据变成

for i in range(10):
    plt.scatter(x_test, y_test[:, i])
    plt.plot(_x, _y[:, i], linewidth=3)

plt.show()







