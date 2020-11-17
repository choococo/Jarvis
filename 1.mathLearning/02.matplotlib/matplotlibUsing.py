import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class MatplotlibUsing:

    def __init__(self):
        """
        构造器
        """
        self._ax = []
        self._bx = []

    def _fontRcParams(self):
        """
        设置字体
        :return:
        """
        plt.rcParams["font.sans-serif"] = ["SimHei"]

    def drawIon(self, function=None, start=1, end=101):
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

    def drawBar(self, x=[], y=[], x1=[], y1=[]):
        """
        绘制柱形图
        :param x: 坐标x
        :param y: 坐标y
        :param x1: 坐标x1
        :param y1: 坐标y1
        :return: 没有返回值，直接显示图像
        """
        plt.bar(x, y)
        plt.bar(x1, y1)
        plt.show()

    def drawHist(self, x, numbers=200):
        """
        绘制条形分布图
        :param x: 坐标x
        :param numbers: 条形的个数
        :return: 直接显示图像
        """
        plt.hist(x, numbers)
        plt.show()

    def drawHist2d(self, x, y, numbers=100):
        """
        绘制2D点图
        :param x: 坐标x
        :param y: 坐标y
        :param numbers: 点的数量
        :return: 直接显示图像
        """
        plt.hist2d(x, y, numbers)
        plt.show()

    def drawPie(self, sizes, explode, labels, title="饼图"):
        """
        绘制饼图
        :param sizes: 所占区域的大小，不用自己进行百分比计算，会自动计算
        :param explode: 饼图之间的间隙
        :param labels: 每个面积所代表的含义
        :param title: 饼图的题
        :return: 显示图像
        """
        self._fontRcParams()
        plt.pie(sizes, explode, labels, autopct="%.f%%", shadow=True, startangle=180)
        plt.title(title)
        plt.show()

    def drawScatter(self, x=[], y=[], x1=[], y1=[], label1=None, label2=None, title="分布点图"):
        """
        绘制点图
        :param x: x
        :param y: y
        :param x1: x1
        :param y1: y1
        :param label1: label1
        :param label2: label2
        :param title: 标题
        :return: 显示图像
        """
        self._fontRcParams()
        plt.scatter(x, y, marker=".", c="b", label=label1)
        plt.scatter(x1, y1, marker="*", c="r", label=label2)
        plt.legend()
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def drawAxes3DScatter(self, xs, ys, zs, label):
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(xs, ys, zs, c='r', marker="p", label=label)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    matplotlib = MatplotlibUsing()
    # matplotlib.drawIon(start=1, end=101)
    # matplotlib.drawBar(x=[5, 8, 10], y=[9, 7, 3], x1=[6, 9, 4], y1=[8, 6, 4])

    # matplotlib.drawHist(np.random.randn(2000))
    # matplotlib.drawHist2d(np.random.randn(1000), np.random.randn(1000), 100)

    # labels = ["教育","医疗","餐饮","交通","房贷","车贷","其他"]
    # sizes = [10, 7, 5, 5, 60, 8, 5]
    # explode = (0, 0, 0, 0, 0.1, 0, 0)   # 间隙
    # matplotlib.drawPie(sizes, explode, labels, title="10月份个人支出")

    # x = np.random.rand(20)
    # y = np.random.rand(20)
    # x1 = np.random.rand(20)
    # y1 = np.random.rand(20)
    # matplotlib.drawScatter(x, y, x1, y1, title="男生女生分布散点图", label1="男生", label2="女生")

    x = np.random.randn(100)
    y = np.random.randn(100)
    z = np.random.randn(100)
    matplotlib.drawAxes3DScatter(x, y, z, label="boy")