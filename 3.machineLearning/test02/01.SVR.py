from sklearn.svm import SVC, SVR
import numpy as np
import matplotlib.pyplot as plt


# 支持向量回归机
rng = np.random.RandomState(0)

x = 5 * rng.rand(100, 1)
# y = np.sin(x).reshape(100)
y = np.sin(x).ravel() # 与上面的效果是一样的

print(x.shape)
print(y.shape)

y[::5] += 3 * (0.5 - rng.rand(20, 1).ravel())
print(y.shape)

svr = SVR(kernel='rbf',C=10, gamma=0.1)
svr.fit(x, y)

x_plot = np.linspace(0, 5, 100).reshape(-1, 1)
print(x_plot.shape)

y_svr = svr.predict(x_plot)
print(y_svr)

plt.scatter(x, y)
plt.plot(x_plot, y_svr, color="red")
plt.show()

