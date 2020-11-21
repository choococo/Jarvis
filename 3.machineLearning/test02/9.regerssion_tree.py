import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model, svm

# 决策回归树
# 创造数据
x = np.array(list(range(1, 11))).reshape(-1, 1)
y = np.array([5.56, 5.70, 5.91, 6.40, 6.80, 7.05, 8.90, 8.70, 9.00, 9.05]).reshape(-1, 1)

# fit regression model
model1 = DecisionTreeRegressor(max_depth=1)
model2 = DecisionTreeRegressor(max_depth=10)
model3 = linear_model.LinearRegression()
model4 = svm.SVR()

model1.fit(x, y)
model2.fit(x, y)
model3.fit(x, y)
model4.fit(x, y)

# Predict
x_test = np.arange(0.0, 10.0, 0.01).reshape(-1, 1)
print(x_test)

y1 = model1.predict(x_test)
y2 = model2.predict(x_test)
y3 = model3.predict(x_test)
y4 = model4.predict(x_test)

plt.figure()
plt.scatter(x, y, s=20, edgecolors="black", c="darkorange", label="data")
plt.plot(x_test, y1, color='cornflowerblue', label="max_depth=1", linewidth=2)
plt.plot(x_test, y2, color='yellowgreen', label="max_depth=3", linewidth=2)
plt.plot(x_test, y3, color='red', label="linear regression", linewidth=2)
plt.plot(x_test, y4, color='blue', label="svr", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
