import cv2
import numpy as np

'分水岭算法'
img = cv2.imread("../images/26.jpg")
cv2.imshow("img", img)


# 1. 图像二值化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("thresh", thresh)

# 2. 噪声去除
kernel = np.ones((3, 3), dtype=np.uint8)
open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2) # 使用两次
cv2.imshow("open", open)
# 3. 确定背景区域
sure_bg = cv2.dilate(open, kernel, iterations=3) # 使用三次膨胀操作
cv2.imshow("sure_bg", sure_bg)

# 4. 寻找前景区域
dist_transform = cv2.distanceTransform(open, 1, 5) # 距离腐蚀，计算距离
cv2.imshow("dist_transform", dist_transform)

ret, sure_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, cv2.THRESH_BINARY)

# 5. 找到未知区域
sure_fg = np.uint8(sure_fg)
cv2.imshow("sure_bg2", sure_fg)

unkown = cv2.subtract(sure_bg, sure_fg)
cv2.imshow("unkown", unkown)

# 6. 类别标记：计算中心
ret, markers = cv2.connectedComponents(sure_fg)

# 7. 为所有标记加1，保证背景是0不是1
markers = markers + 1
# 现在然所有的位置区域为0
markers[unkown == 255] = 0

# 8. 分水岭算法
markers = cv2.watershed(img, markers)
img[markers == -1] = (0, 0, 255)
cv2.imshow("img_watershed", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
