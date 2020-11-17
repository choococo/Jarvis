import matplotlib.pyplot as plt
from sklearn.datasets import make_regression


# n_samples：样本数 n_feature:特征数(自变量个数) n_informative:参与的建模特征数
# noise:噪音 coef:是否输出coef标识
x, y, coef = make_regression(n_samples=100, n_features=1, noise=30, coef=True)

print(coef)

# 画图
plt.scatter(x, y)
plt.plot(x, x * coef, color='r', linewidth=2)
plt.show()