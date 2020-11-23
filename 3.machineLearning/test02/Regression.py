from sklearn.svm import SVR
from sklearn import datasets, preprocessing, linear_model
from sklearn.metrics import accuracy_score, r2_score, explained_variance_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

"""
回归模型：
    线性回归，岭回归，Lasso回归，弹性网络，核岭回归(加入核函数，增加非线性能力)，SVR，决策回归树
"""
iris = datasets.load_iris()

x, y = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# 数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# 模型
model = linear_model.LinearRegression()

# 模型交叉验证
scores = cross_val_score(model, x, y, cv=5)
print(scores)





