import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像梯度——使用到的函数：cv2.Soble(), cv3.Schar(), cv2.Laplacian
# 前两种是求一阶或者二阶导数，Scharr是对Sobel(使用小卷积核求解梯度角度)的优化，Lapplacian是求二阶导数
'高通滤波——去掉低频的信号，留下高频信号（上面的三种不同的梯度滤波器）'
src = cv2.imread("../images/1.jpg")
'1. 锐化操作——使得梯度变得明显'
# 1. 自定义锐化核
kernel = np.float32([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
dst1 = cv2.filter2D(src, ddepth=-1, kernel=kernel)

# USM锐化（）UnSharpMask
gaussian = cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=3, sigmaY=3)  # 进行高斯模糊
dst2 = cv2.addWeighted(src, alpha=2, src2=gaussian, beta=-1, gamma=0)

# cv2.imshow("dst1", dst1)
# cv2.imshow("gaussian", gaussian)
# cv2.imshow("dst2", dst2)

'2. 梯度操作/高通滤波：找轮廓'
gray = cv2.imread("../images/6.jpg", cv2.IMREAD_GRAYSCALE)  # 变成单通道
print(gray.shape)

# 1. Sobel算子：dx和dy表示的是求导的阶数，0表示这个方向上没有导数，一般为0,1,2
sobel_x = cv2.Sobel(gray, ddepth=-1, dx=1, dy=0, ksize=3)  # x轴方向的一阶导数，x方向指的是左右相邻的梯度很大，感觉上是竖着的
sobel_y = cv2.Sobel(gray, ddepth=-1, dx=0, dy=1, ksize=3)  # y轴方向的一阶导数，y方向 指的是上下相邻的梯度很大，感觉上是横着的
sobel_x_abs = cv2.convertScaleAbs(sobel_x, alpha=2, beta=1)  # 对图像进行增强，参数值变大会曝光
sobel_y_abs = cv2.convertScaleAbs(sobel_y, alpha=2, beta=1)  # 对图像进行增强，参数值变大会曝光

sobel = cv2.addWeighted(sobel_x_abs, 0.5, sobel_y_abs, 0.5, gamma=0)  # 近似有|G|=|Gx|+|Gy|

# 2. Scharr算子:dx和dy表示的是求导的阶数，0表示在这个方向上没有求导，一般为0,1,2
scharr_x = cv2.Scharr(gray, ddepth=-1, dx=1, dy=0)  # x轴方向上的一阶导数
scharr_y = cv2.Scharr(gray, ddepth=-1, dx=0, dy=1)  # y轴方向上的一阶导数
scharr_x_abs = cv2.convertScaleAbs(scharr_x)  # 进行图像增强
scharr_y_abs = cv2.convertScaleAbs(scharr_y)  # 进行梯度的增强
scharr = cv2.addWeighted(scharr_x_abs, 0.5, scharr_y_abs, 0.5, 0)  # 近似有|G|=|Gx|+|Gy|

# 3. Laplacian算子
laplacian = cv2.Laplacian(gray, ddepth=-1)

# cv2.imshow("gray", gray)
# cv2.imshow("sobel_x", sobel_x)
# cv2.imshow("sobel_y", sobel_y)
# cv2.imshow("sobel_x_abs", sobel_x_abs)
# cv2.imshow("sobel_y_abs", sobel_y_abs)
# cv2.imshow("sobel", sobel)
# cv2.imshow("scharr_x", scharr_x)
# cv2.imshow("scharr_x_abs", scharr_x_abs)
# cv2.imshow("laplacian", laplacian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 结合matplotlib显示多张图片
titles = ['Original Gray', 'Sobel x', 'Sobel y', 'Sobel', 'Scharr x', 'Scharr y', 'Scharr', 'Laplacian']
images = [gray, sobel_x_abs, sobel_y_abs, sobel, scharr_x, scharr_y, scharr, laplacian]
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
