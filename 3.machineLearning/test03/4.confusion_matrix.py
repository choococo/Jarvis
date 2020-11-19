from sklearn.metrics import confusion_matrix

# 多分类混淆矩阵
y_true = [2, 1, 0, 1, 2, 0]
y_pred = [2, 0, 0, 1, 2, 1]

c = confusion_matrix(y_true, y_pred)
print(c)

"""
        实际值
预测值  [[1 1 0]
        [1 1 0]
        [0 0 2]]
"""
