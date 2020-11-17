import pandas as pd
import numpy as np


d = {
    'name':pd.Series(['小明', '小黑', '小红']),
    'age':pd.Series([12, 16, 14]),
    'score':pd.Series([98, 99, 97])
}
df = pd.DataFrame(d)
print(df)
print(df['name'])                   # 取一列只需要一个[]
print(df[['name', 'age']])          # 取两列值就需要两个[]


'求和'
# sum求和函数,按照轴求和, 默认是按照列求和, axis = 0
print(df.sum())
# 设置按照行求和
print(df.sum(axis=1))

'求平均'
# 默认按照列求平均, 不是数字就不求
print(df.mean())

'求标准差'
print(df.std())

'求最大值、最小值'
print(df.min())
print(df.max())
print(df[['age', 'score']].abs())

'查看汇总的数据'
print(df.describe())

print(df.describe(include="object"))
print(df.describe(include="number"))
print(df.describe(include="all"))
