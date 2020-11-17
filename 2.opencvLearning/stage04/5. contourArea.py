import cv2

'面积、周长、重心'
gray = cv2.imread("../images/23.jpg", 0)
# gray = cv2.imread("../images/1.jpg")
# gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 查找轮廓
# method=cv2.CHAIN_APPROX_SIMPLE: 压缩垂直、水平、对角方向，只保留端点
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)  #

# 重心
# moments(array, binaryImae=None)
# print(contours[0])
M = cv2.moments(contours[0])  # 矩？？？？？？？？？？？？？？？？？？
print(M)
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print("重心：", cx, cy)

# 面积***********
# contourArea(contour, oriented=None)
area = cv2.contourArea(contours[0])
print("面积：", area)

# 周长
# arcLength(curve, closed)
perimeter = cv2.arcLength(contours[0], True)
print("周长：", perimeter)

cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
