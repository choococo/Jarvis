import pandas as pd
import numpy as np

'自定义函数'
# 表格函数的自定义
# 需要将df中所有元素的内容加2


def add(ele1, ele2):
    return ele1 + ele2


df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(df)


# 数据放到管道中, 设计管道函数
df = df.pipe(add, 2)
print(df)

# 利用apply更加细腻的设置函数，按列求均值
print(df.apply(np.mean, axis=0))
print(df.apply(np.std, axis=0))

# 根据水平操作axis=1
print(df.apply(np.std, axis=1))

# 对每一个元素进行操作
print(df.applymap(lambda x:x*100))
