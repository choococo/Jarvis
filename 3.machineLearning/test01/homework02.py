import numpy as np
from sklearn.kernel_ridge import KernelRidge # 核岭回归
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split


"""
核岭回归：就是加入了核函数(就是激活函数)，提供非线性能力
    下面使用到的ravel()的作用
"""
rng = np.random.RandomState(0)
print(rng) # RandomState(MT19937)
# 核岭回归
x = 5 * rng.rand(100, 1) # 生成固定种子的随机数据
y = np.sin(x).ravel() # 标签是一条sin曲线



# print(x)
print(y.shape)

# 给目标添加噪声
y[::5] += 3 * (0.5 - rng.rand(20, 1).ravel())
print(y.shape)
print(y[::5].shape) # (20,)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

kr = KernelRidge(kernel='sigmoid', alpha=0.3, gamma=0.3)
kr = KernelRidge(kernel='linear', alpha=0.5, gamma=0.5)
kr = KernelRidge(kernel='rbf', alpha=0.5, gamma=0.5)

kr = GridSearchCV(KernelRidge(),
                  param_grid={
                      "kernel":['rbf', 'laplacian', 'polynomail', 'sigmoid'],
                      "alpha":[1e0, 0.1, 1e-2, 1e-3],
                       "gamma":np.logspace(-2, 2, 5)
                  })
print(np.logspace(-2, 2, 5))
# 模型拟合
kr.fit(x_train, y_train)
# 查看超级调参的结果:查看最好的分数和最好的参数
print(kr.best_score_, kr.best_params_)

x_plot = np.linspace(0, 5, 100)
print(x_plot[:, None].shape)
y_kr = kr.predict(x_plot[:, None]) # 给数据升维成二维后可以进行预测

plt.scatter(x_test, y_test)
plt.plot(x_plot, y_kr, color='red')
plt.show()
