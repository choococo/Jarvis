from sklearn import datasets, neighbors, preprocessing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 引入数据
iris = datasets.load_iris()

x, y = iris.data, iris.target

# 数据预处理
scaler = preprocessing.StandardScaler().fit(x) # 按照x进行数据预处理

x = scaler.transform(x)

# 设置n_neighbors的值为1到30，通过绘制图像来看训练分数

k_range = range(1, 31)
k_score = []

for k in k_range:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, x, y, cv=5, scoring="accuracy")
    k_score.append(scores.mean())

plt.figure()
plt.plot(k_range, k_score)
plt.xlabel("Value of k for KNN")
plt.ylabel("CrossValidation accuracy")
plt.show()