import cv2
import numpy as np

'轮廓性质_(1)边界聚鑫的宽高比(2)轮廓面积与边界矩形面积比(3)轮廓面积与边界矩形面积比'
'(4)轮廓面积与凸包面积的比(5)对象的方向angle'
img = cv2.imread("../images/23.jpg")

# 1. 图像灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 二值化处理
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 3. 查找轮廓
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

# 4. 边界矩形
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 5.1 最小面积矩形
rect = cv2.minAreaRect(contours[0]) # 矩形两个顶点和旋转角度
print(rect)
box = np.int32(cv2.boxPoints(rect)) # 将两个点和坐标转换成左上角和右下角
cv2.drawContours(image=img, contours=[box], contourIdx=-1, color=(0, 255, 0), thickness=2)

# 5.2 最小外切圆
(x, y), radius = cv2.minEnclosingCircle(points=contours[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (0, 255, 0), 2)

# 5.3 绘制轮廓
cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2)

# 6. 轮廓的一些性质
# 6.1 边界矩形的宽高比
aspect_ratio = float(w) / h
print("边界矩形的宽高比:", aspect_ratio)

# 6.2 轮廓面积与边界矩形面积比
area = cv2.contourArea(contours[0]) # 计算轮廓面积
rect_area = w * h
extent = float(area) / rect_area
print("轮廓面积与边界矩形面积比:", extent)

# 6.3 轮廓面积与凸包面积比
hull = cv2.convexHull(contours[0]) # 凸包和凸包性检测, 纠正曲线，得到凸包的点，
# print("hull:", hull)
area = cv2.contourArea(contours[0]) # 计算轮廓的面积
# print("area:", area)
hull_area = cv2.contourArea(hull) # 计算凸包的面积
# print("hull_area:", hull_area)
solidity = float(area) / hull_area
print("轮廓面积与凸包面积比:", solidity)

# 6.4 与轮廓面积相等的圆的直径
area = cv2.contourArea(contours[0])
equi_diameter = np.sqrt(4 * area / np.pi)
print("与轮廓面积相等的圆的直径:", equi_diameter)

# 6.5 对象的方向
ellipse = cv2.fitEllipse(contours[0])
print(ellipse) # ((150.88723754882812, 124.40936279296875), (78.72029876708984, 261.24176025390625), 138.72865295410156)
print("对象的方向的angle:", ellipse[2])
cv2.ellipse(img, center=(150, 124), axes=(int(78 / 2), int(261 / 2)), angle=138, startAngle=0, endAngle=360, color=(0, 0, 255), thickness=2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()