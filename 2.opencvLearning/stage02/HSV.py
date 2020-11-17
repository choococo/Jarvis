import cv2
import numpy as np

'HSV色彩空间'
arc = cv2.imread("../images/1.jpg")

dst = cv2.cvtColor(arc, cv2.COLOR_BGR2HSV)      # 颜色从红到绿再到蓝RGB

img = cv2.imread("../images/9.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower = np.array([0, 0, 0])                      # 3.jpg
# upper = np.array([90, 255, 200])

# lower = np.array([0, 109, 0])                   # 图像中低于这个值的，图像像素值变为0 2.jpg
# upper = np.array([179, 255, 210])               # 图像中高于这个值的，图像像素值变为0

lower = np.array([0, 120, 100])                      # 3.jpg
upper = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower, upper)


# cv2.imshow("", dst)
cv2.imshow("", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
