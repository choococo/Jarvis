from sklearn.svm import SVR, SVC
from sklearn import neighbors, linear_model, preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix, precision_score, recall_score
from sklearn.tree import DecisionTreeClassifier

"""
分类模型：
    KNN，KD Tree， KDTree with BBF， SVM, 逻辑斯蒂回归， SGD
"""

# 数据集
iris = load_iris()
x, y = iris.data, iris.target

# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# 数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# 模型选择
model = neighbors.KNeighborsClassifier(n_neighbors=5)
model = DecisionTreeClassifier()
model = SVC()
# model = linear_model.LogisticRegression() # 逻辑斯蒂回归是一个二分类器，加入了sigmoid进行分类
model = linear_model.SGDClassifier()


# 拟合数据
model.fit(x_train, y_train)

# 模型预测
y_pred = model.predict(x_test)

# 交叉验证
scores = cross_val_score(model, x, y, cv=5)
print(scores)

# 模型评估
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_test))
print(f1_score(y_test, y_pred, average="micro"))
print(precision_score(y_test, y_pred, average="micro"))
print(recall_score(y_test, y_pred, average="micro"))
