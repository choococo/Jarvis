import cv2
import numpy as np

'轮廓近似：approxPolyDP()'
img = cv2.imread("../images/22.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# 查找轮廓,外边界和端点
contours, hierarchy = cv2.findContours(image=gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# 轮廓近似
# approxPolyDP(curve, epsilon, closed, approxCurve=None)
# curve:输入曲线
# epsilon指定逼近精度的参数, 这是原始曲线与其近似值之间的最大距离
epsilon = 10 # 希腊字母第5个，埃普西隆
approx = cv2.approxPolyDP(curve=contours[0], epsilon=epsilon, closed=True)
print(np.shape(approx))
print(approx)

# 绘制轮廓：直接对原图进行操作
# image:在哪副图像上绘制轮廓, image为三通道才能显示轮廓
# contours:是轮廓本身，是一个list
# contourIdx:指定绘制轮廓list中的哪条轮廓，如果是-1,则绘制其中的所有轮廓
cv2.drawContours(image=img, contours=[approx], contourIdx=-1, color=(0, 255, 0), thickness=3)

cv2.imshow("binary", binary)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
