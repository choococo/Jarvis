import numpy as np
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 生成数据
data = np.random.rand(100, 3)

# 构建模型
estime = KMeans(n_clusters=3)

# 模型聚类
y = estime.fit_predict(data)
print(y)

# 获取聚类中心
center = estime.cluster_centers_

# 获取类别的标签
label_pred = estime.labels_

print(center)
print(label_pred)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=y, marker="*", s=80)
ax.scatter(center[:, 0], center[:, 1], center[:, 2], c=center[0], marker=">", s=120)
plt.show()