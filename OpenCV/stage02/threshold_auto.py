import cv2
import numpy as np
import matplotlib.pyplot as plt


'自适应阈值: 局部二值化'
image = cv2.imread("../images/6.jpg", 0)

# 进行高斯模糊
image = cv2.GaussianBlur(image, ksize=(5, 5), sigmaX=0)

ret, th1 = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_OTSU)
# maxValue:满足条件的 像素点设置为灰度值，adaptiveMethod:自适应阈值方法(1)局部邻域块的平均值(2)局部邻域块的高斯加权平均
# thresholdType=cv2.THRESH_BINARY/cv2.THRESH_BINARY 只能是这两种二值化方法
# blockSize：要分成的区域大小，上面的一般为奇数 C:常数，每个区域计算出的阈值的基础上，减去这个常数作为这个区域的最终阈值，可以为负数 dts:输出图像，可以忽略

th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 3)
th3 = cv2.adaptiveThreshold(src=image, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=9, C=3)

# cv2.imshow("", image)
# cv2.imshow("", th1)
# cv2.imshow("", th2)
# cv2.imshow("", th3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

titles = ['Original Image', 'Global Thresholding (v = 127)',
        'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [image, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1),
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.imshow(th3,"gray")
plt.show()
cv2.waitKey(0)
