import cv2
import numpy as np
import matplotlib.pyplot as plt


'简单阈值'
image = cv2.imread("../images/1.jpg", 0)
image = np.uint8(np.arange(400*400).reshape([400, 400])/(400*400)*255)
print(image)

'阈值二值化 threshold binary'
# 小于等于thresh的取0，大于阈值的取maxval
ret, thresh = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
print(ret)                  # 因为是手动设置的，因此为默认的值

'阈值反二值化(threshold binary Inverted)'
# 小于阈值的取maxval，大于阈值的取0
ret, thresh2 = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
print(ret)

'截断(truncate)'
# 小于等于阈值thresh的值保持原色，大于阈值的像素点置灰127(与阈值theshold一致)
print(image[image>127])
ret, thresh3 = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_TRUNC)
print(ret)
print(thresh3[image>127])

'阈值取零'
# 小于或者等于0的像素点置0，大于阈值thresh的像素点保持原色
print(image[image<=127])
ret, thresh4 = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)
print(thresh4[image<=127])

'阈值反取零 threshold to zero inverted'
# 小于或者等于阈值像素保持原色，大于阈值像素点取0
ret, thresh5 = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_TOZERO_INV)



# cv2.imshow("", thresh)
# cv2.imshow("", thresh2)
# cv2.imshow("", thresh3)
# cv2.imshow("", thresh4)
# cv2.imshow("", thresh5)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [image, thresh, thresh2, thresh3, thresh4, thresh5]
for i  in range(len(images)):
    plt.subplot(2, 3, i + 1)                    # 划分两行三列
    'cmap颜色映射: 当image形状是（HW3）或者(HW4)时，值被解释为RGB或者RGBA此时cmap将被忽略'
    '当image形状是二维矩阵(w,h)时，此时cmap用于值到一个颜色的映射'
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])
    plt.axis("off")
plt.show()






