import pandas as pd
import numpy as np

'重建索引'
df = pd.DataFrame({
    # 'a': pd.date_range(start='2020-01-01', periods=5, freq='D')
    'a': pd.date_range(start='2020-01-01', periods=5, freq="D"),
    'b': [1, 2, 3, 4, 5],
    'c': [0.1, 0.2, 0.3, 0.4, 0.5]
})
print(df)

# 重建索引reIndex函数
df = df.reindex(index=[0, 2, 4], columns=['a', 'b', 'c', 'd'])
print(df)

#
