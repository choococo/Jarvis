from sklearn import preprocessing
import numpy as np

'one_hot'

enc = preprocessing.OneHotEncoder()  # 通过索引
enc1 = preprocessing.OneHotEncoder(sparse=False)

ans = enc.fit_transform([[0], [1], [2], [3]])
print(ans)
"""
  (0, 0)	1.0
  (1, 1)	1.0
  (2, 2)	1.0
  (3, 3)	1.0
"""
ans1 = enc1.fit_transform([[0], [1], [2], [3]])
print(ans1)
"""
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
"""
num_classes = 10
index = [0, 2, 1, 3]
one_hots = np.eye(num_classes)[index]
print(one_hots)

# 返回原始数据
data = [np.argmax(one_hot) for one_hot in one_hots]
print(data)
