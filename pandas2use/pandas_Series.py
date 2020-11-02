import pandas as pd
import numpy as np

'series: 一维标记数据，可以保存任意类型的数据'
# pd.Series(data, index, dtype, copy)
# data->数据, np.ndarray, list, constants
# index->索引,
# dtype:数据类型
# copy: 复制数据
# s = pd.Series()
# print(s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)

'生成字典Series'
data = {
    'user1': 100,
    'user2': 200,
    'user3': 300
}
s = pd.Series(data)
print(s)

'标量创建Series'
# s = pd.Series(5, index=[0, 1, 2, 3])
# print(s)

print(s[['user1', 'user2']])
print(s[-3:])
print(s[:3])
print(s[2])