import cv2
import matplotlib.pyplot as plt

'绘制直方图'
# 1) 一维直方图
img = cv2.imread("../images/30.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)            # 转换为灰度图

# 绘制灰度直方图
hist_gray = cv2.calcHist(images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
cv2.imshow("hist_gray", hist_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()