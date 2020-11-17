import cv2
import numpy as np

# 图像平滑处理（图像模糊）——使用低通滤波器对取出噪声很有帮助
# 方法：1）使用不同的低通滤波器对图像进行模糊
#       使用低通滤波器可以达到图像模糊的目的。这对去除噪音很有帮助。
#       其实就是去除图像中的高频成分（比如：噪声、边界）。所以边界也
#       会被模糊一点。（当然，也有一些技术不会模糊边界）。OpenCV中提供了四种模糊技术
#      2）使用自定义的滤波器对图像进行 卷积（2D卷积）

"""
图像的时域（分析 每个时间点、空间位置的一个点）和频域（分析两个点、线之间的变化：就是梯度）
滤波是将信号中特定波段频率滤除的操作，是抑制和防止干扰的一项重要的措施
图像滤波是图像预处理中不可缺少的操作，其处理的好坏将直接影响到后续图像处理和分析的有效性和可靠性。
图像滤波，即在尽量保留图像细节特征的条件下对目标图像的噪声进行抑制。
图像滤波的目的：
1. 消除图像识别中混入的噪声
2. 为图像识别抽取出图像的特征
滤波可以分为 ：低通滤波、高通滤波、中通滤波、阻带滤波。都是从频域上区别的。
低通滤波：减弱或阻隔高频信号，保留低频信号，只留下变化较小的信号。可使图像变模糊，主要用于去噪。
中通滤波：获取已知范围内的信号，去掉变化较大和较小的信号。一般用于获取图像边缘、轮廓或梯度。
阻带滤波：去掉已知频率范围内的信号，去掉变化适中的信号，留下变化较大和较小的信号
"""

'1. 使用自定义的滤波器对图像进行卷积（2D卷积）'
img = cv2.imread("../images/1.jpg")

# 1. 定义一个卷积核
kernel = np.float32([[1, 1, 0], [1, 0, -1], [0, -1, -1]])
kernel = np.float32([[-1, 1, 0], [1, 0, -1], [0, -1, 1]])
kernel = np.float32([[1, 0, 0], [0, 0, 0], [0, 0, -1]])

# 2. 进行卷积操作filer2D(image, -1, kernel) ddepth:目标所需深度??
dst = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

'使用不同的 低通滤波器（平滑滤波） 实现图像的平滑处理'
# 低通滤波器会保留低频的信息，去除掉高频的信息，会使图像变得模糊
img1 = cv2.imread("../images/132.jpg")  # 图像1加上噪声后的图像,颜色偏亮也比图像比较清晰
img2 = cv2.imread("../images/134.jpg")  # 芙蓉姐

# 1. 均值滤波：blur(src, ksize, dst=None, anchor=None, borderType=None)
# 使用卷积核覆盖区域的所有像素的平均值来代替中心元素
mean = cv2.blur(img1, ksize=(3, 3))  # 均值滤波处理后，图像变得平滑（模糊）

# 2. 中值滤波：medianBlur(src, ksize, dst=None) ksize为大于1的奇数
# 与卷积框对应像素位置的中值来代替像素的值
median = cv2.medianBlur(img1, ksize=3)  # 图像变得平滑，也可以看得清楚，效果较好

# 3. 高斯滤波：GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
# ksize 为奇数，不知道噪声分布的情况下一般使用高斯滤波
# sigmaX是高斯滤波在x轴方向上的标准差。若不指定sigmaX，则sigX=sigmaY
gaussian = cv2.GaussianBlur(img1, ksize=(7, 7), sigmaX=3, sigmaY=3)  # 效果一般

# 4. 双边滤波：bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
# d是每个像素的领域直径，由两个函数组成
# sigmaColor:在颜色空间中的滤波sigma, sigmaSpace:在坐标系空间中的过滤sigma
# sigma无穷大时，效果等价于高斯模糊，sigma=0时，效果与原图一样
bilateral = cv2.bilateralFilter(img1, 33, 77, 77)  # 具有美颜功能

#  高斯滤波与双边滤波的区别：
# 1）高斯滤波只考虑了空间分布，没有考虑像素值的差异 ，会将图像的边缘模糊掉
# 2）双边滤波是高斯滤波提出的，结合了图像的空间邻近度和像素值相似度的一种折中处理，具有保边特性

cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
cv2.imshow("mean", mean)
cv2.imshow("median", median)
cv2.imshow("gaussian", gaussian)
cv2.imshow("bilateral", bilateral)

# cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
