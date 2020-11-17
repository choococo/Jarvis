import cv2
import numpy as np

'二值化'
image = cv2.imread("../images/2.jpg")
print(image.shape)                      # (251, 500, 3) HWC

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色图转换成灰度图
print(gray.shape)                               # (251, 500)
print(gray[gray > 127][0 : 100])                # 查看像素值大于100的前100个像素值

'阈值二值化 threshold binary'
# 小于阈值(thresh)的像素点置0, 大于阈值的像素点置255
# ret, binary = cv2.threshold(gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
# 自动求阈值
ret, binary = cv2.threshold(gray, thresh=0, maxval=255, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(ret)
cv2.imshow("gray", gray)
cv2.imshow("binary", binary)                    # 图片显示出的，就是白底黑字的图片
cv2.waitKey(0)
cv2.destroyAllWindows()

