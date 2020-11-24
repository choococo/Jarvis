import numpy as np

a = np.array([[3, 5, 9], [4, 2, 1], [6, 3, 7]])
print(a[[2, 0, 1], [1, 2, 0]])

y = np.arange(12).reshape((3, 2, 2))
print(y)
print(y[:2, 1:, :1])


class MyList(list):
    def length(self):
        return len(self)


# 自定义列表
ss = MyList()
ss.append("Python")
ss.append("猫")
print(ss)
