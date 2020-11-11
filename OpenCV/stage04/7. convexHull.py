import cv2

'凸包和凸性检测：convexHull()、isContourConvex()'
# 函数 cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷，并能纠正曲线
# 函数 cv2.isContourConvex()可以用来检测一个曲线是不是他凸的，它只能返回True和False
img = cv2.imread("../images/23.jpg")
# 1. 对图像进行灰度化处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 进行二值化操作
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 3. 查找轮廓——得到的是图像原本的轮廓
contours, _ = cv2.findContours(binary, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# 4. 通过这个方法寻找图像的凸包
hull = cv2.convexHull(contours[0])  #
print(hull)
print(cv2.isContourConvex(contours[0]))  # 判断一个曲线是不是凸的
print(cv2.isContourConvex(hull))

# 5. 绘制轮廓
cv2.drawContours(img, [hull], -1, (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
