import matplotlib.pyplot as plt
import numpy as np

ax = []                                                 # 收集x
bx = []                                                 # 收集y

plt.ion()                                               # 打开实时画图
for i in range(1, 101):                                 # 循环
    ax.append(i)                                        # 添加x坐标
    bx.append(-np.log(1 / (1 + np.exp(-i ** 2))))       # 添加y坐标，规定函数类型
    plt.clf()                                           # 清除上一次的图层
    plt.plot(ax, bx, 'y')                               # 绘制直线
    plt.scatter(ax, bx, c="y", marker="*")              # 绘制点
    plt.pause(0.01)                                     # 加入阻塞

plt.ioff()                                              # 关闭实时画图
plt.show()                                              # 展示最后一次效果








