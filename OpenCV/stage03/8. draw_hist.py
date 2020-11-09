import cv2
import matplotlib.pyplot as plt
import numpy as np

'绘制直方图'
# 1）以为直方图, 要使用plt.plot()进行显示，都是一堆像素点
img = cv2.imread("../images/30.jpg")  # 草坪的小图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰度图
print(gray.shape)  # (59, 130)
# 绘制灰度图的直方图
hist_gray = cv2.calcHist(images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
print(hist_gray.shape)  # (256, 1)
# 绘制单通道B的直方图
hist_B = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
# 绘制单通道G的直方图
hist_G = cv2.calcHist([img], channels=[1], mask=None, histSize=[256], ranges=[0, 255])
# 绘制单通道R的直方图
hist_R = cv2.calcHist([img], channels=[2], mask=None, histSize=[256], ranges=[0, 255])
# print(hist_G)

# plt.plot(hist_gray, color="gray", label="Gray")
# plt.plot(hist_B, color="b", label="B")
# plt.plot(hist_G, color="g", label="G")
# plt.plot(hist_R, color="r", label="R")
# plt.show()

# 2)2D直方图
img = cv2.imread("../images/1.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(type(img)) # <class 'numpy.ndarray'>
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 绘制2D直方图
hist_hsv = cv2.calcHist([hsv], channels=[0, 1], mask=None, histSize=[180, 256], ranges=[0, 180, 0, 255])  # ????

# plt.imshow(hsv)
# # plt.plot("hist_hsv", hist_hsv)
# plt.axis('off')
# plt.show()
cv2.imshow("hist_hsv", hist_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
