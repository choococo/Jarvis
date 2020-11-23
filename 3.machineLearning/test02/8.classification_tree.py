import graphviz
import numpy as np
from sklearn import tree, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 决策分类树
# 加载数据
iris = datasets.load_iris()
wine = datasets.load_wine()

# 划分测试集与训练集
x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# 数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# 创建模型,
clf = tree.DecisionTreeClassifier(max_depth=5)

# 模型拟合
clf.fit(x_train, y_train)

# 预测
y_pred = clf.predict(x_test)

# 评估
print(accuracy_score(y_test, y_pred))

# 绘制决策分类树
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names,
                                class_names=iris.target_names, filled=True,
                                rounded=True, special_characters=True)

graph = graphviz.Source(dot_data)
graph.render('iris')





