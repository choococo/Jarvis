import cv2
import numpy

"边界检测: 边界矩形、最小(面积)矩形、最小外接圆以及椭圆拟合、直线拟合"
import cv2
import numpy as np

# img = cv2.imread('../images/23.jpg')
img = cv2.imread('../images/1.jpg')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imggray, 127, 255, 0)
ret, thresh = cv2.threshold(imggray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("thresh", thresh)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 边界矩形
# x, y, w, h = cv2.boundingRect(contours[0])
# img_contour = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# 最小矩形
# rect = cv2.minAreaRect(contours[0])
rect = cv2.minAreaRect(contours[0])
print(rect)
box = cv2.boxPoints(rect)
print(box)
print(box.dtype, box.shape)
box = np.int32(box)
print(box.dtype, box.shape)
img_contour = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
# # 最小外接圆
# (x, y), radius = cv2.minEnclosingCircle(contours[0])
# center = (int(x), int(y))
# radius = int(radius)
# img_contour = cv2.circle(img, center, radius, (255, 0, 0), 2)
#
# # 椭圆拟合
# ellipse = cv2.fitEllipse(contours[0])
# print(ellipse)
# cv2.ellipse(img, ellipse,(0, 255, 255), 2)

cv2.imshow("img_contour", img_contour)
cv2.waitKey(0)
