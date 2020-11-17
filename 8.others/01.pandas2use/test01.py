import pandas as pd
import numpy as np

'pandas 是numpy的一个升级，对数据处理的更加的高效，比numpy更强大更高效'
'类似于一维的数组'
s = pd.Series([1, 2, 3, 4, np.nan, 6, 8])                           # np.nan 非数字
print(s)

'DataFrame 数据结构'
dates = pd.date_range('20200101', periods=6)                         # 生成 随机的日期， periods=6个
print(dates)

'生成数据帧 二维数据'
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))  # (数据[6, 4], 索引=时间， 列索引=[列名字])
print(df)
print(df.head(3))                                                           # 取前面的3条数据
print(df.tail(3))                                                           # 取后面的三条
print(df.columns)
print(df.describe())                                                        # 快速了解数据一些方差等数据

print(df.sort_values(by="B"))                                               # 通过B轴进行排序
print(df["A"])                                                              # 取A轴的数据 索引
print(df[0:3])                                                              # 切片, 取前三行的数据
