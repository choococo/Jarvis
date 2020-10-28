import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


'实时画图'


class RealTimeDrawing:

    def __init__(self):
        self._ax = []
        self._bx = []

    def draw(self, function=None, start=1, end=101):
        """
        实时画图
        :param function: 函数
        :param start: 开始绘制点的坐标
        :param end: 结束绘制点的坐标
        :return: 没有返回，显示实时绘图的结果
        """
        plt.ion()
        for i in range(start, end):
            self._ax.append(i)
            self._bx.append(-np.log(1 / (1 + np.exp(-i ** 2))))
            plt.clf()
            plt.plot(self._ax, self._bx)
            plt.scatter(self._ax, self._bx, c='red', marker=".")
            plt.pause(0.01)
        plt.ioff()
        plt.show()


if __name__ == '__main__':
    draw = RealTimeDrawing()
    draw.draw(start=1, end=101)

# ax = []                                                 # 收集x
# bx = []                                                 # 收集y
#
# plt.ion()                                               # 打开实时画图
# for i in range(1, 101):                                 # 循环
#     ax.append(i)                                        # 添加x坐标
#     bx.append(-np.log(1 / (1 + np.exp(-i ** 2))))       # 添加y坐标，规定函数类型
#     plt.clf()                                           # 清除上一次的图层
#     plt.plot(ax, bx, 'y')                               # 绘制直线
#     plt.scatter(ax, bx, c="y", marker="*")              # 绘制点
#     plt.pause(0.01)                                     # 加入阻塞
#
# plt.ioff()                                              # 关闭实时画图
# plt.show()                                              # 展示最后一次效果








