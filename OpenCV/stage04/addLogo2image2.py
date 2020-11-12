import cv2
import numpy as np

# bg = cv2.imencode(np.fromfile(""))

bg = cv2.imread("../images/bg1.png")
logo = cv2.imread("../images/logo1.png")
rows, cols, c = logo.shape
logo = cv2.resize(logo, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_NEAREST)


# 1. 将logo灰度化
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

# 2. 进行阈值操作
ret, thresh = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)

#
clean_thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel=(3, 3))

contours, hierarchy = cv2.findContours(clean_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(logo, contours, -1, (0, 255, 0), thickness=2)

cv2.imshow("thresh", thresh)
cv2.imshow("clean_thresh", clean_thresh)
cv2.imshow("logo", logo)

cv2.waitKey(0)
cv2.destroyAllWindows()
