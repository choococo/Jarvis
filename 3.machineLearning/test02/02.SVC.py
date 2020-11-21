from sklearn.svm import SVC, SVR
from sklearn.model_selection import train_test_split
from sklearn import linear_model, svm, neighbors, datasets, preprocessing
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

# SVC支持向量分类机
# 1. 加载数据
iris = datasets.load_iris()
x, y = iris.data, iris.target

# random_state=0 设置随机数种子，保证每一次都是同一个随机数，则每次得到的数据都是不一样的
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# 2. 数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# 3. 创建模型
clf = SVC()

# 4. 模型拟合
clf.fit(x_train, y_train)

# 5. 预测
y_pred = clf.predict(x_test)

# 6. 评估
# 分类问题的评估指标：f1分数，精确度，召回率
# 1）f1分数：f1 = 2*(P*R) / (P+R)
print("f1分数: ", f1_score(y_test, y_pred, average="macro"))

# 2)分类报告:用于最终项目提交时的参数文档
print(classification_report(y_test, y_pred))

# 3）混淆矩阵
print(confusion_matrix(y_test, y_pred))

"""
精确度：precision，正确预测为正的，占全部预测为正的比例，TP / (TP+FP)
召回率：recall，正确预测为正的，占全部实际为正的比例，TP / (TP+FN)
F1-score：精确率和召回率的调和平均数，2 * precision*recall / (precision+recall)
类别数量：每类数据标签的数量。

微平均值：micro average，所有数据结果的平均值
宏平均值：macro average，所有标签结果的平均值
加权平均值：weighted average，所有标签结果的加权平均值
"""