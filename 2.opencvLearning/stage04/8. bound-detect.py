import cv2
import numpy as np

'边界检测：边界矩形、最小(面积)矩形、最小外接圆以及椭圆拟合、直线拟合'

img = cv2.imread("../images/23.jpg")
imggray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(imggray, 127, 255, cv2.THRESH_BINARY)

# hierarchy 建立一个等级树结构轮廓，
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

# 边界矩形
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

# 最小矩形, 不是正的, 可能是歪的
rect = cv2.minAreaRect(contours[0])
box = np.int32(cv2.boxPoints(rect))
cv2.drawContours(image=img, contours=[box], contourIdx=0, color=(0, 255, 0), thickness=2)

# 最小外接圆
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (255, 0, 0), 2)

# 椭圆拟合
ellipse = cv2.fitEllipse(contours[0])
cv2.ellipse(img, ellipse, (0, 255, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
