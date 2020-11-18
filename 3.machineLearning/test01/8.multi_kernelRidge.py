from sklearn.kernel_ridge import KernelRidge # 导入核领回归
from sklearn.model_selection import GridSearchCV # 导入超级调参网格图
import numpy as np
import matplotlib.pyplot as plt

# 定义一个种子，保证每次随机出来的数据是固定的
rng = np.random.RandomState(0)

# 核岭回归
# 字定义数据和标签
x = 5 * rng.rand(100, 1)
y1 = np.sin(x).ravel()
print(y1.shape) # (100, 1)
print(y1.ravel().shape) # (100,) ravel() 将标签变成一维的数据

y2 = np.cos(x).ravel()

# 为标签添加一些噪声, 每隔5个数据
y1[::5] += 3 * (0.5 - rng.rand(20, 1).ravel())
y2[::5] += 3 * (0.5 - rng.rand(20, 1).ravel())

# 使用超级调参网格
kr1 = GridSearchCV(KernelRidge(), # 表格搜索
                  param_grid={"kernel": ["rbf", "laplacian", "polynomial", "sigmoid"],
                              "alpha": [1e0, 0.1, 1e-2, 1e-3],
                              "gamma": np.logspace(-2, 2, 5)})
kr2 = GridSearchCV(KernelRidge(), # 表格搜索
                  param_grid={"kernel": ["rbf", "laplacian", "polynomial", "sigmoid"],
                              "alpha": [1e0, 0.1, 1e-2, 1e-3],
                              "gamma": np.logspace(-2, 2, 5)})

# 拟合数据
kr1 = kr1.fit(x, y1)
kr2 = kr2.fit(x, y2)

# 分别得到两个超级调参网络的最好的分数和参数
print(kr1.best_score_, kr1.best_params_)
print(kr2.best_score_, kr2.best_params_)

# 生成横坐标-10到10的100个数据
x_plot = np.linspace(-10, 10, 100)
print(x_plot)
y_kr1 = kr1.predict(x_plot[:, None]) # 给一些数据，得出最终-10,10由100个数据拟合(回归)的预测结果曲线
y_kr2 = kr2.predict(x_plot[:, None])

# 查看随机数据的模型的拟合的效果
plt.scatter(x, y1)
plt.scatter(x, y2)
plt.plot(x_plot, y_kr1)
plt.plot(x_plot, y_kr2)
plt.show()



