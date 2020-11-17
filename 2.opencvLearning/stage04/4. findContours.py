import cv2
import numpy as np

'轮廓查找与绘制：findContours()、drawContours()'
'轮廓检索、轮廓近似'

img = cv2.imread("../images/23.jpg")
# img = cv2.imread("../images/1.jpg")

# 1. 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 阈值二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 3. 查找轮廓：包括的canny算法
# findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
# image:输入图像(二值化图像)
# mode：轮廓检索方式
# method:轮廓近似方法
"""
轮廓检索方式：
cv2.RETR_EXTERNAL 只检测外轮廓    _______________用的是最多的
cv2.RETR_LIST 检测的轮廓不建立等级关系
cv2.RETR_CCOMP 建立两个等级的轮廓，上一层为外边界，里面一层为内孔的边界信息
cv2.RETR_TREE 建立一个等级树结构轮廓，包含关系

轮廓近似方法：
cv2.CHAIN_APPROX_NONE 存储所有外边界
cv2.CHAIN_APPROX_SIMPLE 压缩垂直、水平、对角方向，只保留端点
"""
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
print(len(contours[0]))  # 点的数量
# print(contours[0])
cv2.imshow("thresh", thresh)
print(hierarchy)  # 层次树

# 绘制轮廓：直接对原图进行操作
img_contour = cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow("img_contour", img_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
