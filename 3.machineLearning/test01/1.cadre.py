from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split # 分割数据及
from sklearn.metrics import accuracy_score # 精度分数
from sklearn.model_selection import cross_val_score # 训练时的交叉验证

# 1. 加载数据：内置数据(鸢尾花)
iris = datasets.load_iris()

# 2. 划分数据集
x, y = iris.data, iris.target
print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape)

# 3. 数据预处理
scaler = preprocessing.StandardScaler().fit(x_train) # 数据预处理对象
# print(scaler) # StandardScaler(copy=True, with_mean=True, with_std=True)
print(type(scaler)) # <class 'sklearn.preprocessing._data.StandardScaler'>
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x_train)
print(x_test)
print(x_train.mean(), x_train.std())
print(x_test.mean(), x_test.std())

# 4. 创建KNN分类模型
knn = neighbors.KNeighborsClassifier(n_neighbors=11) # 新数据圈内的原数据数据量

# 5. 模型拟合：给模型传入数据
knn.fit(x_train, y_train)

# 6.在训练的过程中，选择交叉验证方式：数据分割比例，开始交叉训练验证
scores = cross_val_score(knn, x_train, y_train, cv=5, scoring="accuracy")
print("每组评分结果：", scores)
print("评分结果的均值：", scores.mean())

# 7. 模型预测
y_pred = knn.predict(x_test)
print(y_pred)

# 8. 测试集的评估结果使用accuracy
print(accuracy_score(y_test, y_pred))

