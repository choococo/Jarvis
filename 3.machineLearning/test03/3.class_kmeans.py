from sklearn.svm import SVC, SVR
from sklearn import datasets, preprocessing
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score

iris = datasets.load_iris()

x, y = iris.data, iris.target

# 划分训练集与训练集
x_train, x_test, y_trian, y_test = train_test_split(x, y, test_size=0.3)

# 数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train, x_test = scaler.transform(x_train), scaler.transform(x_test)

# 创建模型
clf = SVC()  # SVM模型

# 模型拟合
clf.fit(x_train, y_trian)

# 预测
y_pred = clf.predict(x_test)

# 分类评估：准确度,只是测试的时候，但是不好
print(accuracy_score(y_test, y_pred))
#

# f1_score 由PR曲线(召回率和精确率) average 默认是二分类的binary,决定f1的计算方式
# mirco:通过计算总体的tp值，TP,FN,FP的数量，再计算F1
# macro:分别计算每个类的f1，然后再做平均
print(f1_score(y_test, y_pred, average="macro"))

# 分类报告
# macro avg 宏平均值(所有标签结果的平均值)； weighted avg 加权平均值(所有标签的期望)
# 上面的平均值是不需要的，如果后面的评估报告，是需要这个的
# 多分类用到的是mAP
print(classification_report(y_test, y_pred))

# 混淆矩阵
print(confusion_matrix(y_test, y_pred))

# mAP 对于模型的比较全面的评估 sklearn是用numpy类型的
