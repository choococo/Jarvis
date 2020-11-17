import pandas as pd
import numpy as np

"""
pd.DataFrame(data, index, columns, dtype)
"""
'1. 创建空的DataFrame'
df = pd.DataFrame()
print(df)
"""
result:
    Empty DataFrame
    Columns: []
    Index: []
"""
data = [1, 2, 3, 4, 5, 6]
df = pd.DataFrame(data)
print(df)

'2. 创建两列数据， 1列名字， 1列年龄'
data = [['xiaoming', 10], ["BOB", 12], ['laochen', 13]]
df = pd.DataFrame(data, columns=['username', 'age'])
print(df)

'字典创建DataFrame'
data = {
    'username':['小熊', '小白', '小刘'],
    'income':[1000, 2000, 3000]
}
df = pd.DataFrame(data, index=[1, 2, 3])
print(df)

d = {
    'one':pd.Series(data=[1, 2, 3], index=['a', 'b', 'c']),
    'two':pd.Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)   # 不全的用NaN补充
print(df['one'])
df['three'] = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
print(df)
df['four'] = df['one'] + df['two']
print(df)

del df['four']
print(df)

df.pop('two')
print(df)

print("-----------------------")
'通过标签选择行'
print(df.loc['a'])
print(df)
df2 = pd.DataFrame([[2, 3], [5, 6]], columns=['one', 'three'])
print(df2)
df = df.append(df2)         # 这里一定要赋值，与Python中的操作不同了
print(df)

df = df.drop(0)             # 同理这里也要有返回值
print(df)