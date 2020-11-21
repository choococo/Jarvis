from sklearn import preprocessing
from sklearn.impute import SimpleImputer
import numpy as np

# preprocessing:["mean", "median", "most_frequent", "constant"]
# imp = preprocessing.Imputer(missing_values='NaN', strategy='mean')
# 图像补全
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
y_imp = imp.fit_transform([[np.nan, 2], [6, np.nan], [7, 6]])

print(y_imp)

# 学习填值，学习使用第一组数的均值来给第二组数填充
y_imp = imp.transform([[np.nan, 2], [6, np.nan], [7, 6]])
print(y_imp)

