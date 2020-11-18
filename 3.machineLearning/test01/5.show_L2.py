import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# x是10x10的希尔伯特矩阵
# x = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
x = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, None])
print(x)

y = np.ones(10)

# 计算不同领系数时的回归系数
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(x, y)
    coefs.append(ridge.coef_)

plt.rcParams['figure.figsize'] = (10, 6)  # 图像显示大小
plt.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['lines.linewidth'] = 0.5  # 设置曲线线条宽度

# 绘图
ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim())
plt.xlabel('岭系数alpha')
plt.ylabel('回归系数coef_')
plt.title('岭系数对回归系数的影响')
plt.axis('tight')
plt.show()